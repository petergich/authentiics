from django.urls import path, include
from . import views

app_name="myapp"
urlpatterns = [
    path("",views.home,name="home"),
    path("options/",views.get_filtered_options,name="get_filtered_options"),
    path('item/<int:item_id>/', views.item, name='item_detail'),
 ]
 