#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET

def main():

    graphs = [
        # ["../DE/Automatisierte Ablaufsteuerung.drawio"         , "../EN/automated hump control.drawio"],
        # ["../DE/Automatisierte Planung und Planprüfung.drawio" , "../EN/automated planning and plan review.drawio"],
        # ["../DE/Cloud-Stellwerk.drawio"                        , "../EN/cloud interlocking.drawio"],
        # ["../DE/Dezentrales Stellwerk.drawio"                  , "../EN/decentralized interlocking.drawio"],
        # ["../DE/Emotions- und Absichtserkennung.drawio"        , "../EN/emotion and intent recognition.drawio"],
        # ["../DE/Ferngesteuerte Fahrzeuge.drawio"               , "../EN/remote controlled rolling stock.drawio"],
        # ["../DE/Güterwegemanagement.drawio"                    , "../EN/freight route management.drawio"],
        ["../DE/Intelligente Instandhaltung.drawio"            , "../EN/predictive maintenance.drawio"],
        # ["../DE/Intermodale Güterabfertigung.drawio"           , "../EN/intermodal freight handling.drawio"],
        # ["../DE/Intermodale Reisekette.drawio"                 , "../EN/intermodal travel chain.drawio"],
        # ["../DE/Kontaktlose Fahrscheinkontrolle.drawio"        , "../EN/contactless ticket control.drawio"],
        # ["../DE/Optimierte Reise- und Preisgestaltung.drawio"  , "../EN/optimised travel and price arrangement.drawio"],
        # ["../DE/Optimierung der Fahrgastwechselzeit.drawio"    , "../EN/optimization of passenger changeover time.drawio"],
        # ["../DE/Personenidentifizierung.drawio"                , "../EN/identification of persons.drawio"],
        # ["../DE/Reise- und Lebensmanagement.drawio"            , "../EN/travel and life management.drawio"],
        # ["../DE/Reisendenlenkung.drawio"                       , "../EN/passenger guidance through the train station.drawio"],
        # ["../DE/Steuernder Durchgriff der Disposition.drawio"  , "../EN/steering action for scheduling.drawio"],
        # ["../DE/Virtuelles Kuppeln.drawio"                     , "../EN/virtual coupling.drawio"],
        # ["../DE/Vollautomatisiertes Fahren.drawio"             , "../EN/fully automated driving.drawio"],
        # ["../DE/Vorort-Informationen.drawio"                   , "../EN/on-site information.drawio"],
        # ["../DE/Zugsicherung mit ETCS.drawio"                  , "../EN/ETCS train protection.drawio"]
    ]

    # some labels to exclude from translation
    exclude = ["1", "2", "3", "4", "5", ""]

    # dict to save the translations in
    # format:
    # de: en
    translations = {}

    # load translations from file
    # assume the following format:
    # DE = EN
    # ignore lines that do not have exatly one equal sign "="
    with open("translations.txt") as file:
        for line in file.readlines():
            split = line.split("=")
            if len(split) == 2:
                translations[split[0].strip()] = split[1].strip()

    # do it for all entries in graphs
    for graph in graphs:
        tree = ET.parse(graph[0])
        result = tree.getroot().findall(".//object[@label]")

        for node in result:
            label = node.attrib["label"].replace("\n", "\\n")

            # exclude some labels that we do not need to translate
            if label not in exclude:

                # distinguish between countermeasures and other nodes
                # find countermeasures by their node color
                mxcell = node.findall(".//mxCell[@style]")
                if "fillColor=#DAE8FC" in mxcell[0].attrib["style"]:
                    # countermeasures are translated line by line
                    # therefore, split into lines, try to translate and then reconstruct the label
                    entries = label.split("\\n")
                    for index in range(len(entries)):
                        if entries[index] in translations:
                            entries[index] = translations[entries[index]]
                        else:
                            print(entries[index])
                    node.attrib["label"] = "\n".join(entries)
                else:
                    # non-countermeasures are translated completly
                    # assume linebreaks are "escaped" as \n in translation file
                    if label in translations:
                        node.attrib["label"] = translations[label].replace("\\n", "\n")
                    else:
                        print(label)

        # save the tree to the English version of the file
        tree.write(graph[1], encoding="UTF-8")

if __name__ == '__main__':
    main()