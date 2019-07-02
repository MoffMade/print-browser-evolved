from django.urls import path
from . import views

urlpatterns = [
    # /prints/
    path('', views.index, name='index'),
    # /prints/5
    path('<int:item_id>/', views.detail, name='detail')
]
