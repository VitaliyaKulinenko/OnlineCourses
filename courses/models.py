from django.db import models

from users.models import User


class Lection(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files', default='No files')
    category = models.ForeignKey('Course', on_delete=models.PROTECT, null=True)
    homework = models.TextField(default='Without hometask')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Hometask(models.Model):
    lection_homework = models.ForeignKey('Lection', on_delete=models.PROTECT, null=True)
    grade = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.lection_homework




class Course(models.Model):
    course_name = models.CharField(max_length=100, db_index=True)
    # users = models.ManyToManyField(User)

    def __str__(self):
        return self.course_name









