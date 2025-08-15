from core.models import Wishlist


def cart_total_qty(request):
    """
    Context processor to add cart content to the context.
    """
    cart = request.session.get('cart', {})

    distinct_count = len(cart)              # number of different shoes
    cart_total_qty = sum(cart.values())     # total items across shoes
    return {
        'cart_distinct_count': distinct_count,
        'cart_total_qty': cart_total_qty,
    }

def wishlist_items(request):
    """
    Context processor to add wishlist items to the context.
    """
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(user=request.user)
        return {'wishlist_items': wishlist}
    return {'wishlist_items': []}

def user_context(request):
    return {'user': request.user}   
