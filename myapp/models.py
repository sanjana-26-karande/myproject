from django.db import models

class Menuitems(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Menu(models.Model):
    menu_item = models.CharField(max_length=100)
    price = models.IntegerField()
    category_id = models.ForeignKey(
        MenuCategory,  
        on_delete=models.PROTECT,  
        default=None,  
        related_name='category_name' 
    )

    def __str__(self):
        return self.menu_item
    from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def __str__(self):
        return self.name
class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact time")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name