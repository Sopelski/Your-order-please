'''Each word in the string will contain a single number. This number is the position the word should have in the result.
Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).'''

def order(sentence):
    if len(sentence) == 0:
        return ""
    sentence = sentence.split(" ")
    lista = []
    liczba = 1
    while len(sentence) != len(lista):
        for s in sentence:
            for a in s:
                if a.isdigit() and int(a) == liczba:
                    lista.append(s)
                    liczba += 1
    lista = " ".join(lista)



    return print(lista)

order("4of Fo1r pe6ople g3ood th5e the2")
