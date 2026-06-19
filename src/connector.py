from ib_async import IB

def connect():
    
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=1)
    print(f"Connected: {ib.isConnected()}")
    print(f"Account: {ib.wrapper.accounts}")
    return ib

def get_positions(ib):
    """
    Returns the current portfolio positions as a list of dicts.
    """
    positions = ib.positions()
    result = []
    for p in positions:
        result.append({
            "symbol": p.contract.symbol,
            "exchange": p.contract.exchange,
            "currency": p.contract.currency,
            "quantity": p.position,
            "avg_cost": p.avgCost
        })
    return result

if __name__ == "__main__":
    ib = connect()
    positions = get_positions(ib)
    for p in positions:
        print(p)
    ib.disconnect()
    print("Disconnected.")