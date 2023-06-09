# functionimput -> retorna string

name = input('Como te llamas? \n')
age = int (input('Cuántos años tienes? \n'))
futuro = int (input('Cuantos años más?\n'))

print("Hola "+name)
print("En "+str(futuro)+" años tendrás "+str(age+futuro))

# Format Strings
"""
    Hola Jesher , en 3 años tendras 21 
"""
text_complete="Hola {}, en {} años tendás {} años"
print(text_complete.format(name,futuro,age+futuro))
print(f"Hola {name} , en {futuro} años tendras {age + futuro} años")
