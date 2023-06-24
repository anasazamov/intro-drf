from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET'])
def main(request: Request) -> Response:
    params = request.query_params

    if "a" in params.keys() and "b" in params.keys():
        return Response({
            "sum": int(params['a'])+int(params['b'])
        })
        
    return Response({"error":"invalided value or key"})
