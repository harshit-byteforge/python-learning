# this is calculator program

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

print("\n===== CALCULATOR =====")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    result = x + y
    print("Addition:", result)

elif choice == 2:
    result = x - y
    print("Subtraction:", result)

elif choice == 3:
    result = x * y
    print("Multiplication:", result)

elif choice == 4:
    if y != 0:
        result = x / y
        print("Division:", result)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid choice!")


print(" ====== Type of the result ======")
print(type(result)
      )