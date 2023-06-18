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
