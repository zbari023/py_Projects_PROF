def no_repait(sentence):
    w=sentence.split(' ')
    new_Out=[]
    for i in w:
        if i in new_Out:
            continue
        else:
            new_Out.append(i)
    print(new_Out)
no_repait('My name is is is Bari')