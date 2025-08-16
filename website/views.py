from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'success')
        else:
            messages.add_message(request,messages.ERROR,'error') 
    form = ContactForm()       
    return render(request,'website/contact.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
         return HttpResponseRedirect('/')

# def test_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Done')
#         else:
#             return render(request,'test.html',{'form':ContactForm(),'error':'not valid'})
#     form = ContactForm()
#  render(re)   return render(request,'test.html',{'form':form,'error':''})