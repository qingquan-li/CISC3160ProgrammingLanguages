# function fib(n)
#   # if n==0
#   #   return 1
#   # elseif n == 1
#   #   return 1
#   if n < 2
#     return n
#   else
#     return fib(n - 1) + fib(n - 2)
#   end
# end

# println(fib(0))
# println(fib(1))
# println(fib(5))  # 5

fib(n) = (n == 0) ? 1 : (n == 1) ? 1 : fib(n - 1) + fib(n - 2)
# println(fib(5))

# Run it in Julia interactive command-line REPL (read-eval-print loop):
# path/to/current/file $ julia

# julia> include("demo_fibonacci.jl")
# fib (generic function with 1 method)

# julia> fib(5)
# 8
