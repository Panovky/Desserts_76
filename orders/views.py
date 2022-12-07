from django.shortcuts import render
from django.shortcuts import redirect
import smtplib
from django.utils import timezone
from orders.models import Order


def make_new_order(request):
    if request.method == "POST":
        order = Order()
        order.user_firstname = request.POST.get("user_firstname")
        order.user_lastname = request.POST.get("user_lastname")
        order.date = timezone.now()
        order.save()

        server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
        server.login('', '')
        server.sendmail('', '', "New order!")
        server.quit()
        return redirect('success')
    else:
        return render(
            request,
            'orders/form_order.html',
        )


def show_success(request):

    return render(
        request,
        'orders/success.html',
    )