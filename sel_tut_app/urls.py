from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'sel_tut_app'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('selenium-basics/', views.selenium_basics_view, name='selenium_basics'),
    path('tutorial/', views.tutorial_view, name='tutorial'),
    path('exercises/', views.exercises_view, name='exercises'),
    path('playground/', views.playground_view, name='playground'),
    path('about/', views.about_view, name='about'),
    path('text-formats/', views.text_formats_view, name='text_formats'),
    path('buttons/', views.buttons_view, name='buttons'),
    path('messages/', views.messages_view, name='messages'),
    path('radio-checkbox/', views.radio_checkbox_view, name='radio_checkbox'),
    path('sliders/', views.sliders_view, name='sliders'),
    path('login/', views.login_view, name='login'),
    path('my-account/', views.my_account_view, name='my_account'),
    path('text-fields/', views.text_fields, name='text_fields'),
    path('video-player/', views.video_player, name='video_player'),
    path('audio-player/', views.audio_player, name='audio_player'),
    path('iframe/', views.iframe, name='iframe'),
    path('form_1/', views.form_1, name='form_short'),
    path('form_2/', views.form_2, name='form_long'),
    path('accordion/', views.accordion, name='accordion'),
    path('tabs/', views.tabs, name='tabs'),
    path('sidenav/', views.sidenav, name='sidenav'),
    path('table/', views.table, name='table'),
    path('draggable/', views.draggable, name='draggable'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
