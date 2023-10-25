from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import usercreateserializer, userserializer

class usercreateview(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = usercreateserializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"Message": "User Created Successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class currentuserview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = userserializer(request.user)
        return Response(serializer.data)