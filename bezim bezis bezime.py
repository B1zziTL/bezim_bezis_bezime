#otvorenie suboru
subor = open("skok_do_dialky.txt","r")

#zadeklarovanie premennych a vytvorenie zoznamov
i = 0
vitaz = ""
krajiny = []
opakovane = []
pocty = []
vzdialenosti = []
naj = [0]

#rozdelenie suboru na casti a ich postupna analyza
for riadok in subor:
    riadocek = riadok.split()

    #vlozenie vsetkych krajin s opakovanim do zoznamu
    opakovane.append(riadocek[1])

    #vlozenie krajin do zoznamu bez opakovania
    if not riadocek[1] in krajiny:
        krajiny.append(riadocek[1])

    #vlozenie vzdialenosti do zoznamu    
    vzdialenosti.append(riadocek[2])
    vzdialenosti.append(riadocek[3])
    vzdialenosti.append(riadocek[4])
    vzdialenosti.append(riadocek[5])
    vzdialenosti.append(riadocek[6])

    #podmienka, ak najvacsie vzdialenosti je vacsia ako posledna zapisana
    if int(max(vzdialenosti)) > int(naj[-1]):
        #pridanie najvacsej vzdialenosti do zoznamu
        naj.append(max(vzdialenosti))

        #vlozenie mena vitaza do premennej
        vitaz = riadocek[0]

    #vycistenie zoznamu
    vzdialenosti.clear()
    
#prehladavanie v zozname krajin
for krajina in krajiny:
    #vypocitanie opakovanych krajin
    pocet = str(opakovane.count(krajina))

    #pomocna premenna
    nieco = krajiny[i]

    #vlozenie poctu krajanov do zoznamu
    pocty.append(nieco+"="+pocet)

    #zmena pomocnej premennej
    i += 1

#vypisanie pozadovanych hodnot
print("Zoznam krajín:")
print(*krajiny, sep=",")
print("Počty účastníkov:")
print(*pocty, sep=",")
print("Víťaz je:",vitaz)

#zatvorenie suboru
subor.close()
