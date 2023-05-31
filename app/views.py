from django.shortcuts import render,redirect
import json
from .models import Word
from datetime import date,timedelta
import random

def load():
    result = []
    # check if new words already loaded, if not load
    if not Word.objects.filter(valid=True).filter(chosen=True).filter(learned_date=date.today()):
        new_words = Word.objects.filter(valid=True).filter(chosen=False).order_by('?')[:30]  # pick new words
        for w in new_words: # set learned date and review date to today
            w.learned_date = date.today()
            w.review_date = date.today()
            w.chosen = True
            w.save()
    for w in Word.objects.filter(valid=True).filter(chosen=True).filter(review_date=date.today()):
        result.append(w)
    return result

def merge(data):
    words = []
    translation = []
    sentences = []
    values = []
    for w in data:
        words.append(w.word)
        translation.append(w.translation)
        sentences.append(w.sentences)
        values.append(w.stage)
    return words,translation,sentences, values

def mix(a,b,c,d):
    if not a:
        return a,b,c,d
    l = list(zip(a,b,c,d))
    random.shuffle(l)
    a,b,c,d = zip(*l)
    return a,b,c,d





# Create your views here.
def index(request):
    if request.method == 'GET':
        words,translation,sentences,values = merge(load())
        words,translation,sentences,values = mix(words,translation,sentences,values)
        data = json.dumps({"words":words,"translation":translation,"sentences":sentences,"value":values})
        return render(request,"app/app.html",{"data":data})
    else:
        if "pressed_button" in request.POST:
            d = request.POST.get('pressed_button')
            print(d)
            stage = d[0]
            word = d[2:]
            w = Word.objects.filter(word=word).first()
            w.stage = int(stage)
            w.review_date = date.today()+timedelta(int(stage))
            w.save()
            print(Word.objects.filter(word=word).first().review_date)
            return redirect('index')


        else:
            return redirect('success')

def success(request):
    return render(request,"app/success.html")