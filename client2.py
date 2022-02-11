"""client with GUI"""
import threading
import socket
import json
import PySimpleGUI as sg

MESSAGES = list()
sg.theme('DarkAmber')


def incom_msg():
    while True:
        data = sock.recv(2048)
        msg_tuple = json.loads(data, encoding='utf-8')
        # msg_text = msg_tuple[1]
        # msg_adr = msg_tuple[0]
        MESSAGES.append(msg_tuple)
        window['--LIST--'].update(MESSAGES)
        window['--LIST--'].set_vscroll_position(1.0)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8008))

username = sg.popup_get_text('Enter username')
sock.send(username.encode('utf-8'))

layout = [[sg.Text(username)],
          [sg.Listbox(MESSAGES, size=(50, 10), key='--LIST--')],
          [sg.Input(size=(50, 2), do_not_clear=False)],
          [sg.Button('Send'), sg.Button('Exit')]
          ]
window = sg.Window('Chat V1.1', layout)
thread1 = threading.Thread(target=incom_msg, daemon=True)
thread1.start()
user_name = sg.popup_get_text('Enter user name:')
while True:
    event, value = window.read()
    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break

    if event == 'Send':
        try:
            sock.send(value[0].encode('utf-8'))
        except ConnectionResetError:
            sg.popup('Oops... Server is not responding!')
            continue

window.close()
sock.close()