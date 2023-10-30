import requests
import sys

# if len(sys.argv) !=2:
#     sys.exit()


if len(sys.argv) !=2:
    print("Missing command-line argument")
    sys.exit()
    
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate = response.json()["bpi"]["USD"]["rate"]
    rate = rate.replace(",", "")
    userAmount = float(sys.argv[1])
    amount = float(rate)*userAmount
    print(f"${amount:,.4f}")
except ValueError:
    print("Command-line argument is not number")
    sys.exit()
