from django.shortcuts import render, redirect
from orders.telegram import send_message


def make_new_order(request):
    if request.method == "POST":

        user_firstname = request.POST.get("user_firstname")
        user_lastname = request.POST.get("user_lastname")
        user_phone = request.POST.get("user_phone")

        message = '*НОВАЯ ЗАЯВКА ПЕРЕЗВОНИТЬ*' + '\n\n' + '*Имя:* ' + user_firstname + '\n' + '*Фамилия:* ' + \
                  user_lastname + '\n' + '*Телефон:* ' + user_phone
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