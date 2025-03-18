from django.shortcuts import render

def menu(request):
    
    menu_items = {
        'name': 'Greek Salad',
    }
    return render(request, 'menu.html', {'menu_item': menu_items})