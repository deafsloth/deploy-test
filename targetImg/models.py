from django.db import models

class TargetImg(models.Model):

    target_img_id = models.BigAutoField(primary_key=True)
    file_name = models.CharField(max_length=50)
    pixel_x = models.IntegerField()
    pixel_y = models.IntegerField()
    updated_dt = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True, upload_to="uploads")

    def __str__(self):
        return self.file_name
# Create your models here.
