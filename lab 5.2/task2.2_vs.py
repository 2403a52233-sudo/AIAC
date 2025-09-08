def loan_approval(name, salary, credit_score, loan_amount):
    if salary < 25000:
        return f"Sorry {name}, loan not approved (Salary too low)."
    elif credit_score < 650:
        return f"Sorry {name}, loan not approved (Low credit score)."
    elif loan_amount > salary * 20:
        return f"Sorry {name}, loan not approved (Loan amount too high)."
    else:
        return f"Congratulations {name}, your loan is approved!"

name = "Priya"
salary = 30000
credit_score = 720
loan_amount = 400000

print(loan_approval(name, salary, credit_score, loan_amount))
