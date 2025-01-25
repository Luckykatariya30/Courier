from rest_framework.response import Response
from rest_framework import status
from .models import Courier
from .serializers import CourierSerializer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

# class CourierDetail(generics.RetrieveAPIView):
#     queryset = Courier.objects.all()
#     serializer_class = CourierSerializer
    
class CourierDetail(APIView):
    def get(self,request,format=None):
        qureyset = Courier.objects.all()
        print(qureyset[0])
        serializer = CourierSerializer(qureyset,many=True)
        return Response({'data':serializer.data},status=status.HTTP_200_OK)

class CourierDetail_pages(APIView):
    def get(self,request,format=None, no=None):
        queryset = Courier.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = no
        paginationdata = paginator.paginate_queryset(queryset,request)
        print(paginationdata)
        serializer = CourierSerializer(paginationdata,many=True)
        # return Response({'data':serializer.data},status=status.HTTP_200_OK)
        return paginator.get_paginated_response(serializer.data)

# class CourierDetail_page(APIView):
#     def get(self,request,format=None, no=None,no_of_page=None):
#         queryset = Courier.objects.all()
#         paginators = PageNumberPagination()
#         paginators.page_size = no
#         paginationdatas = paginators.paginate_queryset(queryset,request)
#         paginator = PageNumberPagination()
#         paginator.page_size = no_of_page
#         paginationdata = paginator.paginate_queryset(paginationdatas,request)
#         print(paginationdata)
#         serializer = CourierSerializer(paginationdata,many=True)
#         # return Response({'data':serializer.data},status=status.HTTP_200_OK)
#         return paginator.get_paginated_response(serializer.data)