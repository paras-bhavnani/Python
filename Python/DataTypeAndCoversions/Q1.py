word1 = 'w3resource'
word2 = 'w3'
word3 = 'w'

def task1(word):
    answer = word[0:2] + word[len(word) - 2:len(word)]
    if len(answer) < 4:
        print('Empty String')
    else:
        print(answer)
task1(word1)
task1(word2)
task1(word3)