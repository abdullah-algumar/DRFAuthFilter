from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest.filters import KurulusFilter
from rest.models import Kurulus, Subscribe
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest.serializers.KurulusSerializer import KurulusSerializer
from rest.serializers.SubscribeSerializer import SubscribeSerializer
from rest.serializers.UserSerializer import LoginSerializer, RegistrSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


User = get_user_model()

class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegistrSerializer
    queryset = User.objects.all()

class LoginView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user:
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)


class KurulusViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = KurulusSerializer
    queryset = Kurulus.objects.all()


class KurulusListView(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = KurulusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = KurulusFilter

    def get_queryset(self):
        return Kurulus.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class SubscribeViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['GET'])
    def subscribed_kuruluslar_list(self, request, pk=None):
        subscribes = Subscribe.objects.filter(user=request.user, subscribe_kurulus=pk)
        serializer = SubscribeSerializer(subscribes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def subscribe(self, request, pk=None):
        try:
            kurulus = Kurulus.objects.get(pk=pk)
            subscribe, created = Subscribe.objects.get_or_create(user=request.user, subscribe_kurulus=kurulus)
            if created:
                return Response({'message': 'Kuruluş takip ediliyor.'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Kuruluş zaten takip ediliyor.'}, status=status.HTTP_200_OK)
        except Kurulus.DoesNotExist:
            return Response({'message': 'Kuruluş bulunamadı.'}, status=status.HTTP_404_NOT_FOUND)
