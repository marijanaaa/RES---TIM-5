import json
def Client(self):
    while True:
        print("Select an option:")
        print("1. GET")
        print("2. POST")
        print("3. PATCH")
        print("4. DELETE")
        console1 = input()
        option = int(console1)
        print("Select table: odnos_radnika, radnik, tip_veze, vrsta_radnika")
        table = input()
        
        if option == 1:       # select
            text = "{ \"verb\": \"GET\", \"noun\": \"" + table + "\"" 
            if (table != "odnos_radnika" and table != "radnik" and table != "tip_veze" and table != "vrsta_radnika"): 
                text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv tabele!"
                return text
            print("Unesite uslove za SELECT. Odvojite ih sa ;")
            uslovi = input()
            if uslovi != None:
                niz = uslovi.split(";")
                for x in niz:
                    kolone = x.split("=")
                    for y in kolone[0::2]:
                        if (y != "id" and y != "radnik1" and y != "radnik2" and y != "id_veza"): 
                            text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                            return text
                        else:
                            text += ", \"query\":\"" + uslovi + "\""
            print("Izaberite kolone za filtrianje: id, radnik1, radnik2, id_veza")  
            console3 = input()
            if console3 != None:
                select = console3.split(",")
                for x in select:
                    if x != None:
                        if (x != "id" and x != "radnik1" and x != "radnik2" and x != "id_veza"): 
                            text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                            return text
                text += ", \"fields\":\"" + console3 + "\""
            text += "}"
            print(text)
            jsonString = json.dumps(text)
            jsonFile = open("data.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close
            return jsonFile


        elif option == 2:
            text = "{ \"verb\": \"POST\", \"noun\": \"" + table + "\"" 
            if (table != "odnos_radnika" and table != "radnik" and table != "tip_veze" and table != "vrsta_radnika"): 
                text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv tabele!"
                return text
            print("Unesite vrednosti za kolone. Odvojite ih sa ;")
            uslovi = input()
            if uslovi != None:
                niz = uslovi.split(";")
                for x in niz:
                    kolone = x.split("=")
                    for y in kolone[0::2]:
                        if (y != "id" and y != "radnik1" and y != "radnik2" and y != "id_veza"): 
                            text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                            return text
                        else:
                            text += ", \"query\":\"" + uslovi + "\""
            else:
                text = "BAD FORMAT 5000!\n Niste uneli polja!"
                return text
            text += "}"
            print(text)
            jsonString = json.dumps(text)
            jsonFile = open("data.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close
            return jsonFile


        elif option == 3:
            text = "{ \"verb\": \"PATCH\", \"noun\": \"" + table + "\"" 
            if (table != "odnos_radnika" and table != "radnik" and table != "tip_veze" and table != "vrsta_radnika"): 
                text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv tabele!"
                return text
            print("Unesite nove vrednosti kolona za UPDATE. Odvojite ih sa ;")
            uslovi = input()
            if uslovi != None:
                niz = uslovi.split(";")
                for x in niz:
                    kolone = x.split("=")
                    for y in kolone[0::2]:
                        if (y != "id" and y != "radnik1" and y != "radnik2" and y != "id_veza"): 
                            text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                            return text
                        else:
                            text += ", \"query\":\"" + uslovi + "\""
            print("Unesite uslove za filtriranje. Odvojite ih sa ;")
            uslovi = input()
            if uslovi != None:
                niz = uslovi.split(";")
                for x in niz:
                    kolone = x.split("=")
                    for y in kolone[0::2]:
                        if (y != "id" and y != "radnik1" and y != "radnik2" and y != "id_veza"): 
                            text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                            return text
                        else:
                            text += ", \"query\":\"" + uslovi + "\""
            text += "}"
            print(text)
            jsonString = json.dumps(text)
            jsonFile = open("data.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close
            return jsonFile

        elif option == 4:
            text = "{ \"verb\": \"DELETE\", \"noun\": \"" + table + "\"" 
            if (table != "odnos_radnika" and table != "radnik" and table != "tip_veze" and table != "vrsta_radnika"): 
                text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv tabele!"
                return text
            print("Unesite uslove za DELETE. Odvojite ih sa ;")
            uslovi = input()
            if uslovi != None:
                niz = uslovi.split(";")
                for x in niz:
                    kolone = x.split("=")
                    for y in kolone[0::2]:
                        if (y != "id" and y != "radnik1" and y != "radnik2" and y != "id_veza"): 
                            text = "BAD FORMAT 5000!\n Uneli ste nepostojeci naziv kolone!"
                            return text
                        else:
                            text += ", \"query\":\"" + uslovi + "\""
            text += "}"
            print(text)
            jsonString = json.dumps(text)
            jsonFile = open("data.json", "w")
            jsonFile.write(jsonString)
            jsonFile.close
            return jsonFile
        else:
            text = "BAD FORMAT 5000!\n Uneli ste nepostojecu opciju iz menija!"
            return text


