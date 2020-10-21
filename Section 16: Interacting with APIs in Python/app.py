import time
from libs.openexchange import OpenExchangeClient

# get your ID from openexchangerates.org
# APP_ID = "YOUR_APP_ID_HERE"
APP_ID = "5a497cfd47cd4656aa41e528164f0e19"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000

start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)

print(f"USD {usd_amount} is GBP {gbp_amount:.2f}")