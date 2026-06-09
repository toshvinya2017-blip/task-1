print("select the operation that you would like to perform")
print("1-addition")
print("2-subtraction")
print("3-multiplication")
print("4-dividion")

operation = input()
 
if operation=='1':
   num1=input("enter the first number:")
   num2=input("enter the second number:")
   if(num1.isnumeric and num2.isnumeric):
     sum=int(num1)+int(num2)
     print("the addition of two number is:",sum)
   else:
        print("please enter the valid number")
elif operation=="2":
   num1=input("enter the first number:")
   num2=input("enter the second number:")
   if(num1.isnumeric and num2.isnumeric):
     sub=int(num1)-int(num2)
     print("the subtraction of two number is:",sub)
   else:
        print("please enter the valid number")
elif operation=="3":
    num1=input("enter the first number:")
    num2=input("enter the second number:")
    if(num1.isnumeric and num2.isnumeric):
     mul=int(num1)*int(num2)
     print("the multiplication of two number is:",mul)
    else:
        print("please enter the valid number")
elif operation=="4":
   num1=input("enter the first number:")
   num2=input("enter the second number:")
   if(num1.isnumeric and num2.isnumeric):
     div=int(num1)/int(num2)
     print("the divition of two number is:",div)
   else:
        print("please enter the valid number")
else:
    print("please select the valid number")

