#ÉRETLENEK
if __name__ == '__main__':
    try:
        class Jatek:
            def __init__(self,sor):
                try: 
                    szervezo, jatek_nev, jatekosok_szam, esemeny_szam  = sor.strip().split(";")
                    self.szervezo   = szervezo
                    self.jatek_nev  = jatek_nev
                    self.jatekosok_szam  = jatekosok_szam
                    self.esemeny_szam    = esemeny_szam
                except ValueError:
                    maradek = sor.strip()
                    if maradek[0].isupper() == True: 
                        self.nev = maradek
                    else:
                        self.jatek = maradek
                                


        class Fogadasok:
            def __init__(self,sor):
                fogado_neve, melyik_jatek, tet, kire_fogad, esemeny_szam, fogadas_merete = sor.strip().split(";")
                self.fogado_neve    = fogado_neve
                self.melyik_jatek   = melyik_jatek
                self.tet            = tet
                self.kire_fogad     = kire_fogad
                self.esemeny_szam   = esemeny_szam
                self.fogadas_merete = fogadas_merete



        print("""1-     Játék létrehozása
2-     Fogadás leadása
3-     Játék lezárása
4-     Lekérdezések
5-     Kilépés""")

        menu = input("A menüpont kiválasztásához nyomja meg a megfelelő számot! ")

        #---1. Játék létrehozása
        if menu == "1": 
            szervezo    = input("Ki a szervező?\t")
            jatek_neve  = input("Mi a játék megnevezése? (egyedinek kell lennie)\t")
            jatekosok_szam_tarolo = []
            esemeny_szam_tarolo   = []
            while True:
                print("Simma 'Enter' gobal a következő pontra ugorhat")
                jatekosok_szam = input("Kik az alanyok? (különböznek egymástól)\t")
                if jatekosok_szam == "":
                    break
                else:
                    jatekosok_szam_tarolo.append(jatekosok_szam)
            while True:
                print("Simma 'Enter' gobal a következő pontra ugorhat")
                esemeny_szam = input("Mik az események?\t")
                if esemeny_szam == "":
                    break
                else:
                    esemeny_szam_tarolo.append(esemeny_szam)
            try:
                with open("jatekok.txt","a",encoding="UTF-8") as f:
                    f.write(f"{szervezo};{jatek_neve};{len(jatekosok_szam_tarolo)};{len(esemeny_szam_tarolo)}\n")
                    for i in jatekosok_szam_tarolo:
                        f.write(f"{i}\n")
                    for i in esemeny_szam_tarolo:
                        f.write(f"{i}\n")
                    jatekok = [Jatek(sor) for sor in f]
            except:
                pass       
            
        #---2. Fogadás leadása     
        if menu == "2":
            try:
                with open("fogadasok.txt","r",encoding="UTF-8") as f:
                    fogadasok = [Fogadasok(sor) for sor in f]
            except:
                pass
                
            tarolo = 0
            fogado_neve     = input("Fogadó neve:\t")
            melyik_jatek    = input("Melyik játkra fogadsz?\t")
            tet             = input(f"Hány pontal fogadsz a '{melyik_jatek}'?\t")
            kire_fogad      = input("kire fogadsz?\t")
            esemeny_szam    = input("Milyen tipusu fogadást teszel? pl: (sebessége, kimenete,hibát dob, stb...)\t")
            fogadas_mertek  = input("Mennyire fogadsz?\t")
            try:
                for sor in fogadasok:
                    if fogado_neve == sor.fogado_neve and esemeny_szam == sor.esemeny_szam and kire_fogad == sor.kire_fogad:
                        tarolo = 1
            except: 
                pass
        
            if tarolo == 0:    
                with open("fogadasok.txt","a",encoding="UTF-8") as f:
                    f.write(f"{fogado_neve};{melyik_jatek};{tet};{kire_fogad};{esemeny_szam};{fogadas_mertek}\n")

                        
        #---3. Játék lezárása     
        if menu == "3":
            jatekos     = input("Adja meg a nevét! ")
            jatek_neve  = input("Adja meg jaték nevét! ")
            with open("jatekok.txt","a",encoding="UTF-8")as f:
                jatek = [Jatek(sor) for sor in f]
            for sor in jatek: 
                while True:   
                    if jatekos == sor.szervezo and sor.jatek_nev == jatek_neve:
                        try:
                            for sor in jatek:
                                if jatekos == sor.szervezo and jatek_neve == sor.jatek_nev:
                                    lezaras = True
                                    with open("eredmenyek.txt","a",encoding="UTF-8")as f:
                                        try:
                                            tarolo = 0
                                            for sor in jatek:
                                                if tarolo == 0:
                                                    f.write(sor.jatek_nev)
                                                    tarolo = 1
                                                for i in range(len(esemeny_szam_tarolo)):    
                                                    try:
                                                        for sor in jatek:
                                                            f.write(f"{sor.nev};{sor.jatek_nev}")
                                                    except:
                                                        pass    
                                                    
                                        except:
                                            pass
                        except:
                            pass
        #---4. Lekérdezések     
        if menu == "4":
            pass

        #---5. Kilépés     
        if menu == "5":
            pass
        
            
    except:
        pass
