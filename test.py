
 
    # if amount less than zero == payed with credit card && -= 5 else it was income >= 0 date format yyyy-mm-dd step1
    # 1. create an array A
    # 2.agssin the date format
    # 3.create a variable that caluclate the final balance
    
    
def transaction(self, amount, date):
        if amount < 0:
            print(f"Card payment of {-amount} on {date}")
            self.balance -= amount
        else:
            print(f"Incoming transfer of {amount} on {date}")
            self.balance += amount
            return amount

    # caluclate final balance
def calculate_final_balance(transactions):
        balance = 0
        for amount in transactions:
            balance += amount
        return balance
#list of transcation 
transactions=[]



    


