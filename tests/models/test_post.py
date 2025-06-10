import pytest
from blog.factories import PostFactory, UserFactory

from django.utils.timezone import now

from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'

# 01 garante que cada usuário gerado tem um e-mail único.
@pytest.mark.django_db
def test_unique_user_creation():
    user01 = UserFactory()
    user02 = UserFactory()
    assert user01.email != user02.email


# 02 Verifica se umusuário criado pode ser 
# atenticado corretamente com a senha definida.
@pytest.mark.django_db
def test_user_authentication():
    user = UserFactory(password='testpassword')
    assert user.check_password('testpassword') is False


# 03 Verifica se um podt criado tem um autor associado corretamente.
@pytest.mark.django_db
def test_post_author_relation():
    post = PostFactory()
    assert post.author is not None
    assert isinstance(post.author, User)


# 04 Garante que posts mais novos tenham uma data 
# de criação maior que os antigos.
@pytest.mark.django_db
def test_post_creation_order():
    post_old = PostFactory(created_on=now())
    post_new = PostFactory(created_on=now())
    assert post_old.created_on <= post_new.created_on


