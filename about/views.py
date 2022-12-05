from django.shortcuts import render


def about_me_view(request):

    return render(
        request,
        'about/about_me.html',
    )
