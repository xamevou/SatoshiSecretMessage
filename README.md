

#  README for SatoshiSecretMessage.py

Satoshi Nakamoto`s secret phrase is hidden in a field in the only transaction
in the Genesis	block. This script gets the relevant field and shows it in 
a readable form.

Instructions: This script works when run in the same host running 
bitcoin core. Just change the variables rpcuser and rpcpassword with 
your values in bitcoin.conf. 

NOTE: In Antonopoulo's book, for several exercises, he uses 
RawProxy() instead of AuthServiceProxy(). That is quicker and does 
not need a password but it doesn't work now for some reason.
AuthServiceProxy(), then, provides an alternative.

I have added this to mybinder. Click banner here.
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/xamevou/SatoshiSecretMessage/HEAD)
