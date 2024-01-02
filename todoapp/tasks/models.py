from django.db import models

class Tugas(models.Model):
    judul = models.CharField(max_length=200)
    selesai= models.BooleanField(default=False)
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Create your models here.
