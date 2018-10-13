# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    status_choices = (
        ('in_progress', 'Progress'),
        ('completed', 'Completed'),
        ('pending', 'Pending'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200, choices=status_choices, default='in_progress')
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title 
