from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ArrayObject(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_by')
    last_modified_on = models.DateTimeField(auto_now=True)
    last_modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='last_modified_by')
    is_deleted = models.BooleanField(default=False)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='deleted_by', blank=True, default=None)

    def soft_delete(self, user):
        self.is_deleted = True
        self.deleted_by = user
        self.save()

    def undelete(self):
        self.is_deleted = False
        self.deleted_by = None
        self.save()
    
    def __str__(self):
        return f"Activity Log #{self.pk}"
    