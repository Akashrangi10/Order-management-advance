from django.urls import path
from . import views 


urlpatterns = [
    path('index/',views.index_view,name='index'),
    # path('order/<int:order_id>',views.create_order_view,name='create-oreder'),
    path('Order/Delete/<int:orders_id>/',views.delete_order_view,name = 'delete-order'),
    path('order/',views.create_order,name='order'),
    path('update/<int:order_id>/',views.update_order,name='update'),
]