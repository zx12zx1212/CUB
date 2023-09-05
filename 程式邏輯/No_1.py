def reverse(input):
    output = []
    for i in input:
        number = 0
        while i > 0:
            number =  i % 10 +number * 10
            i = i // 10
        output.append(number)
    return output

input = [35, 46, 57, 91, 29]
print(reverse(input))