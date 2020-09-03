from django.template import library
import csv

register = library.Library()

@register.filter
def get_color(value):

    with open ("inflation_russia.csv", encoding="utf-8") as file:
        reader = list(csv.reader(file, delimiter=';'))
    inflation = reader[1:]

    if value in reader[0] or value == '-':
        return 'White'

    for row in inflation:
        if value == row[0]:
            return 'White'
        if value == row[-1]:
            return 'Grey'

    if float(value) < 0:
        return 'Green'
    elif 1.0 <= float(value) < 2.0:
        return 'LightCoral'
    elif 2.0 <= float(value) <5.0:
        return 'Tomato'
    elif float(value) >= 5.0:
        return 'DarkRed'
