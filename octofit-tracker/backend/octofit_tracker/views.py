from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev'
    return Response({
        'users': base_url + '/api/users/',
        'teams': base_url + '/api/teams/',
        'activities': base_url + '/api/activities/',
        'leaderboard': base_url + '/api/leaderboard/',
        'workouts': base_url + '/api/workouts/'
    })