from src.connector import connect

if __name__ == "__main__":
    ib = connect()
    ib.disconnect()