from algosdk.v2client import indexer
from datetime import datetime   

myindexer = indexer.IndexerClient(indexer_token="", indexer_address="https://algoindexer.algoexplorerapi.io", headers={'User-Agent': 'DoYouLoveMe?'})

today = datetime.now()
f = open("./crescendo_balance_before_vote_" + str(today.strftime("%Y-%m-%d_%H:%M")) + ".csv", "w")
f.write("Wallet Address,CRSD Balance,Last Updated:" + str(today) + '\n')

nexttoken = ""
numtx = 1

# loop using next_page to paginate until there are no more transactions in the response
# for the limit (max is 1000  per request)
while (numtx > 0):
    response = myindexer.asset_balances(asset_id=435335235, min_balance=1, next_page=nexttoken) 
    transactions = response['balances']
    numtx = len(transactions)
    #print(numtx)
    if (numtx > 0):
        nexttoken = response['next-token']
       
        # Pretty Printing JSON string 
        #print(json.dumps(response, indent=2, sort_keys=True))
        for x in range(numtx):
            try:
                wallet_address = response['balances'][x]['address']
                wallet_balance = response['balances'][x]['amount']
            except KeyError:
                pass
            f.write(wallet_address + ", " + str(wallet_balance) + '\n')

f.close()
