import math

def exeInverseCarre():
    nb=input("Entrer le nombre")
    nb=int(nb)
    additionInverseCarre(0,nb)

def additionInverseCarre(total,limite,actuel=1):
    if(actuel>limite):
        print("Total : ",total)
        if(total<=(pow(math.pi,2)/6)):
            print("Proximité à la limite : ", total/(pow(math.pi,2)/6)*100,"%")
        else:
            print("Proximité à la limite : ", (pow(math.pi, 2) / 6) / total * 100, "%")
        return
    total+=1/pow(actuel,2)
    additionInverseCarre(total,limite,actuel+1)
