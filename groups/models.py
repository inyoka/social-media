from django.db import models
from django.utils.text import slugify

# Create your models here.
#import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import templates
register = template.Library()

class Group(models.Model):
    name =  models.Charfield(max_length=255, unique=True, delete=CASCADE)
    slug = models.SlugField
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.namespace

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = model.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
