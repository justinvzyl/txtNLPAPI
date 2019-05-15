from .nlp_utils import SentimentAnalyzer
from django.db import models



class UserComment(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey('auth.User', related_name = 'usercomments', on_delete = models.CASCADE)
    topic = models.CharField(max_length = 254, blank = False, default = 'None')
    comment = models.TextField(blank  = False)
    polarity = models.DecimalField(blank = True, default = 0, max_digits = 6, decimal_places = 6)
    subjectivity = models.DecimalField(blank = True, default = 0, max_digits = 6, decimal_places = 6)
    class Meta:
        ordering = ('created',)
    


