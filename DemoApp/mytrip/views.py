from django.shortcuts import render
from .models import Destination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import auth

# Create your views here.

def index(request):

    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.price = 1000
    # dest1.img = 'destination_1.jpg'
    # dest1.desc = 'The city that never sleeps'
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = 'Chennai'
    # dest2.price = 800
    # dest2.img = 'destination_2.jpg'
    # dest2.desc = 'Beautiful beaches'
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = 'Bangalore'
    # dest3.price = 750
    # dest3.img = 'destination_3.jpg'
    # dest3.desc = 'Tech Park City'
    # dest3.offer = False

    # dests = [dest1,dest2,dest3]

    dests = Destination.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(dests,2)

    try:
        dests = paginator.page(page)
    except PageNotAnInteger:
        dests = paginator.page(1)
    except EmptyPage:
        dests = paginator.page(paginator.num_pages)

    return render(request, "index.html", {'dests':dests})



def destination(request):
    dests = Destination.objects.all()
    return render(request,"destination.html",{'dests':dests})




class DestinationDetailView(LoginRequiredMixin,DetailView):
    model = Destination
    template_name = 'destination.html'
    context_object_name = 'dest'



