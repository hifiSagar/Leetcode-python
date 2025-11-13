print("!! NOW I AM PRINTING SOME CALCULATING OPERATIONS !!\n")

print("Enter the value for >>>")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division\n")

choice = int(input("Enter your choice (1-4): "))
A = int(input("Enter the 1st value: "))
B = int(input("Enter the 2nd value: "))

if choice == 1:
    print("Result:", A + B)
elif choice == 2:
    print("Result:", A - B)
elif choice == 3:
    print("Result:", A * B)
elif choice == 4:
        print("Result:", A // B)
else:
    print("Invalid choice! Please enter a number between 1 and 4.")
    