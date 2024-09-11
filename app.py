import json
import csv
from web3 import Web3

# Connect to local Hardhat blockchain
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Load Contract ABI
with open('abi.json', 'r') as abi_file:
    contract_abi = json.load(abi_file)

# Smart Contract Address (replace with your deployed contract address)
contract_address = Web3.to_checksum_address('0x5fbdb2315678afecb367f032d93f642f64180aa3')
print("Contract Address:", contract_address)
#21BCT0027
# Instantiate Contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Private Key (replace with your private key from Hardhat)
private_key = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80'
account = w3.eth.account.from_key(private_key)

def record_sensor_data(ecg, temperature, spo2):
    """Function to record sensor data on the blockchain."""
    # Build transaction to call the 'recordSensorData' function of the contract
    nonce = w3.eth.get_transaction_count(account.address)
    transaction = contract.functions.recordSensorData(ecg, temperature, spo2).build_transaction({
        'from': account.address,
        'nonce': nonce,
        'gas': 2000000,
        'gasPrice': w3.eth.gas_price
    })
    print("Transaction dict:", transaction)
    
    # Sign the transaction with private key
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

    # Send the transaction
    txn_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)

    # Wait for transaction receipt
    receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    print(f"Transaction successful with hash: {receipt.transactionHash.hex()}")

    # Prepare data for CSV
    transaction_data = {
        'nonce': nonce,
        'gas': transaction['gas'],
        'gasPrice': transaction['gasPrice'],
        'to': transaction['to'],
        'data': transaction['data'],
        'txn_hash': txn_hash.hex(),
        'blockNumber': receipt.blockNumber,
        'status': receipt.status
    }
    csv_file_path = 'transaction_details.csv'
    fieldnames = ['nonce', 'gas', 'gasPrice', 'to', 'data', 'txn_hash', 'blockNumber', 'status']
    
    # Check if CSV file exists, if not, write header
    file_exists = False
    try:
        with open(csv_file_path, 'r') as file:
            file_exists = True
    except FileNotFoundError:
        file_exists = False

    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(transaction_data)
    
