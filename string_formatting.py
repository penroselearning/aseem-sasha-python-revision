name = "David"
course = "Python"
website = "learntocode.penroselearning.com"

print(name,"registered for the",course,"course on",website,"in the year 2021.")

# f -string formatting 

# rules of using f-string formatting

# 1. before starting the quotations, we put an 'f' letter before the string. this is an indicator that we're using the f-string formatting
# 2. enclose variable names in curly brackets {}

print("\nWith F-String Formatting")
print(f"{name} registered for the {course} course on {website} in the year 2021.")

customer_name = "Deacon"

greeting = f'''
Dear {customer_name},

Thank you for taking our yearly membership. 
Hope you enjoy your time with us!
'''

print(greeting)

# thousand seperator

amount = 15231653

print(f"Amount: ${amount:,}")

# character spaces

print(f"{'Name':20} Amount")
print(f"{customer_name:20}${amount:,}")