from django.contrib import admin
from survey.models import SurveyResponse


# Register your models here.
@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    """
    Register Artists Admin
    """

    list_display = ("name", "nationality", "item", "description")
    list_filter = ("read",)