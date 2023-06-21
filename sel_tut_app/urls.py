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
    path('text-formats/', views.text_formats_view, name='text_formats'),
    path('buttons/', views.buttons_view, name='buttons'),
    path('messages/', views.messages_view, name='messages'),
    path('radio-checkbox/', views.radio_checkbox_view, name='radio_checkbox'),
    path('sliders/', views.sliders_view, name='sliders'),
    path('login/', views.login_view, name='login'),
    path('my-account/', views.my_account_view, name='my_account'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
