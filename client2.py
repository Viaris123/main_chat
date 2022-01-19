"""client with GUI"""
import threading
import socket
import json
import PySimpleGUI as sg


def incom_msg():
    while True:
        data = sock.recv(2048)
        msg_tuple = json.loads(data, encoding='utf-8')
        msg_text = msg_tuple[1]
        msg_adr = msg_tuple[0]
        print(msg_text, ' from ', msg_adr)


def client_pipeline():
    while True:
        thread1 = threading.Thread(target=incom_msg, daemon=True)
        thread1.start()

        sock.send(input("Enter message: ").encode('utf-8'))


sg.theme('DarkAmber')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8008))

list1 = list()
layout = [[sg.Listbox(list1, size=(30, 10))],
          [sg.Input(size=(30, 2), do_not_clear=False)],
          [sg.Button('SEND'), sg.Button('EXIT')]
          ]
window = sg.Window('Fake Chat', layout)