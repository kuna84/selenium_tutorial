from django.shortcuts import render


def home_view(request):
    return render(request, 'sel_tut_app/home.html')


def about_selenium_view(request):
    return render(request, 'sel_tut_app/about_selenium.html')


def code_examples_view(request):
    return render(request, 'sel_tut_app/code_examples.html')


def page_object_view(request):
    return render(request, 'sel_tut_app/page_object.html')


def playground_view(request):
    return render(request, 'sel_tut_app/playground.html')


def contact_view(request):
    return render(request, 'sel_tut_app/contact.html')


def text_formats_view(request):
    return render(request, 'sel_tut_app/text_formats.html')


def buttons_view(request):
    return render(request, 'sel_tut_app/buttons.html')


def messages_view(request):
    return render(request, 'sel_tut_app/messages.html')


def radio_checkbox_view(request):
    return render(request, 'sel_tut_app/radio_checkbox.html')


def sliders_view(request):
    return render(request, 'sel_tut_app/sliders.html')


def login_view(request):
    return render(request, 'sel_tut_app/login.html')


def my_account_view(request):
    return render(request, 'sel_tut_app/myaccount.html')


def text_fields(request):
    return render(request, 'sel_tut_app/text_fields.html')


def video_player(request):
    return render(request, 'sel_tut_app/video_player.html')


def audio_player(request):
    return render(request, 'sel_tut_app/audio_player.html')


def iframe(request):
    return render(request, 'sel_tut_app/iframe.html')


def form_1(request):
    return render(request, 'sel_tut_app/form_1.html')


def form_2(request):
    return render(request, 'sel_tut_app/form_2.html')


def accordion(request):
    return render(request, 'sel_tut_app/accordion.html')


def tabs(request):
    return render(request, 'sel_tut_app/tabs.html')


def sidenav(request):
    return render(request, 'sel_tut_app/sidenav.html')
