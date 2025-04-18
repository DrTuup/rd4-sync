import json
import os
import requests
from ics import Calendar, Event, DisplayAlarm
from datetime import date, timedelta, datetime


def generate_ics(postal_code, house_number):
    if postal_code is None or house_number is None:
        # Return an json with status code 400 and message
        return json.dumps({'status': 'error', 'message': 'Postal code and house number are required'}), 400

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

    # Return the calendar as a string
    print(datetime.now(), 'ICS file generated successfully.')
    calendar_string = c.serialize()
    return calendar_string
