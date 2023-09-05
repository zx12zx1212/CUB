def count_num(n):
    number = 0
    for i in range(1, n+1):
        if '3' not in str(i):
            number += 1
    return number


input = 100
print(f'為 {input} 人中的第 {count_num(input)} 順位！')