def is_potential_pump(token):
    try:                                                        mc = float(token.get("marketcap", 0))
        supply = float(token.get("supply", 1))                  return (supply / mc) >= 0.1
    except:
        return False

def ai_scan(token):                                         warnings = token.get("warnings", "").lower()
    red_flags = ["mint", "transfer", "blacklist"]
    return not any(flag in warnings for flag in red_flags)