from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from bs4 import BeautifulSoup

context = {
        "links": [],
        "tvsename": str,
    }


def index(reqest):
    system = reqest.POST.get('search', None)
    context['search'] = system
    # print(context['search'])
    if context['search'] != None:
        requset = requests.get(context['search'])
        web_content = requset.content
        # print ( web_content)
        suop_content = BeautifulSoup(web_content)
        # print (suop_content)
        a_tags = suop_content.find_all("a", href=True)
        namefind=suop_content.find_all("h1")
        tname = []
        for name in namefind:
            tvname = name.text
            tname.append(tvname)
        #name_of = tname[0]
        context["tvsename"]=tname[0]
        #print(name_of)
        for items in a_tags:
            item_text = items.text
            # item_text_dublicate  = items.text
            link = items["href"]
            # print (item_text_dublicate)
            item_text = item_text.split(" ")
            if item_text[0] == "Download":
                context["links"].append(link)
                # print(link)
    else:
        print(context)
    context['search'] = None
    return render(reqest, 'index.html', context)

# Create your views here.

