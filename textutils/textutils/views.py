# I have created this file - Indranil
from django.http import HttpResponse
from django.shortcuts import render

# Demo
# def index(request):
#     return HttpResponse('''<h1>Hello!</h1><a href="https://www.youtube.com/" target="_blank">Youtube</a>''')

# def about(request):
#     return HttpResponse("About Me!")


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the Text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    # Check with checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:`~'"\,<>./?@#$%^&*'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(charcounter == 'on'):
        analyzed = f"The number of Characters in Your text is {len(djtext)}"
        params = {'purpose': 'Number Of Character in Your Text',
                  'analyzed_text': analyzed}

    if(removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcounter != 'on'):
        return HttpResponse("Error! Please select any operation and try again!")

    return render(request, 'analyze.html', params)
