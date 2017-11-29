accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

# Create function that returns the name and balance of cash on an account

# Create function that transfers an amount of cash from one account to another
# it should have three parameters:
#  - from account_number
#  - to account_number
#  - amount to transfer
#
# Print "404 - account not found" if any of the account numbers don't exist

def nameBal(account):
    back = "404 - account not found"
    for i in accounts:
        if i.get('account_number') == account:
            back = i.get('client_name'), i.get('balance')
    return back

def transfer(acc_from, acc_to, amount):
    test = False
    for i in range(len(accounts)):
        if accounts[i]['account_number'] == acc_from:
            a = i
            test = True
        if accounts[i]['account_number'] == acc_to:
            b = i
            test = True
    if test:
        accounts[a]['balance'] -= amount
        accounts[b]['balance'] -= amount
        return "Transaction done!"
    else:
        message = "404 - account not found"
    return message


print(nameBal(43546731))
print(transfer(43546731, 11234543, 1))
for i in accounts:
    print(i)