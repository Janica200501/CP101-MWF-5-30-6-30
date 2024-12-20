name = input("janica")
age = input("19")
# Use an f-string to format the output
print(f"Hello, {janica}! You are {19} years old.")


item = "Orange"
count = 10
# Use the .format() method
sentence = "I bought {10} {Orange} today.".format(count, item)
print(sentence)


city = "US"
temperature = 25
# Use the % operator
print("The temperature in %s is %d degrees Celsius." % (city, temperature))
