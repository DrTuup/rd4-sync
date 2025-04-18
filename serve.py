from flask import Flask, request, Response
from generate_ics import generate_ics
app = Flask(__name__)


@app.route('/')
def calendar():
    postal_code = request.args.get('postal_code')
    house_number = request.args.get('house_number')
    calendar_data = generate_ics(postal_code, house_number)

    if isinstance(calendar_data, tuple):  # e.g., error with status code
        return calendar_data

    return Response(calendar_data, mimetype='text/calendar')
