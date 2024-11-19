from django import forms
from . import models, parser_rezka

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('rezka', 'rezka'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'rezka':
            rezka_pars = parser_rezka.parsing()
            for i in rezka_pars:
                models.Rezka.objects.create(**i)


