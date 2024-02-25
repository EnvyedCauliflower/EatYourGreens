x1 = int(input("Ist Kriterium 1 erfüllt? (0 oder 1)"))
x2 = int(input("Ist Kriterium 2 erfüllt? (0 oder 1)"))
x3 = int(input("Ist Kriterium 3 erfüllt? (0 oder 1)"))
x4 = int(input("Ist Kriterium 4 erfüllt? (0 oder 1)"))
x5 = int(input("Ist Kriterium 5 erfüllt? (0 oder 1)"))

#w1=1
#w2=1
#w3=1
#w4=1
#w5=1
#Reiz= w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5
#Schwellenwert = 1

Reiz=x1+x2+x3+x4+x5
Schwellenwert=3.5

if(Reiz > Schwellenwert):
    print("Der Film ist gut")
else:
    print("Der Film ist nicht gut")
