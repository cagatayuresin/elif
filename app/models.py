from django.db import models


class FileType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    icon = models.ImageField(upload_to='filetype_icons/')

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/')
    file_type = models.ForeignKey(FileType,  on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.name

