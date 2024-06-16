from django.db import models

# Create your models here.
class Room(models.Model):
    # host
    # topic
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = // all users active in a room
    updated = models.DateTimeField(auto_now=True)
        #timestamps everytime the save method is called
    create = models.DateTimeField(auto_now_add=True)
    #auto_now_add - only timestamps when we 1st save this instance, not each update

    def __str__(self):
        return str(self.name)