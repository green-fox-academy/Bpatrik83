'use strict';

var accounts = [
    { 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
    { 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
    { 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

// Create function that returns the name and balance of cash on an account

// Create function that transfers an amount of cash from one account to another
// it should have three parameters:
//  - from account_number
//  - to account_number
//  - amount of cash to transfer
//
// Log "404 - account not found" if any of the account numbers don't exist to the console.


function checkAccounts(accountNumber) {
    for (let i = 0; i < accounts.length; i++) {
        if (accounts[i].account_number === accountNumber) {
            return true;
        }
    }
    return false
}

console.log(checkAccounts(11234543));

function returnAccounts(accountNumber) {
    for (let i = 0; i < accounts.length; i++) {
        if (accounts[i].account_number === accountNumber) {
            return `Name: ${accounts[i].client_name}, Balance: ${accounts[i].balance}`;
        }
    }
    return '404 - account not found!'
}

function cashTransfer(fromAccountNumber, toAccountNumber, amountOfCash) {
    if (checkAccounts(fromAccountNumber) && checkAccounts(toAccountNumber)) {
        accounts.map(account => account.account_number === fromAccountNumber ? account.balance -= amountOfCash : 0);
        accounts.map(account => account.account_number === toAccountNumber ? account.balance += amountOfCash : 0);
        return 'Transaction done!'
    } else {
        return '404 - account not found!'
    }
}

console.log(returnAccounts(11234543));
console.log(cashTransfer(11234543, 23456311, 99.2));
console.log(accounts);