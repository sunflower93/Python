"""   2
str = raw_input()
a = str.split()
m = (int)(a[0])
n = (int)(a[1])
if m % n == 0:
    print "YES\n"
else:
    print "NO\n"
"""
"""3
n = (int)(raw_input())
a = 0
for i in range(2, n, 1):
    if n % i == 0:
        a += 1
if a == 0:
    print "YES\n"
else:
    print "NO\n"
"""
# l = []
# d = {'num': 0, 'sqrt': 0}
# for x in [1, 2, 3]:
#     d['num'] = x
#     d['sqrt'] = x*x
#     l.append(d)
#     print l
"""4
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
input_num = int(raw_input())
print (fibonacci(input_num))
"""
"""5
input_str = raw_input()
strs = input_str.split()
m = int(strs[0])
n = int(strs[1])
t = int(strs[2])
matrix = []
for i in range(0, m, 1):
    i_raw = raw_input()
    iarrays = i_raw.split()
    list = []
    for j in range(0, n, 1):
        list.append(int(iarrays[j]))
    matrix.append(list)
print matrix
if t == 0:
    for i in range(0, m, 1):
        matrix[i].reverse()
    # for i in range(0, m, 1):
    #     for j in range(0, n, 1):
    #         print matrix[i][j],' ',
    #     print '\n',
    for i in range(0, m, 1):
        ans_string = ''
        for j in range(0, n, 1):
            ans_string = ans_string + str(matrix[i][j]) + ' '
        print ans_string
elif t == 1:
    for i in range(0, m / 2, 1):
        t = matrix[i]
        matrix[i] = matrix[m - 1 - i]
        matrix[m - 1 - i] = t
    # for i in range(0, m, 1):
    #     for j in range(0, n, 1):
    #         print matrix[i][j],' ',
    #     print '\n',
    for i in range(0, m, 1):
        ans_string = ''
        for j in range(0, n, 1):
            ans_string = ans_string + str(matrix[i][j]) + ' '
        print ans_string
"""

