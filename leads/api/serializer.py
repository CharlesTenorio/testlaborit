from rest_framework.serializers import ModelSerializer
from leads.models import Lead


class LeadSerializer(ModelSerializer):
    class Meta:
        model = Lead
        fields = ['id', 'name', 'email']
        read_only_fields = ['id', ]
