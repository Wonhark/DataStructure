import sys

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

count = dict()
for i in seq:
    if i in count:
        count[i] += 1
    else: 
        count[i] = 1


ngf_list = [-1 for _ in range(N)]
temp_stack = []
temp_stack.append(0)
for i in range(1,N):
    if count[seq[i]] > count[seq[temp_stack[-1]]]:
        while(temp_stack and count[seq[i]] > count[seq[temp_stack[-1]]]):
            ngf_list[temp_stack.pop()] = seq[i]
    temp_stack.append(i)


print(' '.join(map(str, ngf_list)))