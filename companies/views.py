from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_204_NO_CONTENT
from .serializers import CompanyModelSerializer
from .models import Company
import logging
# Create your views here.

logger = logging.getLogger("logger")

class CompanyListCreateAPIView(ListCreateAPIView):
    model = Company
    serializer_class = CompanyModelSerializer
    queryset = Company.objects.all()


class CompanyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    model = Company
    serializer_class = CompanyModelSerializer
    queryset = Company.objects.all()
    lookup_field = "auto_id"
    http_method_names = [u'get', u'patch', u'delete', u'head', u'options'] 


    def delete(self, request, *args, **kwargs):
        """
        We just add logger to Delete method, to register
        in a log if an error occurs.
        """
        try:
            company = self.get_object()
            company.delete()
            return Response(status=HTTP_204_NO_CONTENT, data={"error:OK"})

        except Exception as e:
            logger.error("companies.views.delete-{}".format(str(e)))
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR, data={"error":"KO"})