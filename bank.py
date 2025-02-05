class BankAccount:
    def __init__(self, init_bal):
        self.curr_bal = init_bal
        self.transactions = []
        self.commits = []
    
    def read(self):
        print(self.curr_bal)
    
    def credit(self, amt):
        self.transactions.append(amt)
        self.curr_bal += amt
    
    def debit(self, amt):
        if amt > self.curr_bal:
            print("Insufficient Money for Debit")
        else:
            self.transactions.append(-amt)
            self.curr_bal -= amt
    
    def abort(self, transaction_index):
        if transaction_index > len(self.commits) and transaction_index <= len(self.transactions):
            transaction_amt = self.transactions[transaction_index - 1]
            self.curr_bal -= transaction_amt
            self.transactions[transaction_index - 1] = 0
    
    def rollback(self, commit_index):
        if commit_index <= len(self.commits):
            self.curr_bal = self.commits[commit_index - 1]
            self.transactions = self.transactions[:commit_index]
            self.transactions = [t for t in self.transactions if t != 0]
    
    def commit(self):
        self.commits.append(self.curr_bal)

def main():
    init_bal = int(input().strip())
    n = int(input().strip())
    
    account = BankAccount(init_bal)
    
    for _ in range(n):
        operation = input().strip().split()
        command = operation[0]
        
        if command == "read":
            account.read()
        elif command == "credit":
            amt = int(operation[1])
            account.credit(amt)
        elif command == "debit":
            amt = int(operation[1])
            account.debit(amt)
        elif command == "abort":
            transaction_index = int(operation[1])
            account.abort(transaction_index)
        elif command == "rollback":
            commit_index = int(operation[1])
            account.rollback(commit_index)
        elif command == "commit":
            account.commit()

if __name__ == "__main__":
    main()