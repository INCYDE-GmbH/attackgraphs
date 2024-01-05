#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

def main():

    graphs = [
        '../DE/Automatisierte Ablaufsteuerung.drawio',
        '../DE/Automatisierte Planung und Planprüfung.drawio',
        '../DE/Cloud-Stellwerk.drawio',
        '../DE/Dezentrales Stellwerk.drawio',
        '../DE/Emotions- und Absichtserkennung.drawio',
        '../DE/Ferngesteuerte Fahrzeuge.drawio',
        '../DE/Güterwegemanagement.drawio',
        '../DE/Intelligente Instandhaltung.drawio',
        '../DE/Intermodale Güterabfertigung.drawio',
        '../DE/Intermodale Reisekette.drawio',
        '../DE/Kontaktlose Fahrscheinkontrolle.drawio',
        '../DE/Optimierte Reise- und Preisgestaltung.drawio',
        '../DE/Optimierung der Fahrgastwechselzeit.drawio',
        '../DE/Personenidentifizierung.drawio',
        '../DE/Reisendenlenkung.drawio',
        '../DE/Reise- und Lebensmanagement.drawio',
        '../DE/Steuernder Durchgriff der Disposition.drawio',
        '../DE/Virtuelles Kuppeln.drawio',
        '../DE/Vollautomatisiertes Fahren.drawio',
        '../DE/Vorort-Informationen.drawio',
        '../DE/Zugsicherung mit ETCS.drawio'
    ]

    labels = set()

    for graph in graphs:
        tree = ET.parse(graph)
        result = tree.getroot().findall(".//object[@label]")
        for node in result:

            mxcell = node.findall("./mxCell[@style]")
            if "fillColor=#DAE8FC" in mxcell[0].attrib["style"]:
                labels.update(node.attrib["label"].split("\n"))
            else:
                labels.add(node.attrib["label"].replace("\n", "\\n"))

    print(len(labels))

    with open("labels.txt", "w") as output:
        for label in sorted(labels):
            output.write(label + "\n")



if __name__ == '__main__':
    main()