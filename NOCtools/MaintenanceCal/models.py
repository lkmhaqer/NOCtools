from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class entry(models.Model):
	title		= models.CharField(max_length=40)
	snippet		= models.CharField(max_length=150, blank=True)
	body		= models.TextField(max_length=10000, blank=True)
	circuitId	= models.TextField(max_length=10000, blank=True)
	created		= models.DateTimeField(auto_now_add=True)
	date		= models.DateField(blank=True)
	creator		= models.ForeignKey(User, blank=True, null=True)
	remind		= models.BooleanField(default=False)

	def __unicode__(self):
		if self.title:
			return unicode(self.creator) + u" - " + self.title
		else:
			return unicode(self.creator) + u" - " + self.snipper[:40]

	def short(self):
		if self.snippet:
			return "<b>%(title)s</b> - %(snippet)s" % {'title': self.title, 'snippet': self.snippet}
		else:
			return self.title
	short.allow_tags = True

	class Meta:
		verbose_name_plural = "entries"

class entryAdmin(admin.ModelAdmin):
	list_display	= ["creator", "date", "title", "snippet"]
	list_filter	= ["creator"]

admin.site.register(entry, entryAdmin)
