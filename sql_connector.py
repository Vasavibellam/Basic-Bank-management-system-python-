import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Vasu@210706',
        database='bank_db'
    )

def create_account():
    user_name = input('Enter Account holder"s name: ')
    balance = float(input('Enter the initial balance: '))

    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO accounts (name, balance) VALUES (%s, %s)"
    cursor.execute(query, (user_name, balance))
    conn.commit()

    print("Account Created Successfully")

    cursor.close()
    conn.close()

# Test connection properly
try:
    conn = get_connection()
    print("Connected to MySQL successfully")
    conn.close()
except mysql.connector.Error as err:
    print("Connection failed:", err)

##create_account()

def deposit():
    account_id = input("Enter the account number:")
    amount = int(input("Enter the amount to be deposited:"))

    conn = get_connection()
    cursor = conn.cursor()
    
    query = "Update accounts set balance = balance + %s where account_id = %s"
    cursor.execute(query, (amount, account_id))
    conn.commit()
    print("Amount Deposited Successfully")

    cursor.close()
    conn.close()

##deposit()

def withdraw():
    account_id = input("Enter the account number:")
    amount = int(input("Enter the amout to withdraw:"))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("Select balance from accounts where account_id = %s", (account_id,))
    data = cursor.fetchone()  ##fetchall return a list and fetchone returns only one record.
    
    
    if data[0] >= amount:
        query = "update accounts set balance = balance - %s where account_id = %s"
        cursor.execute(query, (amount, account_id))
        conn.commit()
        print('Amount withdrawn successfully!!')
    else:
        print("Insufficient Funds")

    cursor.close()
    conn.close()

##withdraw()

def check_balance():
    account_id = input("Enter account number:")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("Select * from accounts where account_id = %s", (account_id,))
    data = cursor.fetchone()
    print("Account Number:", data[0])
    print("Customer Name:", data[1])
    print("Available balance:", data[2])

    cursor.close()
    conn.close()

##check_balance()

def view_account():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("Select * from accounts")
    data = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    for i in data:
        print(i)

##view_account()

while True:
    print('----------Bank System----------')
    print('Enter 1 to Create Bank Account')
    print('Enter 2 to Deposit Amount')
    print("Enter 3 for withdraw")
    print("Enter 4 to check balance")
    print("Enter 5 to view all accounts")
    print("Enter 6 to Exit")

    user_inp = input('Enter the Value:')

    if user_inp == '1':
        create_account()
    elif user_inp == '2':
        deposit()
    elif user_inp == '3':
        withdraw()
    elif user_inp == '4':
        check_balance()
    elif user_inp == '5':
        view_balance()
    elif user_inp == '6':
        print("----------Thank You for using our service----------")
        break
    else:
        print("Invalid Input")
        break


    

    



