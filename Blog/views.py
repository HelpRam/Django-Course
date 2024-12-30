from django.shortcuts import render
from .models import Post
# posts = [
#     {
#         'author': 'Ram',
#         'title': ' Blog Post 1',
#         'content': 'First Post Content',
#         'date_posted': 'August 26 , 2018'
#     },
#     {
#         'author': 'Khusi',
#         'title': ' Blog Post 2',
#         'content': 'First Post Content',
#         'date_posted': 'August 26, 2024'
#     }

# ]



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Blog/home.html', context)


def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})