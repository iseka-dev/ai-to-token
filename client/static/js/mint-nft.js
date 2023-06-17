const ethereum = window.ethereum;
const smartContractAddress = "0xd9145CCE52D386f254917e481eB44e9943F39138"
console.log(smartContractAddress)
const nftButton = document.getElementById("nft-button");
console.log(nftButton)


async function connectToProvider() {
    if (window.ethereum) {
        await window.ethereum.request({ method: "eth_requestAccounts" });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        return provider;
    } else {
        throw new Error("Please install MetaMask or use a compatible Ethereum browser.");
    }
}

async function handleButtonClick() {
    try {
        console.log("Ethering...");
        const provider = await connectToProvider();
        console.log("Provider: ", provider);
        const contractAddress = "0xd9145CCE52D386f254917e481eB44e9943F39138";
        console.log("contract_ address: ", contractAddress );
        const abi = `{
            "inputs": [
                {
                    "internalType": "string",
                    "name": "name",
                    "type": "string"
                },
                {
                    "internalType": "string",
                    "name": "url",
                    "type": "string"
                }
            ],
            "name": "mint",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        }`;

        const name = "MyMessiNFT";
        const url = "https://example.com/nft-image.png";

        const contract = new ethers.Contract(contractAddress, abi, provider.getSigner());

        const result = await contract.mint(name, url);
        
        console.log("Transaction successful:", result);

    } catch (error) {
        console.error("Error:", error);
    }
};

nftButton.addEventListener("click", handleButtonClick);
