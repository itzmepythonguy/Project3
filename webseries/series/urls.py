from django.urls import path
from . import views

app_name='series'

urlpatterns=[
    path('',views.Home,name='Home'),
    path('web/<int:web_id>/',views.web,name='web'),
    path('add/',views.add,name='add'),
    path('update/<int:web_id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]