#while
#while esp_booleana

num = 1
while num <=10:
    print(num)
    num+=1

#for -> iterable
my_string = "Hola"  
for letter in my_string:
    print(letter, end=' ')
print()
my_lista=("a","b","c",12)
for item in my_lista:
    print(item,end=' ')
print()
#funtion range()
#range (fin)
for i in range(3):
    print(i)
print()
#range(ini:fin)
for i in range(3,6):
    print(i)
print()
#range(ini:fin:step)
for i in range(1,11,2):
    print(i)