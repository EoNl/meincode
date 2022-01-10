# Mit diesem Code kann man Gegenstände, die man will einkaufen und dies zeigt es dann in einer Einkaufsliste, welche übereinander steht. 
# Man kann dieses Programm gut benutzten für den Alltag.
# Das vereinfacht das einkaufen.
einkaufsliste = []
# Die Schleife sorgt dafür das, wenn man ein Gegenstand hinzufügt es erneut fragt was für ein Gegenstand man hinzufügen will.
while True:
   neuerArtikel=input("Was möchten Sie hinzufügen  ") 
   einkaufsliste.append(neuerArtikel)
   for element in einkaufsliste:
      # Wenn man das "-" + element wird es schöner dargstellt.
      print("-" + element)
