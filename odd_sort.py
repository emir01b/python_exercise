dizi = [3,4,1,6,9,5,8]

def tek_sayilari_sirala(dizi):
    tek_sayilar = sorted([sayi for sayi in dizi if sayi % 2 != 0])
    sonuc = []
    tek_index = 0
    
    for sayi in dizi:
        if sayi % 2 == 0:
            sonuc.append(sayi)
        else:
            sonuc.append(tek_sayilar[tek_index])
            tek_index += 1
            
    return sonuc

print (tek_sayilari_sirala(dizi))