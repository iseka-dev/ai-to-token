// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";

contract MyNFT is ERC1155 {

    struct NFT {
        string name;
        address owner;
    }

    uint256 private _idCounter;

    mapping (uint256 => NFT) private _nfts;

    constructor() ERC1155("https://testnet-api.opensea.io/api/v1/{id}.json") {}

    function mint(string memory name) public returns (uint256) {
        uint256 id = _idCounter++;
        _nfts[id] = NFT(name, msg.sender);
        _mint(msg.sender, id, 1, "");
        return id;
    }

    function getName(uint256 id) public view returns (string memory) {
        return _nfts[id].name;
    }

    function getOwner(uint256 id) public view returns (address) {
        return _nfts[id].owner;
    }
}