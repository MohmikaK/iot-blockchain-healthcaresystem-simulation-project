import json
from web3 import Web3

# Connect to local Hardhat blockchain
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Load Contract ABI
with open('abi.json', 'r') as abi_file:
    contract_abi = json.load(abi_file)

# Smart Contract Address
contract_address = Web3.to_checksum_address('0x5fbdb2315678afecb367f032d93f642f64180aa3')

# Instantiate Contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def get_all_timestamps():
    """Function to retrieve all timestamps from the blockchain."""
    try:
        timestamps = contract.functions.getAllTimestamps().call()
        return timestamps
    except Exception as e:
        print(f"An error occurred while getting timestamps: {e}")
        return []

def get_sensor_data_for_timestamp(timestamp):
    """Function to retrieve sensor data for a specific timestamp from the blockchain."""
    try:
        data = contract.functions.getSensorData(timestamp).call()
        ecg, temperature, spo2 = data
        print(f"Timestamp: {timestamp}, ECG: {ecg}, Temperature: {temperature}, SPO2: {spo2}")
    except Exception as e:
        print(f"An error occurred while getting sensor data for timestamp {timestamp}: {e}")

if __name__ == '__main__':
    timestamps = get_all_timestamps()
    print("Name: Mohmika Kapoor Registration Number: 21BCT0027")
    print("Data retrived is as follows: ")
    if timestamps:
        for timestamp in timestamps:
            get_sensor_data_for_timestamp(timestamp)
    else:
        print("No timestamps found.")
