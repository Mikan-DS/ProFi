from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=70, unique=True)


class SurveyScoreVariable(models.Model):
    name = models.CharField(max_length=30, unique=True)

    result_title = models.CharField(max_length=70)
    description = models.TextField()


class SurveyQuestionPairTypeStatement(models.Model):
    statement = models.CharField(max_length=256)
    scoreVariable = models.ForeignKey(SurveyScoreVariable, on_delete=models.CASCADE, null=True, blank=True)


class SurveyQuestionPairType(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    statementA = models.ForeignKey(SurveyQuestionPairTypeStatement, on_delete=models.CASCADE, related_name='statementsA')
    statementB = models.ForeignKey(SurveyQuestionPairTypeStatement, on_delete=models.CASCADE, related_name='statementsB')


class EducationalInstitution(models.Model):
    name = models.CharField(max_length=256)

class Profession(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

class Specialty(models.Model):
    institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    link = models.URLField(max_length=256, blank=True, null=True)

class ProfessionSpecialty(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

class TestResultProfession(models.Model):
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
    survey_score_variable = models.ForeignKey(
        SurveyScoreVariable,
        on_delete=models.CASCADE,
        related_name='professionSurveyScoreVariable'
    )





