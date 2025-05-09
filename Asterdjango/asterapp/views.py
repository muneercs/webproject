from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from . models import Moviesinfo
from . forms import Movieform

# Create your views here.
def create(request):
    frm=Movieform()

    if request.POST:
        frm=Movieform(request.POST,request.FILES) 
        if frm.is_valid(): 
            frm.save()
    else:
        frm=Movieform()
    
    return render(request,'create.html',{'frm':frm})

def list(request):
    recent_visits=request.session.get('recent_visits',[])
    count=request.session.get('count',0)
    count=int(count)
    count=(count) + 1
    request.session['count']=count
    recent_movie_set=Moviesinfo.objects.filter(pk__in=recent_visits)
    movie_set=Moviesinfo.objects.all()
    print(movie_set)
    response=render(request,'list.html',{
                    'recent_movie':recent_movie_set,
                    'movies':movie_set,'visits':count})
    return response
  
def edit(request,pk):
    
    instance_to_be_edited=Moviesinfo.objects.get(pk=pk)
    if request.POST:
        frm=Movieform(request.POST,instance=instance_to_be_edited)
        if frm.is_valid():
         instance_to_be_edited.save()
    else:
        recent_visits=request.session.get('recent_visits',[])
        recent_visits.insert(0,pk)
        request.session['recent_visits']=recent_visits
        frm=Movieform(instance=instance_to_be_edited)
    return render(request,'create.html',{'frm':frm})

def delete(request,pk):
    instance=Moviesinfo.objects.get(pk=pk)
    instance.delete()
    movie_set=Moviesinfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})



    