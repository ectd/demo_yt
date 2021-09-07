from django.urls import path
from django.views.generic import DetailView
from demo.models.personne import Personne
from demo.models.application import application
from demo.models.product import product
from demo.models.indication import indication
from demo.models.app_type import app_type
from demo.models.region import region


from .views import home, personne, application, product, indication, app_type, region

urlpatterns = [
    
    path('', home.index, name="home"),
    
    #personne
    path('personnes', personne.personne_list, name="personnes"),
    path('personnes/create', personne.CreatePersonne.as_view(), name="create_personne"),
    path('personnes/update/<int:pk>/', personne.UpdatePersonne.as_view(), name="update_personne"),
    path('personnes/<int:pk>/', DetailView.as_view(model=Personne, template_name="demo/personne/personne_detail.html"), name="detail_personne"),
    
    
    
    # #product
    path('product', product.product_list, name="product"),
    path('product/create', product.CreateProduct.as_view(), name="create_product"),
    path('product/update/<int:pk>/', product.UpdateProduct.as_view(), name="update_product"),
    path('product/<int:pk>/', DetailView.as_view(model=product, template_name="demo/product/product_detail.html"), name="detail_product"),
    # #indication
    path('indication', indication.indication_list, name="indication"),
    path('indication/create', indication.CreateIndication.as_view(), name="create_indication"),
    path('indication/update/<int:pk>/', indication.UpdateIndication.as_view(), name="update_indication"),
    path('indication/<int:pk>/', DetailView.as_view(model=indication, template_name="demo/indication/indication_detail.html"), name="detail_indication"),
    # #application
    path('application', application.application_list, name="application"),
    path('application/create', application.CreateApplication.as_view(), name="create_application"),
    path('application/update/<int:pk>/', application.UpdateApplication.as_view(), name="update_application"),
    path('application/<int:pk>/', DetailView.as_view(model=application, template_name="demo/application/application_detail.html"), name="detail_application"),
# #app_type
    path('app_type', app_type.app_type_list, name="app_type"),
    path('app_type/create', app_type.Createapp_type.as_view(), name="create_app_type"),
    path('app_type/update/<int:pk>/', app_type.Updateapp_type.as_view(), name="update_app_type"),
    path('app_type/<int:pk>/', DetailView.as_view(model=app_type, template_name="demo/app_type/app_type_detail.html"), name="detail_app_type"),

#region
    path('region', region.region_list, name="region"),
    path('region/create', region.Createregion.as_view(), name="create_region"),
    path('region/update/<int:pk>/', region.Updateregion.as_view(), name="update_region"),
    path('region/<int:pk>/', DetailView.as_view(model=region, template_name="demo/region/region_detail.html"), name="detail_region"),

    ]