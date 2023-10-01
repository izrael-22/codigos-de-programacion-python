numero_Inicial = (input( " Dime el numero inicial \n"))
numero_final = (input(" Dime el nuemro final\n"))


if(numero_final.isnumeric()and numero_Inicial.isnumeric() ):
    sumatoria=0
    numero_Inicial = int (numero_Inicial)
    numero_final = int (numero_final)
    
    for numero in range(numero_Inicial,numero_final):
    #{
      print (f" No de la interacion {(numero)}")
      suma =sum(range(numero_Inicial,numero_final))
      sumatoria+=numero
    #}
    print(f" La sumetoria de {numero_Inicial} a {numero_final} es {suma}")
    print(f" La sumetoria de {numero_Inicial} a {numero_final} es {sumatoria}")
else:
    print(" Los valores utilizados no son numeros")

x="hola"
print(x.isnumeric())

y="10"
print(y.isnumeric())

