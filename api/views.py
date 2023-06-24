from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET'])
def main(request: Request) -> Response:
    params = request.query_params

    print(params['name'])

    return Response({
        "name": params['name']
    })
