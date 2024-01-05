#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def main():

    graphs = [
        ["../DE/Automatisierte Ablaufsteuerung.drawio"         , "../EN/automated hump control.drawio"],
        ["../DE/Automatisierte Planung und Planprüfung.drawio" , "../EN/automated planning and plan review.drawio"],
        ["../DE/Cloud-Stellwerk.drawio"                        , "../EN/cloud interlocking.drawio"],
        ["../DE/Dezentrales Stellwerk.drawio"                  , "../EN/decentralized interlocking.drawio"],
        ["../DE/Emotions- und Absichtserkennung.drawio"        , "../EN/emotion and intent recognition.drawio"],
        ["../DE/Ferngesteuerte Fahrzeuge.drawio"               , "../EN/remote controlled rolling stock.drawio"],
        ["../DE/Güterwegemanagement.drawio"                    , "../EN/freight route management.drawio"],
        ["../DE/Intelligente Instandhaltung.drawio"            , "../EN/predictive maintenance.drawio"],
        ["../DE/Intermodale Güterabfertigung.drawio"           , "../EN/intermodal freight handling.drawio"],
        ["../DE/Intermodale Reisekette.drawio"                 , "../EN/intermodal travel chain.drawio"],
        ["../DE/Kontaktlose Fahrscheinkontrolle.drawio"        , "../EN/contactless ticket control.drawio"],
        ["../DE/Optimierte Reise- und Preisgestaltung.drawio"  , "../EN/optimised travel and price arrangement.drawio"],
        ["../DE/Optimierung der Fahrgastwechselzeit.drawio"    , "../EN/optimization of passenger changeover time.drawio"],
        ["../DE/Personenidentifizierung.drawio"                , "../EN/identification of persons.drawio"],
        ["../DE/Reise- und Lebensmanagement.drawio"            , "../EN/travel and life management.drawio"],
        ["../DE/Reisendenlenkung.drawio"                       , "../EN/passenger guidance through the train station.drawio"],
        ["../DE/Steuernder Durchgriff der Disposition.drawio"  , "../EN/steering action for scheduling.drawio"],
        ["../DE/Virtuelles Kuppeln.drawio"                     , "../EN/virtual coupling.drawio"],
        ["../DE/Vollautomatisiertes Fahren.drawio"             , "../EN/fully automated driving.drawio"],
        ["../DE/Vorort-Informationen.drawio"                   , "../EN/on-site information.drawio"],
        ["../DE/Zugsicherung mit ETCS.drawio"                  , "../EN/ETCS train protection.drawio"]
    ]

    translations = {}

    with open("translations.txt") as file:
        for line in file.readlines():
            split = line.split("=")
            if len(split) == 2:
                translations[split[0].strip()] = split[1].strip()

    print(translations)


if __name__ == '__main__':
    main()