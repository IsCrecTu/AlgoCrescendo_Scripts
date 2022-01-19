import interactions
from tinyman.v1.client import TinymanMainnetClient

bot = interactions.Client('DISCORD BOT TOKEN GOES HERE')
client = TinymanMainnetClient()
ALGO = client.fetch_asset(0)
CRSDCOIN = client.fetch_asset(435335235)
pool = client.fetch_pool(CRSDCOIN, ALGO)

@bot.event
async def on_ready():
    print("bot is now online.")

@bot.command(
    name="crsdprice",
    description="Check Tinyman price for CRSD"
)
async def crsdprice(ctx):
    quote = pool.fetch_fixed_input_swap_quote(CRSDCOIN(1), slippage=0.01)
    coin_value = quote.amount_out.amount/1000000
    await ctx.send("Tinyman CRSD price:  " + str(coin_value) + " ALGO")

bot.start()
