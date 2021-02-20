#!/bin/python
import PySimpleGUI as sg
import os
import re

form = sg.FlexForm('Switch Workspace', return_keyboard_events=True)

layout = [ [sg.Text('Enter workspace name'), sg.InputText(size=(25,1))],
           [sg.OK(), sg.Button('Cancel')] ]
form.Layout(layout)

# button, values = form.Layout(layout).Read()
while True:
    event, values = form.read()
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Escape:9':
        exit(0)
    elif event == 'OK':
        break
    #print ("event = " + event + "value =" + values[0])

whitespace_check = re.compile('^\s+$')
values[0] = re.sub(';', '', values[0])
if len(values[0]) > 0 and not whitespace_check.match(values[0]):
    os.system ("i3-msg workspace " + re.escape(values[0]))

