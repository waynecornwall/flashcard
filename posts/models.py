from django.db import models

# Create your models here.


class Source(models.Model):
    title = models.CharField(max_length=200)
    media = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Term(models.Model):
    word = models.CharField(max_length=200)
    definition = models.TextField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    ref_point = models.IntegerField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.definition) > 30:
            return self.word, self.definition[:30]
        else:
            return self.word, self.definition
