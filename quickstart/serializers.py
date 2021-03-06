from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import PoreSpyFuncsNames, Blobs, BundleOfTubes, LatticeSpheres, LocalThickness, PoreSizeDistribution


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PoreSpyFuncsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PoreSpyFuncsNames
        fields = ['porespy_funcs']


class GeneratorBlobsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blobs
        fields = ['porosity', 'blobiness', 'dimension_x', 'dimension_y', 'dimension_z', 'generated_image']


class GeneratorBundleOfTubesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BundleOfTubes
        fields = ['dimension_x', 'dimension_y', 'dimension_z', 'spacing', 'generated_image']


class GeneratorLatticeSpheresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LatticeSpheres
        fields = ['dimension_x', 'dimension_y', 'dimension_z', 'radius', 'offset', 'lattice', 'generated_image']
        # TODO: when newest version of porespy is released, use the commented line instead.
        # fields = ['dimension_x', 'dimension_y', 'dimension_z', 'radius', 'spacing', 'offset', 'smooth', 'lattice', 'generated_image']


class FilterBundleOfTubesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalThickness
        fields = ['local_thickness_image', 'sizes', 'mode', 'local_thickness_image_filtered']


class MetricPoreSizeDistributionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PoreSizeDistribution
        fields = ['psd_im', 'bins', 'log', 'voxel_size', 'x_axis_label', 'y_axis_label', 'psd_im_metric']
