from django.shortcuts import render

# the view handles what happens after typing an address

def index(request):
  return render(request, 'entries/index.html')

def add(request):
  return render(request, 'entries/add.html')