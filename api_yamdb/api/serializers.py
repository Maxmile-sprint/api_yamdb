from rest_framework import serializers

from reviews.models import Comment, Review, User, Category, Title, Genre


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Review
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
    )
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email',
                  'first_name', 'last_name',
                  'role', 'bio')


class CategorySerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required=True,)
    # slug = serializers.SlugField()

    class Meta:
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(required=True,)
    # slug = serializers.SlugField()

    class Meta:
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )
    # middle_star = serializers.IntegerField()

    class Meta:
        fields = '__all__'
        model = Title
