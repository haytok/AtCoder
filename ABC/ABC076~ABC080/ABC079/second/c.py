inputs = input()

length = len(inputs) - 1
for i in range(2 ** length):
    formula = ''
    operator = format(i, 'b').zfill(length)
    for index in range(length):
        formula += inputs[index] + ('+' if operator[index] == '0' else '-')
    formula += inputs[-1]
    if eval(formula) == 7:
        print(formula + '=7')
        break