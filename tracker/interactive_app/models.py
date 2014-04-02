from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount

import hashlib

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    about_me = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'

    def profile_image_url(self):
        """
        Return the URL for the user's Facebook icon if the user is logged in via Facebook,
        otherwise return the user's Gravatar URL
        """
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')

        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)

        return "http://www.dotnetcodesg.com/Register/UserImage/Default.png".format(
            hashlib.md5(self.user.email).hexdigest())

    def account_verified(self):
        """
        If the user is logged in and has verified hisser email address, return True,
        otherwise return False
        """
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class User(models.Model):
    name = models.TextField(null=True)
    skillset = models.TextField(null=True)
    email = models.TextField(null=True)
    graduation_year = models.TextField(null=True)
    bio = models.TextField(null=True)
    major = models.TextField(null=True)
    img_url = models.TextField(null=True)
    portfolio = models.TextField(null=True)
    twitter = models.TextField(null=True)
    current_position = models.TextField(null=True)
    current_city = models.TextField(null=True)
    corrent_company = models.TextField(null=True)
    class Meta(object):
        verbose_name_plural = "Users"
        ordering = ('name',)
    def __unicode__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        super(User, self).save(*args, **kwargs)

class Position(models.Model):
    department = models.TextField(null=True)
    skillset = models.TextField(null=True)

class Organization(models.Model):
    name = models.TextField(null=True)
    url = models.TextField(null=True)
    bio = models.TextField(null=True)
    contact = models.TextField(null=True)
    department = models.TextField(null=True)
    city = models.TextField(null=True)
    opening = models.TextField(null=True)
    twitter = models.TextField(null=True)
    img_url = models.TextField(null=True)
    lat = models.TextField(null=True)
    longitude = models.TextField(null=True)
    class Meta(object):
        verbose_name_plural = "organizations"
        ordering = ('name',)
    def __unicode__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        super(Organization, self).save(*args, **kwargs)

class City(models.Model):
    name = models.TextField(null=True)
    state = models.TextField(null=True)
    lat = models.TextField(null=True)
    longitude = models.TextField(null=True)
    class Meta(object):
        verbose_name_plural = "cities"
        ordering = ('name',)
    def __unicode__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.name=self.name.upper()
        super(City, self).save(*args, **kwargs)

