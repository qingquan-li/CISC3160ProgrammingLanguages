Solutions from the professor.
Selected questions from the Julia, Haskell and Picat homework assignment.

# 1. number_of_zeros
```julia
# julia
function number_of_zeros(lst)
    return length(filter(x -> x == 0, lst))
end
```

```haskell
-- haskell
number_of_zeros [] = 0
number_of_zeros (0:t) = (number_of_zeros t) + 1
number_of_zeros (_:t) = number_of_zeros t
```

```picat
% picat
number_of_zeros([]) = 0.
number_of_zeros([0|T]) = number_of_zeros(T)+1.
number_of_zeros([_|T]) = number_of_zeros(T).
```

## 2. draw_pascal

```julia
function draw_pascal(n)
    row = [1]
    rows = [row]
    for _ in 1:n-1
        row = map(+, [0;row], [row;0])
        push!(rows, row)
    end
    return rows
end
```

```haskell
draw_pascal n = draw_pascal_aux (n-1) [1] [[1]]

draw_pascal 0 row rows = reverse rows
draw_pascal n row rows = draw_pascal (n-1) next_row (next_row:rows)
    where next_row = zipWith (+) (0:row) (row ++ [0])
```

```picat
draw_pascal(N) = Rows =>
    draw_pascal(N, [1], Rows).

draw_pascal(0, Row, Rows) => Rows = [].
draw_pascal(N, Row, Rows) => 
    NextRow = zip(+, [0|Row], Row ++ [0]),
    Rows = [Row|RowsR],
    draw_pascal(N-1, NextRow, RowsR).
```

## 3. euler

```julia
function euler()
    x = floor(Int, sqrt(19293949596979899))
    while !(test(x))
        x -= 1
    end
    return x*10
end

function test(x)
    s = string(x*x)
    if length(s) != 17
        return false
    end
    d1,_,d2,_,d3,_,d4,_,d5,_,d6,_,d7,_,d8,_,d9 = s
    return d1 == '1' && 
           d2 == '2' &&  
           d3 == '3' &&  
           d4 == '4' &&  
           d5 == '5' &&  
           d6 == '6' &&  
           d7 == '7' && 
           d8 == '8' &&  
           d9 == '9'
end
```

```haskell
euler = euler_aux  (floor (sqrt 19293949596979899))

euler_aux x 
    | test show (x*x) = x * 10
    | otherwise = euler_aux (x - 1)

test ['1',_,'2',_,'3',_,'4',_,'5',_,'6',_,'7',_,'8',_,'9'] = True
test _ = False
```

```picat
% generate and test
main =>
    between(sqrt(19293949596979899).to_int(),-1,1,I),
    (I mod 10 == 3; I mod 10 == 7),
    (I*I).to_string() = ['1',_,'2',_,'3',_,'4',_,'5',_,'6',_,'7',_,'8'|_],
     println(I*10).
```

## 4. bc (Binomial Coefficient)
```julia
function bc(n, k)
    if k == 0
        return 1
    elseif n == k 
        return 1
    else
        return bc(n-1, k) + bc(n-1, k-1)
    end
end
```

```haskell
bc n 0 = 1
bc n k
    | n == k = 1
    | otherwise = (bc (n-1) k) + (bc (n-1) (k-1))
```

```picat
table
bc(N,0) = 1.
bc(N,N) = 1.
bc(N,K) = bc(N-1,K) + bc(N-1, K-1).
```

## 5. subsets
```
# subsets(s,n): return the set of n-element subsets of s.
function subsets(s, n)
    if n > length(s)
        return []
    elseif n == 0
        return [[]]
    elseif n == length(s)
        return [s]
    else
        ss1 = subsets(s[2:end], n)
        ss2 = subsets(s[2:end], n-1)
        return vcat(ss1, [[s[1]; s2] for s2 in ss2])
    end
end
```

```haskell
subsets s n = subsets_aux s (length s) n

subsets_aux _ len 0 = [[]]
subsets_aux [] len _ = []
subsets_aux s@(h:t) len n    
    | n > len = []
    | n == len = [s]
    | otherwise = ss1 ++ [(h:s2) | s2 <- ss2]
        where ss1 = subsets_aux t (len - 1) n
              ss2 = subsets_aux t (len -1) (n - 1)
```

```picat
subsets(S,N) = subsets(S,len(S),N).

subsets(_,Len,0) = [[]].
subsets([],Len,_) = [].
subsets([H|T],Len,N) = [], N > Len => true.
subsets([H|T],Len,N) = [S], N == Len => true.
subsets([H|T],Len,N) = SS1 ++ [[H|S2] : S2 in SS2] =>
    SS1 = subsets(T,Len-1,N),
    SS2 = subsets(T,Len-1,N-1).
```
