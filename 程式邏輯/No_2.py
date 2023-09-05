def count(input):
    count_key = {}
    for i in input:
        if i != ' ':
            count_key[i.upper()] = count_key.get(i.upper() ,0) +1
    return count_key


input = 'Hello welcome to Cathay 60th year anniversary'
output = dict(sorted(count(input).items(), key=lambda x : x[0]))
for k , v in output.items():
    print( f'{k} : {v}')