from django.db import models
from django.contrib import admin
import base64
import porespy as ps
from io import BytesIO
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# IMPORTANT: Run these 3 commands when creating a new model
# python manage.py migrate
#
# python manage.py makemigrations
#
# python manage.py migrate

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    height = models.CharField(max_length=5, default="12cm")

    def __str__(self):
        return self.name


class PoreSpyTutorial(models.Model):
    porosity = models.FloatField(null=True, blank=True, default=0.6)
    blobiness = models.IntegerField(null=True, blank=True, default=2)
    dimension_x = models.IntegerField(null=True, blank=True, default=500)
    dimension_y = models.IntegerField(null=True, blank=True, default=500)

    @property
    def generated_image(self):
        int_dimension_x = int(self.dimension_x)
        int_dimension_y = int(self.dimension_y)
        float_porosity = float(self.porosity)
        int_blobiness = int(self.blobiness)
        shape_array = [int_dimension_x, int_dimension_y]

        im = ps.generators.blobs(shape=shape_array, porosity=float_porosity, blobiness=int_blobiness).tolist()
        pil_img = Image.fromarray(np.array(im))
        buff = BytesIO()
        pil_img.save(buff, format="PNG")
        new_im_string = base64.b64encode(buff.getvalue()).decode("utf-8")
        return new_im_string



