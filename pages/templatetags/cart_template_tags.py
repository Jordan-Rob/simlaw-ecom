from django import template
from store.models import Order

register = template.Library()

@register.filter
def cart_item_counter(user):
    if user.is_authenticated:
        qs = Order.objects.filter(customer=user, complete=False)
        if qs:
            return qs[0].orderitem_set.count()
    return 0        
