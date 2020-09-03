from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    with open ("inflation_russia.csv", encoding="utf-8") as file:
        reader = list(csv.reader(file, delimiter=';'))
    inflation = reader[1:]

    for row in inflation:
        ind = 0
        for val in row:
            if not val:
                row[ind] = '-'
            ind+=1

    context = {
            'data_inflation':reader,
                }

    return render(request, template_name,
                  context)