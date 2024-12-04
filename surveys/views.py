from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Survey, SurveyQuestionPairType, SurveyScoreVariable


def surveys_list(request):
    surveys = []
    for survey in Survey.objects.values_list('title', 'id'):
        surveys.append({
            'title': survey[0],
            'id': survey[1]
        })
    return JsonResponse({"surveys": surveys})


def get_survey(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)

    question_pairs = SurveyQuestionPairType.objects.filter(survey=survey)

    score_variables = set()
    # Формируем список вопросов
    questions = []
    for pair in question_pairs:
        score_variables.add(
            pair.statementA.scoreVariable
        )
        score_variables.add(
            pair.statementB.scoreVariable
        )
        questions.append(pair.as_dict)

    # Получаем все переменные оценок для данного опроса
    score_variable_list = []
    for variable in score_variables:
        if variable:
            score_variable_list.append(variable.as_dict)

    # Формируем итоговый JSON
    response_data = {
        'title': survey.title,
        'questionType': 'pair',
        'questions': questions,
        'scoreVariables': score_variable_list
    }

    return JsonResponse(response_data)
