s = str(input())

while 'B' in s:
    if s[0] == 'B':
        s=s[1:]
    s=s.replace('0B','')
    s=s.replace('1B','')

print(s)

############################

result = ''
for x in input():
    if x=='B':
        result = result[:-1]
    else:
        result += x

print(result)