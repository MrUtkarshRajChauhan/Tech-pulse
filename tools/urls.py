from django.urls import path
from . import views

urlpatterns = [
    path('', views.tool_list, name='tool_list'),
    path('tool/<int:pk>/', views.ToolDetailView.as_view(), name='tool_detail'),
    path('add/', views.ToolCreateView.as_view(), name='tool_add'),
]