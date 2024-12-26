x = input("bir sayı girin = ")
def en_yuksek_sayi(x):
    
    rakamlar = list(str(x)) # hepsini lisyte kaydet
   
    rakamlar.sort(reverse=True)  # azalan sırala
    
    return int(''.join(rakamlar)) #tam sayı
print("En büyük sayı :", en_yuksek_sayi(x))
