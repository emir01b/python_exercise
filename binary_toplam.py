#iki sayıyı toplayıp sonrasında binary sayı sistemine çevirip yazdıran python kod bloğu
def binary(sum):
    dizi = []

    while sum > 0:
        dizi.append(sum % 2)
        sum = sum // 2
    dizi.reverse()

    return ''.join(map(str, dizi))

sum = 9 + 6
sonuc = binary(sum)

print ("Giriş: (9, 6) --> Çıkış: binary",sonuc)
