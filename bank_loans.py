def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = 5000
rate = 5
time = 2
print(simple_interest(principal, rate, time))

def compound_interest(principal, rate, time):
    return principal * ((1 + rate / 100) ** time) - principal

principal = 5000
rate = 5
time = 2
print(compound_interest(principal, rate, time))