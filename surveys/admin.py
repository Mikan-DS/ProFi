from django.contrib import admin
from .models import (
    Survey,
    SurveyScoreVariable,
    SurveyQuestionPairTypeStatement,
    SurveyQuestionPairType,
    EducationalInstitution,
    Profession,
    Specialty,
    ProfessionSpecialty,
    TestResultProfession
)


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(SurveyScoreVariable)
class SurveyScoreVariableAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    search_fields = ('name', 'title')


@admin.register(SurveyQuestionPairTypeStatement)
class SurveyQuestionPairTypeStatementAdmin(admin.ModelAdmin):
    list_display = ('id', 'statement', 'scoreVariable')
    search_fields = ('statement',)


@admin.register(SurveyQuestionPairType)
class SurveyQuestionPairTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'survey', 'statementA', 'statementB')
    search_fields = ('survey__title',)


@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('id', 'institution', 'name', 'link')
    search_fields = ('name', 'institution__name')


@admin.register(ProfessionSpecialty)
class ProfessionSpecialtyAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession', 'specialty')
    search_fields = ('profession__name', 'specialty__name')


@admin.register(TestResultProfession)
class TestResultProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession', 'survey_score_variable')
    search_fields = ('profession__name', 'survey_score_variable__name')
