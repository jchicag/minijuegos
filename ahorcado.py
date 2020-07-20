import time #winsound
import os
import random
x=1
b=1
u=1
r=2
#def sonido(): #para sonido q se usa cuando identifica un error
    #winsound.Beep(2349,400)
#def sonido_bien(): #para sonido q se usa cuando identifica un error
    #winsound.Beep(587,400)
#def borrarpan(): #borrar pantalla
    #if os.name==("posix"):
     #   os.sistem("clear")
    #elif os.name== "ce" or os.name=="nt" or os.name =="dos":
     #   os.system("cls")
while x==1:
    u=1
    while r==2:
        #borrarpan()
        palabras2=["BERSERK","ESPLENOMEGALIA","QUUINCALLA","VESANIA","SUMMUN","ALCUZA","INFIBULACION","JAYAN","AGUDO","ATAXIA","ATROFIA"]
        palabras3=["HOLA","CALCULO","PROGRAMACION","JUAN","LISTA","POKEMON","TALLER","LEON","INTRODUCCION","NUMERO","ESTADO","CORRECTO","NOMBRE","ADIOS","CAMINANDO","DURMIENDO","CANSADO","FELIZ","CIRCUITO","CORRIENTE","VOLTAJE","TENSION","MONTAÑA","HABLAR","JUGAR","ESTACIONAR"]
        print()
        print("BIENVENIDO A NUESTRO AHORCADO")
        print("No dejes morir a Don palitos")
        print()
        inicio=input("Que desea hacer?, jugar solo(marque 1) con amigos (marque 2): ")
        if inicio =="1":
            g=input("modo facil(marque 1), modo dificil(marque 2): ")
            if g=="2":
                
                escoja=int(input("digame un numero entre 0 y 10: "))
                if escoja>10 or escoja<0:
                    print()
                else:
                    palabra=list(palabras2[escoja])
                    x=2
                    r=1
            elif g=="1":
                
                escoja=int(input("digame un numero entre 0 y 25: "))
                if escoja>25 or escoja<0:
                    print()
                else:
                    palabra=list(palabras3[escoja])
                    x=2
                    r=1
        elif inicio =="2":
                      palabras=input("Porfavor ingrese la palabra para el ahorcado solo en mayuscula y sin caracteres raros: ")
                      palabra=list(palabras)
                      x=2
                      r=1
        else:
            print("no marco correctamente")
            input("Enter para volver al inicio")
    for i in palabra:
            if i not in("ABCDEFGHIJKLMNOPQRSTVUWXYS"):
                    u=2
                   # sonido()
                    break
            else:
                    y=2
                    r=2
                    s=2
                    f=2
                        
    if u==2:
            x=1
    else:
            b=2

                        
                        
        
while b==2:
        horca= ["      |AYUDA__/",
                "              /",
                "              /",
                "              /",
                "              /",
                "              /",
                "              /",
                "              /",]
        ahorcado=["      |AYUDA__/",
                  "     (°__°)   /",
                  "       |      /",
                  "      /|\     /",
                  "     / | \    /",
                  "      / \     /",
                  "     |   |    /",
                  "     |   |    /",]

       
        letras_usadas=[]
        resultado=[]
        fallos=int(0)
        for i in range(len(palabra)):
            resultado.append("*")

        while f==2:
                if resultado==palabra:
                       # borrarpan()
                        print("GANASTEEEEE")
                        print("La palabra era", "".join(palabra))
                        input("Enter para continuar")
                        x=1
                        b=1
                        y=1
                        f=1
                        u=2
                        break
                if fallos == 8:
                       # borrarpan()
                        print("NO QUIERO MORIRRRRRR ;(")
                        print("Te queda solo una oportunidad")
                        input("Enter para continuar")
                if fallos > 8:
                       # borrarpan()
                        print("Has perdido :(")
                        print("La palabra era", "".join(palabra))
                        input("Enter para continuar")
                        x=1
                        b=1
                        y=1
                        f=1
                        u=2
                        break
                
              #  borrarpan()
                print("*****COMENSEMOS******")
                print("*********************")
                print()
                print("Para ganar tienes que cambiar todas los * del final, por las letras corespodientes.")
                print("Si pones una letra incorrecta te dira cuantos fallos vas y si pones la correcta cambiara el * por la letra")
                print()
                for i in range(fallos):
                        print(ahorcado[i])
                for i in range(len(horca)-fallos):
                        print(horca[i+fallos])
                print()
                #mostrar el resultado
                print("     ", end=" ")
                for i in resultado:
                        print(i, end=" ")
                print()
                print()
                
                letra=input("Cual crees que es la letra que va en los *(en mayuscula porfa)")
                letras_validas=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                while y==2:
                        if len(letra) != 1:
                                print("solo una letra")
                                break
                        elif letra not in (letras_validas):
                                print("no esta en mayuscula o no es una letra. intenta de nuevo")
                                break
                        elif letra in letras_usadas:
                                print("esta ya la usaste")
                                break
                        else:
                                letras_usadas.append(letra)
                                break
                

                for i in range(len(palabra)):
                        if palabra[i] == letra:
                                resultado[i] = letra
                                #sonido_bien()
                if letra not in palabra:
                        fallos +=1
                       # sonido()
                        print("llevas:", fallos, "fallos")
                        input("Enter para continuar")
                print()
                print()
print("a.Snake")
print("b.Ping Pong")
print("c.Ahorcado")
print("d.Triki")
print("e.salir")
