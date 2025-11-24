from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE)
    system_name = models.CharField(max_length=50)
    accessed_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-accessed_at']