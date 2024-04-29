from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from home.models import *



class AboutView(APIView):
    def get(self, req: Request):
        return Response({'data': About.objects.all().values()})
    
    def post(self, req: Request):
        title = req.data.get('title')
        desc = req.data.get('desc')
        video = req.data.get('video')

        if not video.name.withend('webm') and not video.name.withend('mp4'):
            return Response({'Error': 'Video'})
        
        about = About.objects.create(title=title, desc=desc, video=video)

        return Response({'data': about})
    


class ContactView(APIView):
    def get(self, req: Request):
        return Response({'data': Contact.objects.all().values()})
    
    def post(self, req: Request):
        name = req.data.get('name')
        email = req.data.get('email')
        msg = req.data.get('msg')


        
        contact = Contact.objects.create(name=name, email=email, msg=msg)

        return Response({'data': contact})
        

class TeamView(APIView):
    def get(self, req: Request):
        return Response({'data': Team.objects.all().values()})
    
    def post(self, req: Request):
        name = req.data.get('name')
        profesion = req.data.get('profesion')
        desc = req.data.get('desc')
        img = req.data.get('img')


        team = Team.objects.create(name=name, profesion=profesion, desc=desc, img=img)

        return Response({'data': team})




class WebView(APIView):
    def get(self, req: Request):
        return Response({'data': Website.objects.all().values()})
    
    def post(self, req: Request):
        name = req.data.get('name')
        link = req.data.get('link')
        desc = req.data.get('desc')


        web = Team.objects.create(name=name, link=link, desc=desc)

        return Response({'data': web})
    

class WebImgView(APIView):
    def get(self, req: Request, pk):
        return Response({'data': WebImg.objects.all().filter(pk=pk).values()})
    
    def post(self, req: Request, pk):
        web_id = pk
        img = req.data.get('img')


        web = WebImg.objects.create(web_id=web_id, img=img)

        return Response({'data': web})