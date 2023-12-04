def romantointeger(r):
    roman_no={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total=0
    prev=0
    for ch in r[::-1]:
        current=roman_no[ch]
        if current>=prev:
            total+=current
        else:
            total-=current
            prev=total
    return total
r=input("Enter roman number: ")
res=romantointeger(r)
print(res)
