from django.urls import path
from .views import FishList, FishDetail

urlpatterns = [
    path('', FishList.as_view(), name='fish_list'),
    path('<int:pk>/', FishDetail.as_view(), name='fish_detail'),
]