// SPDX-License-Identifier: MIT
pragma solidity ^0.8.10;

contract SolidityStorage {
    uint256 storeData = 4;

    function set(uint256 _x) public {
        storeData = _x;
    }

    function get() public view returns (uint256) {
        return storeData;
    }
}

