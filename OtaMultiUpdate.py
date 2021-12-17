import os
import PySimpleGUI as Psg
import module_software_prepare as module

command = ""
BAR_MAX = 30
status = 1
Psg.theme('Dark 2')
layout = [[Psg.Text('Welcome in Ota Multi Update !')],
          [Psg.Text('Chose main BIN file', size=(20, 1)), Psg.Input(), Psg.FileBrowse()],
          [Psg.Text('IP List', size=(20, 1)), Psg.Input(), Psg.FileBrowse()],
          [Psg.Text('Module prefix :', size=(20, 1)), Psg.Input()],
          [Psg.Text('Progress:', size=(20, 1)), Psg.ProgressBar(BAR_MAX, orientation='h', size=(20, 4), key='-PROG-'),
           Psg.Text('', key='_bar_'), Psg.Text('of'), Psg.Text('', key='_len_')],
          [Psg.Submit('Upload'), Psg.Cancel('Exit')]]
window = Psg.Window('OTA Multi-Update', layout)

while True:
    event, values = window.Read()
    if event is None:
        break
    if event == 'Exit':
        window.Close()
        os.remove('Preparing')
    if event == 'Upload':

        file = open(values[1]).read()
        adress = file.split("\n")
        many = len(adress)
        BAR_MAX = many
        window['_bar_'].update(status)
        window['_len_'].update(many)

        for i in adress:
            if status < 10:
                module.PrepareAnotherFiles.hex(str(values[0]), str(values[2]), '0' + str(status))
                command = 'python espota.py -d -i ' + i + ' -f ' + 'Preparing/' + str(values[2]).replace('0', '') + '0' + str(status) + '.bin'
            if status >= 10:
                module.PrepareAnotherFiles.hex(str(values[0]), str(values[2]), str(status))
                command = 'python espota.py -d -i ' + i + ' -f ' + 'Preparing/' + str(values[2]).replace("0", "") + str(status) + '.bin'
            event, values = window.read(timeout=10)
            window['-PROG-'].update(status)
            window['_bar_'].update(status)

            print(command)
            os.system(command)
            status += 1
        Psg.popup('Uploading Done !', 'Wait for reboot all devices')

        status = 0
