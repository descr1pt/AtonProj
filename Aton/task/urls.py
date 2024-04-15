from django.urls import path
from .views import login_view, client_list, change_status

urlpatterns = [
    path('login/', login_view, name='login'),
    path('client_list/', client_list, name='client_list'),
    path('change_status/<int:client_id>/', change_status, name='change_status'),
]
