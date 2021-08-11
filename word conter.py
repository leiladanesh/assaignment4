def counter_word(string):
    a = 0
    for i in range (len(string )):
        if(( string [i] != ' ' and i == 0) or (string [i-1] ==' ')):
            a += 1

    return a

str= input('enter the sentence:')
count = counter_word(str)
print(count )