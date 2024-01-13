from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# post = [
#     {
#         'author':'Jhon Cena',
#         'title': '1st post',
#         'content': "Today is Gift That's why it called Present ",
#         'date_posted': 'Jan 12 2024',
#     },
#     {
#         'author':'Rey Mysterio',
#         'title': '2nd post',
#         'content': "Bhuyaaka bhuyakaa 619 ",
#         'date_posted': 'Jan 13 2024',
#     }
# ]

# Create your views here.
def home(request):
    context = {'post':Post.objects.all()}
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title' : 'About'})