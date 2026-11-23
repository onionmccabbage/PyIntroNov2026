j = 'hello'
k = 32
l = 66.5

s = [j, k, l]

for i in s:
    if type(i) in (int, float):
        print('number')
    else:
        print('not a number')