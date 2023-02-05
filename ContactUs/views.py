from django.shortcuts import render, redirect
from .forms import ContactUsForm
from .models import ContactUs
from django.contrib import messages


# def contact_us(request):
#     print(request.path)
#     if request.method == "POST":
#         print(request.POST)
#         contact_form = ContactUsForm(request.POST)
#         print(f'IS Valid {contact_form.is_valid()}')
#         if contact_form.is_valid():
#             name = contact_form.cleaned_data.get('name')
#             email = contact_form.cleaned_data.get('email')
#             subject = contact_form.cleaned_data.get('subject')
#             text = contact_form.cleaned_data.get('text')
#             ContactUs.objects.create(
#                 name=name,
#                 text=text,
#                 email=email,
#                 subject=subject
#             )
#             messages.add_message(request, messages.SUCCESS, 'پیام شام با موفقیت ثبت گردید')
#             return redirect('ContactUs:contact_us_page')
#         messages.add_message(request, messages.ERROR, 'پیام شما ثبت نشد لطفا ورودی های فرم را چک کنید')
#     else:
#         contact_form = ContactUsForm()
#     context = {'form': contact_form}
#     return render(request, 'ContactUs/contact-us.html', context)


def contact_us(request):
    contact_form = ContactUsForm(request.POST or None)
    if contact_form.is_valid():
        print(f'IS Valid {contact_form.is_valid()}')
        if contact_form.is_valid():
            name = contact_form.cleaned_data.get('name')
            email = contact_form.cleaned_data.get('email')
            subject = contact_form.cleaned_data.get('subject')
            text = contact_form.cleaned_data.get('text')
            ContactUs.objects.create(
                name=name,
                text=text,
                email=email,
                subject=subject
            )
            messages.add_message(request, messages.SUCCESS, 'پیام شام با موفقیت ثبت گردید')
            return redirect('ContactUs:contact_us_page')
        messages.add_message(request, messages.ERROR, 'پیام شما ثبت نشد لطفا ورودی های فرم را چک کنید')
    context = {'form': contact_form}
    return render(request, 'ContactUs/contact-us.html', context)
