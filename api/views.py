from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer

class WheelSpecificationAPIView(APIView):
 #API view for creating and listing wheel specifications.
    def post(self, request, *args, **kwargs):
        data=request.data
        serializer = WheelSpecificationSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": {
                    "formNumber": serializer.data.get("formNumber"),
                    "submittedBy": serializer.data.get("submittedBy"),
                    "submittedDate": serializer.data.get("submittedDate"),
                    "status": "Saved"
                }
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "message": "Invalid data provided.",
            "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        queryset = WheelSpecification.objects.all()
        # Apply filters from query parameters
        form_number = request.query_params.get('formNumber')
        submitted_by = request.query_params.get('submittedBy')
        submitted_date = request.query_params.get('submittedDate')
    
        if form_number:
            queryset = queryset.filter(formNumber=form_number)
        if submitted_by:
            queryset = queryset.filter(submittedBy=submitted_by)
        if submitted_date:
            queryset = queryset.filter(submittedDate=submitted_date)
    
        serializer = WheelSpecificationSerializer(queryset, many=True)
        response_data = {
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)