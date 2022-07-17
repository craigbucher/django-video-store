from django.shortcuts import render

# Create your views here.
def index(request):
    response = render(request, 'pages/index.html')
    return response

def get_videos(request):
    pass

def get_customers(request):
    pass

def get_customer(request):
    pass

def add_customer(request):
    pass

def rent_video(request):
    pass

def return_video(request):
    pass