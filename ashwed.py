a=int(input("Enter a number:"))
num=a
result=0
b=len(a)
while a!=0:
    digit=a%10
    result=result+digit**b
    a=a//10
if result==num:
    print("Given number is Armstrong number")
else:
    print("Given number is not Armstrong number")