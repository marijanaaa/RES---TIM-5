import json
def Client():
    while True:
        print("Select an option: GET, POST, PATCH, DELETE.")
        option = input()
        if (option != "GET" and option != "POST" and option != "PATCH" and option != "DELETE"):
            text = "BAD FORMAT 5000!\n Uneli ste nepostojecu opciju!"
            return text
        print("Select table: odnos_radnika, radnik, tip_veze, vrsta_radnika")
        table = input()
        if (table != "odnos_radnika" and table != "radnik" and table != "tip_veze" and table != "vrsta_radnika"): 
            text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv tabele!"
            return text
        text = "{ \"verb\": \"" + option + "\", \"noun\": \"" + table + "\"" 

        if (option == "GET" or option == "DELETE"):
            if table == "odnos_radnika":
                print("Unesite nove vrednosti kolona (za INSERT i UPDATE), odnosno vrednosti za filtriranje (SELECT i DELETE). Odvojite ih sa \";\".")
                uslovi = input()
                if uslovi != None:
                    niz = uslovi.split(";")
                    for x in niz:
                        kolone = x.split("=")
                        for y in kolone[0::2]:
                            if (y != "id" and y != "radnik1" and y != "radnik2" and y != "id_veza"): 
                                text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                                return text
                    text += ", \"query\":\"" + uslovi + "\""
                if option == "GET":
                    print("Izaberite kolone koje zelite da se prikazu: id, radnik1, radnik2, id_veza")  
                    console3 = input()
                    if console3 != None:
                        select = console3.split(",")
                        for x in select:
                            if x != None:
                                print(x)
                                if (x != "id" and x != "radnik1" and x != "radnik2" and x != "id_veza"): 
                                    text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                                    return text
                        text += ", \"fields\":\"" + console3 + "\""
            elif table == "radnik":
                print("Unesite nove vrednosti kolona (za INSERT i UPDATE), odnosno vrednosti za filtriranje (SELECT i DELETE). Odvojite ih sa \";\".")
                uslovi = input()
                if uslovi != None:
                    niz = uslovi.split(";")
                    for x in niz:
                        kolone = x.split("=")
                        for y in kolone[0::2]:
                            if (y != "jmbg" and y != "ime" and y != "opis" and y != "id_vrsta"): 
                                text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                                return text
                    text += ", \"query\":\"" + uslovi + "\""
                if option == "GET":
                    print("Izaberite kolone koje zelite da se prikazu: jmbg, ime, opis, id_vrsta")  
                    console3 = input()
                    if console3 != None:
                        select = console3.split(",")
                        for x in select:
                            if x != None:
                                if (x != "jmbg" and x != "ime" and x != "opis" and x != "id_vrsta"): 
                                    text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                                    return text
                        text += ", \"fields\":\"" + console3 + "\""
            elif table == "tip_veze":
                print("Unesite nove vrednosti kolona (za INSERT i UPDATE), odnosno vrednosti za filtriranje (SELECT i DELETE). Odvojite ih sa \";\".")
                uslovi = input()
                if uslovi != None:
                    niz = uslovi.split(";")
                    for x in niz:
                        kolone = x.split("=")
                        for y in kolone[0::2]:
                            if (y != "id" and y != "naziv"): 
                                text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                                return text
                    text += ", \"query\":\"" + uslovi + "\""
                if option == "GET":
                    print("Izaberite kolone koje zelite da se prikazu: id, naziv")  
                    console3 = input()
                    if console3 != None:
                        select = console3.split(",")
                        for x in select:
                            if x != None:
                                if (x != "id" and x != "naziv"): 
                                    text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                                    return text
                        text += ", \"fields\":\"" + console3 + "\""
            else:
                print("Unesite nove vrednosti kolona (za INSERT i UPDATE), odnosno vrednosti za filtriranje (SELECT i DELETE). Odvojite ih sa \";\".")
                uslovi = input()
                if uslovi != None:
                    niz = uslovi.split(";")
                    for x in niz:
                        kolone = x.split("=")
                        for y in kolone[0::2]:
                            if (y != "id" and y != "vrsta"): 
                                text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                                return text
                    text += ", \"query\":\"" + uslovi + "\""
                if option == "GET":
                    print("Izaberite kolone koje zelite da se prikazu: id, vrsta")  
                    console3 = input()
                    if console3 != None:
                        select = console3.split(",")
                        for x in select:
                            if x != None:
                                if (x != "id" and x != "vrsta"): 
                                    text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                                    return text
                        text += ", \"fields\":\"" + console3 + "\""
        
        elif (option == "POST" or option == "PATCH"):
            if table == "odnos_radnika":
                print("Unesite nove vrednosti kolona (za INSERT i UPDATE), odnosno vrednosti za filtriranje (SELECT i DELETE). Odvojite ih sa \";\".")
                uslovi = input()
                niz = uslovi.split(";")
                for x in niz:
                    kolone = x.split("=")
                    for y in kolone[0::2]:
                        if (y != "id" and y != "radnik1" and y != "radnik2" and y != "id_veza"): 
                            text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                            return text
                text += ", \"query\":\"" + uslovi + "\""
                if option == "PATCH":
                    print("Unesite uslove za filtriranje. Odvojite ih sa ;")
                    uslovi = input()
                    niz = uslovi.split(";")
                    for x in niz:
                        kolone = x.split("=")
                        for y in kolone[0::2]:
                            if (y != "id" and y != "radnik1" and y != "radnik2" and y != "id_veza"): 
                                text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                                return text
                            
                    text += ", \"query\":\"" + uslovi + "\""

            elif table == "radnik":
                print("Unesite nove vrednosti kolona (za INSERT i UPDATE), odnosno vrednosti za filtriranje (SELECT i DELETE). Odvojite ih sa \";\".")
                uslovi = input()
                niz = uslovi.split(";")
                for x in niz:
                    kolone = x.split("=")
                    for y in kolone[0::2]:
                        if (y != "jmbg" and y != "ime" and y != "opis" and y != "id_vrsta"): 
                            text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                            return text
                        
                text += ", \"query\":\"" + uslovi + "\""
                if option == "PATCH":
                    print("Unesite uslove za filtriranje. Odvojite ih sa ;")
                    uslovi = input()
                    niz = uslovi.split(";")
                    for x in niz:
                        kolone = x.split("=")
                        for y in kolone[0::2]:
                            if (y != "jmbg" and y != "ime" and y != "opis" and y != "id_vrsta"): 
                                text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                                return text
                    text += ", \"query\":\"" + uslovi + "\""
            elif table == "tip_veze":
                print("Unesite nove vrednosti kolona (za INSERT i UPDATE), odnosno vrednosti za filtriranje (SELECT i DELETE). Odvojite ih sa \";\".")
                uslovi = input()
                niz = uslovi.split(";")
                for x in niz:
                    kolone = x.split("=")
                    for y in kolone[0::2]:
                        if (y != "id" and y != "naziv"): 
                            text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                            return text
                        
                text += ", \"query\":\"" + uslovi + "\""
                if option == "PATCH":
                    print("Unesite uslove za filtriranje. Odvojite ih sa ;")
                    uslovi = input()
                    niz = uslovi.split(";")
                    for x in niz:
                        kolone = x.split("=")
                        for y in kolone[0::2]:
                            if (y != "id" and y != "naziv"): 
                                text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                                return text
                            
                    text += ", \"query\":\"" + uslovi + "\""
            else:
                print("Unesite nove vrednosti kolona (za INSERT i UPDATE), odnosno vrednosti za filtriranje (SELECT i DELETE). Odvojite ih sa \";\".")
                uslovi = input()
                niz = uslovi.split(";")
                for x in niz:
                    kolone = x.split("=")
                    for y in kolone[0::2]:
                        if (y != "id" and y != "vrsta"): 
                            text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                            return text
                        
                text += ", \"query\":\"" + uslovi + "\""
                if option == "PATCH":
                    print("Unesite uslove za filtriranje. Odvojite ih sa ;")
                    uslovi = input()
                    niz = uslovi.split(";")
                    for x in niz:
                        kolone = x.split("=")
                        for y in kolone[0::2]:
                            if (y != "id" and y != "vrsta"): 
                                text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                                return text
                            
                    text += ", \"query\":\"" + uslovi + "\""
        text += "}"
        jsonString = json.dumps(text)
        return jsonString











        
print(Client())