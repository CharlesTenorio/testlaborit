from leads.models import Lead
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.response import Response

from .serializer import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('email',)

    def create(self, request, *args, **kwargs):
        email_lead = request.data['email']
        email_lead_exist = Lead.objects.filter(email=email_lead).first()

        if email_lead_exist:
            return Response(dict(mensagem='email já cadastrado'), status=status.HTTP_409_CONFLICT)

        return super(LeadViewSet, self).create(request, *args, kwargs)
