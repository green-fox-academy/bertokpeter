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
def your_account(account_list):
    the_account = int(input("Please input your 8-digit account number: "))
    be_in_database = False
    for i in account_list:
        if i["account_number"] == the_account:
            be_in_database = True
            print(i["client_name"] + " " + str(i["balance"]))
    if not be_in_database:
        print("404 - account not found")
your_account(accounts)
def transfer(account_list):
    from_account_number = int(input("Please input the 8-digit account number you want to trasnfer from: "))
    to_account_number = int(input("Please input the 8-digit account number you want to trasnfer to: "))
    amount_to_transfer =  int(input("Please input the amount you want to trasnfer: "))
    be_in_database1 = False
    be_in_database2 = False
    for i in account_list:
        if i["account_number"] == from_account_number:
            be_in_database1 = True
            for j in account_list:
                if j["account_number"] == to_account_number:
                    be_in_database2 = True
                    i["balance"] = i["balance"] - amount_to_transfer
                    print(i["client_name"] + " " + str(i["balance"]))
                    j["balance"] = j["balance"] + amount_to_transfer
                    print(j["client_name"] + " " + str(j["balance"]))
    if not be_in_database1 or not be_in_database2:
        print("404 - One of the account numbers you entered is not in our database")
transfer(accounts)