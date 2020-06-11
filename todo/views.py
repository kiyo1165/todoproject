from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel # todomodelの呼び出し
from django.urls import reverse_lazy # リダイレクトモジュールの呼び出し。


# Create your views here.
class Todolist(ListView):
    template_name  = 'list.html' # 対象のテンプレートを指定
    model = TodoModel #使用するmodelを指定する。

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate') # クリエイトはセーブするモデルをfieldsで指定する必要がある。
    success_url = reverse_lazy('list') #データの作成後にリダイレクトする場所を指定する。

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
