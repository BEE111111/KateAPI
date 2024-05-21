from rest_framework import serializers
from .models import BibText, User
import bibtexparser
from django.db import transaction


class BibTexSerializer(serializers.ModelSerializer):
    bibtex = serializers.CharField(write_only=True)

    class Meta:
        model = BibText
        fields = ('bibtex', 'username')

    def to_representation(self, instance):

        return {
            'id': instance.id,
            'doi': instance.doi,
            'url': instance.url,
            'year': instance.year,
            'month': instance.month,
            'publisher': instance.publisher,
            'volume': instance.volume,
            'pages': instance.pages,
            'author': instance.author,
            'title': instance.title,
            'journal': instance.journal,
            'bibtexkey': instance.bibtexkey,
            'address': instance.address,
            'annote': instance.annote,
            'booktitle': instance.booktitle,
            'chapter': instance.chapter,
            'crossref': instance.crossref,
            'edition': instance.edition,
            'editor': instance.editor,
            'howpublished': instance.howpublished,
            'institution': instance.institution,
            'key': instance.key,
            'note': instance.note,
            'number': instance.number,
            'organization': instance.organization,
            'school': instance.school,
            'series': instance.series,
            'type': instance.type,
            'affiliation': instance.affiliation,
            'abstract': instance.abstract,
            'eid': instance.eid,
            'contents': instance.contents,
            'copyright': instance.copyright,
            'isbn': instance.isbn,
            'issn': instance.issn,
            'keywords': instance.keywords,
            'language': instance.language,
            'location': instance.location,
            'lccn': instance.lccn,
            'mrnumber': instance.mrnumber,
            'price': instance.price,
            'size': instance.size,
            'author_in_russian': instance.author_in_russian,
            'first_author': instance.first_author,
            'other_authors': instance.other_authors,
            'quartile': instance.quartile,
            'number_of_authors': instance.number_of_authors,
            'subdivision': instance.subdivision,
            'relations': instance.relations,
            'number_of_affiliation': instance.number_of_affiliation,
            'number_of_theme': instance.number_of_theme,
            'gratitude': instance.gratitude,
            'index': instance.index,
            'ball': instance.ball,
        }

    def validate_username(self, value):
        try:
            user = User.objects.get(username=value)
            return user
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this username does not exist")

    def validate(self, data):
        user = data.get('username')
        bibtex_data = data.get('bibtex')
        parsed = bibtexparser.loads(bibtex_data)
        entry = parsed.entries[0]

        if 'doi' in entry and BibText.objects.filter(username=user.username, doi=entry['doi']).exists():
            raise serializers.ValidationError(f"This DOI '{entry['doi']}' has already been submitted by the user.")
        if 'url' in entry and BibText.objects.filter(username=user.username, url=entry['url']).exists():
            raise serializers.ValidationError(f"This URL '{entry['url']}' has already been submitted by the user.")

        data.update(entry)
        return data

    @transaction.atomic
    def create(self, validated_data):
        validated_data.pop('bibtex', None)
        validated_data.pop('ENTRYTYPE', None)
        validated_data.pop('ID', None)

        bibtext_instance = BibText.objects.create(**validated_data)
        return bibtext_instance

    def update(self, instance, validated_data):
        validated_data.pop('bibtex', None)
        validated_data.pop('ENTRYTYPE', None)
        validated_data.pop('ID', None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance



class BibTexUpdateSerializer(serializers.ModelSerializer):

    booktitle = serializers.CharField(required=False, allow_blank=True)
    number = serializers.CharField(required=False, allow_blank=True)
    author_in_russian = serializers.CharField(required=False, allow_blank=True)
    other_authors = serializers.CharField(required=False, allow_blank=True)
    quartile = serializers.CharField(required=False, allow_blank=True)
    subdivision = serializers.CharField(required=False, allow_blank=True)
    relations = serializers.CharField(required=False, allow_blank=True)
    number_of_theme = serializers.CharField(required=False, allow_blank=True)
    gratitude = serializers.CharField(required=False, allow_blank=True)
    doi = serializers.CharField(required=True, allow_blank=False)
    url = serializers.CharField(required=True, allow_blank=False)
    username = serializers.CharField(required=False, allow_blank=True)
    year = serializers.IntegerField(required=False)
    month = serializers.CharField(required=False, allow_blank=True)
    publisher = serializers.CharField(required=False, allow_blank=True)
    volume = serializers.IntegerField(required=False)
    pages = serializers.CharField(required=False, allow_blank=True)
    author = serializers.CharField(required=False, allow_blank=True)
    title = serializers.CharField(required=False, allow_blank=True)
    journal = serializers.CharField(required=False, allow_blank=True)
    checked = serializers.IntegerField(required=False)
    bibtexkey = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    annote = serializers.CharField(required=False, allow_blank=True)
    chapter = serializers.IntegerField(required=False,)
    crossref = serializers.CharField(required=False, allow_blank=True)
    edition = serializers.CharField(required=False, allow_blank=True)
    editor = serializers.CharField(required=False, allow_blank=True)
    howpublished = serializers.CharField(required=False, allow_blank=True)
    institution = serializers.CharField(required=False, allow_blank=True)
    key = serializers.CharField(required=False, allow_blank=True)
    note = serializers.CharField(required=False, allow_blank=True)
    organization = serializers.CharField(required=False, allow_blank=True)
    school = serializers.CharField(required=False, allow_blank=True)
    series = serializers.CharField(required=False, allow_blank=True)
    type = serializers.CharField(required=False, allow_blank=True)
    affiliation = serializers.CharField(required=False, allow_blank=True)
    abstract = serializers.CharField(required=False, allow_blank=True)
    eid = serializers.CharField(required=False, allow_blank=True)
    contents = serializers.CharField(required=False, allow_blank=True)
    copyright = serializers.CharField(required=False, allow_blank=True)
    isbn = serializers.CharField(required=False, allow_blank=True)
    issn = serializers.CharField(required=False, allow_blank=True)
    keywords = serializers.CharField(required=False, allow_blank=True)
    language = serializers.CharField(required=False, allow_blank=True)
    location = serializers.CharField(required=False, allow_blank=True)
    lccn = serializers.CharField(required=False, allow_blank=True)
    mrnumber = serializers.CharField(required=False, allow_blank=True)
    price = serializers.CharField(required=False, allow_blank=True)
    size = serializers.CharField(required=False, allow_blank=True)
    first_author = serializers.CharField(required=False, allow_blank=True)
    number_of_authors = serializers.CharField(required=False, allow_blank=True)
    number_of_affiliation = serializers.IntegerField(required=False)
    index = serializers.CharField(required=False, allow_blank=True)
    ball = serializers.CharField(required=False, allow_blank=True)


    class Meta:
        model = BibText
        fields = '__all__'

    def update(self, instance, validated_data):

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.checked = 1
        instance.save()
        return instance
