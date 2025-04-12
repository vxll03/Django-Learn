from django.contrib import admin
from django.urls import include, path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/', views.ProductsView.as_view(), name='products_list'),
    path('products/add/', views.AddProductView.as_view(), name='add_product')
]
