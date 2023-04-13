from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('log/',log_in),
    path('edit/<int:a>/',edit_page),
    path('edit1/<int:a>/',showall_edit_page),
    path('delete/<int:a>/',delete_data),
]
