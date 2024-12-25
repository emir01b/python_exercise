x = int(input("Bir sayı girin: "))
toplam = 0
if x > 0:
    for i in range( 0 , x+1 ):
        if i % 3 == 0 or i % 5 == 0:
            toplam += i
else:
    toplam = 0
print(toplam)
