from django import forms
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
    TestResultProfession, SurveyQuestionPlusType
)


class SurveyQuestionPairTypeInlineForm(forms.ModelForm):
    variableA = forms.ModelChoiceField(queryset=None, label='Параметр А', required=False)
    variableB = forms.ModelChoiceField(queryset=None, label='Параметр Б', required=False)
    statementAtext = forms.CharField(label='Утверждение А', required=True, show_hidden_initial=True,
                                     widget=forms.Textarea)
    statementBtext = forms.CharField(label='Утверждение Б', required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['variableA'].queryset = SurveyScoreVariable.objects.all()
        self.fields['variableB'].queryset = SurveyScoreVariable.objects.all()

    def get_initial_for_field(self, field, field_name):
        if field_name == 'variableA' and self.instance.survey_id:
            field.queryset = SurveyScoreVariable.objects.filter(
                survey=self.instance.survey
            )
            if self.instance.statementA_id:
                return self.instance.statementA.scoreVariable
        elif field_name == 'variableB' and self.instance.survey_id:
            field.queryset = SurveyScoreVariable.objects.filter(
                survey=self.instance.survey
            )
            if self.instance.statementB_id:
                return self.instance.statementB.scoreVariable
        elif field_name == 'statementAtext' and self.instance.statementA_id:
            return self.instance.statementA.statement
        elif field_name == 'statementBtext' and self.instance.statementB_id:
            return self.instance.statementB.statement
        return super().get_initial_for_field(field, field_name)

    def save(self, commit=True):
        statementAtext = self.cleaned_data.get('statementAtext', None)
        variableA = self.cleaned_data.get('variableA', None)
        statementBtext = self.cleaned_data.get('statementBtext', None)
        variableB = self.cleaned_data.get('variableB', None)

        if not self.instance.statementA_id:
            self.instance.statementA = SurveyQuestionPairTypeStatement.objects.create(
                statement=statementAtext,
                scoreVariable=variableA
            )
        else:
            self.instance.statementA.scoreVariable = variableA
            self.instance.statementA.statement = statementAtext
            self.instance.statementA.save()

        if not self.instance.statementB_id:
            self.instance.statementB = SurveyQuestionPairTypeStatement.objects.create(
                statement=statementBtext,
                scoreVariable=variableB
            )
        else:
            self.instance.statementB.scoreVariable = variableB
            self.instance.statementB.statement = statementBtext
            self.instance.statementB.save()

        return super().save(commit=commit)

    class Meta:
        model = SurveyQuestionPairType
        fields = ["statementAtext", "variableA", "statementBtext", "variableB"]


class SurveyQuestionPlusTypeInlineForm(forms.ModelForm):
    variable = forms.ModelChoiceField(queryset=None, label='Параметр', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['variable'].queryset = SurveyScoreVariable.objects.all()
        if self.instance.pk:
            self.fields['variable'].queryset = SurveyScoreVariable.objects.filter(
                survey=self.instance.survey
            )
        else:
            self.fields['variable'].queryset = SurveyScoreVariable.objects.all()

    def get_initial_for_field(self, field, field_name):
        if field_name == 'variable' and self.instance.survey_id:
            if self.instance.scoreVariable:
                return self.instance.scoreVariable
        return super().get_initial_for_field(field, field_name)


    def save(self, commit=True):
        variable = self.cleaned_data.get('variable', None)

        self.instance.scoreVariable = variable

        return super().save(commit=commit)

    class Meta:
        model = SurveyQuestionPlusType
        fields = ["question", "variable"]


class SurveyQuestionPairTypeInline(admin.StackedInline):
    model = SurveyQuestionPairType
    extra = 1
    # form = SurveyQuestionPairTypeStatementInlineForm
    # inlines = [SurveyQuestionPairTypeStatementInline]
    form = SurveyQuestionPairTypeInlineForm

class SurveyQuestionPlusTypeInline(admin.TabularInline):
    model = SurveyQuestionPlusType
    form = SurveyQuestionPlusTypeInlineForm
    extra = 1

class SurveyScoreVariableInline(admin.TabularInline):
    model = SurveyScoreVariable
    extra = 0


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

    inlines = [
        SurveyScoreVariableInline,
        SurveyQuestionPairTypeInline,
        SurveyQuestionPlusTypeInline
    ]


#
#

class TestResultProfessionInline(admin.TabularInline):
    model = TestResultProfession
    extra = 1


@admin.register(SurveyScoreVariable)
class SurveyScoreVariableAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'survey')
    search_fields = ('name', 'title')
    list_filter = ('survey',)
    inlines = [TestResultProfessionInline]


#
#
# @admin.register(SurveyQuestionPairTypeStatement)
# class SurveyQuestionPairTypeStatementAdmin(admin.ModelAdmin):
#     list_display = ('id', 'statement', 'scoreVariable')
#     search_fields = ('statement',)
#
#
# @admin.register(SurveyQuestionPairType)
# class SurveyQuestionPairTypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'survey', 'statementA', 'statementB')
#     search_fields = ('survey__title',)
#
#


class SpecialtyInline(admin.TabularInline):
    model = Specialty
    extra = 1


@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    search_fields = ('name',)
    inlines = [SpecialtyInline]


class ProfessionSpecialtyInline(admin.TabularInline):
    model = ProfessionSpecialty
    extra = 1


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)

    inlines = [ProfessionSpecialtyInline, TestResultProfessionInline]


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'id')
    search_fields = ('name', 'institution')

    inlines = [ProfessionSpecialtyInline]
#
#
# @admin.register(ProfessionSpecialty)
# class ProfessionSpecialtyAdmin(admin.ModelAdmin):
#     list_display = ('id', 'profession', 'specialty')
#     search_fields = ('profession__name', 'specialty__name')
#
#
# @admin.register(TestResultProfession)
# class TestResultProfessionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'profession', 'survey_score_variable')
#     search_fields = ('profession__name', 'survey_score_variable__name')
