from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'sel_tut_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about-selenium/', views.about_selenium_view, name='about_selenium'),
    path('code-examples/', views.code_examples_view, name='code_examples'),
    path('page-object/', views.page_object_view, name='page_object'),
    path('playground/', views.playground_view, name='playground'),
    path('contact/', views.contact_view, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
