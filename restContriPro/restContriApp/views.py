from django.shortcuts import render
import requests
# Create your views here.
def restContriApp(request):
    country = request.GET.get("country")  if request.GET.get("country") else "India"
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)
    jsonResp = response.json()

    payload={
        "country" : jsonResp[0]["name"]["common"],
        "capital" : (str(jsonResp[0]["capital"])),
        "population" : (int(jsonResp[0]["population"])), # in k
        "flag" : (jsonResp[0]["flags"]["png"]),
        

    }

    context = {"jsonResp" : payload}


    return render(request, 'index.html',context) 