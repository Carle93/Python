#entradas con retorno de un str
num = input (" ingresa un numero: ")
print (type( num))

#entradas con retorno de dato int
num_1 = int(input ("ingresa un numero: "))
print (type( num_1))

#operadores Logicos and, or , not en python 
num_2 = 5 > 4 and 6 < 8
print (num_2) 

# or ( uno de las expresiones es verdadera)
num_3 = 5 > 6 or 6 > 4
print (num_3)

# not  ( en este caso la expresion es verdadera y nos )
num_4 = not 6 <  5
print (num_4)
#Operadores relacionales > < =
cadena = "ABC" < "A"
cadena_ = "A"  < "B"
cadena_1= "B"  >  "A"
cadena_2=  "C" != "D"
cadena_3 = "D"  == "D"
print (cadena , cadena_ , cadena_1 , cadena_2, cadena_3)

#operadores de asignacion 
edad =  45
print (edad)
edad += 5 
print (edad)
edad *= 3
print (edad)
edad_ = 6
print (edad_)
edad_ %= 2
print (edad_)

