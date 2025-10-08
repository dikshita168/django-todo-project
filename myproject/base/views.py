from django.shortcuts import render,redirect
from .models import TodoModel,HistoryModel,CompletedTask
from django.db.models import Q

# Create your views here.

#2
def home(request):
    # data = TodoModel.objects.filter(host=request.user)

    if 'q' in request.GET:
        q_data = request.GET['q']
        print(q_data)
        # data = TodoModel.objects.filter(Q(title__icontains= q_data)& Q(host=request.user) |
        #                                  Q(desc__icontains=q_data) & Q(host=request.user))

        data = TodoModel.objects.filter(Q(title__icontains= q_data)| Q(desc__icontains=q_data),host=request.user)
    else:
        data= TodoModel.objects.filter(host= request.user)
        
            

    return render(request, 'home.html', {'data':data})

def about(request):

    return render(request, 'about.html')

#1
def add(request):

    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']
        # print(title_data, desc_data)

        TodoModel.objects.create(title = title_data, desc= desc_data, host= request.user)
        return redirect('home')

    return render(request, 'add.html')

#3
def update(request,pk):
    task = TodoModel.objects.get(id=pk)

    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']

        task.title = title_data
        task.desc = desc_data
        task.save()

        return redirect('home')

    return render(request, 'update.html', {'data':task})

#4 

def delete_task(request,pk):
    task = TodoModel.objects.get(id=pk)

    return render(request, 'delete.html',{'task':task})

def confirm_del(request,pk):
    task = TodoModel.objects.get(id=pk) #return object similar to python dictionary , we target key = to get value , here task.title is key which store in HistoryModel DB 
    HistoryModel.objects.create(title = task.title, desc= task.desc,host = request.user)
    task.delete()

    return redirect('history')

#5
def history(request):
    history_data = HistoryModel.objects.filter(host=request.user)

    return render(request, 'history.html', {'task': history_data})

def restore_task(request,pk):
    delete_task = HistoryModel.objects.get(id=pk)

    TodoModel.objects.create(
        title= delete_task.title, 
        desc= delete_task.desc,
        host = request.user 
         )

    
    delete_task.delete()
    return redirect('home')

def permenant_delete(request,pk):
    history_task = HistoryModel.objects.get(id=pk)
    history_task.delete()
    return redirect('history')


# restore all & delete all 

def restore_all (request):
    deleted_task = HistoryModel.objects.filter(host= request.user)

    for task in deleted_task :
        TodoModel.objects.create(
            title= task.title,
            desc = task.desc,
            host= request.user
        )
        task.delete()

    return redirect('home')


def delete_all (request):
    task = HistoryModel.objects.filter(host = request.user).delete()
    
    return redirect('history')

#6
def details(request,pk):
    task = TodoModel.objects.get(id=pk)

    return render(request ,'details.html',{'task':task})

#7 completed

def mark_as_completed(request,pk):
    task = TodoModel.objects.get(id=pk)

    CompletedTask.objects.create(
        title= task.title,
        desc = task.desc,
        host = request.user
    )
    task.delete()

    return redirect('completed')

    
def completed(request):
    tasks = CompletedTask.objects.filter(host= request.user)

    return render(request, 'completed.html', {'tasks':tasks})



def restore_complete(request,pk):
    restore_complete = CompletedTask.objects.get(id=pk)
    TodoModel.objects.create(
        title= restore_complete.title, 
        desc= restore_complete.desc,
        host = request.user 
        )
    restore_complete.delete()
    return redirect('completed')

def remove_complete(request,pk):
    delete_complete = CompletedTask.objects.get(id=pk)
    delete_complete.delete()
    return redirect('completed')

# all 

def restore_all_complete(request):
    tasks = CompletedTask.objects.filter(host= request.user)

    for i in tasks:
        TodoModel.objects.create(
            title= i.title,
            desc = i.desc,
            host= request.user
        )
        i.delete()
    return redirect('home')


def remove_all_completed(request):
    completed_task = CompletedTask.objects.filter(host = request.user)

    completed_task.delete()
    return redirect('completed')