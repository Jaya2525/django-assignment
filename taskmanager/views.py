from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    filter_backends = [
        filters.SearchFilter,
    ]

    search_fields = ['title']  # ?search=keyword

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request

        # Custom filter: search_date
        search_date = request.query_params.get('search_date')
        if search_date:
            queryset = queryset.filter(date=search_date)

        # Custom sort: sort_by_date=true or desc
        sort_by_date = request.query_params.get('sort_by_date')
        if sort_by_date == 'true':
            queryset = queryset.order_by('date')
        elif sort_by_date == 'desc':
            queryset = queryset.order_by('-date')

        return queryset