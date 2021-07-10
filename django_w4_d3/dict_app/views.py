from PyDictionary import PyDictionary
from django.shortcuts import render

# Create your views here.
def first_page(request):
    return render(request, 'index.html')

def display_page(request):
    word= request.POST['search']
    a=PyDictionary()
    meaning=a.meaning(word)
    synonym=a.synonym(word)
    antonym=a.antonym(word)

    context={
        'meaning':meaning['Noun'][0],
        'synonym':synonym,
        'antonym':antonym,
        }

    return render(request,'display.html',context)



