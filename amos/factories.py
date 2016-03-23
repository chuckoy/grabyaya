import factory
import string
import random

from django.contrib.auth.models import User

CHARS = string.ascii_uppercase + string.ascii_lowercase + string.digits


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
        django_get_or_create = ('username',)

    username = factory.Sequence(lambda n: 'user%d' % n)
    email = factory.LazyAttribute(lambda obj: '%s@test.com' % obj.username)
    password = (factory
                .PostGenerationMethodCall('set_password',
                                          ''.join(random.choice(CHARS)
                                                  for _ in range(8))))

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.raw_password = password
            user.set_password(password)
            if create:
                user.save()
        return user
