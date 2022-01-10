#Assuming that we have some email addresses in the"username@companyname.com" format, please write program to print the
#user name of a given email address. Both user names and company namesare composed of letters only.

import re

my_str = input("Enter your email: ")
pattern = re.compile(r'(\w+)@(\w+)(\.\w{3})')
name = pattern.sub(r'\1',my_str)
print("Name: "+name)
company = pattern.sub(r'\2',my_str)
print("Company: "+company)

#name_i = re.findall('^\w+',my_str)
#compant_i = re.findall('\w+',my_str)
#print(name_i[0])
#print(compant_i[1])
