def merge_sort(list1,l,r):
    if l>=r:
        return
    m=(l+r)//2
    merge_sort(list1,l,m)
    merge_sort(list1,m+1,r)
    merge(list1,l,r,m)
def merge(list1,l,r,m):
    l_sub=list1[l:m+1]
    r_sub=list1[m+1:r+1]
    lindex=rindex=0
    sorted_index=l
    while(lindex<len(l_sub) and rindex<len(r_sub)):
        if(l_sub[lindex]<=r_sub[rindex]):
            list1[sorted_index]=l_sub[lindex]
            lindex+=1
        else:
            list1[sorted_index]=r_sub[rindex]
            rindex+=1
        sorted_index+=1
    while(lindex<len(l_sub)):
        list1[sorted_index]=l_sub[lindex]
        lindex+=1
        sorted_index+=1
    while(rindex<len(r_sub)):
        list1[sorted_index]=r_sub[rindex]
        rindex+=1
        sorted_index+=1
list1=[]
n=int(input("Enter the list size:"))
print("Enter ",n," elements")
for i in range(n):
    ele=int(input())
    list1.append(ele)
merge_sort(list1,0,len(list1)-1)
print("After sorting:")
print(list1)

def insertion_sort(list1):
    for i in range(1,len(list1)):
        temp=list1[i]
        j=i-1
        while(j>=0 and list1[j]>temp):
            list1[j+1]=list1[j]
            j=j-1
        list1[j+1]=temp
list1=[]
n=int(input("Enter the list size:"))
print("Enter ",n," elements")
for i in range(n):
    ele=int(input())
    list1.append(ele)
insertion_sort(list1)
print("After sorting:")
print(list1)
