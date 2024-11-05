# from decimal import Decimal
#
# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
#
# from delivery.models.cart import Cart
#
#
# @receiver(m2m_changed, sender=Cart.products.through)
# def sum_cart(sender, instance, action, **kwargs):
#     if action in ('post_add', 'post_remove', 'post_clear'):
#         total = Decimal('0.00')
#         for product in instance.products.all():
#             total += product.price
#         instance.sum = total
#         instance.save(update_fields=['sum'])