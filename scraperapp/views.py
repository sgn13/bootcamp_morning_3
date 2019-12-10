from django.shortcuts import render
from django.http import HttpResponse
import requests
import bs4
# Create your views here.

def home(request):
    #return HttpResponse('sakdfnkfnklsd')
    page = requests.get('https://fabpedigree.com/james/mathmen.htm')
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    li=soup.find_all('li')

    names=[]
    for each in li:
        names.append(each.find('a').string)

        d={
          'names':names
        }
    return render(request,'home.html',d)

