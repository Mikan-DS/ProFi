from django.db import models
from typing import Dict, Optional


class Survey(models.Model):
    """
    Модель для опроса.
    """
    title: str = models.CharField(max_length=70, unique=True, verbose_name="Название опроса")

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    def __str__(self) -> str:
        return self.title


class SurveyScoreVariable(models.Model):
    """
    Модель для параметра оценки опроса.
    """
    name: str = models.CharField(max_length=30, unique=True, verbose_name="Имя параметра")
    title: str = models.CharField(max_length=70, verbose_name="Заголовок при результате")
    description: Optional[str] = models.TextField(blank=True, null=True, verbose_name="Описание при результате")

    @property
    def as_dict(self) -> Dict[str, Optional[str]]:
        """
        Возвращает представление параметра оценки в виде словаря.
        """
        return {
            "name": self.name,
            "title": self.title,
            "description": self.description
        }

    class Meta:
        verbose_name = "Переменная оценки"
        verbose_name_plural = "Переменные оценки"

    def __str__(self) -> str:
        return f"{self.name} - {self.title}"


class SurveyQuestionPairTypeStatement(models.Model):
    """
    Модель для вопроса в виде пары утверждений.
    """

    statement: str = models.CharField(max_length=256, verbose_name="Утверждение")
    scoreVariable: Optional[SurveyScoreVariable] = models.ForeignKey(
        SurveyScoreVariable,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Параметр оценки"
    )

    @property
    def as_dict(self):
        """
        Возвращает представление утверждения в виде словаря.
        """
        return {
            "statement": self.statement,
            "variable": self.scoreVariable.name if self.scoreVariable else None
        }

    class Meta:
        verbose_name = "Утверждение"
        verbose_name_plural = "Утверждения"

    def __str__(self) -> str:
        return self.statement


class SurveyQuestionPairType(models.Model):
    """
    Модель для вопроса в виде пары.
    """
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name="Опрос")

    statementA: SurveyQuestionPairTypeStatement = models.OneToOneField(
        SurveyQuestionPairTypeStatement,
        on_delete=models.CASCADE,
        related_name='statementA',
        verbose_name="Утверждение A"
    )
    statementB: SurveyQuestionPairTypeStatement = models.OneToOneField(
        SurveyQuestionPairTypeStatement,
        on_delete=models.CASCADE,
        related_name='statementB',
        verbose_name="Утверждение B"
    )

    @property
    def as_dict(self) -> Dict[str, Dict[str, Optional[str]]]:
        """
        Возвращает словарь с данными пары утверждений.
        """
        return {
            "statementA": self.statementA.as_dict,
            "statementB": self.statementB.as_dict,
        }

    class Meta:
        verbose_name = "Пара вопросов"
        verbose_name_plural = "Пары вопросов"

    def __str__(self) -> str:
        return f"{self.statementA.statement} - {self.statementB.statement}"


class EducationalInstitution(models.Model):
    """
    Модель для образовательного учреждения.
    """
    name: str = models.CharField(max_length=256, verbose_name="Название учреждения")

    class Meta:
        verbose_name = "Образовательное учреждение"
        verbose_name_plural = "Образовательные учреждения"

    def __str__(self) -> str:
        return self.name


class Profession(models.Model):
    """
    Модель для профессии.
    """
    name: str = models.CharField(max_length=256, verbose_name="Название профессии")
    description: str = models.TextField(verbose_name="Описание профессии в формате Markdown", blank=True, null=True)
    class Meta:
        verbose_name = "Профессия"
        verbose_name_plural = "Профессии"

    def __str__(self) -> str:
        return self.name


class Specialty(models.Model):
    """
    Модель для специальности.
    """
    institution: EducationalInstitution = models.ForeignKey(
        EducationalInstitution,
        on_delete=models.CASCADE,
        verbose_name="Учебное заведение"
    )
    name: str = models.CharField(max_length=256, verbose_name="Название специальности")
    link: Optional[str] = models.URLField(max_length=256, blank=True, null=True, verbose_name="Ссылка на официальный сайт")

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self) -> str:
        return f'{self.name} - {self.institution}'


class ProfessionSpecialty(models.Model):
    """
    Модель для связи между профессией и специальностью.
    """
    profession: Profession = models.ForeignKey(Profession, on_delete=models.CASCADE, verbose_name="Профессия")
    specialty: Specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name="Специальность")

    class Meta:
        verbose_name = "Специальность профессии"
        verbose_name_plural = "Специальности профессий"

    def __str__(self) -> str:
        return f"{self.profession.name} - {self.specialty.name}"


class TestResultProfession(models.Model):
    """
    Модель для соотношения результатов (параметров) к профессиям.
    """
    profession: Profession = models.ForeignKey(Profession, on_delete=models.CASCADE, verbose_name="Профессия")
    survey_score_variable: SurveyScoreVariable = models.ForeignKey(
        SurveyScoreVariable,
        on_delete=models.CASCADE,
        related_name='professionSurveyScoreVariable',
        verbose_name="Параметр оценки опроса"
    )

    class Meta:
        unique_together = (('profession', 'survey_score_variable'),)
        verbose_name = "Результат теста по профессии"
        verbose_name_plural = "Результаты тестов по профессиям"

    def __str__(self) -> str:
        return f"{self.profession} - {self.survey_score_variable}"
