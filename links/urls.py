from django.urls import path
from .views import LinkListCreate, LinkRetrieveUpdateDestroy

urlpatterns = [
    path('links/', LinkListCreate.as_view(), name='link-list-create'),
    path('links/<int:pk>/', LinkRetrieveUpdateDestroy.as_view(), name='link-detail'),
]
