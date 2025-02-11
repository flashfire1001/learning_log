from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic (models.Model):

    """A topic the user is learning about."""
    #all the information that mentioned in the models will be documented in the database in format.
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
    
class Entry (models.Model):
    '''specific info learned about a topic ,logged by entries'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # cascade 指的是瀑布  
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'entries'

    def __str__ (self):
        '''a string that gives a clip if the entry, with ellipsis.'''
        if len(self.text>=50):
            return f'{self.text[:50]}...'
        else:return self.text


