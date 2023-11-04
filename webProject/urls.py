"""
URL configuration for webProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

### Static files importing to url structure
from django.conf import settings
from django.conf.urls.static import static

"""

URL YAPILARINDA VE UYGULAMA YAPISINDA GENEL AMAÇ ŞU:

Her okul için ayrı bir uygulama oluşturulacak. Bu uygulamaların içindeki url yapıları da ayrı olacak. 
Bu url yapıları django subdomain yapısına uygun olacak şekilde oluşturulacak, 
her bir uygulama store uygulamasını baz alacak. store uygulamasında sm değişkeni ile okul yönetimi belirlenecek.
Bu sm değişkeni ile okul yönetimine ait ürünlerin listelenmesi sağlanacak. 
Benzer şekilde bu değişken sayesinde giriş ekranı da okula göre seçilmiş olacak.

Yeni bir okul kaydedilmek istendiğinde tek yapılması gereken yeni bir uygulama oluşturmak (store uygulaması kopyalanacak) 
ve bu uygulamayı settings.py içindeki INSTALLED_APPS listesine eklemek olacak, 
daha sonrasında sm değişkeni ile okul yönetimi belirlenecek ve okula özel url yapısı oluşturulacak.

"""



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('store.urls')),
    path("user/", include('members.urls')), # Bu buradan silinip store.urls içine entegre edilecek
    # path("bahcesehir/", include('bahcesehir.urls')),
    # path("mektebim/", include('mektebim.urls')),
    # path("bil/", include('bil.urls')),
    # path("kavram/", include('kavram.urls')),
    # path("girne/", include('girne.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
