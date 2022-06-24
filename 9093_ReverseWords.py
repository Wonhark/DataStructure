import sys

T = int(sys.stdin.readline())
sentences = []
for i in range(T):
    sentence = sys.stdin.readline()[::-1].split()   # [::-1] -> 전체범위(:)를 역순으로 읽는다.
                                                    # .split() -> str to list
    sentence.reverse()                              # list 내부 요소 reverse order
    sentences.append(sentence)

for sentence in sentences:
    print(' '.join(sentence))                       # .join()으로 list to str
