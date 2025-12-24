# Basic-Bank-management-system-python-
This project is a console-based Bank Management System developed using Python and MySQL. It simulates basic banking operations such as account creation, deposit, withdrawal, balance enquiry, and viewing all accounts, while maintaining persistent data storage using a MySQL database.

Features:

Create Bank Account:
Allows users to create a new bank account by entering the account holder’s name and initial balance.

Deposit Amount:
Enables users to deposit money into an existing account.

Withdraw Amount:
Allows users to withdraw money with insufficient balance validation.

Check Account Balance:
Displays account number, customer name, and current balance.

View All Accounts:
Shows details of all existing bank accounts stored in the database.

Menu-Driven Interface:
User-friendly console menu for easy navigation.

Technologies Used:
Programming Language: Python
Database: MySQL
Database Connector: mysql-connector-python
Concepts Used:
Functions
Loops
Conditional statements
SQL CRUD operations
Exception handling

Database Structure:-
Database Name: bank_db
Table Name: accounts

CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    balance DECIMAL(10,2)
);

How to Run the Project

Install MySQL and create the database and table.

Install MySQL connector:

pip install mysql-connector-python


Update database credentials in the code:

host='localhost'
user='root'
password='your_password'
database='bank_db'


Run the Python file:

python bank_system.py
