from django.shortcuts import render
from markdown2 import Markdown
from . import util
from django.http import HttpResponseRedirect
from django.urls import reverse
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):

    apnaMarkdown=Markdown()
    entryPage=util.get_entry(entry)

    if entryPage:

        return render(request, "encyclopedia/entry.html",
            { "entry": apnaMarkdown.convert(entryPage), "entryTitle": entry })
    
    else:

        return render(request, "encyclopedia/notFound.html",{"entryTitle":entry})


def search(request):

    apnaMarkdown=Markdown()
    # entriesList=util.list_entries()

    if request.method=="POST":

        entry=request.POST['q']
        content=util.get_entry(entry)

        if content:

            return render(request, "encyclopedia/entry.html",
            { "entry": apnaMarkdown.convert(content), "entryTitle": entry })

        
        else:

            listWithEntry=[]
            allEntries=util.list_entries()

            for x in allEntries:

                if entry.lower() in x.lower():

                    listWithEntry.append(x)

            if listWithEntry:

                return render(request, "encyclopedia/searchResults.html", {
                "entries": listWithEntry
            })

            else:
                
                return render(request, "encyclopedia/notFound.html",{"entryTitle":entry})


def createNewPage(request):

    
    if request.method=='GET':

        return render(request, "encyclopedia/createNewPage.html")
    
    elif request.method=='POST':

        apnaMarkdown=Markdown()
        entriesList=util.list_entries()

        title=request.POST['title']
        content=request.POST['content']

        if title in entriesList:

            return render(request, "encyclopedia/alreadyExists.html",{'title':title})
        
        else:

            util.save_entry(title,content)
            return render(request, "encyclopedia/entry.html",
            { "entry": apnaMarkdown.convert(content), "entryTitle": title })


def edit(request):

    if request.method=='POST':

        entry=request.POST['entryTitle']
        content=util.get_entry(entry)

        return render(request, 'encyclopedia/edit.html',{'entry':entry, 'content':content})
    
def save(request):

    title=request.POST['title']
    content=request.POST['content']
    util.save_entry(title,content)

    apnaMarkdown=Markdown()

    return render(request, "encyclopedia/entry.html",
            { "entry": apnaMarkdown.convert(content), "entryTitle": title })


def randomPage(request):

    allEntries=util.list_entries()
    entry=random.choice(allEntries)

    content=util.get_entry(entry)

    apnaMarkdown=Markdown()

    return render(request, "encyclopedia/entry.html",
            { "entry": apnaMarkdown.convert(content), "entryTitle": entry })

