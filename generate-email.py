import calendar
import datetime

td_tm = input('Today or tomorrow?\n1 - Today\n2 - Tomorrow\nChoose 1 or 2 [2]: ')
td_tm = {'1': 'today', '2': 'tomorrow'}.get(td_tm, 'tomorrow')
time = input('Enter the time [3pm]: ')
if time == '':
    time = '3pm'
loc_str = 'Select location for meeting.\n1 - Research Auditorium\n'
loc_str += '2 - B520-1122\n3 - South Atrium\n4 - B16 B001E\n'
loc_str += 'Choose from 1, 2, 3, 4 [1]: '
location = input(loc_str)
location = {'1': 'the Research Auditorium', '2': 'B520-1122',
        '3': 'the South Atrium', '4': 'B16-B001E'}.get(location, 'B520-1122')
presenter = input('Who is presenting?\nEnter presenter: ')
title = input('Enter the title of the paper: ')
link = input('Enter the url to the paper: ')
pdt_presenter = input('Who is presenting in the postdoc tank?\nEnter PDT presenter: ')
input_str = 'Who are the next presenters?\nEnter the next 3 presenters, separated'
input_str += ' by commas: '
next_speakers = input(input_str)


weekday = calendar.day_name[datetime.datetime.today().weekday()]
if td_tm == 'today':
    date = datetime.datetime.today()
elif td_tm == 'tomorrow':
    date = datetime.date.today() + datetime.timedelta(days=1)
msg = 'Happy {} folks,\n\n'.format(weekday)
msg += 'This is a reminder about the lit review meeting '
msg += '{} ({}/{}/{}) at {} '.format(td_tm, date.month, date.day, 
        str(date.year)[-2:], time)
msg += 'in {}. '.format(location)
msg += '{} will be presenting the following paper:\n\n'.format(presenter)
msg += '{}\n{}\n\n'.format(title, link)
msg += '{} will be presenting in the PDT after the '.format(pdt_presenter)
msg += 'lit review, so stick around if you can give valuable feedback on '
msg += 'their latest work.\n\nThe next few presenters are:\n'
for person in next_speakers.split(','):
    msg += '{}\n'.format(person)
msg += '\nLooking forward to seeing y\'all there.\nTim'
print('\n')
print(msg, '\n')
