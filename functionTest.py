phone = '403-333(333) 333'
charToRemove = " -()"
for i in charToRemove:
    phone = phone.replace(i, '')

print(phone)
phone = '4031112222'
areaCode = phone[0:3]
telephonePrefix = phone[3:6]
lineNumber = phone[6:10]
print(areaCode)
print(telephonePrefix)
print(lineNumber)
