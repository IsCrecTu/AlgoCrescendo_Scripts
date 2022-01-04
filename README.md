# AlgoCrescendo Scripts
Just some python scripts for use with the Algorand ASA Crescendo

Requirements:

- Python
- Algorand Python SDK: https://github.com/algorand/py-algorand-sdk


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
