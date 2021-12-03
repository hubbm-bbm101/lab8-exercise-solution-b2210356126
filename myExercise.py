with open('student.txt') as f:
    line = f.readlines()
    info = dict(x.split(':') for x in line)
arg = input().split(',')
for i in arg:
    try: print(f'Name: {i}, University: {info[i]}', end='')
    except KeyError: print(f'No record of \'{i}\' found')
