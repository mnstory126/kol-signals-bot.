import requests
                                                        def fetch_pumpfun_tokens():
    try:                                                        res = requests.get("https://pump.fun/api/recent")                                                               return res.json() if res.status_code == 200 else []                                                         except:
        return []                                       
def fetch_jupiter_tokens():                                 try:
        res = requests.get("https://quote-api.jup.ag/v6/tokens")
        return res.json() if res.status_code == 200 else []
    except:                                                     return []
                                                        def fetch_dexscreener_tokens():
    try:                                                        res = requests.get("https://api.dexscreener.com/latest/dex/pairs/solana")                                       data = res.json()
        return data.get("pairs", []) if data else []        except:
        return []                                                                                               def fetch_new_tokens():
    tokens = []                                         
    # Fetch from Pump.fun                                   pumpfun = fetch_pumpfun_tokens()
    for item in pumpfun:                                        token = {
            "name": item.get("name"),                               "address": item.get("mint"),
            "marketcap": item.get("market_cap", 1),                 "supply": item.get("supply", 1),
            "source": "pumpfun"                                 }
        tokens.append(token)                            
    # Fetch from Jupiter                                    jupiter = fetch_jupiter_tokens()
    for item in jupiter:                                        token = {
            "name": item.get("name"),                               "address": item.get("address"),
            "marketcap": 1,  # Jupiter tidak ada marketcap
            "supply": 1,     # Jupiter tidak ada supply             "source": "jupiter"
        }                                                       tokens.append(token)
                                                            # Fetch from Dexscreener
    dex = fetch_dexscreener_tokens()                        for item in dex:
        token = {                                                   "name": item.get("baseToken", {}).get("name"),
            "address": item.get("baseToken", {}).get("address"),
            "marketcap": item.get("liquidity", {}).get("usd", 1),
            "supply": 1,
            "source": "dexscreener"                             }
        tokens.append(token)                            
    return tokens