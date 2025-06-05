from django.contrib import admin
from .models import CourtCase, CaseDocument, AccessCode


class CaseDocumentInline(admin.TabularInline):
    model = CaseDocument
    extra = 1


class AccessCodeInline(admin.TabularInline):
    model = AccessCode
    extra = 1
    readonly_fields = ['code']


@admin.register(CourtCase)
class CourtCaseAdmin(admin.ModelAdmin):
    inlines = [CaseDocumentInline, AccessCodeInline]
    readonly_fields = ['access_code', 'created_at']
    list_display = ['case_title', 'client_name', 'trial_date']