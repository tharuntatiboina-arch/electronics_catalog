from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from.models import Product, Brand, Category, Review, Wishlist, PriceAlert, PriceHistory
from django.db.models import Q, Avg

def product_list(request):
    products = Product.objects.all()
    q = request.GET.get('q')
    brand_id = request.GET.get('brand')
    cat_id = request.GET.get('category')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    ram = request.GET.get('ram')

    # Advanced Search - Medium Priority
    if q:
        products = products.filter(Q(name__icontains=q) | Q(processor__icontains=q) | Q(brand__name__icontains=q))
    if brand_id:
        products = products.filter(brand_id=brand_id)
    if cat_id:
        products = products.filter(category_id=cat_id)
    if ram:
        products = products.filter(ram__icontains=ram)
    if min_price:
        products = products.filter(current_price__gte=min_price)
    if max_price:
        products = products.filter(current_price__lte=max_price)

    brands = Brand.objects.all()
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {'products':products, 'brands':brands, 'categories':categories})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    reviews = product.reviews.all()
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    price_history = product.price_history.all().order_by('date')
    # Check wishlist
    in_wishlist = False
    if request.user.is_authenticated:
        in_wishlist = Wishlist.objects.filter(user=request.user, product=product).exists()

    if request.method == 'POST' and request.user.is_authenticated:
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        if rating and comment:
            Review.objects.create(product=product, user=request.user, rating=rating, comment=comment)
            return redirect('product_detail', id=id)

    return render(request, 'products/product_detail.html', {
        'product':product, 'reviews':reviews, 'avg_rating':avg_rating,
        'price_history':price_history, 'in_wishlist':in_wishlist
    })

def compare(request):
    ids = request.GET.getlist('ids')
    products = Product.objects.filter(id__in=ids)
    return render(request, 'products/compare.html', {'products':products})

@login_required
def add_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('product_detail', id=id)

@login_required
def wishlist_view(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'products/wishlist.html', {'items':items})

@login_required
def price_alert(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        target = request.POST.get('target_price')
        PriceAlert.objects.create(user=request.user, product=product, target_price=target)
        # Email Alerts - Low but we do it
        from django.core.mail import send_mail
        send_mail(
            f'Price Alert Set for {product.name}',
            f'You will be notified when {product.name} drops below Rs.{target}',
            'admin@electrocatalog.com',
            [request.user.email],
            fail_silently=True
        )
        return redirect('product_detail', id=id)
    return render(request, 'products/price_alert.html', {'product':product})