'''
Basierend auf Einlesen und Auslesen.py soll diese Datei eine weitere Pythondatei schreiben, damit ein Ungleichungssystem gelöst wird.
'''

'''
"from Hello import *" importiert alle Funktionen aus Hello.py --> #print(summe([1, 2])) (am Ende) nutzt die definierte Funktion aus Hello.py hier; 
vgl. https://www.gutefrage.net/frage/wie-kann-ich-einen-python-script-mit-einem-anderem-python-script-ausfuehren
'''

#https://www.youtube.com/watch?v=sATGr9ffB28 15:10
import json

'''
gelabeltes Netz mit ohne Hilfsvariablen wird hier eingelesen
Das Netz wird u.a. dafür genutzt, damit die Kanten (Stellen,Transitionen) und (Transitionen,Stellen) gefunden werden.
Weierhin sind die beiden ausgezeichneten Stellen hier zu finden, um insgesamt die drei Zwangsbedingungen für ein sound WFN zu formulieren.
'''
pfad_gelabeltes_Netz_ohne_Hilfsvariable = "C:/Users/Anwender/Desktop/Abschlussarbeit (gesichert)/Netze/für die Masterarbeit/Sequenz ABCEBCBFGD soll fehlerhaft sein.json"
#"C:/Users/Anwender/Desktop/Abschlussarbeit (gesichert)/Netze/für die Masterarbeit/Halbordnung ABC-FG-B-D funktionierend.json"#"C:/Users/Anwender/Downloads/small-model.json"
#pfad = "C:/Users/Anwender/Downloads/small-model Hilfsvariable.json"
json_daten_ohne_Hilfsvariable = open(pfad_gelabeltes_Netz_ohne_Hilfsvariable,'r').read()
python_daten_gelabeltes_Netz_ohne_Hilfsvariable = json.loads(json_daten_ohne_Hilfsvariable)
pfadohneEndung_gelabeltes_Netz_ohne_Hilfsvariable = pfad_gelabeltes_Netz_ohne_Hilfsvariable[:-5]


'''
Das zugehöriges gelabeltes Netz mit Hilfsvariablen wird hier eingelesen, um ein Ungleichungssystem mit den Hilfsvariablen aufzustellen.
'''
############################################################################################
# Problem entsteht, wenn Figure 15 gelabelt wird und ungelabelt small-model betrachtet wird. 
# Die Übersetzung in ein ungelabeltes Netz kann zu Überläufen führen.
############################################################################################

pfad_gelabeltes_Netz = "C:/Users/Anwender/Desktop/Abschlussarbeit (gesichert)/Netze/für die Masterarbeit/Sequenz ABCEBCBFGD soll fehlerhaft sein Hilfsvariable.json"#"C:/Users/Anwender/Downloads/small-model Hilfsvariable.json"
#pfad = "C:/Users/Anwender/Downloads/small-model Hilfsvariable.json"
json_daten = open(pfad_gelabeltes_Netz,'r').read()
python_daten_gelabeltes_Netz = json.loads(json_daten)
pfadohneEndung_gelabeltes_Netz = pfad_gelabeltes_Netz[:-5]

'''
Das zu untersuchende ungelabelte Netz eingelesen, um ein später die Kanten (Stelle,Transition) imd (Transition, Stelle) zu untersuchen.
Weiterhin sind die ausgezeichneten Stellen hier zu finden, um insgesamt die drei Zwangsbedingungen für ein sound WFN zu formulieren.
'''
#Hier wird das ungelabelte Netz eingelesen. Ziel ist es die Kantengewichte der geweiligen ein- und ausgehenden Kanten aus jeder Stelle herauszuextrahieren,
#  damit das Ungleichungssystem befüllt werden kann.
pfad_ungelabeltes_Netz = "C:/Users/Anwender/Desktop/Abschlussarbeit (gesichert)/Netze/für die Masterarbeit/Figure-1 (7) m0 = p1  WFN ohne p5 Doppelloop.json"#"C:/Users/Anwender/Downloads/Figure-15.json"
##pfadX = "C:/Users/Anwender/Downloads/small-model Hilfsvariable.json"
json_daten_ungelabeltes_Netz = open(pfad_ungelabeltes_Netz,'r').read()
#Eingelesene Datei wird als String geladen.
python_daten_ungelabeltes_Netz = json.loads(json_daten_ungelabeltes_Netz)
pfadohneEndung_ungelabeltes_Netz = pfad_ungelabeltes_Netz[:-5]


#Neue Datei wird angelegt und in der neuen Datei wird das Ungleichungssystem geschrieben werden, was dort auch gelöst werden wird

'''
Hier werden globale Arrays und Listen leer initialisiert.
'''

Kandidat_Anfang_ungelabelt = []
Kandidat_Ende_ungelabelt = []
Anfang_gelabelt = []
Ende_gelabelt = []

'''
Hier werden die Transitionen erzeugt
'''
Transitionen_gelabeltes_Netz_ohne_Hilfsvariable = python_daten_gelabeltes_Netz_ohne_Hilfsvariable['transitions']
Transitionen_gelabeltes_Netz = python_daten_gelabeltes_Netz['transitions']
Transitionen_ungelabeltes_Netz = python_daten_ungelabeltes_Netz['transitions']

'''
Hier werden die Kanten erzeugt
'''
Kanten_gelabeltes_Netz_ohne_Hilfsvariable = list(python_daten_gelabeltes_Netz_ohne_Hilfsvariable['arcs'])
Kanten_gelabeltes_Netz = list(python_daten_gelabeltes_Netz['arcs'])
Kanten_ungelabeltes_Netz = list(python_daten_ungelabeltes_Netz['arcs'])
    

'''
Hier werden die Labels erzeugt
'''
Labels_gelabeltes_Netz_ohne_Hilfsvariable = python_daten_gelabeltes_Netz_ohne_Hilfsvariable['labels']
Labels_gelabeltes_Netz = python_daten_gelabeltes_Netz['labels']
Labels_ungelabeltes_Netz = python_daten_ungelabeltes_Netz['labels']

Schnittmenge = list(set(Labels_ungelabeltes_Netz.values())-(set(Labels_ungelabeltes_Netz.values())-set(Labels_gelabeltes_Netz.values())))
Liste_Schnittmenge = list(Schnittmenge)




'''
Hier das soll in die for Schleife und je Stelle wird eine neue Datei erzeugt und ein Ungleichungssystem geschrieben.
'''

for z in range(len(python_daten_ungelabeltes_Netz['places'])):

    '''
    Hier wird  gesucht, an welchen Kanten eine Stelle jeweils beteiligt ist, um am Ende zu ermitteln, ob sie nur ausgehende, nur eingehende oder auch 
    ein- und ausgehende Kanten hat. (im ungelabeltem Netz)

    
    Hier wird nach potentiellen Kandidaten für i und o gesucht.
    '''
    for v in range(len(python_daten_ungelabeltes_Netz['transitions'])):

        if str(python_daten_ungelabeltes_Netz['places'][z])+str(',')+str(python_daten_ungelabeltes_Netz['transitions'][v]) in Kanten_ungelabeltes_Netz:
            Kandidat_Anfang_ungelabelt .append(python_daten_ungelabeltes_Netz['places'][z])

        if str(python_daten_ungelabeltes_Netz['transitions'][v])+str(',')+str(python_daten_ungelabeltes_Netz['places'][z]) in Kanten_ungelabeltes_Netz:
            Kandidat_Ende_ungelabelt.append(python_daten_ungelabeltes_Netz['places'][z])


    SET_Kandidat_Ende_ungelabelt = set(Kandidat_Ende_ungelabelt)
    SET_Kandidat_Anfang_ungelabelt = set(Kandidat_Anfang_ungelabelt)


    


for z in range(len(python_daten_gelabeltes_Netz_ohne_Hilfsvariable['places'])):
    '''
    Hier wird danach gesucht, an welchen Kanten eine Stelle jeweils beteiligt ist, um am Ende zu ermitteln, ob sie nur ausgehende, nur eingehende oder auch 
    ein- und ausgehende Kanten hat. (im gelabeltem Netz)

    Hier wir auch nach potentielle Kandidaten für die Anfangs- und Endstellen im gelabeltem Netz gesucht.
    '''

    for v in range(len(python_daten_gelabeltes_Netz_ohne_Hilfsvariable['transitions'])):

        if str(python_daten_gelabeltes_Netz_ohne_Hilfsvariable['places'][z])+str(',')+str(python_daten_gelabeltes_Netz_ohne_Hilfsvariable['transitions'][v]) in Kanten_gelabeltes_Netz:

            Anfang_gelabelt.append(python_daten_gelabeltes_Netz_ohne_Hilfsvariable['places'][z])

        if str(python_daten_gelabeltes_Netz_ohne_Hilfsvariable['transitions'][v])+str(',')+str(python_daten_gelabeltes_Netz_ohne_Hilfsvariable['places'][z]) in Kanten_gelabeltes_Netz:

            Ende_gelabelt.append(python_daten_gelabeltes_Netz_ohne_Hilfsvariable['places'][z])

    SET_Kandidat_Ende_gelabelt = set(Ende_gelabelt)
    SET_Kandidat_Anfang_gelabelt = set(Anfang_gelabelt)


    Anfangsstelle = SET_Kandidat_Anfang_gelabelt.difference(SET_Kandidat_Ende_gelabelt)

    Anfangsstelle = next(iter(Anfangsstelle))

    Endstelle = SET_Kandidat_Ende_gelabelt.difference(SET_Kandidat_Anfang_gelabelt)

    Endstelle = iter(Endstelle)





'''
Hier werden via grundlegenden Mengenoperationen die Anfangs- und Endstellen bzw. i und o der Workflownetze ermittelt.
'''

Endstelle = SET_Kandidat_Ende_gelabelt.difference(SET_Kandidat_Anfang_gelabelt)
Endstelle = iter(Endstelle)

Anfangsstelle_gelabelt = SET_Kandidat_Anfang_gelabelt.difference(SET_Kandidat_Ende_gelabelt)

Endstelle_gelabelt = SET_Kandidat_Ende_gelabelt.difference(SET_Kandidat_Anfang_gelabelt)

Anfangsstelle_ungelabelt = SET_Kandidat_Anfang_ungelabelt.difference(SET_Kandidat_Ende_ungelabelt)

Endstelle_ungelabelt = SET_Kandidat_Ende_ungelabelt.difference(SET_Kandidat_Anfang_ungelabelt)


'''
Hier wird der erste Teil bzw. der generische Teil eines Programms in eine weitere *.py-Datei geschrieben, um einen ILP-Solver mit Python zu nutzen.
'''

'''
Hier werden die Hilfsvariablen über Mengenoperationen ermittelt und dann alphanumerisch sortiert, um diese dann als zu minimierende Funktion summandenweise zu übergeben.
'''
LISTE_SET_Hilfsvariable = list(set(python_daten_gelabeltes_Netz['places'])-set(python_daten_ungelabeltes_Netz['places']))
LISTE_SET_Hilfsvariable_sort = sorted(LISTE_SET_Hilfsvariable)


for z in range(len(python_daten_ungelabeltes_Netz['places'])):
    file = open(pfadohneEndung_ungelabeltes_Netz + ' ' + python_daten_ungelabeltes_Netz['places'][z] + ' Advent.py','w')
    file.writelines('from gekko import GEKKO' + '\n' + 'm = GEKKO()' + '\n')
    
    x = 0
    #Alle Elemente werden in einer Zeile aufgeschrieben jeweils mit Komma getrennt, das letzte Element wird anders behandelt und ohne Komma getrennt
    for x in range(len(python_daten_gelabeltes_Netz['places'])-1):
        file.writelines(python_daten_gelabeltes_Netz['places'][x] + ', ')
    x = x + 1
    file.writelines(python_daten_gelabeltes_Netz['places'][x])
    file.writelines(' = m.Array(m.Var,' + str(len(python_daten_gelabeltes_Netz['places'])) + ',integer=True,lb=0)' + '\n')
    file.writelines('m.Minimize(')
    #for-Schleife startet von x = 0
    '''
    for x in range(len(python_daten_gelabeltes_Netz['places'])-1):
        file.writelines(python_daten_gelabeltes_Netz ['places'][x] + ' + ')
    x = x + 1
    file.writelines(python_daten_gelabeltes_Netz ['places'][x] + ')' + '\n')'''
    for x in range(len(LISTE_SET_Hilfsvariable_sort)-1):
        file.writelines(LISTE_SET_Hilfsvariable_sort[x] + ' + ')
    x = x + 1
    file.writelines(LISTE_SET_Hilfsvariable_sort[x] + ')' + '\n')




    file.writelines('m.Equations([' + '\n' )
 
    Kantengewichte_ungelabeltes_Netz = list(python_daten_ungelabeltes_Netz['arcs'].values())

    '''
    Algorithmus weist einen Fehler auf und muss noch behoben werden
    In Worten, was im Algorithmus geschehen muss:
    1.) Für jede Transition wird gesucht, in welchem Listeneintrag sie enthalten ist.
    2.) Für jede Transition wird der Input jeweils gesucht samt Kantengewicht.
    3.) Für jede Transition wird der Output jeweils gesucht samt Kantengewicht.
    '''
    '''
    Für jede Transition wird in jeder Kante gesucht, ob sie enthalten ist.
    Ist sie enthalten, so wird die ein- oder ausgehende Kante jeweils identifiziert und aktuell in jeweils unterschiedlichen Arrays gespeichert.
    '''

    '''
    Hier wird über jede Transition über alle Kanten gesucht.
    '''



    '''
    Nachfolgend werden die Gleichungen des Ungleichungssystems geschrieben.
    Out_x(e) == In_x(e) + W(l(e),p) - W(p, l(e))
    '''

    '''
    Das kleinere beschränkt das Aufstellen der Gleichungen und Ungleichungen für das Ungleichungssystem.
    '''

    for x in range(len(Transitionen_gelabeltes_Netz)):

        '''
        Schnelle Fehlerbehebung, da die Listen nicht gleich lang sind, werden sie gleich lang gemacht, damit es funktioniert
        '''
        if len(Transitionen_gelabeltes_Netz) < len(Transitionen_ungelabeltes_Netz):
            while len(Transitionen_gelabeltes_Netz) < len(Transitionen_ungelabeltes_Netz):
                Transitionen_gelabeltes_Netz.append(Transitionen_ungelabeltes_Netz[x])
        
        if len(Transitionen_gelabeltes_Netz) > len(Transitionen_ungelabeltes_Netz):
            while len(Transitionen_gelabeltes_Netz) > len(Transitionen_ungelabeltes_Netz):
                Transitionen_ungelabeltes_Netz.append(Transitionen_gelabeltes_Netz[x])
        
        Input = []
        Output = []
        for a in range(len(Kanten_gelabeltes_Netz)):
            Split = Kanten_gelabeltes_Netz[a].split(",")
            if str(Transitionen_gelabeltes_Netz[x]) == Split[0]:
                Output.append(Split[1])
            if str(Transitionen_gelabeltes_Netz[x]) == Split[1]:
                Input.append(Split[0])


        b = 0
        '''
        Jede Transition im gelabeltem Netz mit Hilfsstellen hat mindestens zwei Outputs, sodass der Fall b = 1 nicht abgefangen werden muss.
        '''
        for b in range(len(Output)-1):
            file.writelines(Output[b] + ' + ')
        
        b = b + 1
        file.writelines(Output[b] + ' == ')
        
        c = 0
        for c in range(len(Input)-1):
            file.writelines(Input[c] + ' + ')
        '''
        !TO-DO!
        hier muss vom gelabelten Netz ins ungelabelte Netz übersetzt werden
        '''
        if Labels_gelabeltes_Netz[Transitionen_gelabeltes_Netz[x]] in Schnittmenge:
            STRING = str(python_daten_ungelabeltes_Netz['places'][z])+str(',')+str(list(Labels_ungelabeltes_Netz.keys())[list(Labels_ungelabeltes_Netz.values()).index(Labels_gelabeltes_Netz[Transitionen_gelabeltes_Netz[x]])])#list(Labels_ungelabeltes_Netz.keys())[list(Labels_gelabeltes_Netz.values()).index( Labels_gelabeltes_Netz[Transitionen_gelabeltes_Netz[x]])])#Transitionen_ungelabeltes_Netz[x])
            GNIRTS = str(list(Labels_ungelabeltes_Netz.keys())[list(Labels_ungelabeltes_Netz.values()).index(Labels_gelabeltes_Netz[Transitionen_gelabeltes_Netz[x]])])+str(',')+str(python_daten_ungelabeltes_Netz['places'][z])
            if GNIRTS in Kanten_ungelabeltes_Netz:
                file.writelines('1 + ')
            #if erlaubt Eigenloops, elif nicht, ich schaue mir sound WFN an, somit gibt es keinen Eigenloop, der zu erlauben wäre
            elif STRING in Kanten_ungelabeltes_Netz:
                file.writelines(' (- 1) + ')
            else:
                file.writelines('0 + ')
            c = c + 1
            file.writelines(Input[c] + ', ')
            file.writelines('\n')
        if Labels_gelabeltes_Netz[Transitionen_gelabeltes_Netz[x]] not in Schnittmenge:
            file.writelines(' 0, ')
            file.writelines('\n')

    

    '''
    Hier werden die UNGLEICHUNGEN des Ungleichungssystems formuliert


    '''


    for x in range(len(Transitionen_gelabeltes_Netz)):
        Input = []
        for a in range(len(Kanten_gelabeltes_Netz)):
            Split = Kanten_gelabeltes_Netz[a].split(",")
            '''
            hier wird vom gelabelten Netz ins ungelabelte Netz übersetzt werden
            '''
            if str(Transitionen_gelabeltes_Netz[x]) == Split[1]:
                Input.append(Split[0])
            #nach jeden Durchlauf wird je ein neuer Input und ein neuer Output gespeichert.

        
        b = 0

        if len(Input) == 1:
            file.writelines(Input[b] + ' >= ')
        else: 
            if len(Input) > 1:
                for b in range(len(Input)-1):
                    #print('IM_ ', Input[b])
                    file.writelines(Input[b] + ' + ')
        
        b = b + 1
        file.writelines(Input[b] + ' >= ') #PLATZHALTER, \n')

        '''
        Probeversion
        '''
        if Labels_gelabeltes_Netz[Transitionen_gelabeltes_Netz[x]] in Schnittmenge:
            STRING = str(python_daten_ungelabeltes_Netz['places'][z])+str(',')+str(list(Labels_ungelabeltes_Netz.keys())[list(Labels_ungelabeltes_Netz.values()).index(Labels_gelabeltes_Netz[Transitionen_gelabeltes_Netz[x]])])#list(Labels_ungelabeltes_Netz.keys())[list(Labels_gelabeltes_Netz.values()).index( Labels_gelabeltes_Netz[Transitionen_gelabeltes_Netz[x]])])#Transitionen_ungelabeltes_Netz[x])
            if STRING in Kanten_ungelabeltes_Netz:
                file.writelines('1, \n')
            else:
                file.writelines('0, \n')
        if Labels_gelabeltes_Netz[Transitionen_gelabeltes_Netz[x]] not in Schnittmenge:
            file.writelines('0, \n')
        
    '''
    Hier werden die drei verschiedenen Zwangsbedingungen formuliert, die für ein sound WFN für den Anfangs- und Endzustand gelten.
    '''

    if python_daten_ungelabeltes_Netz['places'][z] in SET_Kandidat_Anfang_ungelabelt:
        if python_daten_ungelabeltes_Netz['places'][z] in SET_Kandidat_Ende_ungelabelt:
            if len(str(SET_Kandidat_Ende_gelabelt - SET_Kandidat_Anfang_gelabelt)) == 7:###
                file.writelines(f"{Anfangsstelle_gelabelt}"[:-2][-2:] +' == 0,\n' + f"{SET_Kandidat_Ende_gelabelt - SET_Kandidat_Anfang_gelabelt}"[:-2][-3:] + ' == 0\n')
            else:
                file.writelines(f"{Anfangsstelle_gelabelt}"[:-2][-2:] +' == 0,\n' + f"{SET_Kandidat_Ende_gelabelt - SET_Kandidat_Anfang_gelabelt}"[:-2][-2:] + ' == 0\n')
    if  python_daten_ungelabeltes_Netz['places'][z] in SET_Kandidat_Ende_ungelabelt-SET_Kandidat_Anfang_ungelabelt:
        if len(str(SET_Kandidat_Ende_gelabelt - SET_Kandidat_Anfang_gelabelt)) == 7:###
            file.writelines(f"{Anfangsstelle_gelabelt}"[:-2][-2:] +' == 0,\n' + f"{SET_Kandidat_Ende_gelabelt - SET_Kandidat_Anfang_gelabelt}"[:-2][-3:] + ' == 1\n')###
        else:###
            file.writelines(f"{Anfangsstelle_gelabelt}"[:-2][-2:] +' == 0,\n' + f"{SET_Kandidat_Ende_gelabelt - SET_Kandidat_Anfang_gelabelt}"[:-2][-2:] + ' == 1\n')
    if  python_daten_ungelabeltes_Netz['places'][z] in SET_Kandidat_Anfang_ungelabelt-SET_Kandidat_Ende_ungelabelt:
        if len(str(SET_Kandidat_Ende_gelabelt - SET_Kandidat_Anfang_gelabelt)) == 7:###
            file.writelines(f"{Anfangsstelle_gelabelt}"[:-2][-2:] +' == 1,\n' + f"{SET_Kandidat_Ende_gelabelt - SET_Kandidat_Anfang_gelabelt}"[:-2][-3:] + ' == 0\n')###
        else:###
            file.writelines(f"{Anfangsstelle_gelabelt}"[:-2][-2:] +' == 1,\n' + f"{SET_Kandidat_Ende_gelabelt - SET_Kandidat_Anfang_gelabelt}"[:-2][-2:] + ' == 0\n')

    

    

    file.writelines('])\nm.options.SOLVER = 1' + '\n' + 'm.solve()' + '\n')
    for x in range(len(python_daten_gelabeltes_Netz ['places'])-1):
        file.writelines('print("' + python_daten_gelabeltes_Netz ['places'][x] + ':", ' + python_daten_gelabeltes_Netz ['places'][x] + '.value[0])\n')
    

    file.close()
