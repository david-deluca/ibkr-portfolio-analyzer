from ib_async import IB

def connect():
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=1)
    print(f"Connected: {ib.isConnected()}")
    print(f"Account: {ib.wrapper.accounts}")
    return ib

if __name__ == "__main__":
    ib = connect()
    ib.disconnect()
    print("Disconnected.")