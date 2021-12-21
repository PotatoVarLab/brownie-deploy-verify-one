# -*- coding: utf-8 -*-

from brownie import accounts, config


def test_account_balance():
    deployer = accounts.add(config['wallets']['from_key'])
    print(f'address: {deployer}')
    balance = deployer.balance()
    # accounts[0].transfer(accounts[1], "10 ether", gas_price=0)
    print(f'balance: {balance}')
    assert balance >= 0
    
