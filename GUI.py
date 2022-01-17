import PySimpleGUI as sg
import time
import threading

"""Fake chat"""


def add_to_list(list_m): # fake incoming messages
    for i in range(15):
        list_m.append(i)
        time.sleep(8)


sg.theme('DarkAmber')

list1 = ['fghytht', '56khlb', 'j5uuvk5k', 'tkklcxlel']

layout = [[sg.Listbox(list1, size=(40, 10), key='--INPUT--')],
          [sg.Input(size=(40, None), do_not_clear=False)],
          [sg.Button('Send'), sg.Button('Exit')]
          ]
window = sg.Window('Fake Chat', layout).Finalize()
thread1 = threading.Thread(target=add_to_list, args=(list1, ), daemon=True)
thread1.start()

while True:
    window['--INPUT--'].update(list1)
    event, value = window.read()
    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break

    if event == 'Send':
        list1.append(value[0])
    else:
        continue


window.close()