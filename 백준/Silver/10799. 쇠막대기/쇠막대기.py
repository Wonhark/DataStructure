import sys

seq = sys.stdin.readline().strip()

stick_stack = []
laser_flag = False
stick_num = 0

for i in range(len(seq)):
    if seq[i]=='(':
        stick_stack.append(i)
        laser_flag = True
    else:
        if laser_flag:
            stick_stack.pop()
            stick_num = stick_num + len(stick_stack)
            laser_flag = False
        else: 
            stick_stack.pop()
            stick_num = stick_num + 1

print(stick_num)