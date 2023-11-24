#Golden Bits
szotar = {
  "esemenyek" : []
}
with open("fogadasok.txt", "w") as file:
  file.truncate(0)
with open("eredmenyek.txt", "w") as file:
  file.truncate(0)
with open("jatekok.txt", "w") as file:
  file.truncate(0)

class FogadasJatek:
  def __init__(self):
      pass

  def menu(self):
      while True:
          print("\nMenü:")
          print("1- Játék létrehozása")
          print("2- Fogadás leadása")
          print("3- Játék lezárása")
          print("4- Lekérdezések")
          print("5- Kilépés")

          valasztas = input("Válassz egy menüpontot: ")

          if valasztas == "1":
              self.jatek_letrehozasa()
          elif valasztas == "2":
              self.fogadas_leadasa()
          elif valasztas == "3":
              self.jatek_lezarasa()
          elif valasztas == "4":
              self.lekerdezesek()
          elif valasztas == "5":
              break
          else:
              print("Érvénytelen választás. Kérlek válassz újra.")

  def jatek_letrehozasa(self):
      szervezo = input("Ki a szervező? ")
      jatek_neve = input("Mi a játék megnevezése? (egyedinek kell lennie) ")
      alanyok = input("Kik az alanyok? (különböznek egymástól, vesszővel elválasztva) ").split(',')
      esemenyek = input("Mik az események? (vesszővel elválasztva) ").split(',')

      jatek_adatok = f"{szervezo};{jatek_neve};{len(alanyok)};{len(esemenyek)}\n"
      jatek_adatok += '\n'.join(alanyok) + '\n'
      jatek_adatok += '\n'.join(esemenyek) + '\n'

      with open("jatekok.txt", 'a') as file:
          file.write(jatek_adatok)

      print("Játék létrehozva!")

  def fogadas_leadasa(self):
      nev = input("Fogadó neve: ")
      pontok_file = "pontok_" + nev + ".txt"

      try:
          with open(pontok_file, 'r') as file:
              pontszam = int(file.read())
      except FileNotFoundError:
          pontszam = 100

      print(f"{nev} jelenlegi pontszáma: {pontszam}")

      jatekok_file = "jatekok.txt"
      print(esemenyek)
      esemenyek = []
      try:
          with open(jatekok_file, 'r') as file:
              for line in file:
                  if line.startswith(nev):
                      esemeny_start_index = line.find(';') + 1
                      esemenyek_str = line[esemeny_start_index:].strip()
                      esemenyek.extend(esemenyek_str.split(';'))
      except FileNotFoundError:
          print("Nincs elérhető játék.")
          return

      if esemenyek:
          print("\nEsemények:")
          for index, elem in enumerate(esemenyek, start=1):
              print(f"{index}- {elem}")

          esemeny_idx = int(input("Válassz egy eseményt a fenti listából (szám szerint): ")) - 1

          if 0 <= esemeny_idx < len(esemenyek):
              jatek_neve = esemenyek[esemeny_idx]
              alany = input("Add meg az alany nevét: ")
              ertek = input("Add meg az értéket: ")
              tet = int(input("Add meg a tétet (pozitív egész szám): "))

              if pontszam >= tet:
                  pontszam -= tet
                  fogadas_adatok = f"{nev};{jatek_neve};{tet};{alany};{ertek}\n"
                  with open("fogadasok.txt", 'a') as file:
                      file.write(fogadas_adatok)

                  print(f"\nFogadás sikeresen rögzítve!\n"
                        f"Jelenlegi pontszámod: {pontszam}")
              else:
                  print("Nincs elegendő pontod a fogadás leadásához.")
          else:
              print("Érvénytelen választás.")
      else:
          print("Nincs elérhető esemény a fogadás leadásához.")

  def jatek_lezarasa(self):
      szervezo = input("Add meg a szervező nevét: ")
      jatek_neve = input("Add meg a játék megnevezését: ")

      jatek_idx = -1
      try:
          with open("jatekok.txt", 'r') as file:
              for i, line in enumerate(file):
                  if szervezo + ';' + jatek_neve in line:
                      jatek_idx = i
                      break
      except FileNotFoundError:
          print("Nincs elérhető játék.")
          return

      if jatek_idx != -1:
          eredmenyek = []
          for alany in input(f"Add meg az eredményeket {jatek_neve}-re (vesszővel elválasztva): ").split(','):
              for esemeny in input(f"Add meg az eseményeket {alany}-ra (vesszővel elválasztva): ").split(','):
                  eredmeny = input(f"Add meg az eredményt {alany} - {esemeny} párosra: ")
                  szorzo = float(input(f"Add meg a szorzót {alany} - {esemeny} párosra: "))
                  eredmenyek.append(f"{alany};{esemeny};{eredmeny};{szorzo}\n")

          with open("eredmenyek.txt", 'a') as file:
              file.write(f"{szervezo};{jatek_neve}\n")
              file.write(''.join(eredmenyek))

          print("Játék lezárva és eredmények rögzítve!")
      else:
          print("Nem található ilyen játék a listában.")

  def lekerdezesek(self):
      while True:
          print("\nLekérdezések:")
          print("1- Ranglista")
          print("2- Játék statisztika")
          print("3- Fogadási statisztika")
          print("4- Vissza a főmenübe")

          lekerdezes = input("Válassz egy lekérdezést: ")

          if lekerdezes == "1":
              self.ranglista()
          elif lekerdezes == "2":
              self.jatek_statisztika()
          elif lekerdezes == "3":
              self.fogadasi_statisztika()
          elif lekerdezes == "4":
              break
          else:
              print("Érvénytelen választás. Kérlek válassz újra.")

  def ranglista(self):
      try:
          with open("rangsor.txt", 'r') as file:
              rangsor = file.read()
          print("\nRanglista:")
          print(rangsor)
      except FileNotFoundError:
          print("Nincs elérhető ranglista.")

  def jatek_statisztika(self):
      try:
          with open("jatekok.txt", 'r') as file:
              jatekok = file.read()
          print("\nJátékok:")
          print(jatekok)
      except FileNotFoundError:
          print("Nincs elérhető játék.")

      jatek_neve = input("Válassz egy játékot a fenti listából: ")
      jatek_idx = -1
      try:
          with open("jatekok.txt", 'r') as file:
              for i, line in enumerate(file):
                  if jatek_neve in line:
                      jatek_idx = i
                      break
      except FileNotFoundError:
          print("Nincs elérhető játék.")
          return

      if jatek_idx != -1:
          fogadasok_szama = 0
          tetek_osszege = 0
          nyeremenyek_osszege = 0

          try:
              with open("fogadasok.txt", 'r') as file:
                  for sor in file:
                      _, jatek, tet, _, _, _ = sor.strip().split(';')
                      if jatek == jatek_neve:
                          fogadasok_szama += 1
                          tetek_osszege += int(tet)
          except FileNotFoundError:
              print("Nincs elérhető fogadás.")

          try:
              with open("eredmenyek.txt", 'r') as file:
                  for _ in range(2):  # Az első két sor a játék neve és az alanyok/eredmények
                      next(file)
                  for sor in file:
                      _, _, _, szorzo = sor.strip().split(';')
                      nyeremenyek_osszege += float(szorzo)
          except FileNotFoundError:
              print("Nincs elérhető eredmény.")

          print(f"\nJáték statisztika {jatek_neve}-re:")
          print(f"Fogadások száma: {fogadasok_szama}")
          print(f"Feltett tétek összege: {tetek_osszege} pont")
          print(f"Nyeremények összege: {nyeremenyek_osszege} pont")
      else:
          print("Nem található ilyen játék a listában.")

  def fogadasi_statisztika(self):
      try:
          with open("jatekok.txt", 'r') as file:
              jatekok = file.read()
          print("\nJátékok:")
          print(jatekok)
      except FileNotFoundError:
          print("Nincs elérhető játék.")

      jatek_neve = input("Válassz egy játékot a fenti listából: ")
      jatek_idx = -1
      try:
          with open("jatekok.txt", 'r') as file:
              for i, line in enumerate(file):
                  if jatek_neve in line:
                      jatek_idx = i
                      break
      except FileNotFoundError:
          print("Nincs elérhető játék.")
          return

      if jatek_idx != -1:
          print(f"\nFogadási statisztika {jatek_neve}-re:")
          try:
              with open("fogadasok.txt", 'r') as file:
                  for sor in file:
                      _, jatek, _, alany, _, _ = sor.strip().split(';')
                      if jatek == jatek_neve:
                          print(f"{alany} fogadott")
          except FileNotFoundError:
              print("Nincs elérhető fogadás.")
      else:
          print("Nem található ilyen játék a listában.")

if __name__ == "__main__":
  jatek = FogadasJatek()
  jatek.menu()