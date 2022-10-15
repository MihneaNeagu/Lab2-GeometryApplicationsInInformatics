import glm
import math
import numpy as np
import shapely.geometry.polygon

def citire_dreapta():
    l = []
    givenString = input("Dati lista, cu a,b,c separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(float(x))
    return l


def inters_dreapta(l):
    pctinters = -l[2]/l[0]
    return pctinters

def matrice_translatie(l):
    if l[0]>=l[1]:
        hk = l[0]-l[1]
        A = np.array([[1, 0, hk], [0, 1, l[1]],[0, 0, 1]])
    else:
        hk=l[1]-l[0]
        A = np.array([[1, 0, l[1]], [0, 1, hk], [0, 0, 1]])

    return A

def matrice_rotatie(l):
    panta = -l[0]/l[1]
    angle = math.atan(panta)
    B = np.array([[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])
    return B

def matrice_reflexie():
    C = np.array([[-1 , 0, 0], [0 , 1, 0], [0, 0, 1]])
    return C

def matrice_rotatie_origine(l):
    panta = -l[0] / l[1]
    angle = math.atan(panta)
    D = np.array([[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])
    return D

def matrice_translatie_poz_initiala(l):
     E = np.array([[1, 0, -l[0]], [0, 1, -l[1]], [0, 0, 1]])
     return E

def inmultire_matrice(M1, M2):
    M3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(M1)):
        for k in range(len(M2)):
            M3[i][k] = M1[i][k] * M2[i][k]
    return M3

def inmultire_5_matrici(A,B,C,D,E):
    A1=inmultire_matrice(A,B)
    A2=inmultire_matrice(A1,C)
    A3=inmultire_matrice(A2,D)
    A4=inmultire_matrice(A3,E)
    return A4

def citire_poligon():
    p = []
    givenint = int(input("Dati nr de varfuri ale poligonului: "))
    for i in range(givenint):
        a=input("Dati coordonata x a punctului: ")
        b=input("Dati coordonata y a punctului: ")
        p.append([a,b])
    return p

def reprez_matrice_poligon(p):
    a = []
    b = []
    for i in range(int(len(p))):
        a.append(p[i][0])
        b.append(p[i][1])
    aa=np.array(a)
    ba=np.array(b)
    M = np.array([aa,ba])
    return M

def main():
    while True:
        print("1. Citire dreapta: ")
        print("2. Afiseaza punctul de intersectie dintre dreapta si axa OX: ")
        print("3. Afiseaza matricea translatiei care face dreapta sa treaca prin origine: ")
        print("4. Afiseaza matricea rotatiei cu axa OX: ")
        print("5. Afiseaza matricea de reflexie fata de axa OX: ")
        print("6. Afiseaza matricea de rotatie fata de origine care aduce dreapta la directia initiala: ")
        print("7. Afiseaza matricea de translatie care aduce dreapta in pozitia initiala : ")
        print("8. Afiseaza matricea de transformare inmultind cele 5 matrice anterioare: ")
        print("9. Citirea varfurilor poligonului: ")
        print("10. Afisarea matricii omogene a poligonului dat: ")
        print("d. Afisare dreapta: ")
        print("x. Iesire")

        optiune = input("Dati optiunea: ")

        if optiune == "1":
            l = citire_dreapta()
        elif optiune == "2":
            print(inters_dreapta(l))
        elif optiune == "3":
            print(matrice_translatie(l))
        elif optiune == "4":
            print(matrice_rotatie(l))
        elif optiune == "5":
            print(matrice_reflexie())
        elif optiune == "6":
            print(matrice_rotatie_origine(l))
        elif optiune == "7":
            print(matrice_translatie_poz_initiala(l))
        elif optiune == "8":
            print(inmultire_5_matrici(matrice_translatie(l), matrice_rotatie(l), matrice_reflexie(),
                                      matrice_rotatie_origine(l),matrice_translatie_poz_initiala(l)))
        elif optiune == "9":
            p = citire_poligon()
            print(p)
        elif optiune == "10":
            print(reprez_matrice_poligon(p))
        elif optiune == "d":
            print(l[0],"*x+",l[1],"*y+",l[2])
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")

main()