input_string = input()
input_list = []

for i in input_string:
    input_list.append(i)

if len(input_string) % 2 == 1:
    length = int((len(input_string) - 1)/2)
    input_list.pop()
else:
    length = int((len(input_string) - 2)/2)
    input_list.pop()
    input_list.pop()

while length > 0:
    if input_list[:length] == input_list[length:]:
        print(len(input_list))
        break
    else:
        length -= 1
        input_list.pop()
        input_list.pop()