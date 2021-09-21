from rest_framework.serializers import Serializer
from tagapp.helper import write_file
from tagapp.models import TagModel
from tagapp.serializers import TagSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets 


class TagView(viewsets.ModelViewSet):
    queryset = TagModel.objects.all()
    authentication_classes=[JWTAuthentication]
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer
    
    def create(self, request):
        serializer = TagSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            tag = serializer.data.get('tag')
            content = write_file(tag,request)
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        obj=TagModel.objects.filter(id=pk).first()
        serializer = TagSerializer(obj,data=request.data, partial=True, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            tag = serializer.data.get('tag')
            data = serializer.data
            data['content']= write_file(tag,request)
            return Response(data,status=201)
        return Response(serializer.errors, status=400)   

    def retrieve(self, request,pk):
        obj=TagModel.objects.filter(id=pk).first()
        if obj:
            data=TagSerializer(obj,context={'request':request}).data
            try:
                f=open(f'data/{obj.tag}.txt','r')
                line=f.readline()
                f.close()
            except:
                line=''
            data['content']=line    
            return Response(data,status=200)
        Response({"status":"invalid id"}, status=400)     

    def destroy(self, request,pk):
        obj=TagModel.objects.filter(id=pk).first()
        if obj:
            data=TagSerializer(obj,context={'request':request}).data
            try:
                f=open(f'data/{obj.tag}.txt','r')
                f.detach()
            except:
                pass
            obj.delete()
            return Response(data,status=204)
        Response({"status":"invalid id"}, status=400)     


            
