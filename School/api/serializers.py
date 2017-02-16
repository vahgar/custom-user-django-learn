from rest_framework import serializers

from School.models import School

class SchoolCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = [
        'school_id',
        'school_name',
        'school_branch_area',
        'affiliation_number',
        'board',
        'address',
        'zone',
        'city',
        'state',
        'pincode',
        'transport_incharge',
        'transport_incharge_number',
        ]
