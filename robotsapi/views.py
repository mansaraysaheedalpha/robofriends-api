
from django.http import JsonResponse
from .models import RobotFriends
from .serializer import RobotFriendsSerialized

# Create your views here.


# def items_list(request):
#     robots = RobotFriends.objects.all()
#     robots_list = []
#     for robot in robots:
#         robots_list.append({
#             "name": robot.name,
#             "username": robot.username,
#             "email": robot.email
#         })
#     return JsonResponse(robots_list, safe=False)

def robots_list_serialized(request):
    robot_friends = RobotFriends.objects.all()
    serializer = RobotFriendsSerialized(robot_friends, many=True)
    return JsonResponse(serializer.data, safe=False)
