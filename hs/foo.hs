
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


data Bool' = False | True
data Sharp' = Circle Float Float Float | Rectangle Float Float Float Float


area :: Sharp' -> Float
area (Circle _ _ r) = pi * r ^ 2
area (Rectangle x1 y1 x2 y2) = (abs $ x2 - x1) * (abs $ y2 - y1)


data Point = Point Float Float deriving (Show)
data Sharp2 = Circle2 Point Float | Rectangle2 Point Point deriving (Show)

area2 :: Sharp2 -> Float
area2 (Circle2 _ r) = pi * r ^ 2
area2 (Rectangle2 (Point x1 y1) (Point x2 y2)) =
    (abs $ x2 - x1) * (abs $ y2 - y1)


--instance Functor IO where
--    fmap f action = do
--        result <- action
--        return (f result)

--main1 = do line <- getLine
--    let line1 = reverse line
--    putStrLn $ "You said " ++ line1 ++ " backwards!"
--    putStrLn $ "Yes, you said " ++ line1 ++ " backwards!"
--

data User = User String String deriving (Show)

