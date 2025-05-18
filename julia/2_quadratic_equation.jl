# quadratic_equation(a,b,c): a function that computes the real roots of a
# given quadratic equation a*X^2+b*X+c=0.

# using the quadratic formula:
# If there is one real root, it returns a list with one element
# If there are no real roots, it prints a message and returns an empty vector.

function quadratic_equation(a, b, c)
    # Handle degenerate case when a=0
    if a == 0
        if b == 0
            error("Not a valid equation: a and b cannot both be 0.")
        else
            # Linear equation: b*x + c = 0 => x = -c/b
            return [-c / b]
        end
    end
    # Calculate the discriminant
    discriminant = b^2 - 4 * a * c
    if discriminant < 0
        println("No real roots.")
        return []
    elseif discriminant == 0
        # One real root
        x = -b / (2*a)
        return [x]
    else
        # Two real roots
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)
        return [x1, x2]
    end
end

# Example usage:
roots = quadratic_equation(1, -3, 2)  # Equation: x^2 - 3x + 2 = 0
println("Quadratic Equation Roots: ", roots)
# Quadratic Equation Roots: [2.0, 1.0]
