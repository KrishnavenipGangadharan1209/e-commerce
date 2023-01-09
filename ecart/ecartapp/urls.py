from django.urls import path
from . import views
app_name='ecartapp'

urlpatterns = [
    path('',views.alProdCat,name='alproductcat'),
    path('<slug:c_slug>/',views.alProdCat,name='prod_by_categ'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodDetail,name='prodDetail'),
]