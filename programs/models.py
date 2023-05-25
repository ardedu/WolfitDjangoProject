from django.db import models

class Articles(models.Model):
    title = models.CharField('Titre', max_length=50)
    description = models.CharField('Description', max_length=250)
    full_text = models.TextField('Le contenu')
    date = models.DateField('Date de publication')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'
