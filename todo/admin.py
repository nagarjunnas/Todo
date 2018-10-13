# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv

from django.http import HttpResponse
from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ('status','created_at', 'modified_at', 'created_date_time')
    actions = ["export_as_csv"]
    list_display = ('title', 'description','created_date_time' , 'status', 'created_at', 'modified_at')


    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names_headers = [field.name.title().replace('_', ' ') for field in meta.fields]
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=todos.csv'
        writer = csv.writer(response)

        writer.writerow(field_names_headers)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected as CSV"

admin.site.register(Todo, TodoAdmin)