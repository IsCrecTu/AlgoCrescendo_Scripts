# requires Python SDK version 1.3 or higher
from algosdk.v2client import indexer

# instantiate indexer client
myindexer = indexer.IndexerClient(indexer_token="", indexer_address="https://algoindexer.algoexplorerapi.io", headers={'User-Agent': 'DoYouLoveMe?'})

# Check for wallets with a minimum balance of 1 CRSD
nexttoken = ""
numtx = 1
totaltx = 0

# loop using next_page to paginate until there are no more transactions in the response
# for the limit (max is 1000  per request)
while (numtx > 0):
    response = myindexer.asset_balances(asset_id=435335235, min_balance=1, next_page=nexttoken) 
    wallet_balance = response['balances']
    numtx = len(wallet_balance)
    totaltx = totaltx + numtx
    if (numtx > 0):
        nexttoken = response['next-token']
        # Pretty Printing JSON string 
        #print(json.dumps(response, indent=2, sort_keys=True))
print ("Wallets with >1 CSRD: " + str(totaltx))


# Check for wallets with a minimum balance of 1,000 CRSD
nexttoken = ""
numtx = 1
totaltx = 0

# loop using next_page to paginate until there are no more transactions in the response
# for the limit (max is 1000  per request)
while (numtx > 0):
    response = myindexer.asset_balances(asset_id=435335235, min_balance=999, next_page=nexttoken) 
    wallet_balance = response['balances']
    numtx = len(wallet_balance)
    totaltx = totaltx + numtx
    if (numtx > 0):
        nexttoken = response['next-token']
        # Pretty Printing JSON string 
        #print(json.dumps(response, indent=2, sort_keys=True))
print ("Wallets with >1,000 CSRD: " + str(totaltx))


# Check for wallets with a minimum balance of 10,000 CRSD
nexttoken = ""
numtx = 1
totaltx = 0
# loop using next_page to paginate until there are no more transactions in the response
# for the limit (max is 1000  per request)
while (numtx > 0):
    response = myindexer.asset_balances(asset_id=435335235, min_balance=9999, next_page=nexttoken) 
    wallet_balance = response['balances']
    numtx = len(wallet_balance)
    totaltx = totaltx + numtx
    if (numtx > 0):
        nexttoken = response['next-token']
        # Pretty Printing JSON string 
        #print(json.dumps(response, indent=2, sort_keys=True))
print ("Wallets with >10,000 CSRD: " + str(totaltx))


# Check for wallets with a minimum balance of 100,000 CRSD
nexttoken = ""
numtx = 1
totaltx = 0
# loop using next_page to paginate until there are no more transactions in the response
# for the limit (max is 1000  per request)
while (numtx > 0):
    response = myindexer.asset_balances(asset_id=435335235, min_balance=99999, next_page=nexttoken) 
    wallet_balance = response['balances']
    numtx = len(wallet_balance)
    totaltx = totaltx + numtx
    if (numtx > 0):
        nexttoken = response['next-token']
        # Pretty Printing JSON string 
        #print(json.dumps(response, indent=2, sort_keys=True))
print ("Wallets with >100,000 CSRD: " + str(totaltx))


# Check for wallets with a minimum balance of 1,000,000 CRSD
nexttoken = ""
numtx = 1
totaltx = 0
# loop using next_page to paginate until there are no more transactions in the response
# for the limit (max is 1000  per request)
while (numtx > 0):
    response = myindexer.asset_balances(asset_id=435335235, min_balance=999999, next_page=nexttoken) 
    wallet_balance = response['balances']
    numtx = len(wallet_balance)
    totaltx = totaltx + numtx
    if (numtx > 0):
        nexttoken = response['next-token']
        # Pretty Printing JSON string 
        #print(json.dumps(response, indent=2, sort_keys=True))
print ("Wallets with >1,000,000 CSRD: " + str(totaltx))


# Check for wallets with a minimum balance of 10,000,000 CRSD
nexttoken = ""
numtx = 1
totaltx = 0
# loop using next_page to paginate until there are no more transactions in the response
# for the limit (max is 1000  per request)
while (numtx > 0):
    response = myindexer.asset_balances(asset_id=435335235, min_balance=9999999, next_page=nexttoken) 
    wallet_balance = response['balances']
    numtx = len(wallet_balance)
    totaltx = totaltx + numtx
    if (numtx > 0):
        nexttoken = response['next-token']
        # Pretty Printing JSON string 
        #print(json.dumps(response, indent=2, sort_keys=True))
print ("Wallets with >10,000,000 CSRD: " + str(totaltx))