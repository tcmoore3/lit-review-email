import calendar
import collections
import datetime

td_tm = input('Today or tomorrow?\n1 - Today\n2 - Tomorrow\nChoose 1 or 2 [2]: ')
td_tm = {'1': 'today', '2': 'tomorrow'}.get(td_tm, 'tomorrow')
time = input('Enter the time [3pm]: ')
if time == '':
    time = '3pm'
locations = collections.OrderedDict([
    ('1', 'the Research Auditorium'),
    ('2', 'B520-1122'),
    ('3', 'the South Atrium'),
    ('4', 'B16-B001E'),
    ('5', 'G063 & 064'),
    ('6', 'B10-G065'),
    ('7', 'Blue Jeans'),
    ('8', 'Zoom'),
    ])
loc_str = 'Select location for meeting.\n'
for n, loc in locations.items():
    loc_str += '{} - {}\n'.format(n, loc)
loc_str += 'Choose [8]: '
location = input(loc_str)
location = locations.get(location, locations['8'])
presenter = None
while not presenter:
    presenter = input('Who is presenting?\nEnter presenter: ')
title = None
while not title:
    title = input('Enter the title of the paper: ')
link = None
while not link:
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

if pdt_presenter:
    msg += '{} will be presenting in the PDT after the '.format(pdt_presenter)
    msg += 'lit review, so stick around if you can give valuable feedback on '
    msg += 'their latest work.\n\n'

msg += 'The next few presenters are:\n'
for person in next_speakers.split(','):
    msg += '{}\n'.format(person.strip())
msg += '\nLooking forward to seeing y\'all there.\nTim'
print('\n')
print(msg, '\n')
