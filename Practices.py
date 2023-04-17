print("¡ Hello World!")
num = 15
print ( num )
#Usando la misma variable num para cambiar su valor 
num = 8
print ( num )
num + 2
print (num + 2)

#Definir tipo de datos 
 #Type de datos Int ( numeros enteros tanto positivos como negativos, incluyendo el cero)
print (type(-2))
print (type(8))

#Type de datos Float ( representa numero con decimales tanto positivos como negativos incluyendo 0,0
print (type(1.5))
print (type(-4.0))

#Type datos boolenos ( son los valores de True or False, estos valores deben comenzar con la 1era letra en mayuscula)
print (type(True))
print (type(False))

#Type datos String ( Str, textos)
Name = " Paula"
print( type( Name))
#La funcion len se utiliza para medir la longitud del Str
print (len( Name))
#En los string podemos indexar partes de una cadena 
print (Name [3])
#Slicing ( rebanadas tambien se puede llamar una porcion de un string)
print (Name [1:5])
#Slicing saltando espacios 
print (Name[1:6:2])