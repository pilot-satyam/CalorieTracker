from django.shortcuts import redirect, render
from .models import food,consume
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed'] #here the plain text of data is recieved,i.e only text egg will appear
        consumed = food.objects.get(name=food_consumed) #here we will get the actual object
        user = request.user #here we will get the current logged in user
        consumed = consume(user=user,food_consumed=consumed)
        consumed.save()
        foods = food.objects.all()
    else:
        foods = food.objects.all()
    consumed_food = consume.objects.filter(user=request.user) #creating these objects to display the consumed food on the page hence pass this to the index.html
    return render(request,'myapp/index.html',{'foods':foods,'consumed_food':consumed_food})

def delete_consume(request,id):
    consumed_food = consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')#to return back to the homepage
    return render(request,'myapp/delete.html')
