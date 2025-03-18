from django.shortcuts import render

def menu(request):
    # Create a dictionary with dynamic content
    menu_items = {
        'mains': [
            {'name': 'Greek Salad', 'price': 12},
            {'name': 'Bruschetta', 'price': 8},
            {'name': 'Grilled Fish', 'price': 20},
        ]
    }
    # Pass the dictionary to the template
    return render(request, 'menu.html', menu_items)