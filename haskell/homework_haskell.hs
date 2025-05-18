-- Selected 5 questions from the homework assignment.

-- 3. number_of_zeros(lst): a function that returns the number of zeros in a given simple list of numbers lst.
numberOfZeros :: (Eq a, Num a) => [a] -> Int
numberOfZeros []     = 0
numberOfZeros (x:lst) = (if x == 0 then 1 else 0)
                      + numberOfZeros lst


-- 4. draw_pascal(n): a function that takes an integer n as a parameter and prints the first n rows of the Pascal's triangle.
module Main where

-- Compute the next row from the current:
nextRow :: [Int] -> [Int]
nextRow row = zipWith (+) ([0] ++ row) (row ++ [0])

-- Generate an infinite list of Pascal rows:
pascals :: [[Int]]
pascals = iterate nextRow [1]

-- Print the first n rows:
drawPascal :: Int -> IO ()
drawPascal n = mapM_ printRow (take n pascals)
  where
    printRow row = putStrLn $ unwords (map show row)


-- 8. remove_dups(lst): return a copy of lst with duplicates of elements eliminated. For example, for lst = [a,a,a,a,b,c,c,a,a,d,e,e,e,e], the returned list is [a,b,c,d,e].
removeDups :: Eq a => [a] -> [a]
removeDups []     = []
removeDups (x:lst) = x : removeDups (filter (/= x) lst)


-- 9. replicate(lst,n): Replicate each of the elements of lst a given number of times. For example, for lst = [a,b,c] and n = 3, the returned list is [a,a,a,b,b,b,c,c,c].
replicateElems :: Int -> [a] -> [a]
replicateElems _ []     = []
replicateElems n (x:lst)
  | n <= 0    = []                     -- if n ≤ 0, no repetitions
  | otherwise = replicateN n x ++ replicateElems n lst
  where
    -- helper to replicate a single element m times
    replicateN 0 _ = []
    replicateN m y = y : replicateN (m-1) y


-- 10. split_list(lst,n): split lst into two parts with the first part having n elements, and return a list that contains these two parts.
splitList :: Int -> [a] -> ([a],[a])
splitList n lst
  | n <= 0    = ([], lst)
  | otherwise = go n lst
  where
    go 0 ys       = ([], ys)
    go _ []       = ([], [])
    go k (y:ys)   =
      let (as, bs) = go (k - 1) ys
      in  (y:as, bs)

