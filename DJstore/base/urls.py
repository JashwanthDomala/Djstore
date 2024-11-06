from django.urls import path
from . import views as v

app_name = 'base'
urlpatterns = [
    path('',v.index,name='index'),
    path('add',v.add,name='add'),
    path('itpage/<str:pk>/',v.itpage,name='itpage'),
    path('buy/<str:pk>/',v.buy,name='buy'),
    path('myorder/',v.myorders,name='order'),
    path('mycart/',v.mycart,name='cart'),
    path('addcart/<str:pk>/',v.addcart,name='addcart')
]