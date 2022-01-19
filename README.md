# AlgoCrescendo Scripts
Just some python scripts for use with the Algorand ASA Crescendo

Requirements:

- Python
- Algorand Python SDK: https://github.com/algorand/py-algorand-sdk

# CRSD_Price_Bot_Discord.py
Requirements:

- Python
- Tinyman Python SDK: https://github.com/tinymanorg/tinyman-py-sdk
- Goverfl0w Discord SDK: https://github.com/goverfl0w/interactions.py
- Discord Bot Token: https://www.writebots.com/discord-bot-token/

Once you have invited the bot to your Discord Server, then all you have to do is type "/crsdprice" in chat and it will respond with the following:

    Tinyman CRSD price:  0.000881 ALGO



# Crescendo_Holders.py
This one outputs similar to the following:

    Wallets with >1 CSRD: 2961
    Wallets with >1,000 CSRD: 1010
    Wallets with >10,000 CSRD: 649
    Wallets with >100,000 CSRD: 238
    Wallets with >1,000,000 CSRD: 74
    Wallets with >10,000,000 CSRD: 21

# Crescendo_CheckVote.py
This one checks for transactions of Exactly 1 CRSD to the designated voting wallet and then outputs the wallets address, current CRSD balance, and decrypted note field.

Example output:

    RKLSJDFKLJSDFSFROZUZ6FAVYPF53HGUZDSKLKJLSDFU,99999999,1.Yes 2.No 3.No
    
    
# Crescendo_Balance_Dump.py
This one pulls the current CRSD balances of all wallets that have opted in and have at least 1 CRSD and then outputs to a CSV file crescendo_balance_XXXX-XX-XX_XX:XX.csv

Examples file output:

    7HGT7JASDFASD237823894234209ADSFAS12123SADF2VJKM, 99999999
