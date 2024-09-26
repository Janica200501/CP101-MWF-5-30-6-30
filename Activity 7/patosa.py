# Function to calculate bonus based on years in service and office
def calculate_bonus(years, office):
    if office == "IT":
        if years >= 10:
            return 10000
        else:
            return 5000
    elif office == "ACCT":
        if years >= 10:
            return 12000
        else:
            return 6000
    elif office == "HR":
        if years >= 10:
            return 15000
        else:
            return 7500
    else:
        return "Invalid office"

# Input from user
name = input("Enter your name: ")
years = int(input("Enter years in service: "))
office = input("Enter office (IT, ACCT, HR): ").upper()

# Calculate and display bonus
bonus = calculate_bonus(years, office)
if isinstance(bonus, int):
    print(f"Hi {name}, your bonus is: {bonus}")
else:
    print(bonus)
