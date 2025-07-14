from web3 import Web3

# Replace with your Infura URL
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'))
eth_address = "0x95504694bAa1837Ff81897a7E0dB55355623199c"

balance = w3.eth.get_balance(eth_address)
eth = w3.from_wei(balance, 'ether')
print(f"Current ETH balance at {eth_address}: {eth} ETH")
