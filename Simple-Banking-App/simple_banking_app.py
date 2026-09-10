balance = 0.0
kyc_documents = {}

def check_balance():
    print(f"Your Current balance is : {balance}")
    print("=============================")
    

def deposite(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print("Cannot deposite a negative amount.")
        print("=============================")

def withdraw(amount):
    global balance
    if amount < 0:
        print("Cannot withdraw a negative or zero amount")
        print("=============================")
    elif amount > balance:
        print("Cannot Withdraw. Insufficient balance.")
        print("=============================")
    else:
        balance -= amount

def update_kyc(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc():
    if len(kyc_documents) == 0:
        print("KYC not done")
        print("=============================")
    for doc in kyc_documents:
        print(f"{doc}: {kyc_documents[doc]}")
        print("=============================")


if __name__ == "__main__":
    print("=============================")
    print("!!Welcome to Muradpur bank!!")
    print("=============================")

    while True:
        print("1. Check your balance")
        print("2. Deposite an amount")
        print("3. Withdraw an amount")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")
        choice = input("Enter your choice (1-6) : ")
        print("===========================")

        if choice == '1':
            check_balance()
        elif choice == '2':
            amt = float(input("Enter the amount to deposite: "))
            deposite(amt)
            print(f"Amount {amt} deposited Successfully!!")
            print("=============================")
        elif choice == '3':
            amt = float(input("Enter the amount to withdraw: "))
            withdraw(amt)
            print(f"Amount {amt} withdrawn Successfully!!")
            print("=====================================")
        elif choice == '4':
            if len(kyc_documents) == 0:
                print("KYC not done")
            check_kyc()
        elif choice == '5':
            kyc_docs = {}
            n_documents = int(input("Enter the number of documents you want to add: "))
            for i in range(n_documents):
                key = input("Enter the document type: ")
                value = input("Enter the documents number: ")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print(f"KYC updated!")
        elif choice == '6':
            print("Quitting, have a nice day!!")
            break
        else:
            print("Invalid choice!!! Re-try.")
            print("=============================")
    print()
    print("Thanking For banking with us!")
