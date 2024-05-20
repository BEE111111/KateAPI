from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


    def __str__(self):
        return self.username


class BibText(models.Model):
    username = models.CharField(max_length=255, null=True)
    doi = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    year = models.IntegerField(null=True)
    month = models.CharField(max_length=255, null=True)
    publisher = models.CharField(max_length=255, null=True)
    volume = models.IntegerField(null=True)
    pages = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    journal = models.CharField(max_length=255, null=True)
    checked = models.IntegerField(default=0)
    bibtexkey = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    annote = models.CharField(max_length=255, null=True)
    booktitle = models.CharField(max_length=255, null=True)
    chapter = models.IntegerField(null=True)
    crossref = models.CharField(max_length=255, null=True)
    edition = models.CharField(max_length=255, null=True)
    editor = models.CharField(max_length=255, null=True)
    howpublished = models.CharField(max_length=255, null=True)
    institution = models.CharField(max_length=255, null=True)
    key = models.CharField(max_length=255, null=True)
    note = models.CharField(max_length=255, null=True)
    number = models.CharField(max_length=255, null=True)
    organization = models.CharField(max_length=255, null=True)
    school = models.CharField(max_length=255, null=True)
    series = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    affiliation = models.CharField(max_length=255, null=True)
    abstract = models.CharField(max_length=255, null=True)
    eid = models.CharField(max_length=255, null=True)
    contents = models.CharField(max_length=255, null=True)
    copyright = models.CharField(max_length=255, null=True)
    isbn = models.CharField(max_length=255, null=True)
    issn = models.CharField(max_length=255, null=True)
    keywords = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    lccn = models.CharField(max_length=255, null=True)
    mrnumber = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)
    size = models.CharField(max_length=255, null=True)
    index = models.CharField(max_length=255, null=True)
    ball = models.CharField(max_length=255, null=True)
    author_in_russian = models.CharField(max_length=255, null=True)
    first_author = models.CharField(max_length=255, null=True)
    other_authors = models.CharField(max_length=255, null=True)
    quartile = models.CharField(max_length=255, null=True)
    number_of_authors = models.CharField(max_length=255, null=True)
    subdivision = models.CharField(max_length=255, null=True)
    relations = models.CharField(max_length=255, null=True)
    number_of_affiliation = models.IntegerField(null=True)
    number_of_theme = models.CharField(max_length=255, null=True)
    gratitude = models.CharField(max_length=255, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'doi'], name='unique_user_doi'),
            models.UniqueConstraint(fields=['username', 'url'], name='unique_user_url')
        ]

    def __str__(self):
        return self.title


class Scientist(models.Model):
    username = models.CharField(max_length=255, unique=True)
    author_in_russian = models.CharField(max_length=255, null=True)
    first_author = models.CharField(max_length=255, null=True)
    job_title = models.CharField(max_length=255, null=True)
    relations = models.CharField(max_length=255, null=True)
    science_title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.username


