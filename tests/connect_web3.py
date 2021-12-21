# -*- coding: utf-8 -*-

from web3 import Web3, HTTPProvider


INFURA_PRODUCT_ID = 'b7e1ee4af9e64991bda0dbd1220a54c2'

INFURA_URL = f'https://ropsten.infura.io/v3/{INFURA_PRODUCT_ID}'

private_key = 'c0dc14ef79b0088e0c33f8d2f7b8a512ecf096c4639a9756e7e8e7b191e08f0c'


w3 = Web3(HTTPProvider(INFURA_URL))

print(f'is connect to ropsten: {w3.isConnected()}')

# account
acc = w3.eth.account.privateKeyToAccount(private_key)
print(f'address: {acc.address}')

balance = w3.eth.get_balance(acc.address)
print(f'balance: {balance}')
print(f"balance ether: {w3.fromWei(balance,'ether')}")

# get transaction info
txhash = '0x52696723033ae2a9af0cdaa2c113be6cae17cb3227b342ab1181014bf513c512'

txinfo = w3.eth.get_transaction(txhash)

print(txinfo)


# transaction
tx = {
    'to': '0x459A0136E53B122e902f8bC9f13154c53C43aBF5',
    'value': 1000000000,
    'gas': 2000000,
    'maxFeePerGas': 2000000000,
    'maxPriorityFeePerGas': 1000000000,
    'nonce': 0,
    'chainId': 1,
    'type': '0x2',  # the type is optional and, if omitted, will be interpreted based on the provided transaction parameters
    'accessList': (  # accessList is optional for dynamic fee transactions
        {
            'address': '0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae',
            'storageKeys': (
                '0x0000000000000000000000000000000000000000000000000000000000000003',
                '0x0000000000000000000000000000000000000000000000000000000000000007',
            )
        },
        {
            'address': '0xbb9bc244d798123fde783fcc1c72d3bb8c189413',
            'storageKeys': ()
        },
    )
}

signed = w3.eth.account.sign_transaction(tx, private_key)
print(f'signed raw transaction: {signed.rawTransaction}')

print(f'signed hash: {signed.hash}')
print(w3.toHex(signed.hash))
