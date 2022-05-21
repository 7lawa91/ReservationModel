from django.db import models



class Reservation(models.Model): 
    customer_name = models.CharField(max_length=50)
    customer_phone = models.CharField(max_length=11)
    number_of_people = models.IntegerField(default=1)
    # hotelre = models.ManyToManyField(Hotels)
    # hotel =  models.ForeignKey( Hotels, on_delete=models.CASCADE )
    hotel_name = models.CharField(max_length=50)
    res_date = models.DateField()
    trip_date = models.DateField()
    achieved_money = models.IntegerField()
    rest_of_money = models.IntegerField()
    def __str__(self) :
        return self.customer_name 


# Create your models here.
