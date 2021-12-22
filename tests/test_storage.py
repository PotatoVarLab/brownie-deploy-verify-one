# -*- coding: utf-8 -*-

import pytest
from brownie import accounts
from brownie import SolidityStorage


@pytest.fixture
def contract():
    # fixture and use local account
    return accounts[0].deploy(SolidityStorage)


def test_get(contract):
    get_values = contract.get()
    print(f'test get value: {get_values}')
    assert get_values == 4
    

def test_set(contract):
    get_values = contract.get()
    assert get_values == 4 
    contract.set(5)
    get_values = contract.get()
    assert get_values == 5
    

