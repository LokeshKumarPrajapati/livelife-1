from django.contrib import admin
from .models import DonationCause, Donor, BlogPost, ContactForm


# Register your models here.
admin.site.register(Donor)
admin.site.register(DonationCause)
admin.site.register(BlogPost)
admin.site.register(ContactForm)
