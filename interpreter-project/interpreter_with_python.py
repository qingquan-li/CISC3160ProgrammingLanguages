import re
import sys

# -------------------------------
# 1) LEXER / TOKENIZER
# -------------------------------

# Read the entire input program from stdin:
input_text = sys.stdin.read()

# A token is represented as a (type, value) pair
# e.g. ('INT', 42) or ('ID', 'x')
Token = tuple

def tokenize(s):
    """
    Turn the string `s` into a stream of tokens.
    Recognizes:
      - INTEGER literals: either "0" or nonzero followed by digits
      - IDENTIFIERS: letter or '_' followed by letters, digits, or '_'
      - +, -, *, =, ;, parentheses
    Enforces no leading zeros (e.g. "001" is invalid).
    Raises SyntaxError on invalid characters or bad literals.
    """
    token_specification = [
        # Order matters
        ('NUMBER',   r'0|[1-9][0-9]*'),
        ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),
        ('PLUS',     r'\+'),
        ('MINUS',    r'-'),
        ('MUL',      r'\*'),
        ('EQ',       r'='),
        ('SEMI',     r';'),
        ('LPAREN',   r'\('),
        ('RPAREN',   r'\)'),
        ('SKIP',     r'[ \t\n\r]+'),  # whitespace (skip)
        ('MISMATCH', r'.'),           # any other single character
    ]
    # Build the combined regex
    tok_regex = '|'.join(f'(?P<{name}>{pattern})'
                         for name, pattern in token_specification)
    get_token = re.compile(tok_regex).match
    pos = 0
    mo = get_token(s, pos)  # mo = match object
    while mo:
        typ = mo.lastgroup
        val = mo.group(typ)
        if typ == 'NUMBER':
            # Reject leading-zero integers like "01", "005"
            if val.startswith('0') and val != '0':
                raise SyntaxError('invalid literal')
            yield ('INT', int(val))
        elif typ == 'ID':
            yield ('ID', val)
        elif typ in ('PLUS','MINUS','MUL','EQ','SEMI','LPAREN','RPAREN'):
            yield (typ, val)
        elif typ == 'SKIP':
            pass  # ignore whitespace
        else:  # 'MISMATCH'
            raise SyntaxError(f'Unexpected character {val!r}')
        pos = mo.end()
        mo = get_token(s, pos)
    # Finally, signal end of file
    yield ('EOF', '')


# -------------------------------
# 2) PARSER (Recursive Descent)
# -------------------------------

class ParseError(Exception):
    pass

# AST node classes
class AST: pass

class BinOp(AST):
    def __init__(self, op, left, right):
        self.op = op; self.left = left; self.right = right

class UnaryOp(AST):
    def __init__(self, op, expr):
        self.op = op; self.expr = expr

class Literal(AST):
    def __init__(self, value):
        self.value = value

class Var(AST):
    def __init__(self, name):
        self.name = name


class Parser:
    def __init__(self, tokens):
        # Convert the token generator into a list for easy lookahead
        self.tokens = list(tokens)
        self.pos = 0

    def current(self):
        # Return the token at the current position
        return self.tokens[self.pos]

    def eat(self, typ):
        """
        Consume the current token if its type matches `typ`,
        and return its value. Otherwise, error.
        """
        if self.current()[0] == typ:
            val = self.current()[1]
            self.pos += 1
            return val
        else:
            raise ParseError(f'Expected {typ} got {self.current()[0]}')

    def parse(self):
        """
        program => Assignment*
        Assignment => ID '=' Exp ';'

        Returns a list of (variable_name, expression_AST) and
        a list of var names in first-assignment order.
        """
        assignments = []
        var_order = []
        while self.current()[0] != 'EOF':
            # Each statement must start with an identifier
            if self.current()[0] != 'ID':
                raise ParseError('Assignment must start with ID')
            name = self.eat('ID')
            self.eat('EQ')
            expr = self.parse_expr()
            self.eat('SEMI')
            assignments.append((name, expr))
            if name not in var_order:
                var_order.append(name)
        return assignments, var_order

    def parse_expr(self):
        """
        Exp -> Term (( '+' | '-' ) Term)*
        Left-associative chain of +/-
        """
        node = self.parse_term()
        while self.current()[0] in ('PLUS', 'MINUS'):
            op = self.eat(self.current()[0])
            right = self.parse_term()
            node = BinOp(op, node, right)
        return node

    def parse_term(self):
        """
        Term -> Fact ( '*' Fact )*
        Left-associative chain of *
        """
        node = self.parse_factor()
        while self.current()[0] == 'MUL':
            op = self.eat('MUL')
            right = self.parse_factor()
            node = BinOp(op, node, right)
        return node

    def parse_factor(self):
        """
        Fact -> '(' Exp ')' | ('+'|'-') Fact | Literal | Identifier
        Handles unary +/- via recursion.
        """
        tok = self.current()
        if tok[0] == 'PLUS':
            self.eat('PLUS')
            return UnaryOp('+', self.parse_factor())
        if tok[0] == 'MINUS':
            self.eat('MINUS')
            return UnaryOp('-', self.parse_factor())
        if tok[0] == 'LPAREN':
            self.eat('LPAREN')
            node = self.parse_expr()
            self.eat('RPAREN')
            return node
        if tok[0] == 'INT':
            val = self.eat('INT')
            return Literal(val)
        if tok[0] == 'ID':
            name = self.eat('ID')
            return Var(name)
        # Anything else is a syntax error
        raise ParseError(f'Unexpected token {tok}')


# -------------------------------
# 3) EVALUATOR
# -------------------------------

class EvalError(Exception):
    pass

def eval_expr(node, sym):
    """
    Recursively evaluate the AST `node` using variable values in `sym` dict.
    - Literal: return the integer
    - Var: look up in sym (error if not initialized)
    - UnaryOp: +x or -x
    - BinOp: x + y, x - y, x * y
    """
    if isinstance(node, Literal):
        return node.value

    if isinstance(node, Var):
        if node.name not in sym:
            raise EvalError(f"Uninitialized var {node.name}")
        return sym[node.name]

    if isinstance(node, UnaryOp):
        val = eval_expr(node.expr, sym)
        return +val if node.op == '+' else -val

    if isinstance(node, BinOp):
        l = eval_expr(node.left, sym)
        r = eval_expr(node.right, sym)
        if node.op == '+': return l + r
        if node.op == '-': return l - r
        if node.op == '*': return l * r

    raise EvalError("Unknown AST node")


# -------------------------------
# 4) MAIN DRIVER
# -------------------------------

def main():
    try:
        # 1. Lex
        tokens = tokenize(input_text)
        # 2. Parse
        parser = Parser(tokens)
        assignments, var_order = parser.parse()
        # 3. Evaluate assignments in order
        sym = {}
        for name, expr in assignments:
            val = eval_expr(expr, sym)
            sym[name] = val
        # 4. Print results
        for name in var_order:
            print(f"{name} = {sym[name]}")
    # On any error, print exactly "error"
    except (SyntaxError, ParseError, EvalError):
        print("error")

if __name__ == "__main__":
    main()


# Usage:

# Test Input 1 (should print “error”):
# $ echo "x = 001;" | python3 interpreter_with_python.py
# error

# Test Input 2 (should print “x_2 = 0”):
# $ echo "x_2 = 0;" | python3 interpreter_with_python.py
# x_2 = 0

# Test Input 3 (syntax error: missing semicolon on first line):
# $ printf "x = 0\ny = x;\nz = ---(x+y);\n" | python3 interpreter_with_python.py
# error

# Test Input 4 (should print x,y,z):
# $ printf "x = 1;\ny = 2;\nz = ---(x+y)*(x+-y);\n" | python3 interpreter_with_python.py
# x = 1
# y = 2
# z = 3

# Another way to run the test (run it in a terminal):
# $ python3 interpreter_with_python.py
# x = 1;
# y = 2;
# z = ---(x+y)*(x+-y);
# <Ctrl-D>   # (on Linux/macOS) to send EOF
# x = 1
# y = 2
# z = 3
