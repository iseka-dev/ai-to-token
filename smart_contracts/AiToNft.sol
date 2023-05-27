// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC1155/extensions/ERC1155URIStorage.sol";
import "@openzeppelin/contracts/utils/Base64.sol";
import "@openzeppelin/contracts/utils/Counters.sol";


contract AiToNFT is ERC1155URIStorage {

    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct aiToNFT {
        string name;
        address owner;
    }

    mapping (uint256 => aiToNFT) private _nfts;

    constructor() ERC1155("") {}

    function mint(string memory name, string memory url) public returns (uint256) {
        // determine index for NFT
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        // Create Token URI
        // TODO: Move to a Pinata file
        string memory uri = Base64.encode(
            bytes(
                string(
                    abi.encodePacked(
                        '{"name":"', name, '",',
                        '"description":"Esta es una descripcion fija",', // Valor fijo de la descripción
                        '"image":"', url, '"}'
                    )
                )
            )
        );
        string memory tokenURI = string(
            abi.encodePacked("data:application/json;base64,", uri)
        );

        _nfts[tokenId] = aiToNFT(name, msg.sender);
        _mint(msg.sender, tokenId, 1, "");
        _setURI(tokenId, tokenURI);

        return tokenId;
    }

    function getName(uint256 id) public view returns (string memory) {
        return _nfts[id].name;
    }

    function getOwner(uint256 id) public view returns (address) {
        return _nfts[id].owner;
    }
}
