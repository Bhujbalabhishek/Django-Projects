from django.shortcuts import render,redirect,HttpResponse
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline


def scrape(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  url = "https://www.theonion.com/"
  content = session.get(url, verify=False).content
  soup = BSoup(content, "html.parser")
#   sc-1pw4fyi-3 ziaet, sc-1qkakgd-0 eSMucW, sc-1whp23a-1 kphRNd, a1de4o-5 cKrhTm
  News = soup.find_all('div', {"class":["sc-1qkakgd-0 eSMucW","sc-1whp23a-1 kphRNd"]})
  for artcile in News:
      main = artcile.find_all('a')[0]
      link = main['href']
      image_src = str(main.find('img')['srcset']).split(" ")[-4]
      title = "News"
      new_headline = Headline()
      new_headline.title = title
      new_headline.url = link
      new_headline.image = image_src
      new_headline.save()
  return redirect("../")

        
def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }


    return render(request, "news/home.html", context)


def setcookie(request):
    html = HttpResponse("<h1>News Aggregator Django </h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('NewsAggregator', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)
    return html

def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('NewsAggregator')
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/setcookie')


def delete_co(request):
    if request.COOKIES.get('visits'):
       response = HttpResponse("<h1>news aggregator<br>Cookie deleted</h1>")
       response.delete_cookie("visits")
    else:
        response = HttpResponse("<h1>news aggregator</h1>need to create cookie before deleting")
    return response



def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("NewsAggregator")


def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("news aggregator<br> cookie createed")
    else:
        response = HttpResponse("news aggregator <br> Your browser doesnot accept cookies")
    return response




def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>News Aggregator<br> the session is set</h1>")

def access_session(request):
    response = "<h1>Welcome to Sessions of News Aggregator</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')



def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")