# A Function that don't repeat the element in the new list
def no_repait(sentence):
    w=sentence.split(' ')
    new_Out=[]
    for i in w:
        if i in new_Out:
            continue
        else:
            new_Out.append(i)
    print(' '.join(new_Out))      # list to str

no_repait('my name is is is Bari')  # my name is Bari