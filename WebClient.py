import json
def Client():
    while True:
        print("Select an option: GET, POST, PATCH, DELETE.")
        option = input()
        if (option != "GET" and option != "POST" and option != "PATCH" and option != "DELETE"):
            text = "BAD FORMAT 5000!\n You have entered a non-existent option!"
            return text
        print("Select table: odnos_radnika, radnik, tip_veze, vrsta_radnika")
        table = input()
        if (table != "odnos_radnika" and table != "radnik" and table != "tip_veze" and table != "vrsta_radnika"): 
            text = "BAD FORMAT 5000!\n You have entered a non-existent table!"
            return text
        text = "{ \"verb\": \"" + option + "\", \"noun\": \"" + table + "\"" 

        if (option == "GET" or option == "DELETE"):
            if table == "odnos_radnika":
                print("Enter a new values of the columns (INSERT and UPDATE), etc. values for filtering (SELECT and DELETE). Separate them with \";\".")
                values = input()
                if values != None:
                    array = values.split(";")
                    for element in array:
                        columns = element.split("=")
                        for item in columns[0::2]:
                            if (item != "id" and item != "radnik1" and item != "radnik2" and item != "id_veza"): 
                                text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                                return text
                    text += ", \"query\":\"" + values + "\""
                if option == "GET":
                    print("Choose the columns which you want to display: id, radnik1, radnik2, id_veza")  
                    input_columns = input()
                    if input_columns != None:
                        select = input_columns.split(",")
                        for element in select:
                            if element != None:
                                #print(element)
                                if (element != "id" and element != "radnik1" and element != "radnik2" and element != "id_veza"): 
                                    text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                                    return text
                        text += ", \"fields\":\"" + input_columns + "\""
            elif table == "radnik":
                print("Enter a new values of the columns (INSERT and UPDATE), etc. values for filtering (SELECT and DELETE). Separate them with \";\".")
                value = input()
                if value != None:
                    array = value.split(";")
                    for element in array:
                        columns = element.split("=")
                        for item in columns[0::2]:
                            if (item != "jmbg" and item != "ime" and item != "opis" and item != "id_vrsta"): 
                                text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                                return text
                    text += ", \"query\":\"" + value + "\""
                if option == "GET":
                    print("Choose the columns which you want to display: jmbg, ime, opis, id_vrsta")  
                    input_columns = input()
                    if input_columns != None:
                        select = input_columns.split(",")
                        for element in select:
                            if element != None:
                                if (element != "jmbg" and element != "ime" and element != "opis" and element != "id_vrsta"): 
                                    text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                                    return text
                        text += ", \"fields\":\"" + input_columns + "\""
            elif table == "tip_veze":
                print("Enter a new values of the columns (INSERT and UPDATE), etc. values for filtering (SELECT and DELETE). Separate them with \";\".")
                value = input()
                if value != None:
                    array = value.split(";")
                    for element in array:
                        cloumns = element.split("=")
                        for item in cloumns[0::2]:
                            if (item != "id" and item != "naziv"): 
                                text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                                return text
                    text += ", \"query\":\"" + value + "\""
                if option == "GET":
                    print("Choose the columns which you want to display: id, naziv")  
                    input_columns = input()
                    if input_columns != None:
                        select = input_columns.split(",")
                        for element in select:
                            if element != None:
                                if (element != "id" and element != "naziv"): 
                                    text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                                    return text
                        text += ", \"fields\":\"" + input_columns + "\""
            else:
                print("Enter a new values of the columns (INSERT and UPDATE), etc. values for filtering (SELECT and DELETE). Separate them with \";\".")
                value = input()
                if value != None:
                    array = value.split(";")
                    for element in array:
                        columns = element.split("=")
                        for item in columns[0::2]:
                            if (item != "id" and item != "vrsta"): 
                                text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                                return text
                    text += ", \"query\":\"" + value + "\""
                if option == "GET":
                    print("Choose the columns which you want to display: id, vrsta")  
                    input_columns = input()
                    if input_columns != None:
                        select = input_columns.split(",")
                        for x in select:
                            if x != None:
                                if (x != "id" and x != "vrsta"): 
                                    text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                                    return text
                        text += ", \"fields\":\"" + input_columns + "\""
        
        elif (option == "POST" or option == "PATCH"):
            if table == "odnos_radnika":
                print("Enter a new values of the columns (INSERT and UPDATE), etc. values for filtering (SELECT and DELETE). Separate them with \";\".")
                value = input()
                array = value.split(";")
                for element in array:
                    columns = element.split("=")
                    for item in columns[0::2]:
                        if (item != "id" and item != "radnik1" and item != "radnik2" and item != "id_veza"): 
                            text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                            return text
                text += ", \"query\":\"" + value + "\""
                if option == "PATCH":
                    print("Enter filter conditions. Separate them with \";\".")
                    value = input()
                    array = value.split(";")
                    for element in array:
                        columns = element.split("=")
                        for item in columns[0::2]:
                            if (item != "id" and item != "radnik1" and item != "radnik2" and item != "id_veza"): 
                                text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                                return text
                            
                    text += ", \"query\":\"" + value + "\""

            elif table == "radnik":
                print("Enter a new values of the columns (INSERT and UPDATE), etc. values for filtering (SELECT and DELETE). Separate them with \";\".")
                value = input()
                array = value.split(";")
                for element in array:
                    columns = element.split("=")
                    for item in columns[0::2]:
                        if (item != "jmbg" and item != "ime" and item != "opis" and item != "id_vrsta"): 
                            text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                            return text
                        
                text += ", \"query\":\"" + value + "\""
                if option == "PATCH":
                    print("Enter filter conditions. Separate them with \";\".")
                    value = input()
                    array = value.split(";")
                    for element in array:
                        columns = element.split("=")
                        for item in columns[0::2]:
                            if (item != "jmbg" and item != "ime" and item != "opis" and item != "id_vrsta"): 
                                text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                                return text
                    text += ", \"query\":\"" + value + "\""
            elif table == "tip_veze":
                print("Enter a new values of the columns (INSERT and UPDATE), etc. values for filtering (SELECT and DELETE). Separate them with \";\".")
                value = input()
                array = value.split(";")
                for element in array:
                    columns = element.split("=")
                    for item in columns[0::2]:
                        if (item != "id" and item != "naziv"): 
                            text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                            return text
                        
                text += ", \"query\":\"" + value + "\""
                if option == "PATCH":
                    print("Enter filter conditions. Separate them with \";\".")
                    value = input()
                    array = value.split(";")
                    for element in array:
                        columns = element.split("=")
                        for item in columns[0::2]:
                            if (item != "id" and item != "naziv"): 
                                text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                                return text
                            
                    text += ", \"query\":\"" + value + "\""
            else:
                print("Enter a new values of the columns (INSERT and UPDATE), etc. values for filtering (SELECT and DELETE). Separate them with \";\".")
                value = input()
                array = value.split(";")
                for element in array:
                    columns = element.split("=")
                    for item in columns[0::2]:
                        if (item != "id" and item != "vrsta"): 
                            text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                            return text
                        
                text += ", \"query\":\"" + value + "\""
                if option == "PATCH":
                    print("Enter filter conditions. Separate them with \";\".")
                    value = input()
                    array = value.split(";")
                    for element in array:
                        columns = element.split("=")
                        for item in columns[0::2]:
                            if (item != "id" and item != "vrsta"): 
                                text = "BAD FORMAT 5000!\n You have entered a non-existent column!"
                                return text
                            
                    text += ", \"query\":\"" + value + "\""
        text += "}"
        #print(text)
        jsonString = json.dumps(text)
        return jsonString











        
print(Client())