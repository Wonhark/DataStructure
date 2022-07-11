import sys

N = int(sys.stdin.readline())
seq = sys.stdin.readline().strip()
num_list = []
for i in range(N):
    num_list.append(int(sys.stdin.readline()))

oper = {'+': (lambda x,y: y+x),
        '-': (lambda x,y: y-x),
        '*': (lambda x,y: y*x),
        '/': (lambda x,y: y/x)}

num_stack = []
for i in seq:
    n = ord(i) - ord('A')
    if n>=0 and n<N:
        num_stack.append(num_list[n])
    else:
        num_stack.append(oper[i](num_stack.pop(), num_stack.pop()))

print('%.2f' %num_stack.pop())
    