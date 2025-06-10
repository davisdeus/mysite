import factory
from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from blog.models import Post

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(lambda x: faker.name())


    @classmethod
    def _prepare(cls, model_class, *args, **kwargs):
        password = kwargs.pop("password", None)
        user = super()._create(model_class, *args, **kwargs)
        if password:
            user.set_password(password)
            user.save()
            return user
        
class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
        
    title = factory.LazyAttribute(lambda x: faker.sentence())
    slug = factory.LazyAttribute(lambda x: faker.slug())
    created_on = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UserFactory)
    status = 0


    class Meta:
        model = Post