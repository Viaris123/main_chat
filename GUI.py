import PySimpleGUI as sg
import time
import threading

"""Fake chat"""


def add_to_list(list_m): # fake incoming messages

    for i in range(15):
        list_m.append(i)
        window['--OUTPUT--'].update(list1)
        window['--OUTPUT--'].set_vscroll_position(1.0)
        time.sleep(8)


sg.theme('DarkAmber')


list1 = ['fghytht', '56khlb', 'j5uuvk5k', 'tkklcxlel']

layout = [[sg.Listbox(list1, size=(50, 10), key='--OUTPUT--')],
          [sg.Input(size=(40, None), do_not_clear=False)],
          [sg.Button('Send'), sg.Button('Exit')]
          ]
window = sg.Window('Fake Chat', layout).Finalize()
thread1 = threading.Thread(target=add_to_list, args=(list1, ), daemon=True)
thread1.start()

while True:

    event, value = window.read()
    if event == 'Exit' or event == sg.WINDOW_CLOSED:
        break

    if event == 'Send':
        list1.append(value[0])
        window['--OUTPUT--'].update(list1)
        window['--OUTPUT--'].set_vscroll_position(1.0)


window.close()