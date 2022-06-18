import json
import socket
from sqlite3 import connect

def conenct_to_server(json_object):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('localhost', 10005))
    data=json.dumps(json_object)
    server_socket.sendall(bytes(data, encoding="utf-8"))
    data=server_socket.recv(1024)
    response=json.loads(data)
    server_socket.close()
    print_response(response)

def print_response(response):
    status=response['status']
    print(status)
    if status == 'SUCCESS':
        list=response['payload']
        if isinstance(list, str):
            print(list[1:-1])
        else:
            for item in list:
                data=item[1:-1]
                print(data)
    else:
        print(response['payload'])

def client():
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
        values=values.strip()
        if values:
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
    json_request = json.loads(text)
    return json_request

if __name__ == '__main__':
    while True:
        request=client()
        conenct_to_server(request)