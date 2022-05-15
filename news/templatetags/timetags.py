from django import template
import datetime
register = template.Library()

def convert_timestamp(timestamp):
    try:
        #assume, that timestamp is given in seconds with decimal point
        ts = float(timestamp)
    except ValueError:
        return None
    return datetime.datetime.fromtimestamp(ts)

register.filter(convert_timestamp)