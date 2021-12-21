# -*- coding: utf-8 -*-

import json
from web3 import Web3, HTTPProvider


INFURA_PRODUCT_ID = 'b7e1ee4af9e64991bda0dbd1220a54c2'

INFURA_URL = f'https://ropsten.infura.io/v3/{INFURA_PRODUCT_ID}'

private_key = 'c0dc14ef79b0088e0c33f8d2f7b8a512ecf096c4639a9756e7e8e7b191e08f0c'


w3 = Web3(HTTPProvider(INFURA_URL))

print(f'is connect to ropsten: {w3.isConnected()}')

#===============================================#
# account
#===============================================#
acc = w3.eth.account.privateKeyToAccount(private_key)
print(f'address: {acc.address}')
print(f'balance: {w3.eth.get_balance(acc.address)}')


def signature_use_priv(tx_param: dict):
    """signature transaction with paramater dict"""
    # signature transaction
    signed_txn = w3.eth.account.sign_transaction(tx_param, private_key)
    print(f'signature hash: {signed_txn}')

    # send signed transaction
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f'send txn hash: {Web3.toHex(txn_hash)}')

    # transaction receipt
    receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    print(f'receipt: {receipt}')


#===============================================#
# send
#===============================================#
def test_send():
    nonce = w3.eth.get_transaction_count(acc.address)
    print(f'{acc.address} nonce: {nonce}')
    bob_addr = '0x2A02DfaCb1B6826bb2a79700CF6f7DE1B7fBd5F0'
    value = w3.toWei(0.0001, "ether")

    tx_data = dict(
        to=bob_addr,
        value=value,
        gas=21000,
        nonce=nonce,
        maxFeePerGas=3000000000,
        maxPriorityFeePerGas=2000000000,
        chainId=3,  # ropsten
    )

    # signature transaction
    signature_use_priv(tx_data)

    # check balance
    print(f'{acc.address} after send balance: {w3.eth.get_balance(acc.address)}')
    print(f'{bob_addr} receive balance: {w3.eth.get_balance(bob_addr)}')

# test_send()

#===============================================#
# contract
#===============================================#
def test_contract():
    contract_addr = '0x2F488bf1446f49eCaC017eEe7E1ff8891801229B'
    with open(f'build/deployments/3/{contract_addr}.json', 'r') as fr:
        file = json.load(fr)
    deployed_contract = w3.eth.contract(address=contract_addr, abi=file['abi'])
    # deployed_contract = w3.eth.contract(address=contract_addr, bytecode=file['bytecode'], abi=file['abi'])

    print(f'contract bytecode: {deployed_contract.bytecode}')
    print(f'contract abi: {deployed_contract.abi}')

    # call view function
    get_res = deployed_contract.functions.get().call()
    print(f'call function `get` result: {get_res}')
    
    # build public function transaction
    set_value = 4
    build_tx = deployed_contract.functions.set(set_value).buildTransaction({
        "nonce": w3.eth.get_transaction_count(acc.address),
        "chainId": 3,
        'gas': 70000,
        'maxFeePerGas': w3.toWei('2', 'gwei'),
        'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
    })
    print(f'call function `set`: {build_tx}')
    
    # signature transaction
    signature_use_priv(build_tx)
    
    get_res = deployed_contract.functions.get().call()
    print(f'call function `get` result: {get_res}')
    

test_contract()

