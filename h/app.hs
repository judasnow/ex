{-# LANGUAGE OverloadedStrings #-}
import Web.Scotty

import Network.Wai.Middleware.RequestLogger -- install wai-extra if you don't have this

import Control.Monad.Trans
import Data.Monoid
import System.Random (newStdGen, randomRs)

import Network.HTTP.Types (status302)
import Network.Wai
import qualified Data.Text.Lazy as T


import Data.Text.Lazy.Encoding (decodeUtf8)
main = scotty 6000 $ do

    matchAny "/all" $ do
        text "<p>test</p>"

