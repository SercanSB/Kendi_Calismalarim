def asal_sayi_bul(sayi_gir):
    liste = list()

    if sayi_gir == 1:
        print("Asal değil: ", sayi)

    elif sayi_gir == 0:
        print("Asal değil: ", sayi)

    elif sayi_gir == 2:
        print("Asal Sayı:", sayi)

    else:

        for i in range(2, sayi_gir+1):

            for x in range(2, i):

                if i % x == 0:
                    break
            else:
                liste.append(i)

        print("Asal Sayı: ", liste)

        print("Asal Sayı Adedi: ", len(liste))


while True:

    sayi = input("Sayı: ")

    if sayi == "q":
        print("Program sonlandırıldı..")
        break

    else:
        sayi = int(sayi)

        asal_sayi_bul(sayi)
