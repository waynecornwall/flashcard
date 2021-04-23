from django.db import models


class TermManager(models.Manager):
    def get_type_count(self, term_type):
        return self.filter(word__icontains=term_type).count()


class Term(models.Model):
    word = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    objects = TermManager()

    def __str__(self):
        return self.word


class Source(models.Model):
    title = models.CharField(max_length=200)
    media = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Definition(models.Model):
    definition = models.TextField(blank=True, null=True)
    ref_point = models.IntegerField(blank=True, null=True)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, null=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self):
        return self.definition

