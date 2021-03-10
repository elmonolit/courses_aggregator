from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

from pytils.translit import slugify


class Specialization(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название специализации")
    courses = models.ManyToManyField('Course', verbose_name='Курсы в специализации', blank=True)
    schools = models.ManyToManyField('School', verbose_name='Школы в специализации', blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # return super().save(*args, **kwargs)
        super().save(*args, **kwargs)
        for s in self.schools.all():
            print(s)
            s.school_spec.add(self)
            print(s.school_spec)
            s.save()
        # return super().save(*args, **kwargs)

    def get_absolute_url(self):
        ct = self.__class__.__name__.lower()
        return reverse('detail', kwargs={'ct': ct, 'slug': self.slug})

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class School(models.Model):
    name = models.CharField(max_length=255, verbose_name='Школа')
    logo = models.ImageField(upload_to='school', verbose_name='Логотип школы')
    school_spec = models.ManyToManyField(Specialization, verbose_name='Специализация школы', blank=True)
    description = models.TextField(verbose_name='Описание школы')
    rating = models.PositiveSmallIntegerField(default=5, verbose_name='Рейтинг')
    courses = models.ManyToManyField('Course', verbose_name='Список курсов', blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def rating_by_reviews(self):
        sum_of_reviews_rating = sum([r.rating for r in self.schoolreview_set.all()])
        number_of_reviews = len(self.schoolreview_set.all())
        self.rating = sum_of_reviews_rating / number_of_reviews
        self.save()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        ct = self.__class__.__name__.lower()
        return reverse('detail', kwargs={'ct': ct, 'slug': self.slug})

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название курса')
    photo = models.ImageField(upload_to='courses', verbose_name='Фото курса', blank=True, null=True)
    which_school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name='Школа')
    price = models.IntegerField(verbose_name='Цена за курс', blank=True, null=True)
    start_date = models.DateTimeField(verbose_name='Дата начала', blank=True, null=True)
    duration = models.IntegerField(verbose_name='Продолжительность мес.', blank=True, null=True)
    school_spec = models.ManyToManyField(Specialization, verbose_name='Специализация курса')
    course_description = models.TextField(verbose_name='Описание курса', blank=True)
    diplome = models.BooleanField(verbose_name='Наличие диплома')
    course_programm = models.TextField(verbose_name='Программа курса')
    rating = models.PositiveSmallIntegerField(verbose_name='Рейтинг курса', default=5)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def rating_by_review(self):
        sum_of_reviews_rating = sum([r.rating for r in self.coursereview_set.all()])
        number_of_reviews = len(self.coursereview_set.all())
        self.rating = sum_of_reviews_rating / number_of_reviews
        self.save()

    def get_absolute_url(self):
        ct = self.__class__.__name__.lower()
        return reverse('detail', kwargs={'ct': ct, 'slug': self.slug})

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Review(models.Model):
    owner = models.ForeignKey('UserProfile', on_delete=models.DO_NOTHING, verbose_name='Кто написал')
    rating = models.PositiveSmallIntegerField(default=5, verbose_name='Рейтинг')
    comment = models.CharField(max_length=1000, verbose_name="Комментарий")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner.user.username

    class Meta:
        abstract = True


class SchoolReview(Review):
    school_review = models.ForeignKey(School, on_delete=models.DO_NOTHING, verbose_name='какая школа')

    def save(self, *args, **kwargs):
        super(SchoolReview, self).save(*args, **kwargs)
        self.school_review.rating_by_reviews()

    def __str__(self):
        return super().__str__() + str(self.school_review)

    class Meta:
        verbose_name = 'Отзыв о школе'
        verbose_name_plural = "Отзывы о школе"
        # unique_together = [['owner','school_review']]


class CourseReview(Review):
    course_review = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='какой курс')

    def save(self, *args, **kwargs):
        super(CourseReview, self).save(*args, **kwargs)
        self.course_review.rating_by_review()

    def __str__(self):
        return super().__str__() + str(self.course_review)

    class Meta:
        verbose_name = 'Отзыв о курсе'
        verbose_name_plural = 'Отзывы о курсе'
        # unique_together = [['owner', 'course_review']]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, verbose_name='Имя пользователя')
    email = models.EmailField(verbose_name='Электронная почта', blank=True)
    photo = models.ImageField(upload_to='userpics', blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
