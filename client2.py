"""client with GUI"""
import threading
import socket
import json
import PySimpleGUI as sg

M_LIST = list()
sg.theme('DarkAmber')


def incom_msg():
    while True:
        data = sock.recv(2048)
        msg_tuple = json.loads(data, encoding='utf-8')
        # msg_text = msg_tuple[1]
        # msg_adr = msg_tuple[0]
        M_LIST.append(msg_tuple)
        window['--LIST--'].update(M_LIST)
        window['--LIST--'].set_vscroll_position(1.0)


# def client_pipeline():
#     while True:
#         thread1 = threading.Thread(target=incom_msg, daemon=True)
#         thread1.start()
#
#         sock.send(input("Enter message: ").encode('utf-8'))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8008))


layout = [[sg.Listbox(M_LIST, size=(50, 10), key='--LIST--')],
          [sg.Input(size=(50, 2), do_not_clear=False)],
          [sg.Button('Send'), sg.Button('Exit')]
          ]
window = sg.Window('Chat V1.0', layout)
thread1 = threading.Thread(target=incom_msg, daemon=True)
thread1.start()
while True:
    event, value = window.read()
    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break

    if event == 'Send':
        sock.send(value[0].encode('utf-8'))

window.close()
sock.close()