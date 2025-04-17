import os
import requests
from ics import Calendar, Event, DisplayAlarm
from datetime import date, timedelta, datetime

postal_code = os.getenv('POSTAL_CODE')
house_number = os.getenv('HOUSE_NUMBER')
if postal_code is None or house_number is None:
    raise ValueError(
        'POSTAL_CODE and HOUSE_NUMBER environment variables must be set.')

res = requests.get(
    f'https://data.rd4.nl/api/v1/waste-calendar?postal_code={postal_code}&house_number={house_number}&year={date.today().year}',)

events = res.json()['data']['items'][0]

translate_dict = {
    'gft': 'GFT en etensresten',
    'pmd': 'PMD-verpakking',
    'pruning_waste': 'Snoeiafval op afspraak',
    'residual_waste': 'Restafval',
    'best_bag': 'BEST-tas',
    'paper': 'Papierafval',
    'christmas_trees': 'Kerstbomen',
}

c = Calendar()

for event in events:
    e = Event()
    event_date = event['date']
    event_type = event['type']

    e.name = translate_dict[event_type]
    e.begin = event_date
    e.make_all_day()
    e.alarms = [DisplayAlarm(trigger=timedelta(
        hours=-6), display_text=f'{e.name} wordt morgen opgehaald')]

    c.events.add(e)

# Save the calendar to a file
with open('data/schedule.ics', 'w') as f:
    f.writelines(c.serialize())

print(datetime.now(), 'ICS file generated successfully.')
