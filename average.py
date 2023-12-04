a=int(input("Enter the first test marks"))
b=int(input("Enter the second test marks"))
c=int(input("Enter the third test marks"))
if(a>b and c>b):
    avg=(a+c)/2
elif(b>a and c>a):
    avg=(b+c)/2
else:
    avg=(a+b)/2
print("Average of given test marks is: ",avg)
