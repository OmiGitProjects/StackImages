from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def index(request):
        if request.method == 'POST':
                name = request.POST['imageName']
                height = request.POST['height']
                width = request.POST['width']

                context = {'stackimage':name, 'height':height, 'width':width,'NextImage':'Next Image', 'title_page':'StackImages'}
        else:
                context={}
        return render(request, 'pixogo/index.html', context)


def about(request):
        if request.method  == 'POST':
                message = request.POST['message']

                contact = Contact(contact_message=message)
                contact.save()
                messages.success(request, 'Your Message has been Sent!')
                return redirect('homepage')

        return render(request, 'pixogo/about.html')