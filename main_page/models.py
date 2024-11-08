from django.core.validators import MinValueValidator, MaxValueValidator
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

    def average_rating(self):
        reviews  = self.review_films.all()
        if reviews:
            return sum(review.mark for review in reviews) / reviews.count()
        return None

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'

    def __str__(self):
        return f'{self.title}-{self.price}$'


class ReviewFilm(models.Model):
    review_films = models.ForeignKey(Films, on_delete=models.CASCADE,
                                     related_name='review_films')
    created_at = models.DateField(auto_now_add=True)
    description = models.TextField(verbose_name='Оставьте отзыв о фильме')
    mark = models.PositiveIntegerField(verbose_name='Укажите оценку от 1 до 5',
                                       validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.review_films}-{self.created_at}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'
