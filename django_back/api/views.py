'''from django.shortcuts import render
from rest_framework.decorators import api_view,parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status  
import numpy as np
import joblib
import os
from .serializers import django_backSerializer

@api_view(['POST', 'GET'])  # Allow both POST and GET requests
def predict(request):
    # Define the path to the machine learning model
    current_directory = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_directory, '..', 'Model', 'Electricitybill (2).pkl')

    try:
        # Load the machine learning model
        with open(model_path, 'rb') as f:
            model = joblib.load(f)
    except FileNotFoundError:
        return Response({"error": "Model file not found."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    if request.method == 'POST':
        # Serialize the input data from the request
        serializer = django_backSerializer(data=request.data)
        if serializer.is_valid():
            # Convert the input data input format for the model
            input_data = tuple(serializer.validated_data.values())
            input_data_as_numpy_array = np.asarray(input_data)
            input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

            # Make a model prediction using the loaded model
            prediction = model.predict(input_data_reshaped)

            # Return the prediction in a JSON response
            return Response(prediction, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        # Return some default response or explanation
        return Response({"message": "Send a POST request with data to make predictions"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
'''
# Assuming this code is inside your Django view function
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import joblib
import numpy as np
from .models import Prediction
from .serializers import PredictionSerializer

@api_view(['POST'])
def predict(request):
    # Load your machine learning model
    model = joblib.load('C:\Frontend_and_Backend\Backend_Mlops\Django\django_back\Model\Electricitybill (2).pkl')

    # Extract input features from request data
    feature1 = request.data.get('Fan', 0)
    feature2 = request.data.get('Refrigerator', 1)
    feature3 = request.data.get('Television', 3)
    feature4 = request.data.get('MonthlyHours', 9)
    input_data = np.array([[feature1, feature2, feature3, feature4]])

    # Make prediction
    prediction = model.predict(input_data)

    # Save prediction to database
    prediction_obj = Prediction(result=prediction[0])
    prediction_obj.save()

    # Serialize prediction and return response
    serializer = PredictionSerializer(prediction_obj)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

