#the world is not enough
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
#    params={'name':'devil','place':'king'}
    return render(request,'index.html')

#    return HttpResponse('Home')

def removepunch(request):
    djtext=request.POST.get('txt',"default")
    removepunch=request.POST.get('removepunch',"off")
    fullcaps=request.POST.get('fullcaps','off')
    newlineremo=request.POST.get('newlineremo','off')
    charcount=request.POST.get('charcount','off')
    #print(djtext)
    #print(removepunch)
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed=""
    
    if removepunch=='on':    
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed + char
        params={'Purpose':'Analyzed Text','analyzed_text':analyzed}
        djtext=analyzed
    if fullcaps=='on':
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper() 
        params={'Purpose':'change to upper Text','analyzed_text':analyzed} 
        djtext=analyzed
    if newlineremo=='on':
        analyzed=""
        for char in djtext:
            if char!='\n' and char!="\r":
                analyzed=analyzed+char
        params={'Purpose':'change to remove new line Text','analyzed_text':analyzed}
        djtext=analyzed 
    if charcount=='on':
        count=0
        for index,char in enumerate(djtext):
            if not(djtext[index]==' '):
                count=count+1
        params={'Purpose':'change to count Text','analyzed_text':analyzed,'count':count}
        djtext=analyzed 
    
    return render(request,"anaylize.html",params)

def captilize(request):
    return HttpResponse("Captilize First")


