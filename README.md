# Banking-System-using-Object-Oriented-Programming-in-Python

**🌟 Exciting Python Project: Building a Banking System with OOP 🌟**

In this project, I developed a fully functional banking system using Object-Oriented Programming (OOP) principles. Let me break it down for you:

**1. Class Structure:**
- **`BankAccount`:** This class represents a basic bank account. It handles functionalities like checking balance, depositing funds, withdrawing funds (with error handling for insufficient balance), and transferring funds between accounts.
  
- **`InterestRewardsAcct` (Inherits from `BankAccount`):** An enhanced bank account with an added feature where deposits accrue interest at a rate of 5% upon deposit.

- **`SavingsAcct` (Inherits from `InterestRewardsAcct`):** A specialized savings account that includes a withdrawal fee of ₹5 for each transaction.

**2. Key Features & Highlights:**
- **Account Initialization:** Creating new bank accounts with an initial balance and account name, printing out account details upon creation.
  
- **Deposit:** Adding funds to an account, including an interest reward for specific account types.
  
- **Withdrawal:** Deducting funds from an account, with proper checks for sufficient balance and handling of withdrawal fees for specific account types.
  
- **Transfer:** Transferring funds between accounts, ensuring that the transaction is valid and updating both sender and receiver account balances accordingly.

**3. User Interactions in Main Function:**
- Setting up multiple bank accounts (`Dave`, `Sara`, `Jim`, `Blaze`) with different functionalities and balance levels.
  
- Performing a variety of transactions:
  - Deposits, withdrawals, and transfers between accounts.
  - Demonstrating the inheritance structure and overridden methods in action.

**4. What You Can Learn:**
This project offers a hands-on demonstration of OOP concepts in Python:
- Class inheritance and method overriding.
- Exception handling for managing errors during transactions.
- Encapsulation for organizing and managing account functionalities.

**5. Why This Matters:**
Understanding OOP through real-world examples like this banking system project is crucial for aspiring developers. It illustrates how to design and implement scalable and modular solutions using Python.
