from typing import Any

from django.http import HttpResponse
from django.shortcuts import render


#
# def index(request: Any):
#     return HttpResponse('''<h1>hello</h1>
#     <a href="https://www.youtube.com/">Hello Ganesh</a>''')
#
# def about(request: Any):
#     return HttpResponse("about harry")

# Code for vedio 7
def index(request):
    # params = {'name': 'ganesh', 'place': 'Mars'}
    return render(request, 'index.html')
    # return HttpResponse("Home")


def index2(request):
    return render(request, 'index2.html')


def analyze(request):
    # get the text
    global params
    global punctuations
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + djtext.upper()
            params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)

    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
                params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
            # Analayze the text
        return render(request, 'analyze.html', params)

    elif extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

                params = {'purpose': 'Removed the space', 'analyzed_text': analyzed}
            # Analayze the text
        return render(request, 'analyze.html', params)

    elif charcount == "on":
        analyzed = ""
        # for char in djtext:
        #    analyzed = len(djtext)
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1

        params = {'purpose': 'characters counter', 'analyzed_text': analyzed}
        # analyze the text
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')


def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse(sites)

# def removepunc(request):
#     #Get the text
#     djtext=print(request.GET.get('text', 'default'))
#     print(djtext)
# Analyze the text
#     return HttpResponse("remove punc")
#
#
# def capfirst(request):
#     return HttpResponse("capitalize first <a href='/'>back</a>")
