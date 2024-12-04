
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

    # Формируем список вопросов
    questions = []
    for pair in question_pairs:
        questions.append({
            'statementA': {
                'statement': pair.statementA.statement,
                'variable': {
                    'name': pair.statementA.scoreVariable.name if pair.statementA.scoreVariable else None,
                    'description': pair.statementA.scoreVariable.description if pair.statementA.scoreVariable else None,
                    'title': pair.statementA.scoreVariable.result_title if pair.statementA.scoreVariable else None,
                }
            },
            'statementB': {
                'statement': pair.statementB.statement,
                'variable': {
                    'name': pair.statementB.scoreVariable.name if pair.statementB.scoreVariable else None,
                    'description': pair.statementB.scoreVariable.description if pair.statementB.scoreVariable else None,
                    'title': pair.statementB.scoreVariable.result_title if pair.statementB.scoreVariable else None,
                }
            }
        })

    # Получаем все переменные оценок для данного опроса
    score_variables = SurveyScoreVariable.objects.all()
    score_variable_list = []
    for variable in score_variables:
        score_variable_list.append({
            'name': variable.name,
            'description': variable.description,
            'title': variable.result_title,
        })

    # Формируем итоговый JSON
    response_data = {
        'title': survey.title,
        'questionType': 'pair',
        'questions': questions,
        'scoreVariables': score_variable_list
    }

    return JsonResponse(response_data)
