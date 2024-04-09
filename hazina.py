def calculate_loan_repayments(loan_amount, annual_interest_rate, duration_months):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    principal_payment = loan_amount / duration_months
    remaining_loan_amount = loan_amount
    total_interest_paid = 0  # Initialize total interest paid
    
    print("{:<10} {:<15} {:<15} {:<20} {:<15}".format("Month", "Principal", "Interest", "Outstanding Principal", "Installment Amount"))
    for month in range(1, duration_months + 1):
        interest_payment = remaining_loan_amount * monthly_interest_rate
        total_interest_paid += interest_payment  # Update total interest paid
        total_payment = principal_payment + interest_payment
        remaining_loan_amount -= principal_payment
        print("{:<10} {:<15.2f} {:<15.2f} {:<20.2f} {:<15.2f}".format(month, principal_payment, interest_payment, remaining_loan_amount, total_payment))
    
    print("\nTotal Interest Paid: {:.2f}".format(total_interest_paid))  # Print total interest paid

# Taking input from user
loan_amount = float(input("Enter loan amount: "))
annual_interest_rate = float(input("Enter annual interest rate (%): "))
duration_months = int(input("Enter loan duration in months: "))

calculate_loan_repayments(loan_amount, annual_interest_rate, duration_months)
