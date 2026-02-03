account={
   1001:{"name":"SAVKAR Sanjay","pin":2310,"Balance":10000000},
   1002:{"name":"Theerthan","pin":1234,"Balance":100}
}
acc_no=1100
def new_account(acc):
    global acc_no
    name=input("Enter the name: ")
    pin=int(input("Enter the 4-digit pin: "))
    balance=int(input("Enter the balance: "))

    acc_no +=1
    acc[acc_no]={
        "name":name,
        "pin":pin,
        "Balance":balance
    }
    print("Your account is created ✅✅")
    print("Your account number is: ",acc_no)

def login(a):
    id=int(input("Enter your account number: "))
    if id in a:
        pi=int(input("Enter the PIN: "))
        if a[id]["pin"] == pi:
            print("Logged in sucessfully")
            print("Account Details: ")
            print("Name: ",a[id]["name"])
            print("Balance: ",a[id]["Balance"])
            return id
        else:
            print("Incorrect PIN")
            return None
    else:
        print("Wrong ID")
        return None

def deposit(accou,m): 
    if m is not None:
        money=int(input("Enter the amount to be deposied: "))
        accou[m]["Balance"] += money
        print("Amount DEPOSITED Sucesssfully...")

def withdraw(accou,m):
    if m is not None:
        money=int(input("Enter the amount to WITHDRAW: "))
        if money>accou[m]["Balance"]:
            print("Insufficient Balance")
        else:
            accou[m]["Balance"] -= money
            print("Amount WITHDRAWN Sucessfuly...")

def check_bal(aacov,m):
    if m is not None:
        print("Current Balance is: ",aacov[m]["Balance"])

l = None

while True: 
    print("1.Create new account\n2.Login to your account\n3.Exit")
    n=int(input("Enter your choice: "))
    if n==1:
        new_account(account)
        print("\n")
      
    elif n==2:
         l=login(account)
         print("\n")
       
         print("SECOND MENU:\n1.WITHDRAW\n2.DEPOSIT\n3.CHECK BALANCE\n4.EXIT")
         c=int(input("Enter your choice: "))
         match c:
          case 1:
            withdraw(account,l)
            print("\n")
          case 2:
             deposit(account,l)
             print('\n')
          case 3:
             check_bal(account,l)
             print("\n")
          case 4:
             print("EXITING...")
             print("\n")
             break
          case _:
            print("Invalid choice..")  
            print("\n")
            
    elif n==3:
       print("EXITING...")
       break
    else:
       print("Invalid Choice..")