import json
import socket
from sqlite3 import connect
def conenctToServer(json_object):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.connect(('localhost', 10005))
    data=json.dumps(json_object)
    serverSocket.sendall(bytes(data, encoding="utf-8"))
    data=serverSocket.recv(1024)
    response=json.loads(data)
    serverSocket.close()
    printResponse(response)
def printResponse(response):
    status=response['status']
    print(status)
    if status == 'SUCCESS':
        list=response['payload']
        for item in list:
            data=item[1:-1]
            print(data)
            data_list=data.split(',')
            for x in data_list:
                print(x, end="")
            print()
    else:
        print(response['payload'])

def Client():
    while True:
        print("Select an option: GET, POST, PATCH, DELETE.")
        text = "{ "
        option = input()
        option=option.strip()
        if option:
             text += "\"verb\": \"" + option + "\""
        print("Select table: odnos_radnika, radnik, tip_veze, vrsta_radnika")
        table = input()
        table.strip()
        if table:
            text += ", \"noun\": \"" + table + "\"" 
        if (option == "DELETE"):
            print("Enter values of the columns for filtering. Separate them with \";\".")
            values = input()
            if values != None:
                text += ", \"query\":\"" + values + "\""
        elif (option == "GET"):
            print("Enter values of the columns for filtering. Separate them with \";\".")
            values = input()
            values=values.strip()
            if values:
                text += ", \"query\":\"" + values + "\""
            print("Choose the columns which you want to display.")  
            input_columns = input()
            input_columns=input_columns.strip()
            if input_columns:
                text += ", \"fields\":\"" + input_columns + "\""
        elif (option == "POST"):
            print("Enter new values of the columns. Separate them with \";\".")
            value = input()
            value=value.strip();
            if value:
                text += ", \"query\":\"" + value + "\""
        else:
            print("Enter new values of the columns. Separate them with \";\".")
            value = input()
            value=value.strip()
            if value:
                text += ", \"query\":\"" + value + "\""
            print("Enter filter conditions. Separate them with \";\".")
            conditions = input()
            conditions=conditions.strip()
            if conditions:
                text += ", \"fields\":\"" + conditions + "\""
        text += "}"
        jsonRequest = json.loads(text)
        conenctToServer(jsonRequest)
Client()