
def narsisistik_sayi_mi(sayi):
    basamaklar = [int(digit) for digit in str(sayi)]
    basamak_sayisi = len(basamaklar)
    toplam = sum(digit ** basamak_sayisi for digit in basamaklar)
    
    return 'doğru' if toplam == sayi else 'yanlış'

sayi = int(input("Lütfen bir sayı girin: "))
print(narsisistik_sayi_mi(sayi))

