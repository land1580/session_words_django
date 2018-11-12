from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    return render(request,'session_words/index.html')

def add_word(request):
    if request.method == "POST":
        if "words" in request.session:
            word_list = request.session['words']
        else:
            word_list = []

        if "show_big" in request.POST:
            show_big = 1
        else:
            show_big = 0    

        word_list.append({
            "word": request.POST['new_word'], 
            "color": request.POST['color'], 
            "show_big": show_big, 
            "time":strftime("%I:%M %p, %b %d, %Y ", gmtime())
        })

        request.session['words'] = word_list
        request.session.modified = True

        for word in request.session['words']:
            print(word)
            
        return redirect("/")

    else:
        return redirect("/")

def clear(request):
    request.session.clear()
    return redirect("/")