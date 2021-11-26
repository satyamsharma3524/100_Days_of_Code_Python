current_age = int(input("What is your current age?"))
total_age = 60

age_left = total_age-current_age

months_left = age_left*12
weeks_left = age_left*52
days_left = age_left*365

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

