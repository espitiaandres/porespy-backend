from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer, GeneratorBlobsSerializer, GeneratorLatticeSpheresSerializer, PoreSpyFuncsSerializer, GeneratorBundleOfTubesSerializer, FilterBundleOfTubesSerializer, MetricPoreSizeDistributionSerializer
from .models import PoreSpyFuncsNames, Blobs, BundleOfTubes, LatticeSpheres, LocalThickness, PoreSizeDistribution


# TODO: Maybe separate out all the Generators/Filters/Metrics viewsets into separate files
#  so that this file is not too long?


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PoreSpyFuncsViewSet(viewsets.ModelViewSet):
    queryset = PoreSpyFuncsNames.objects.all()
    serializer_class = PoreSpyFuncsSerializer


class GeneratorsBlobsViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows user to interact with the blobs function inside the Generators module.
    """
    queryset = Blobs.objects.all()
    serializer_class = GeneratorBlobsSerializer


class GeneratorsBundleOfTubesViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows user to interact with the bundle_of_tubes function inside the Generators module
    """
    queryset = BundleOfTubes.objects.all()
    serializer_class = GeneratorBundleOfTubesSerializer


class GeneratorsLatticeSpheresViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows user to interact with the lattice_spheres function inside the Generators module
    """
    queryset = LatticeSpheres.objects.all()
    serializer_class = GeneratorLatticeSpheresSerializer


class FiltersLocalThicknessViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows user to interact with the local_thickness function inside the Filters module
    """
    queryset = LocalThickness.objects.all()
    serializer_class = FilterBundleOfTubesSerializer


class MetricsPoreSizeDistributionViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows user to interact with the pore_size_distribution function inside the Metrics Module
    """
    queryset = PoreSizeDistribution.objects.all()
    serializer_class = MetricPoreSizeDistributionSerializer
