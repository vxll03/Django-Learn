from django.shortcuts import redirect, render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from .forms import ProductsForm
from .models import Product


class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'myapp/products_list.html', {'products': products})
    
    
@method_decorator(login_required, name="dispatch")
class AddProductView(View):
    def get(self, request):
        form = ProductsForm()
        return render(request, 'myapp/add_product.html', {'form': form})

    def post(self, request):
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_list')
        return render(request, 'myapp/add_product.html', {'form': form})
