from django.db import models
# from .utilities import user_directory_path
import time

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'uploads/{0}/{1}'.format(instance.id, filename)
class Detections(models.Model):

    # User inputs
    image_to_detect = models.ImageField(upload_to=f'uploads/{time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())}/',
                                        default='')
    confidence = models.FloatField(default=0.25)

    # Control field
    processed = models.BooleanField(default=False)

    # Expected results: TODO
    # code_generated = models.FileField(upload_to='codes/', null=True)
    # json_file = models.FileField(upload_to='jsonfile/', null=True)
    # detected_image_path = models.ImageField(upload_to='detectedimage/', null=True)


    def __str__(self):
        return f'{self.processed}'


