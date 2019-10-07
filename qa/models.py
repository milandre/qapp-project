"""QAPP models.

This file has the database models used
for qa module.
"""

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    """Tag model

    Fields:
      slug (char): Name of the tag, unique
    """

    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return u'%s' % self.slug

    def __unicode__(self):
        return u'%s' % self.slug

    class Meta:
        ordering = ('slug',)


class Question(models.Model):
    """Question model

    Fields:
      author (obj): ForeignKey to User
      title (char): Title of the question
      question_text (char): The question itself
      closed (bool): True if the question was
                     answered, otherwise false.
                     Default: False
      likes (int): Number of likes of the question
      tags (obj): List of objects Tags asociated to
                  the question
      pub_date (date): Publish question date
      last_update (date): Last updated
    """

    author = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               related_name='questions',
                               blank=True)
    title = models.CharField(max_length=100)
    question_text = models.TextField()
    closed = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return u'%s' % self.title

    def __unicode__(self):
        return u'%s' % self.title


class Answer(models.Model):
    """Answer model

    Fields:
      author (obj): ForeignKey to User
      question (obj): ForeignKey to Question
      answer_text (char): The answer itself
      likes (int): Number of likes of the answer
      checked (bool): True if the answer was
                      checked as good answer,
                      otherwise false. Default: False
      pub_date (date): Publish answer date
      last_update (date): Last updated
    """

    author = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               related_name='answers',
                               blank=True)
    question = models.ForeignKey(Question,
                                 on_delete=models.PROTECT,
                                 related_name='answers')
    answer_text = models.TextField()
    likes = models.IntegerField(default=0)
    checked = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.answer_text

    def __unicode__(self):
        return self.answer_text


class Comment(models.Model):

    author = models.ForeignKey(User,
                               on_delete=models.PROTECT,
                               related_name='comments',
                               blank=True)
    answer = models.ForeignKey(Answer,
                               on_delete=models.PROTECT,
                               related_name='comments')
    comment_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text

    def __unicode__(self):
        return self.comment_text
