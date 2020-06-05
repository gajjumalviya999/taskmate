from django.urls import path
from todolist import views

urlpatterns = [
    path('', views.todolist,name="todolist"),
    path('delete/<id>',views.delete_task,name="delete_task"),
   
    path('edit_task/<id>',views.edit_task, name="edit_task"),
    path('complete_task/<id>',views.complete_task,name="complete_task"),
    path('about',views.about,name="about")
   
]   
