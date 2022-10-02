from django.http import HttpResponse
from django.shortcuts import render

data = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}
def omlet(request,servings):
    new_dict = data.copy()
    for key in new_dict:
        for x in new_dict[key]:
           new_dict[key][x] = new_dict[key][x] * servings
    return render(request, 'demo.html', context=new_dict)

def pasta(request, servings):
    new_dict = data.copy()
    for key in new_dict:
        for x in new_dict[key]:
            new_dict[key][x] = new_dict[key][x] * servings
    return render(request, 'pasta.html', context=new_dict)

def buter(request, servings):
    new_dict = data.copy()
    for key in new_dict:
        for x in new_dict[key]:
            new_dict[key][x] = new_dict[key][x] * servings
    return render(request, 'buter.html', context=new_dict)

