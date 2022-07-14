import sys

oper_order = {'(': 2, ')': 2, '+': 1, '-': 1, '*': 0, '/': 0}

seq = sys.stdin.readline().strip()
paren_flag = 0
post_seq = []
oper_stack = []

for i in seq:
    if ord(i) >= ord('A') and ord(i) <= ord('Z'):
        post_seq.append(i)
    else: 
        if oper_order[i] != 2:
            while(oper_stack and oper_order[i] >= oper_order[oper_stack[-1]]):
                post_seq.append(oper_stack.pop())
            oper_stack.append(i)
        
        elif i=='(':        # (의 order값이 가장 크므로, )가 나오기 전까지 oper_stack에 계속 쌓이게 된다.
            oper_stack.append(i)
        
        else:       # when i==')'
            while(oper_stack[-1] != '('):
                post_seq.append(oper_stack.pop())
            oper_stack.pop()        # '(' 제거

while(oper_stack):
    post_seq.append(oper_stack.pop())

print(''.join(post_seq))
        