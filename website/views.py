from django.shortcuts import render, redirect
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
            modify_name = 'unknown'
            my_model = form.save(commit=False)
            my_model.name = modify_name
            my_model.save()
            messages.add_message(request,messages.SUCCESS,'success')
        else:
            for errors in form.errors.values():
                for error in errors: 
                    messages.add_message(request,messages.ERROR,f'{error}') 
    else:        
        form = ContactForm()       
    return render(request,'website/contact.html',{'form':form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            next_url = request.POST.get('next')
            return redirect(next_url)
    return redirect(next_url)

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