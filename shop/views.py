from django.shortcuts import render
from django.views.generic import ListView
from .models import Cart, CartItem, Product

# Create your views here.
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
def boss(request):
    return render(request, 'shop/confiance.html')


def is_admin(user):
    return user.is_authenticated
@method_decorator(user_passes_test(is_admin, login_url='/shop/boss'), name='dispatch')
class BoutiqueView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=user)
            context['cart_products'] = cart.products.all()
        return context




def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    
    
    quantity = int(request.POST.get('quantity', 1))  # Récupérer la quantité choisie
    
    # Vérifier si le produit est déjà dans le panier
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()
    if cart_item:
        cart_item.quantity += quantity  # Ajouter la quantité choisie
        cart_item.save()
    else:
        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=quantity)
    
    return redirect('cart')  # Redirige vers la page du panier après l'ajout au panier
@method_decorator(user_passes_test(is_admin, login_url='/users/login'), name='dispatch')
class CartView(ListView):
    model = Cart
    template_name = 'cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def delete_cart_item(request, pk):
        cart_item = get_object_or_404(CartItem, pk=pk)
        cart_item.delete()
        return redirect('cart')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.get_queryset().first()  # Récupérer le panier de l'utilisateur
        if cart:
            cart_items = CartItem.objects.filter(cart=cart)
            context['cart_items'] = cart.cartitem_set.all()  # Récupérer les produits du panier
        return context
    
def error(request):
    return render(request, 'shop/error.html')