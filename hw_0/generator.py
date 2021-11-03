

def meow(num = 1):
    for i in range(10):
        yield "meow "*num
        num = num*2
# Möglichkeit eins
iter = meow() #liefert mir Objekt: "Box mit vielen Elementen drin"
while True:
    try:
        next(iter) # Klopft auf die Box, damit Elemente rauskommen (Wird in for loop automatisch gemacht)
    except StopIteration:
        print("ended")
        break
#---------------------------------------------
#Möglichkeit zwei

for i in meow(): # Automatische Objekterzeugung und next-iteration
    print(i)

#-------------------------------------------------

def r(anf, end, step):
    i = anf
    while i < end:
        yield i
        i += step

#Anderer Test--------------------------------------
for i in [1,2,3,4,5,6]:
    break

def gen():
    x = 0
    for i in range(1000000000):
        x += i

def ohne():
    x = 0
    for i in [j for j in range(1000000000)]:
        x += i

timeit gen()
