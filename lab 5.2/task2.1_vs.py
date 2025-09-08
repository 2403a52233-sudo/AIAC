def loan_approval(name, income, credit_score):
    if name.lower() != "john":
        print("Applicant is not John. Only John can apply in this demo.")
        return
    if income >= 30000 and credit_score >= 700:
        print("Loan approved for John.")
    else:
        print("Loan not approved for John.")

applicant_name = "John"
applicant_income = 35000
applicant_credit_score = 720

loan_approval(applicant_name, applicant_income, applicant_credit_score)