einkaufsliste = []
while True:
   neuerArtikel=input("Was möchten Sie hinzufügen  ") 
   einkaufsliste.append(neuerArtikel)
   for element in einkaufsliste:
      print("-" + element)
