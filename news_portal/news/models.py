from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.OneToOneField(User, verbose_name='Автор', on_delete=models.CASCADE)
    rating = models.IntegerField('Рейтинг', default=0)

    def __str__(self):
        return self.name.username

    @property
    def update_rating(self):
        new_rating = (sum([post.rating * 3 for post in Post.objects.filter(author=self.name_id)])
                      + sum(
                    [comment.rating for comment in Comments.objects.filter(author=self.name_id)])
                      + sum([comment.rating_comment for comment in
                             Comments.objects.filter(post__author=self.name_id)]))
        self.rating = new_rating
        self.save()

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Category(models.Model):
    name = models.CharField('Категория', max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    story = 'ST'
    news = 'NW'
    VARIANTS = [
        (story, 'статья'),
        (news, 'новость'),
    ]
    type = models.CharField('Тип', max_length=2, choices=VARIANTS)
    time = models.DateTimeField('Дата публикации', auto_now_add=True)
    header = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    rating = models.IntegerField('Рейтинг', default=0)
    author = models.ForeignKey(Author, verbose_name='Автор', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, verbose_name='Категории', related_name='post_category')

    @property
    def preview(self):
        size = 124 if len(self.text) > 124 else len(self.text)
        return self.text[:size] + '...'

    @property
    def like(self):
        self.rating += 1
        self.save()

    @property
    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return f'/news/{self.pk}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class Comments(models.Model):
    text = models.TextField('Текст')
    time = models.DateTimeField('Время комментария', auto_now_add=True)
    author = models.ForeignKey(Author, verbose_name='Автор комментария', on_delete=models.CASCADE)
    rating = models.IntegerField('Рейтинг', default=0)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    @property
    def like(self):
        self.rating += 1
        self.save()

    @property
    def dislike(self):
        self.rating -= 1
        self.save()

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

