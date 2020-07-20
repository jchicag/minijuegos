##Menu minijuegos
print("Bienvenido a tus minijuegos, estos son tus juegos")
a=print("a.Snake")
b=print("b.Ping Pong")
c=print("c.Ahorcado")
d=print("d.Triki")
e=print("e.salir")
z=str(input("Ingrese la letra del juego que desea jugar: "))
while z!="e":
    if z=="a":
        import snake
        z=str(input("Ingrese la letra del juego que desea jugar: "))
    else:
        if z=="b":
            import pong
            z=str(input("Ingrese la letra del juego que desea jugar: "))
        else:
            if z=="c":
                import ahorcado
                z=str(input("Ingrese la letra del juego que desea jugar: "))
            else:
                if z=="d":
                    import triki
                    z=str(input("Ingrese la letra del juego que desea jugar: "))

if z=="e":
    print("Gracias por jugar")
input("Oprime enter para cerrar")
