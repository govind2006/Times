from django.db import models

# Create your models here.
class today_stories(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class current_news(models.Model):
    current_image = models.ImageField(upload_to='pics')
    Image_Description = models.TextField('Description')

class state(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class latestnews(models.Model):
    link = models.URLField('Link')
    Description = models.TextField('Description')

class editorial(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class weeklyspecial(models.Model):
    link = models.URLField('Link')
    Description = models.TextField('Description')

class otherimportantlink(models.Model):
    link = models.URLField('Link')
    Description = models.TextField('Description')

class AdvertiseTariffPlan(models.Model):
    link = models.URLField('Link')
    Description = models.TextField('Description')  


class International(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class Buisness(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')


class Sport(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')


class National(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class opinion_editorial(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class column_editorial(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class letter_editorial(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class sunday_magazine_top_stories(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class Bollywood_Buzz(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class Personality(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class Health(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class Career_Education(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class Society(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class Book_Review(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class Fashion(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class Heritage(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class Science_Technology(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')


class Art_Culture(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')

class photo_gallery(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')


class Magazine_photo(models.Model):
    image = models.ImageField(upload_to='pics')
    link = models.URLField('Link')
    Description = models.TextField('Description')
