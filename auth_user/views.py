from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from auth_user.models import User




class Singup(APIView):
    def get(self, req: Request):
        return Response({'msg': 'Singup'})
    

    def post(self, req: Request):
        first_name = req.data.get('first_name')
        last_name = req.data.get('last_name')
        email = req.data.get('email')
        phone = req.data.get('phone')
        region = req.data.get('region')
        password = req.data.get('password')
        img = req.FILES.get('img')

        if User.objects.all().filter(email=email).exists():
            return Response({'msg': 'This user already exist'})


        user = User.objects.create_user(username=f'{first_name} {last_name}',first_name=first_name, last_name=last_name, email=email, phone=phone, region=region, password=password, img=img)
        token = RefreshToken.for_user(user=user)

        return Response({
            'access_token': str(token.access_token),
            'refresh_token': str(token),
        })



class Singin(APIView):
    def get(self, req: Request):
        return Response({'msg': 'Singin'})
    

    def post(self, req: Request):
        email = req.data.get('email')


        if not User.objects.all().filter(email=email).exists():
            return Response({'msg': 'This user doesn`t exist'})


        user = User.objects.all().filter(email=email).first()
        token = RefreshToken.for_user(user=user)

        return Response({
            'access_token': str(token.access_token),
            'refresh_token': str(token),
        })



# {
#     "aaccess_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0MTQ5ODg0LCJpYXQiOjE3MTQxNDYyODQsImp0aSI6IjllZTk1ZThjNmMxNTRmODI4MmYxYmJmYjUzZDcyZWM0IiwidXNlcl9pZCI6M30.F5MjStKthergsJwxgmVsNGwP8oVoNM5DH374OcIW4UQ",
#     "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNDIzMjY4NCwiaWF0IjoxNzE0MTQ2Mjg0LCJqdGkiOiI3Y2UwYTQyYThmNzA0OWE5OWYwMjU3ZjE5ODQyYzU2NCIsInVzZXJfaWQiOjN9.xM2oKjXRpniuEbNddf7VMuqCCgiT51qjCkAKdaT6ZuI"
# } mu