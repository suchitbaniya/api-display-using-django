from django.shortcuts import render
import requests

def home(request):
    return render(request, 'data_display/home.html')

def search(request):
    resource_number = request.GET.get('resource_number',"" )
    print(resource_number)

    if resource_number:
        api_url =f"https://stat.ripe.net/data/announced-prefixes/data.json?resource={resource_number}"
        response = requests.get(api_url)
        data = response.json()
        print(data)


        prefixes = data['data']['prefixes']
        print(prefixes)
        context = {
            'prefixes': prefixes,
            'resource_number': resource_number,
        }

        return render(request, 'data_display/result.html', context)
    return render(request, 'data_display/home.html')



