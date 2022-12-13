from django.shortcuts import render, redirect
from orders.telegram import send_message


def make_new_order(request):
    if request.method == "POST":

        user_firstname = '\n\n' + '*Имя:* ' + request.POST.get("user_firstname")

        user_lastname = request.POST.get("user_lastname")
        if user_lastname != '':
            user_lastname = '\n*Фамилия:* ' + user_lastname

        user_phone = '\n' + '*Телефон:* ' + request.POST.get("user_phone")

        order_description = request.POST.get("order_description")
        if order_description != '':
            order_description = '\n*Пожелания к заказу:* ' + order_description

        message = '*ОФОРМЛЕН НОВЫЙ ЗАКАЗ*' + user_firstname + user_lastname + user_phone + order_description
        send_message(message)

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