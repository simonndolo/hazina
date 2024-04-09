def calculate_emi(principal, annual_interest_rate, duration_months):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    emi = (principal * (monthly_interest_rate + (monthly_interest_rate / (((1 + monthly_interest_rate) ** duration_months) - 1))))
    return emi

def calculate_interest(principal, monthly_interest_rate):
    return principal * monthly_interest_rate

# Taking input from user
principal = float(input("Enter loan amount: "))
annual_interest_rate = float(input("Enter annual interest rate (%): "))
duration_months = int(input("Enter loan duration in months: "))

monthly_interest_rate = annual_interest_rate / 12 / 100
emi = calculate_emi(principal, annual_interest_rate, duration_months)

print("Equated Monthly Installment (EMI): {:.2f}".format(emi))

print("\nRepayment Schedule:")
print("{:<10} {:<15} {:<15} {:<20}".format("Month", "Principal", "Interest", "Outstanding Principal"))
remaining_principal = principal
total_interest = 0
for month in range(1, duration_months + 1):
    interest_payment = calculate_interest(remaining_principal, monthly_interest_rate)
    principal_payment = emi - interest_payment
    remaining_principal -= principal_payment
    total_interest += interest_payment
    print("{:<10} {:<15.2f} {:<15.2f} {:<20.2f}".format(month, principal_payment, interest_payment, remaining_principal))

print("\nTotal Interest Paid: {:.2f}".format(total_interest))
