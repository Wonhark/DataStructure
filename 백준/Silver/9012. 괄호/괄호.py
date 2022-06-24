import sys

T = int(sys.stdin.readline())
sentences = []
for i in range(T):
    sentences.append(sys.stdin.readline())

for i in range(T):
    sentence = sentences[i]
    n = len(sentence)
    stack_num = 0

    for j in range(n):
        if stack_num<0:
            continue
        
        if sentence[j]=='(':
            stack_num = stack_num+1
        elif sentence[j]==')':
            stack_num = stack_num-1
    if stack_num==0:
        print("YES")
    else:
        print("NO")
    stack_num = 0
