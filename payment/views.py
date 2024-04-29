from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from payment.models import *
from auth_user.models import User
from rest_framework.permissions import IsAuthenticated


class Pay(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, req: Request):
        return Response({'msg': 'Payment'})
    
    def post(self, req: Request):
        user = req.user
        client = Client.objects.all().filter(user_id=User).first()
        if not bool(client):
            client = Client.objects.create(user_id=user)
        money = int(req.data.get('money'))
        video = Video.objects.all().filter(pk=int(req.data.get('video'))).first()
        

        if video.price == money:
            video.buyers.add(client)
            video.save()
        
        else:
            return Response({'Error': True})

       
