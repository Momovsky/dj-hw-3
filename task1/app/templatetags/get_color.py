from django.template import library
import csv

register = library.Library()

@register.filter
def get_color(value):

    try:
        if float(value) < 0:
            return 'Green'
        elif 1.0 <= float(value) < 2.0:
            return 'LightCoral'
        elif 2.0 <= float(value) <5.0:
            return 'Tomato'
        elif float(value) >= 5.0:
            return 'DarkRed'
    except:
        return 'White'
