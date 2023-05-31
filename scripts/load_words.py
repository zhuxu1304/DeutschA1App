from app.models import Word
import csv
from datetime import date,datetime


def run():
    with open('data.csv',encoding='utf-8') as file:
        reader = csv.reader(file)
        #next(reader)  # Advance past the header

        Word.objects.all().delete()

        for row in reader:
            #print(row)

            #genre, _ = Genre.objects.get_or_create(name=row[-1])

            word = Word(word=row[0], 
            translation=row[1],sentences=row[2])
            word.save()