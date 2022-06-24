import sys

N = int(sys.stdin.readline())
num = 1

seq_list = []
num_stack = []
calc_list = []
success_flag = 1

for i in range(N):
    seq_list.append(int(sys.stdin.readline()))

for seq_num in seq_list:

    while(num<=seq_num):
        calc_list.append('+')
        num_stack.append(num)
        num = num + 1
    
    if num_stack[-1]==seq_num:
        num_stack.pop()
        calc_list.append('-')
    elif num_stack[-1]>seq_num:
        print("NO")
        success_flag = 0
        break

if success_flag != 0:
    for i in calc_list:
        print(i)
