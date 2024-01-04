import re 

name = '1Hello'
lower = False
upper = False
num = False
if re.search(r"[a-z]", name):
    # print('hi')
    lower = True
if re.search(r'[A-Z]', name):
    upper = True
if bool(re.search(r'[0-9]$',name)):
    num = True

print(lower,upper, num)
# if not re.search(r'[\d$]',name): 

# x = re.search(r"[a-z]", name)
# y = re.search(r'[A-Z]', name)
# z = re.search(r'[\d$]',name)
# print(z)
# if z.group(0):
#     print('yes')
# print(x.group(0), y.group(0))
