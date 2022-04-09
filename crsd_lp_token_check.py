from algosdk.v2client import indexer    

## Change this to the number of LP tokens you want
lptokens_wanted = 10

### No need to mess with anything below unless you are changing the LP pool####
def check_lp_token(lptokens_wanted):
    myindexer = indexer.IndexerClient(indexer_token="", indexer_address="https://algoindexer.algoexplorerapi.io", headers={'User-Agent': 'DoYouLoveMe?'})
    response = myindexer.account_info(address="C3DUWF4E4WHD4NQ52S3QEWB6EOFAEVZ55UBYFJNBJSI2LYFTUSO3IABT34")
    totaltransactions = len(response['account']['apps-local-state'][0]['key-value'])

    issued_lp_tokens = 0
    crsd_reserve = 0
    algo_reserve = 0

    for x in range(totaltransactions):
        try: 
            if response['account']['apps-local-state'][0]['key-value'][x]['key'] == 'aWx0':
                issued_lp_tokens = response['account']['apps-local-state'][0]['key-value'][x]['value']['uint']

            if response['account']['apps-local-state'][0]['key-value'][x]['key'] == 'czE=':
                crsd_reserve = response['account']['apps-local-state'][0]['key-value'][x]['value']['uint']
            
            if response['account']['apps-local-state'][0]['key-value'][x]['key'] == 'czI=':
                algo_reserve = response['account']['apps-local-state'][0]['key-value'][x]['value']['uint']
        except KeyError:
            pass
    if issued_lp_tokens > 0:
        # print(f"CRSD LP Tokens Issued: {issued_lp_tokens/1000000:,}")
        # print(f"ALGO Reserve: {algo_reserve/1000000:,} ALGO")
        # print(f"CRSD Reserve: {crsd_reserve:,}CRSD")
        asset1_out = (crsd_reserve * (lptokens_wanted / issued_lp_tokens))
        asset2_out = (algo_reserve * (lptokens_wanted / issued_lp_tokens))
        output = f"Need to add {asset1_out*1000000:,.0f} CRSD and {asset2_out:.6f} ALGO to get {lptokens_wanted} CRSD LP Token(s)"
        return output

print(check_lp_token(lptokens_wanted))