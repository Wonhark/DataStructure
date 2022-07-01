import sys

N = int(sys.stdin.readline())
seq = sys.stdin.readline().split()
for i in range(N):
    seq[i] = int(seq[i])

nge_list = [-1 for _ in range(N)]
temp_stack = []     # list of indexes, seq[index]가 내림차순

temp_stack.append(0)
for i in range(1,N):
    if seq[i] > seq[temp_stack[-1]]:
        while(temp_stack and seq[i] > seq[temp_stack[-1]]):
            nge_list[temp_stack.pop()] = seq[i]
        temp_stack.append(i)
    else: 
        temp_stack.append(i)

print(' '.join(map(str, nge_list)))