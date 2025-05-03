from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title']
    filterset_fields = ['date']
    ordering_fields = ['date']

def get_queryset(self):
        queryset = super().get_queryset()

        # Handle /tasks/?sort_by_date=true
        sort_by_date = self.request.query_params.get('sort_by_date')
        if sort_by_date == 'true':
            queryset = queryset.order_by('date')

        return queryset