from django.shortcuts import render,HttpResponse
#from django.utils.datastructures import MultiValueDictKeyError
from requests.exceptions import ConnectionError
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from datetime import datetime
from home.models import Contact
from home.models import Post,Comment
from .forms import PostForm
import requests
from django.contrib import messages
import json
import urllib
from urllib.parse import urlencode
# Create your views here.
def index(request):
    q={}
    if 'query' in request.GET:
        query=request.GET['query']
        places_endpoints="https://api.tomtom.com/search/2/search/%s.JSON"%query
        api_key='FQ1sLg4uqEfaszO2Xbgm8ywIPbe4jsAb'
        params_3={
            "query":query,
            "key":api_key,
            "lat":19.2183,
            "lon":72.9781,
            "limit":20,
            "countrySet":"IN",
            "radius":50000,
            "openingHours":"nextSevenDays",
            "idxSet":"POI"
             }
        params_3_encoded=urlencode(params_3)
        places_urls=f"{places_endpoints}?{params_3_encoded}"
        r3=requests.get(places_urls)
        #print(r3.json())
        #print(type(r3))
        #print(r3.status_code)
        txts=r3.text
        objs=json.loads(txts)
        #print(objs)
        q=(objs['results'])
    #messages.success(request,"this is a test message")
    return render(request,'home/index.html',{'q':q})
    #return HttpResponse("this is homepage")

def about(request):
    return render(request,'home/about.html')
    #return HttpResponse("this is aboutpage")

def makeup(request):
    b={}
    if 'product_type' in request.GET:
        product_type=request.GET['product_type']
        places_endpoint="http://makeup-api.herokuapp.com/api/v1/products.json"
        params_2={
            "product_type":product_type
            }
        params_2_encoded=urlencode(params_2)
        places_url=f"{places_endpoint}?{params_2_encoded}"
        r2=requests.get(places_url)
        txt=r2.text
        b=json.loads(txt)
        
    return render(request,'home/makeup.html',{'b':b})
    #return HttpResponse("this is servicespage")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been sent')
    
    return render(request,'home/contact.html')
    #return HttpResponse("this is contactpage")

def doctor(request):
    api_key='FQ1sLg4uqEfaszO2Xbgm8ywIPbe4jsAb'
    places_endpoint="https://api.tomtom.com/search/2/nearbySearch/.JSON"
    params_2={
        "key":api_key,
    "lat":19.2183,
    "lon":72.9781,
    "limit":10,
    "countrySet":"IN",
    "radius":30000,
    "categorySet":7326
    }
    params_2_encoded=urlencode(params_2)
    t1={}
    places_url=f"{places_endpoint}?{params_2_encoded}"
    r2=requests.get(places_url)
    txt=r2.text
    obj=json.loads(txt)
    t1=(obj['results'])
    return render(request,'home/doctor.html',{'t1':t1})

def wedding(request):
    api_key='FQ1sLg4uqEfaszO2Xbgm8ywIPbe4jsAb'
    places_endpoint="https://api.tomtom.com/search/2/nearbySearch/.JSON"
    params_2={
        "key":api_key,
    "lat":19.2183,
    "lon":72.9781,
    "limit":10,
    "countrySet":"IN",
    "radius":30000,
    "categorySet":9352046
    }
    params_2_encoded=urlencode(params_2)
    t1={}
    places_url=f"{places_endpoint}?{params_2_encoded}"
    r2=requests.get(places_url)
    txt=r2.text
    obj=json.loads(txt)
    t1=(obj['results'])
    return render(request,'home/wedding.html',{'t1':t1})

def fashion(request):
    api_key='FQ1sLg4uqEfaszO2Xbgm8ywIPbe4jsAb'
    places_endpoint="https://api.tomtom.com/search/2/nearbySearch/.JSON"
    params_2={
        "key":api_key,
    "lat":19.2183,
    "lon":72.9781,
    "limit":10,
    "countrySet":"IN",
    "radius":30000,
    "categorySet":7397
    }
    params_2_encoded=urlencode(params_2)
    t1={}
    places_url=f"{places_endpoint}?{params_2_encoded}"
    r2=requests.get(places_url)
    txt=r2.text
    obj=json.loads(txt)
    t1=(obj['results'])
    return render(request,'home/fashion.html',{'t1':t1})

def painter(request):
    api_key='FQ1sLg4uqEfaszO2Xbgm8ywIPbe4jsAb'
    places_endpoint="https://api.tomtom.com/search/2/nearbySearch/.JSON"
    params_2={
        "key":api_key,
    "lat":19.2183,
    "lon":72.9781,
    "limit":10,
    "countrySet":"IN",
    "radius":30000,
    "categorySet":7372012
    }
    params_2_encoded=urlencode(params_2)
    t1={}
    places_url=f"{places_endpoint}?{params_2_encoded}"
    r2=requests.get(places_url)
    txt=r2.text
    obj=json.loads(txt)
    t1=(obj['results'])
    return render(request,'home/painter.html',{'t1':t1})

def jwellery(request):
    api_key='FQ1sLg4uqEfaszO2Xbgm8ywIPbe4jsAb'
    places_endpoint="https://api.tomtom.com/search/2/nearbySearch/.JSON"
    params_2={
        "key":api_key,
    "lat":19.2183,
    "lon":72.9781,
    "limit":10,
    "countrySet":"IN",
    "radius":30000,
    "categorySet":9361036
    }
    params_2_encoded=urlencode(params_2)
    t1={}
    places_url=f"{places_endpoint}?{params_2_encoded}"
    r2=requests.get(places_url)
    txt=r2.text
    obj=json.loads(txt)
    t1=(obj['results'])

    

    #print(t1)
    return render(request,'home/jwellery.html',{'t1':t1})

def food(request):
    api_key='FQ1sLg4uqEfaszO2Xbgm8ywIPbe4jsAb'
    places_endpoint="https://api.tomtom.com/search/2/nearbySearch/.JSON"
    params_2={
        "key":api_key,
    "lat":19.2183,
    "lon":72.9781,
    "limit":10,
    "countrySet":"IN",
    "radius":30000,
    "categorySet":7315023
    }
    params_2_encoded=urlencode(params_2)
    t1={}
    places_url=f"{places_endpoint}?{params_2_encoded}"
    r2=requests.get(places_url)
    txt=r2.text
    obj=json.loads(txt)
    t1=(obj['results'])


    
        

    
    return render(request,'home/food.html',{'t1':t1})

def recipe(request):
    recipe={}
    if 'i' in request.GET:
        i=request.GET['i'] 
        places_endpoint="http://www.recipepuppy.com/api/"
        params_2={
            "i":i,
            #"q":q,
            "p":10
            }
        params_2_encoded=urlencode(params_2)
        places_url=f"{places_endpoint}?{params_2_encoded}"
        r2=requests.get(places_url)
        txt=r2.text
        obj=json.loads(txt)
        #print(type(obj["results"]))
        recipe=(obj["results"])

    
    return render(request,'home/recipe.html',{'recipe':recipe})

def clothes(request):
    api_key='FQ1sLg4uqEfaszO2Xbgm8ywIPbe4jsAb'
    places_endpoint="https://api.tomtom.com/search/2/nearbySearch/.JSON"
    params_2={
        "key":api_key,
    "lat":19.2183,
    "lon":72.9781,
    "limit":10,
    "countrySet":"IN",
    "radius":30000,
    "categorySet":9361004
    }
    params_2_encoded=urlencode(params_2)
    t1={}
    places_url=f"{places_endpoint}?{params_2_encoded}"
    r2=requests.get(places_url)
    txt=r2.text
    obj=json.loads(txt)
    t1=(obj['results'])
    return render(request,'home/clothes.html',{'t1':t1})

def travel(request):
    api_key='FQ1sLg4uqEfaszO2Xbgm8ywIPbe4jsAb'
    places_endpoint="https://api.tomtom.com/search/2/nearbySearch/.JSON"
    params_2={
        "key":api_key,
    "lat":19.2183,
    "lon":72.9781,
    "limit":10,
    "countrySet":"IN",
    "radius":30000,
    "categorySet":9361041
    }
    params_2_encoded=urlencode(params_2)
    t1={}
    places_url=f"{places_endpoint}?{params_2_encoded}"
    r2=requests.get(places_url)
    txt=r2.text
    obj=json.loads(txt)
    t1=(obj['results'])
    return render(request,'home/travel.html',{'t1':t1})

class PostView(ListView):
    model=Post
    template_name='home/post_list.html'
    ordering=['-id']
    

class PostDetailView(DetailView):
    model=Post
    template_name='home/post_detail.html'
    

class PostUpdateView(UpdateView):
    model=Post
    template_name='home/editpost.html'
    fields=['title','title_tag','body']

class PostDeleteView(DeleteView):
    model=Post
    template_name='home/delete_post.html'
    success_url=reverse_lazy('post_list')

class PostAddView(CreateView):
    model=Post
    form_class=PostForm
    template_name='home/post_add.html'
    #fields='__all__'

class PostCommentView(CreateView):
    model=Comment
    template_name='home/comments.html'
    fields='__all__'
    success_url=reverse_lazy('post_list')

class RegisterUserView(generic.CreateView):
    form_class=UserCreationForm
    template_name='home/register.html'
    success_url=reverse_lazy('login')








