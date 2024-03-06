from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Outlet
from .serializers import OutletSerializer

from rest_framework.permissions import IsAdminUser

@api_view(['GET', 'POST'])
def outlet_list(request):
    if request.method == 'GET':
        outlets = Outlet.objects.all()
        serializer = OutletSerializer(outlets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OutletSerializer(data=request.data)
        if serializer.is_valid():
            # Extract flavors from the request data
            flavors = request.data.get('flavors', '').split(',')
            mandatory_flavors = ['chocolate', 'vanilla', 'mint']

            # Combine mandatory flavors with additional flavors
            all_flavors = set(flavors + mandatory_flavors)

            # Create the outlet with the combined flavors
            serializer.save(flavors=','.join(all_flavors))

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def outlet_detail(request, pk):
    try:
        outlet = Outlet.objects.get(pk=pk)
    except Outlet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = OutletSerializer(outlet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OutletSerializer(outlet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        outlet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def admin_outlet_list(request):
    if request.method == 'GET':
        outlets = Outlet.objects.all()
        serializer = OutletSerializer(outlets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OutletSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAdminUser])
def admin_outlet_detail(request, pk):
    try:
        outlet = Outlet.objects.get(pk=pk)
    except Outlet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OutletSerializer(outlet)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        outlet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)