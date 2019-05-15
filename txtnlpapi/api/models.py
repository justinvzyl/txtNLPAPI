from django.db import models

class UserComment(models.Model):
    created = models.DateTimeField(auto_add_now = True)
    #user
    topic = models.CharField(max_length = 254, blank = False, required = True, default = 'None')
    comment = models.TextField(required = True, blank  = False)
    polarity = models.FloatField(blank = True, default = 0)
    subjectivity = models.FloatField(blank = True, default = 0)
    
    class Meta:
        ordering = ('created',)



