import base64

# requires Python SDK version 1.3 or higher
from algosdk.v2client import indexer

# instantiate indexer client
myindexer = indexer.IndexerClient(indexer_token="", indexer_address="https://algoindexer.algoexplorerapi.io", headers={'User-Agent': 'DoYouLoveMe?'})

# gets transactions for an account after a timestamp
response = myindexer.search_transactions_by_address(
    address="34IOOGFLLWPB43R3LSHTZE5AG33TFEKHCM4UELGGXUCZQ6DR7ETGMG7TCA", 
    asset_id=435335235, 
    start_time="2022-01-04T17:38:00-05:00",  
    end_time="2022-01-07T17:38:00-05:00",
    min_amount=0,
    max_amount=2
)

totaltransactions = len(response['transactions'])

print("Wallet Address,CRSD Balance,Vote")
for x in range(totaltransactions):
    try: 
        if response['transactions'][x]['asset-transfer-transaction']['receiver'] == '34IOOGFLLWPB43R3LSHTZE5AG33TFEKHCM4UELGGXUCZQ6DR7ETGMG7TCA':
            #decode note field and strip new line
            note_string = response['transactions'][x]['note']
            note_string_bytes = note_string.encode("ascii")
            note_decode_bytes = base64.b64decode(note_string_bytes)
            note_decode_string = note_decode_bytes.decode("ascii")
            note_strip_decode_string = note_decode_string.replace("\n", "")

            #Check CRSD balance
            account_balance = myindexer.account_info(response['transactions'][x]['sender'])
            totalasa = len(account_balance['account']['assets'])
            for y in range(totalasa):
                if account_balance['account']['assets'][y]['asset-id'] == 435335235:
                    crescendo_balance = account_balance['account']['assets'][y]['amount']

            print(response['transactions'][x]['sender'] + ',' + str(crescendo_balance) + ',' + note_strip_decode_string)
    except KeyError:
        pass