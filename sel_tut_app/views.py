from django.shortcuts import render


def home_view(request):
    return render(request, 'sel_tut_app/home.html')


def selenium_basics_view(request):
    return render(request, 'sel_tut_app/selenium_basics.html')


def tutorial_view(request):
    return render(request, 'sel_tut_app/tutorial.html')


def exercises_view(request):
    return render(request, 'sel_tut_app/exercises.html')


def playground_view(request):
    return render(request, 'sel_tut_app/playground.html')


def about_view(request):
    return render(request, 'sel_tut_app/about.html')


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


def text_fields_view(request):
    return render(request, 'sel_tut_app/text_fields.html')


def video_player_view(request):
    return render(request, 'sel_tut_app/video_player.html')


def audio_player_view(request):
    return render(request, 'sel_tut_app/audio_player.html')


def iframe_view(request):
    return render(request, 'sel_tut_app/iframe.html')


def form_1_view(request):
    return render(request, 'sel_tut_app/form_1.html')


def form_2_view(request):
    return render(request, 'sel_tut_app/form_2.html')


def accordion_view(request):
    return render(request, 'sel_tut_app/accordion.html')


def tabs_view(request):
    return render(request, 'sel_tut_app/tabs.html')


def sidenav_view(request):
    return render(request, 'sel_tut_app/sidenav.html')


def table_view(request):
    return render(request, 'sel_tut_app/table.html')


def draggable_view(request):
    return render(request, 'sel_tut_app/draggable.html')


def delayed_view(request):
    return render(request, 'sel_tut_app/delayed_content.html')
