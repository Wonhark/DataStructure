import sys

sentence = sys.stdin.readline()
tag_flag = False
word_stack = []         # reverse -> stack
tag_word = ""
result_sen = ""

sen_len = len(sentence)
for i in range(sen_len):
    temp = sentence[i]
    if temp=='<':
        tag_flag=True
        tag_word = tag_word + temp
        
    elif temp=='>':
        while(word_stack):
            result_sen = result_sen + word_stack.pop()
        tag_flag=False
        tag_word = tag_word + temp
        result_sen = result_sen + tag_word
        tag_word = ""
        
    elif (not tag_flag and temp==' ') or temp=='\n':
        while(word_stack):
            result_sen = result_sen + word_stack.pop()
        if temp==' ':
            result_sen = result_sen + temp
    
    elif tag_flag:
        tag_word = tag_word + temp
    else:
        word_stack.append(temp)

print(result_sen)
    


