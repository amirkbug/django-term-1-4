from rest_framework.response import Response
from rest_framework.decorators import api_view , permission_classes
from services.models import Services , Comments
from .serializer import ServiceSerializer , CommentSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser , IsAuthenticated , IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly
from rest_framework.views import APIView 
from rest_framework.generics import (
    GenericAPIView ,
    ListAPIView , 
    RetrieveAPIView , 
    UpdateAPIView , 
    DestroyAPIView ,
    CreateAPIView
)
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin
)
from rest_framework.viewsets import ViewSet , ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter , SearchFilter



class ServiceView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ServiceSerializer
    queryset = Services.objects.all()
    filter_backends = [DjangoFilterBackend , OrderingFilter , SearchFilter]
    ordering_fields = ["id" , "created_at"]
    search_fields = ["title" , "category__title"]







# class ServiceView(ViewSet):
#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer
#     queryset = Services.objects.all()



#     def list(self, request, *args, **kwargs):
#         service = Services.objects.all()
#         serialize = self.serializer_class(service, many=True)
#         return Response(serialize.data, status=status.HTTP_200_OK)
    


#     def create(self , request , *args , **kwargs):
#          serilize = self.serializer_class(data=request.data)
#          serilize.is_valid(raise_exception=True)
#          serilize.save()
#          return Response(serilize.data,status=status.HTTP_201_CREATED)
         


#     def retrieve(self , request , *args , **kwargs):
#          pk = kwargs["pk"]
#          services = get_object_or_404(Services , id=pk )
#          serialize = self.serializer_class(services)
#          return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
    


#     def update(self , request , *args , **kwargs):
#          pk = kwargs["pk"]
#          services = get_object_or_404(Services , id=pk )
#          serialize = self.serializer_class(services , data=request.data)
#          serialize.is_valid(raise_exception=True)
#          serialize.save()
#          return Response (serialize.data, status=status.HTTP_201_CREATED)

    

#     def destroy(self , request , *args , **kwargs):
#          pk = kwargs["pk"]
#          services = get_object_or_404(Services , id=pk )
#          services.delete()
#          return Response ({"object":"deleted"},status=status.HTTP_204_NO_CONTENT)
         



# class ListServicesView(ListAPIView , CreateAPIView):
#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer
#     queryset = Services.objects.all()




# class DetailServicesView(RetrieveAPIView , UpdateAPIView , DestroyAPIView):
#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer
#     lookup_field = "pk"
#     queryset = Services.objects.filter(status=True)





# class ListServicesView(GenericAPIView , ListModelMixin , CreateModelMixin):
#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer


#     def get_queryset(self):
#          return Services.objects.all()



#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)


#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)








# class DetailServicesView(GenericAPIView , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin):
#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer
#     lookup_field = "pk"
#     queryset = Services.objects.filter(status=True)

    
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)


#     def patch(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
    


#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)











# class ListServicesView(GenericAPIView):
#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer


#     def get_queryset(self):
#          return Services.objects.all()



#     def get(self ,request):
#         services = self.get_queryset()
#         serilize = self.serializer_class(services, many=True)
#         return Response (serilize.data, status=status.HTTP_200_OK)


#     def post(self ,request):
#         serilize = self.serializer_class(data=request.data)
#         serilize.is_valid(raise_exception=True)
#         serilize.save()
#         return Response(serilize.data,status=status.HTTP_201_CREATED)









# class DetailServicesView(GenericAPIView):
#     permission_classes = [IsAdminOrReadOnly]
#     serializer_class = ServiceSerializer


#     def get_queryset(self , **kwargs):
#         pk = self.request.parser_context["kwargs"]["pk"]
#         return get_object_or_404(Services , id=pk)
#         # return get_object_or_404(Services , id=self.kwargs.get("pk"))

    



#     def get(self ,request , **kwargs):
#         services = self.get_queryset()
#         serilize = self.serializer_class(services)
#         return Response (serilize.data, status=status.HTTP_200_OK)


#     def put(self ,request , **kwargs):
#         services = self.get_queryset()
#         serialize = self.serializer_class(services)
#         serialize.is_valid(raise_exception=True)
#         serialize.save()
#         return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
    


#     def patch(self ,request , **kwargs):
#         services = self.get_queryset()
#         serialize = self.serializer_class(services)
#         serialize.is_valid(raise_exception=True)
#         serialize.save()
#         return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
    


#     def delete(self ,request , **kwargs):
#         services = self.get_queryset()
#         services.delete()
#         return Response ({"object":"deleted"},status=status.HTTP_204_NO_CONTENT)














# class ListServicesView(APIView):
#     permission_classes = [IsAdminOrReadOnly]



#     def get(self ,request):
#         services = Services.objects.all()
#         serilize = ServiceSerializer(services, many=True)
#         return Response (serilize.data, status=status.HTTP_200_OK)


#     def post(self ,request):
#         serilize = ServiceSerializer(data=request.data)
#         serilize.is_valid(raise_exception=True)
#         serilize.save()
#         return Response(serilize.data,status=status.HTTP_201_CREATED)
        


# class DetailServicesView(APIView):
#     permission_classes = [IsAdminOrReadOnly]



#     def get(self ,request , **kwargs):
#         services = get_object_or_404(Services , id=kwargs.get("pk"))
#         serilize = ServiceSerializer(services)
#         return Response (serilize.data, status=status.HTTP_200_OK)


#     def put(self ,request , **kwargs):
#         services = get_object_or_404(Services , id=kwargs.get("pk"))
#         serialize = ServiceSerializer(services , data = request.data)
#         serialize.is_valid(raise_exception=True)
#         serialize.save()
#         return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
    


#     def patch(self ,request , **kwargs):
#         services = get_object_or_404(Services , id=kwargs.get("pk"))
#         serialize = ServiceSerializer(services , data = request.data)
#         serialize.is_valid(raise_exception=True)
#         serialize.save()
#         return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
    


#     def delete(self ,request , **kwargs):
#         services = get_object_or_404(Services , id=kwargs.get("pk"))
#         services.delete()
#         return Response ({"object":"deleted"},status=status.HTTP_204_NO_CONTENT)
    


    



@api_view(["GET", "POST"])
@permission_classes([IsAdminOrReadOnly])
def all_services(request):
    if request.method == "GET":
        services = Services.objects.all()
        serilize = ServiceSerializer(services, many=True)
        return Response (serilize.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        
            serilize = ServiceSerializer(data=request.data)
            if serilize.is_valid():
                serilize.save()
                return Response(serilize.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serilize.errors , status=status.HTTP_400_BAD_REQUEST)
        
        
    
         
        
    

@api_view(["GET","PATCH","DELETE"])
def single_services (request, id):
        services = get_object_or_404(Services , id=id)
        if request.method == "GET":
            serialize = ServiceSerializer(services)
            return Response (serialize.data, status=status.HTTP_200_OK)
        elif request.method == "PATCH":
             serialize = ServiceSerializer(services , data = request.data)
            #  if serialize.is_valid():
             serialize.is_valid(raise_exception=True)
             serialize.save()
             return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
        
        elif request.method == "DELETE":
            services.delete()
            return Response ({"object":"deleted"},status=status.HTTP_204_NO_CONTENT)
             



@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def all_comments(request):
    if request.method == "GET":
        comments = Comments.objects.all()
        serilize = CommentSerializer(comments, many=True)
        return Response (serilize.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serilize = CommentSerializer(data=request.data)
        if serilize.is_valid():
            serilize.save()
            return Response(serilize.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serilize.errors , status=status.HTTP_400_BAD_REQUEST)
        
    
         
        
    

@api_view(["GET","PATCH","DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def single_comment (request, id):
        comments = get_object_or_404(Comments , id=id)
        if request.method == "GET":
            serialize = CommentSerializer(comments)
            return Response (serialize.data, status=status.HTTP_200_OK)
        elif request.method == "PATCH":
             if request.user.id == comments.name.id:
                serialize = CommentSerializer(comments , data = request.data)
                #  if serialize.is_valid():
                serialize.is_valid(raise_exception=True)
                serialize.save()
                return Response (serialize.data, status=status.HTTP_202_ACCEPTED)
             else :
                 return Response ({"message":"ridi comment male to nist"},status=status.HTTP_403_FORBIDDEN)
        
        elif request.method == "DELETE":
            if request.user.id == comments.name.id:
                comments.delete()
                return Response ({"object":"deleted"},status=status.HTTP_204_NO_CONTENT)
            else :
                return Response ({"message":"ridi comment male to nist"},status=status.HTTP_403_FORBIDDEN)