from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list" : [{
    "restaurant_name":"New restaurant",
    "food_type":"New food!!"
    }]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object" : {
    "restaurant_name":"New restaurant",
    "food_type":"New food!!"
    }
    }
    return render(request, 'detail.html', context)
