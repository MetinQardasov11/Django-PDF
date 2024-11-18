from django.urls import path
from .views import *

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list-view'),
    path('test/', render_pdf_view, name='render_pdf_view'),
    path('pdf/<int:pk>/', customer_render_pdf_view, name='customer_render_pdf_view'),
]