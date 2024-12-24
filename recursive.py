def negatif_sayi_toplami(dizi):
    if not dizi:
        return 0
    else:
        ilk_eleman = dizi[0]
        kalan_dizi = dizi[1:]
        if ilk_eleman < 0:
            return ilk_eleman + negatif_sayi_toplami(kalan_dizi)
        else:
            return negatif_sayi_toplami(kalan_dizi)
