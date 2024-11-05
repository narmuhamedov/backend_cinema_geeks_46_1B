from django.db import models


class Films(models.Model):
    GENRE_CHOICE = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Боевик', 'Боевик')
    )
    image = models.ImageField(upload_to='film/', verbose_name='загрузите картинку')
    title = models.CharField(max_length=100, verbose_name='Укажите описание фильма')
    description = models.TextField(verbose_name='Укажите описание к фильму', default='Lorem Ipsum', null=True)
    price = models.FloatField(verbose_name='Укажите цену')
    start_film = models.DateField(verbose_name='укажите дату выхода')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE, default='Комедия',
                             verbose_name='Укажите жанр')
    time_end = models.TimeField(verbose_name='Укажите время продолжительности фильма')
    director = models.CharField(max_length=30, verbose_name='Укажите режиссёра')
    trailer = models.URLField(verbose_name='Укажите ссылку трейлера с youtube')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return f'{self.title}-{self.price}$'