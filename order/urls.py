from django.urls import path
from . import views

urlpatterns = [
    path('create_item/', views.create_item, name='create_item'),
    path('item_list/', views.item_list, name='item_list'),
    path('items/<int:item_id>/', views.item_detail, name='item_detail'),  # رابط لصفحة التفاصيل

    path('create_item2/', views.create_item2, name='create_item2'),
    path('item_list2/', views.item_list2, name='item_list2'),
    path('items2/<int:item_id>/', views.item_detail2, name='item_detail2'),  # رابط لصفحة التفاصيل

    path('create_item3/', views.create_item3, name='create_item3'),
    path('item_list3/', views.item_list3, name='item_list3'),
    path('items3/<int:item_id>/', views.item_detail3, name='item_detail3'),  # رابط لصفحة التفاصيل


]