
class New_Game():
    # A Function that don't repeat the element in the new list
    def no_repait(self,sentence):
        w = sentence.split(' ')
        new_Out = []
        for i in w:
            if i in new_Out:
                continue
            else:
                new_Out.append(i)
        print(' '.join(new_Out))  # list to str

    # new function that give us how many letter in the one element
    def w_count(self,names):
        new_out2 = []
        for i in names:
            new_out2.append(len(i))

        print(new_out2)

    # new function that give us the nummbers between 1 and 100 which it divided on x ,y
    def div_mod(self,x, y):
        new_out3 = []
        for i in range(101):
            if (i % x) == 0 and (i % y) == 0:
                new_out3.append(i)
        print(new_out3)

c1 = New_Game()
c1.no_repait('you you are awesome')


# no_repait('my name is is is Bari')  # my name is Bari
# w_count(['zaid' ,'Bari' ,'Ibrahim'])     # [4, 4, 7]
# div_mod(2,5)           # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]