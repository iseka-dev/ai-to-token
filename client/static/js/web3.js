// @ts-checkts

/*****************************************/
/* Detect the MetaMask Ethereum provider */
/*****************************************/

//import detectEthereumProvider from '@metamask/detect-provider';
//
//const provider = await detectEthereumProvider();
//
//if (provider) {
//  startApp(provider);
//} else {
//  console.log('Please install MetaMask!');
//}
//
//function startApp(provider) {
//  if (provider !== window.ethereum) {
//    console.error('Do you have multiple wallets installed?');
//  }
//}


/*********************************************/
/* Access the user's accounts (per EIP-1102) */
/*********************************************/


const ethereumButton = document.querySelector('.enableEthereumButton');
const showAccount = document.querySelector('.showAccount');

ethereumButton.addEventListener('click', () => {
  void getAccount();
});

async function getAccount() {
  const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' })
    .catch((err) => {
      if (err.code === 4001) {
        console.log('Please connect to MetaMask.');
      } else {
        console.error(err);
      }
    });
  const account = accounts[0];
  }
  /*
  if (showAccount.innerHTML === "") {
    showAccount.innerHTML = account;
    ethereumButton.innerText =  "Hide Account";
  } else {
    showAccount.innerHTML = ""
    ethereumButton.innerText = "Show Account";
  };
} */

///***********************************************************/
///* Handle user accounts and accountsChanged (per EIP-1193) */
///***********************************************************/

let currentAccount = null;
window.ethereum.request({ method: 'eth_accounts' })
  .then(handleAccountsChanged)
  .catch((err) => {
    console.error(err);
  });

window.ethereum.on('accountsChanged', handleAccountsChanged);

function handleAccountsChanged(accounts) {
  if (accounts.length === 0) {
    console.log('Please connect to MetaMask.');
  } else if (accounts[0] !== currentAccount) {
    currentAccount = accounts[0];
    showAccount.innerHTML = currentAccount;
  }
}


/**********************************************************/
/* Handle chain (network) and chainChanged (per EIP-1193) */
/**********************************************************/

const chainId = await window.ethereum.request({ method: 'eth_chainId' });

console.log(chainId, "*********************")

window.ethereum.on('chainChanged', handleChainChanged);

function handleChainChanged(chainId) {
  window.location.reload();
}


///***********************************************************/
///* Mint */
///***********************************************************/

// const ethers = require('ethers');


// // const smartContractAddress = "0xd9145CCE52D386f254917e481eB44e9943F39138";

//let params = [
//  {
//    from: currentAccount,
//    to: smartContractAddress,
//    data: []
//  }
//]


