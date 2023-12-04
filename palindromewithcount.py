a=int(input("Enter a number:"))
temp=a
rev=0
while temp>0:
    dig=temp%10
    rev=rev*10+dig
    temp=temp//10
if rev==a:
    print("Given number is palindrome")
else:
    print("Given number is not palindrome")
for i in range(0,10):
    temp=a
    count=0
    while temp>0:
        dig=temp%10
        temp=temp//10
        if dig==i:
            count=count+1
    if count>0:
        print("The number ",i," occurs ",count," times")
