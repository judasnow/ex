
doubleMe x = x + x

doubleUs x y =
    x * 2 + y * 2


doubleSmallNum x =
    (if x < 100
        then x * 2
        else x) + 1

len' xs =
    sum [1 | _ <- xs]


fistletter :: String -> String
fistletter all@(x:xs) = "The first" ++ all ++ " is " ++ [x]


bimTell :: Double -> String
bimTell bim
    | bim <= p = "123"
    | bim <= 18.5 = "You 1"
    | bim <= 25.0 = "You 2"
    | otherwise = "other"
    where p = 3


initials :: String -> String -> String
initials firstname lastname = [f] ++ ". " ++ [l] ++ "."
    where (f:_) = firstname
          (l:_) = lastname

desc :: [a] -> String
desc ls = "This list is " ++ what ls
    where what [] = "empty"
          what [x] = "singletion list"
          what xs = "a longer list"


