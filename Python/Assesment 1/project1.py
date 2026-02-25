accounts = {}

def create_account():
    name = input("Enter account holder name: ")
    acc_no = input("Enter account number: ")
    pin = input("Set 4-digit PIN: ")
    accounts[acc_no] = {
        "name": name,
        "pin": pin,
        "balance": 0,
        "history": []
    }
    print("Account created successfully!")

def authenticate(acc_no):
    pin = input("Enter PIN: ")
    return acc_no in accounts and accounts[acc_no]["pin"] == pin

def deposit():
    acc_no = input("Enter account number: ")
    if authenticate(acc_no):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            accounts[acc_no]["balance"] += amount
            accounts[acc_no]["history"].append(f"Deposited: +{amount}")
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

def withdraw():
    acc_no = input("Enter account number: ")
    if authenticate(acc_no):
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= accounts[acc_no]["balance"]:
            accounts[acc_no]["balance"] -= amount
            accounts[acc_no]["history"].append(f"Withdrawn: -{amount}")
            print("Amount withdrawn successfully!")
        else:
            print("Invalid or insufficient balance!")

def check_balance():
    acc_no = input("Enter account number: ")
    if authenticate(acc_no):
        print("Account Holder:", accounts[acc_no]["name"])
        print("Balance:", accounts[acc_no]["balance"])

def transaction_history():
    acc_no = input("Enter account number: ")
    if authenticate(acc_no):
        print("\n--- Transaction History ---")
        for record in accounts[acc_no]["history"]:
            print(record)

while True:
    print("\n--- BANK MANAGEMENT SYSTEM ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        transaction_history()
    elif choice == "6":
        print("Thank you for using Bank Management System")
        break
    else:
        print("Invalid choice")


 # quiz game 

 
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. All of these"],
        "answer": "D"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Elon Musk", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Mark Zuckerberg"],
        "answer": "B"
    }
]

def start_quiz():
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        ans = input("Enter your answer (A/B/C/D): ").upper()
        if ans == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("\nFinal Score:", score, "/", len(questions))


while True:
    print("\n--- QUIZ GAME ---")
    print("1. Start Quiz")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        start_quiz()
    elif choice == "2":
        print("Thank you for playing Quiz Game")
        break
    else:
        print("Invalid choice")
