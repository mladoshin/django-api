from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User
from .serializers import UserSerializer

@api_view(["GET"])
def getData(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)


@api_view(["POST"])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
        return Response(status=400)

    return Response(serializer.data)


def updateUserInfo(request, id):
    user = User.objects.filter(id=id).first()
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status="400")


@api_view(['GET', 'PUT', 'DELETE'])
def user_views(request, id):
    if request.method == 'GET':
        return getUserInfo(request, id)
    elif request.method == 'PUT':
        return updateUserInfo(request, id)
    elif request.method == 'DELETE':
        return deleteUser(request, id)


def getUserInfo(request, id):
    try:
        user = User.objects.filter(id=id).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except BaseException:
        return Response(status=400)

def deleteUser(request, id):
    try:
        user = User.objects.filter(id=id).first()
        serializer = UserSerializer(user)
        user.delete()
        return Response(serializer.data, status=204)

    except BaseException:
        return Response(status=400)



