# -*- coding: utf-8 -*-

from brownie import accounts, config
from brownie import SolidityStorage


def main():
    deployer = accounts.add(config['wallets']['from_key'])
    print(f'account: {deployer}')
    
    # verify source use publish_source=True
    SolidityStorage.deploy({"from": deployer}, publish_source=True)
    
