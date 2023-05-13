from django.shortcuts import render

# Create your views here.
def userdefined_filetrs(request):
    d={'data':'Hi my NAMe is RamESHreddy'}
    return render(request,'userdefined_filetrs.html',d)