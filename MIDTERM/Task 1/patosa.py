def calculator():
   print("Welcome to the Calculator!")
   print("Select an operation:")
   print("1. 10 + 10 ")
   print("2. 10 - 5")
   print("3. 2 * 5 ")
   print("4. 20 ÷ 5")

   while True:
       choice = input("Enter choice (10 + 10 /10 - 5 / 2 * 5 / 20 ÷ 20 ) or 'q' to quit: ")

       if choice == 'q':
           print("Exiting the calculator. Goodbye!")
           break

       if choice in ['10 + 10', '10 - 5', '2 * 5', '20 ÷ 5']:
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))

       if choice == '10 + 10':
           print(f"{num1} + {num2} {num1 + num2}")
       elif choice == '10 - 5':
            print(f"{num1} - {num2} = {num1- num2}")
       elif choice == '2 * 5':
             print(f"{num1} {num2} {num1 * num2}")
       elif choice == '20 ÷ 5':  
           if num2 !=0:
              print(f"{num1} / {num2} = {num1 / num2}")
           else:
                print("Error! Division by zero.")
       else:
         print("Invalid input. Please enter a number between 1 and 4.")
          
if __name__ == "__main__":
     calculator()
