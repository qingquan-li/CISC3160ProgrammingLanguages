import java.util.*;
import java.io.*;

class Tag {
    public final static int IL = 0,
                            ID = 1,
                            OP = 2,
                            PM = 3;
}

class Token {
    public final int tag;
    public Token(int t){tag = t;}
}

class IntegerLiteral extends Token {
    public final int value;
    public IntegerLiteral(int v){
        super(Tag.IL);
        value = v;
    }
}

class Identifier extends Token {
    public final String lexeme;
    public Identifier(String s){
        super(Tag.ID);
        lexeme = s;
    }
}

class Operator extends Token {
    public final char name;
    public Operator(char name){
        super(Tag.OP);
        this.name = name;
    }
}

class PunctuationMark extends Token {
    public final char name;
    public PunctuationMark(char name){
        super(Tag.PM);
        this.name = name;
    }
}

public class Lexer {
    public int line = 1;
    private char peek = ' ';
    private Hashtable<String, Token> symbolTable = new Hashtable<>();
    InputStream input;
    Token t;
    public Lexer(InputStream input){
        this.input = input;
    }
    public Token scan() throws IOException {
        for ( ; ; peek = (char)input.read()){
            if (Character.isWhitespace(peek)){
                if (peek == '\n') line++;
            } else {
                break;
            }
        }
        switch (peek){
        case '=':
        case '+':
        case '-':
        case '*':
            t = new Operator(peek);
            peek = ' ';
            return t;
        case ';':
            t = new PunctuationMark(peek);
            peek = ' ';
            return t;
        case '0':
            t = new IntegerLiteral(0);
            peek = ' ';
            return t;
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9':
            int v = 0;
            do {
                v = 10*v + (peek - '0');
                peek = (char)input.read();
            } while (Character.isDigit(peek));
            return new IntegerLiteral(v);
        default:
            if (Character.isLetter(peek) || peek == '_'){
                StringBuffer sb = new StringBuffer();
                do {
                    sb.append(peek);
                    peek = (char)input.read();
                } while (Character.isLetterOrDigit(peek) || peek == '_');
                String s = new String(sb);
                t = symbolTable.get(s);
                if (t == null){
                    t = new Identifier(s);
                    symbolTable.put(s, t);
                }
                return t;
            }
            return null;
        }
    }
}


// Example usage
class Main {
    public static void main(String[] args) {
        try {
            Lexer lexer = new Lexer(System.in);
            Token token;
            while ((token = lexer.scan()) != null) {
                if (token instanceof IntegerLiteral) {
                    System.out.println("Integer Literal: " + ((IntegerLiteral) token).value);
                } else if (token instanceof Identifier) {
                    System.out.println("Identifier: " + ((Identifier) token).lexeme);
                } else if (token instanceof Operator) {
                    System.out.println("Operator: " + ((Operator) token).name);
                } else if (token instanceof PunctuationMark) {
                    System.out.println("Punctuation Mark: " + ((PunctuationMark) token).name);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

// To test it in the terminal, you can run the program and input some text.
// For example, you can type "x = 1 + 2;" and then press Enter.
// The program will output the tokens it recognizes from the input.
// Ex:
// x = 1 + 2
// Identifier: x
// Operator: =
// Integer Literal: 1
// Operator: +
// Integer Literal: 2
