from django.shortcuts import render, get_object_or_404
# from django.views.generic import CreateView
from .models import posts, Product

# class PostCreateView(CreateView):
#     model = posts
#     fields = ['author', 'image']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)



def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product':product})