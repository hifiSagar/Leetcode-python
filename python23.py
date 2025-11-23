
#This program done by own#

print("Enter the value >>>\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")

choice=int(input("Enter the Operations >>> "))
a=int(input("Enter the first value : "))
b=int(input("Enter the Second value : "))

if choice==1:
    print("Result:",a+b)
elif choice==2:
       print("Result:",a-b)
elif choice==2:
       print("Result:",a*b)
elif choice==2:
       print("Result:",a//b)
else:
      print("You Have Enterd Wrong Option, So Please Enter Correct operation")
      
