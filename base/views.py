from django.shortcuts import render,redirect
from base.models import TaskModel,HistoryModel,CompleteModel

# Create your views here.


def home(request):

    all_tasks=TaskModel.objects.all()

    if len(all_tasks)==0:
        return render(request,'home.html',{'all_tasks':all_tasks,'notask':True})

    return render(request,'home.html',{'all_tasks':all_tasks})

def add(request):

    if request.method=='POST':
        title_data=request.POST['title']
        desc_data=request.POST['desc']
        
        TaskModel.objects.create(title=title_data,desc=desc_data)
        return redirect('home')

    return render(request,'add.html')


def edit(request,pk):
    task=TaskModel.objects.get(id=pk)
    print(task.title)

    if request.method == 'POST':
        title_data=request.POST['title']
        desc_data=request.POST['desc']

        task.title = title_data
        task.desc =desc_data
        task.save()
        return redirect('home')

    return render(request,'edit.html',{'task':task})


def confirm_delete(request,pk):
    task=TaskModel.objects.get(id=pk)
   
    return render(request,'confirm_delete.html',{'task':task})


def delete_(request,pk):
    task=TaskModel.objects.get(id=pk)
    HistoryModel.objects.create(title=task.title,desc=task.desc)
    task.delete()
    return redirect('home')


def history(request):

    history_all=HistoryModel.objects.all()
    if len(history_all)==0:
        return render(request,'history.html',{'history_all':history_all,'nohistory':True})

    return render(request,'history.html',{'history_all':history_all})


def delete_history_confirm(request,pk):

        history_task=HistoryModel.objects.get(id=pk)
      
        return render(request,'delete_history_confirm.html',{'history_task':history_task})

def history_delete(request,pk):
    history_task=HistoryModel.objects.get(id=pk)
    history_task.delete()
    return redirect('history')
      
def history_restore(request,pk):
    history_task=HistoryModel.objects.get(id=pk)
    TaskModel.objects.create(title=history_task.title,desc=history_task.desc)
    history_task.delete()
    return redirect('home')

def history_clear(request):
    history_clear_all=HistoryModel.objects.all()
    history_clear_all.delete()
    return redirect('history')


def history_restore_all(request):
    history_all=HistoryModel.objects.all()
    for i in history_all:
        TaskModel.objects.create(title=i.title,desc=i.desc)
    history_all.delete()
    return redirect('home')


def complete_task(request,pk):
    task=TaskModel.objects.get(id=pk)
    CompleteModel.objects.create(title=task.title,desc=task.desc)
    task.delete()
    return redirect('home')

def complete(request):
    completed_data=CompleteModel.objects.all()
    return render(request,'complete.html',{'comp':completed_data})

def about(request):
    return render(request,'about.html')