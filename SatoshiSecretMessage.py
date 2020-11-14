#! python3 
#  SatoshiSecretMessage.py

""" 
	Satoshi Nakamoto secret phrase is hidden in a field in the only transaction
	in the Genesis	block. This script gets the relevant field and shows it in 
	a readable form.

	Instructions: This script works when run in the same host running 
	bitcoin core. Just change the variables rpcuser and rpcpassword with 
	your values in bitcoin.conf. 
	
	NOTE: In Antonopoulo's book he uses RawProxy() instead 
	of AuthServiceProxy(). That is quicker and does not need
	a password but it doesn't work now for some reason.
	AuthServiceProxy provides an alternative.

"""

from bitcoinrpc.authproxy import AuthServiceProxy

import codecs
import pprint

# REMEMBER to use your own values here.
rpcuser = 'MY_RPC_USERNAME'
rpcpassword = 'MY_RPC_PASSWORD'
p = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%(rpcuser, rpcpassword))

# Hash of the Genesis block is obtained first. 
blockheight = 0
blockhash = p.getblockhash(blockheight) 

# Retrieve the block by its hash. 2nd parameter asks for a json object
block = p.getblock(blockhash,2)

# Pretty print the Genesis block:
print(f"\nThis is block #0, The Genesis Block:\n")
pprint.pprint(block)

# Element tx has the list of transactions in a block (only 1 for block #0)
transactions = block['tx'] 
print(f"\nThe Genesis Block {blockheight} has {len(transactions)} transaction(s).")


# Get the value of the only transaction
# Some convolution of dictionaries and strings needs to be accesed
value = transactions[0]['vout'][0]['value'] 
print(f"The value of the only transaction in the block is {value} BTC.")

# The 'hex' field has the message. 
# From hexadecimal we must convert it to ASCII
msg_satoshi = transactions[0]['hex']
print(f"\nThe secret message is hidden in the 'hex' field:\n{msg_satoshi} ")
print(f"\nThe ASCII version of that hex is the following:")
print(codecs.decode(msg_satoshi, "hex"))


# Done. Goodbye. Pay some respects.
print(f"\nThanks for your gift, Mr. Satoshi!")



