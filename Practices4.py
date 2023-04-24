import sys


#Tuplas 
colors = ( "red" , "blue" , "green" , 155 , 1/2 , "CH")
print ( colors [2])

print ("red" in colors)

#diccionarios 
edad = { "a" : 45, "b" : 52, "c" : 15 }
print (edad ["c"])

edad ["a"] = 35
print (edad)
sys.exit ("detener")

del edad ["b"]
print (edad)

