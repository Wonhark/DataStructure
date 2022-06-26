import sys

seq = sys.stdin.readline().strip()
N = int(sys.stdin.readline())
cursor = len(seq)
seq_len = len(seq)

left_stack = list(seq)
right_stack = []


for i in range(N):
    temp = sys.stdin.readline()
    if temp[0]=='L':
        if cursor!=0:
            cursor = cursor - 1
            right_stack.append(left_stack.pop())
    elif temp[0]=='D':
        if cursor!=seq_len:
            cursor = cursor + 1
            left_stack.append(right_stack.pop())
    elif temp[0]=='B':
        if cursor!=0:
            left_stack.pop()
            cursor = cursor - 1
            seq_len = seq_len - 1
    elif temp[0]=='P':
        left_stack.append(temp[2])
        cursor = cursor+1
        seq_len = seq_len + 1

if left_stack:
    left_str = ''.join(left_stack)
else:
    left_str = ""

if right_stack:
    right_stack.reverse()
    right_str = ''.join(right_stack)
else:
    right_str = ""

print(left_str + right_str)
