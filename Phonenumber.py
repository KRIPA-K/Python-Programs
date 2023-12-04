import re
def is_phoneno(numstr):
    if len(numstr)!=12:
        return False
    else:
        for i in range (len(numstr)):
            if(i==3 or i==7):
                if numstr[i]!='-':
                    return False
            else:
                if(numstr[i].isdigit()==False):
                    return False
    return True
def chkphoneno(numstr):
    regex='\d{3}-\d{3}-\d{4}$'
    if re.match(regex,numstr):
        return True
    else:
        return False
ph_num=input("Enter a phone number:")
print("Without using regular expression")
if is_phoneno(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")
print("With using regular expression")
if chkphoneno(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")
