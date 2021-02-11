import PySimpleGUI as sg
import datetime

TZ_USA = datetime.timezone(datetime.timedelta(hours=-8))
TZ_AUS = datetime.timezone(datetime.timedelta(hours=11))

dt_now_jpn = datetime.datetime.now()
dt_now_usa = datetime.datetime.now(TZ_USA)
dt_now_aus = datetime.datetime.now(TZ_AUS)

jpn_now = dt_now_jpn.strftime('%H:%M')
usa_now = dt_now_usa.strftime('%H:%M')
aus_now = dt_now_aus.strftime('%H:%M')


def get_time():
    global dt_now_jpn, dt_now_usa, dt_now_aus
    global jpn_now, usa_now, aus_now

    dt_now_jpn = datetime.datetime.now()
    dt_now_usa = datetime.datetime.now(TZ_USA)
    dt_now_aus = datetime.datetime.now(TZ_AUS)

    jpn_now = dt_now_jpn.strftime('%H:%M')
    usa_now = dt_now_usa.strftime('%H:%M')
    aus_now = dt_now_aus.strftime('%H:%M')


sg.theme('Dark Brown 1')

layout = [
    [sg.Text('JPN',font=('Helvetica', 20)), sg.Text(jpn_now, key='jpn', font=('Helvetica', 20))],
    [sg.Text('USA',font=('Helvetica', 20)), sg.Text(usa_now, key='usa', font=('Helvetica', 20))],
    [sg.Text('AUS',font=('Helvetica', 20)), sg.Text(aus_now, key='aus', font=('Helvetica', 20))]
]

window = sg.Window('WorldWideClocks', layout)

while True:
    event, values = window.read(timeout=1000, timeout_key='-timeout-')

    print(event, values)

    if event is None:
        print('exit')
        break

    if event in '-timeout-':
        get_time()
        window['jpn'].update(jpn_now)
        window['usa'].update(usa_now)
        window['aus'].update(aus_now)



window.close()