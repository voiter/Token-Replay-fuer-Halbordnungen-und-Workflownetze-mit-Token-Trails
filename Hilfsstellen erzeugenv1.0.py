#Dieses Programm erzeugt aus einem gelabelten Netz (ohne Hilfsvariablen) ein gelabeltes Netz mit Hilfsvariablen.
#Einlesen und Auslesen.py diente hier als Basis

#https://www.youtube.com/watch?v=sATGr9ffB28 15:10
import json
print('Beginn')
pfad = "C:/Users/Anwender/Desktop/Abschlussarbeit (gesichert)/Netze/für die Masterarbeit/Neuer Ordner/WFN mit Loop ABCBCBFG-E-D funktionierend soll fehlerhaft sein BC Loop.json"

#"C:/Users/Anwender/Desktop/Abschlussarbeit (gesichert)/Netze/für die Masterarbeit/Neuer Ordner/Halbordnung ABCEBCB-FG-D funktionierend soll fehlerhaft sein.json"
#"C:/Users/Anwender/Desktop/Abschlussarbeit (gesichert)/Netze/für die Masterarbeit/Halbordnung ABC-FG-B-D funktionierend.json" #"C:/Users/Anwender/Downloads/Figure-15.json" #C:/Users/Anwender/Desktop/Abschlussarbeit (gesichert)/Netze/für die Masterarbeit/Sequenz ABCFGBD funktionierend.json

json_daten = open(pfad,'r').read()
#json_daten = open("C:/Users/Anwender/Desktop/Abschlussarbeit (gesichert)/Netze/Figure-1 (8) - Spezifikation ABCBD - Basic.json", 'r').read()
#Test mit gelabeltem Netz
#json_daten = open("C:/Users/Anwender/Downloads/Figure-1 (7) - Spezifikation ABBB als beschriftetes WFN.json", 'r').read()

python_daten = json.loads(json_daten)

#gelabeltes Netz mit Hilfsstellen wird gespeichert im gleichen Ordner und entsprechend benannt, somit überschreibt sich die json-Datei nicht immer.
pfadohneEndung = pfad[:-5]
###################################file = open('Hilfsvariable.json','w')###################################
file = open(pfadohneEndung + ' Hilfsvariable.json','w')

#Hier werden die alten Stellen mit den Hilfsstellen genannt in der *.json-Datei
file.writelines('{\n\t "places": [\n\t')

for x in range(len(python_daten['places'])-1):
    file.writelines('"' + python_daten['places'][x] + '", ')
x = x + 1
file.writelines('"' + python_daten['places'][x] + '",')

#Hier wird an den Hilfsstellen gebastelt. Jede Transition erhält zwei Hilfsstellen, eine eingehende und eine ausgehende.
for x in range(len(python_daten['transitions'])-1):
    file.writelines('"' + python_daten['transitions'][x] + 'in"' + ', ')
    file.writelines('"' + python_daten['transitions'][x] + 'out"' + ', ')
x = x + 1
file.writelines('"' + python_daten['transitions'][x] + 'in"' + ', ')
file.writelines('"' + python_daten['transitions'][x] + 'out"\n')

file.writelines('\t],\n')

#Hier werden die Transitionen unbearbeitet übernommen
file.writelines('\n\t"transitions": [\n')

for x in range(len(python_daten['transitions'])-1):
    file.writelines('\t"' + python_daten['transitions'][x] + '", ')
x = x + 1
file.writelines('"' + python_daten['transitions'][x] + '"\n\t],\n')

#Hier werden die Kanten aus der *.json-Datei übernommen
#https://www.youtube.com/watch?v=eesV_i3ZlIc
file.writelines('\n\t"arcs": {\n\t')

Kantengewichte = list(python_daten['arcs'].values())

liste_python_daten = list(python_daten['arcs'])

Liste = list(liste_python_daten)

for x in range(len(liste_python_daten)):
    file.writelines('\t"' + liste_python_daten[x] + '": ' + str(Kantengewichte[x]) + ", \n" )


#Hier werden zusätzlich die Hilfsstellen verbunden mit den Kanten zu den entsprechenden Transitionen
for x in range(len(python_daten['transitions'])-1):
    file.writelines('"' + python_daten['transitions'][x] + 'in,' + python_daten['transitions'][x] + '"' + ': 1,' + '\n\t')
    file.writelines('"' + python_daten['transitions'][x] + ',' + python_daten['transitions'][x] + 'out"' + ': 1, ' + '\n\t')
x = x + 1
file.writelines('"' + python_daten['transitions'][x] + 'in,' + python_daten['transitions'][x] + '"' + ': 1,' + '\n\t')
file.writelines('"' + python_daten['transitions'][x] + ',' + python_daten['transitions'][x] + 'out"' + ': 1 ' + '\n')
file.writelines('\t},\n')

#Actions werden übernommen
file.writelines('\n\t"actions": [\n\t')
for x in range(len(python_daten['actions'])-1):
    file.writelines('"' + python_daten['actions'][x] + '", ')
x = x + 1
file.writelines('"' + python_daten['actions'][x] + '"\n\t],\n')

#Hier werden die Labels hinzugefügt.
file.writelines('\n\t"labels": {\n\t')
Transitionsliste = list(python_daten['transitions'])


for x in range(len(list(python_daten['transitions']))-1):
    file.writelines('\t"' + python_daten['transitions'][x] + '": ' + '"' + str( python_daten['labels'][Transitionsliste[x]]) + '", \n' )
x = x + 1
file.writelines('\t"' + python_daten['transitions'][x] + '": ' + '"' + str( python_daten['labels'][Transitionsliste[x]]) + '"' )
file.writelines('\n\t},\n')

#Marking bleibt leer, da später eine Markenverteilung berechnet wird.
file.writelines('\n\t"marking": {\n\t')
file.writelines('\n\t},\n')

#Hier werden die Stellen noch ins Layout hinzugefügt.
#Das müsste eine einfache Aufgabe sein, da es nur noch eine for-Schleife sein müsste und alles andere bereits bekannt ist.
file.writelines('\n\t"layout": {\n\t')

#hier werden die Transitionen aufgestellt
for x in range(len(python_daten['transitions'])):
    file.writelines('\t"' + python_daten['transitions'][x] + '": {\n\t"x": 149,\n\t"y": 405\n\t}' + ',\n ')

#hier werden die Stellen aufgestellt
for x in range(len(python_daten['places'])):
    file.writelines('\t"' + python_daten['places'][x] + '": {\n\t"x": 149,\n\t"y": 405\n\t}' + ',\n ')

#hier werden die Hilfsstellen aufgestellt
for x in range(len(python_daten['transitions'])-1):
    file.writelines('\t"' + python_daten['transitions'][x] + 'in": {\n\t"x": 149,\n\t"y": 405\n\t}' + ',\n ')
    file.writelines('\t"' + python_daten['transitions'][x] + 'out": {\n\t"x": 149,\n\t"y": 405\n\t}' + ',\n ')
x = x + 1
file.writelines('\t"' + python_daten['transitions'][x] + 'in": {\n\t"x": 149,\n\t"y": 405\n\t}, \n')
file.writelines('\t"' + python_daten['transitions'][x] + 'out": {\n\t"x": 149,\n\t"y": 405\n} \n\t')
file.writelines('\t\n')
file.writelines('\n\t}\n')
file.writelines('}')
file.close()
print(pfadohneEndung, ' Hilfsvariable.json wurde erfolgreich erstellt.')