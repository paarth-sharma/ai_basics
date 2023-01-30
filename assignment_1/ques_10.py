class ques_10:
    def ci(self, p,r,t):
        a = p*((1+pow((r/100), t)))
        ci = a-p
        return ci

class comp_int:

    def comp(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t
        comp = ques_10.ci(self, p, r, t)
        print('Compound interest is: ' + str(comp))
    

# making child class's object
obj = comp_int()
p = float(input("enter principal amount:"))
r = float(input("enter rate of interest:"))
t = float(input("enter time:"))

obj.comp(p, r, t)

