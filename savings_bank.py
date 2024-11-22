def calculate_savings(initial_savings, monthly_deposit, months):
    total_savings = initial_savings + (monthly_deposit * months)
    return total_savings

initial_savings = 1000
monthly_deposit = 500
months = 12
print(calculate_savings(initial_savings, monthly_deposit, months))