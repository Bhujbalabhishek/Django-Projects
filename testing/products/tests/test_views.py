from mixer.backend.django import mixer
from django.urls import reverse
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User, AnonymousUser
from products.views import product_detail
import pytest

# @pytest.mark.django_db
# class TestView():
    # @classmethod
    # def setUpClass(cls):
    #     super(TestView, cls).setUpClass()
    #     mixer.blend('products.Product')
    #     cls.factory = RequestFactory()

@pytest.fixture(scope='module')
def factory():
    print("factory instantiated")
    return RequestFactory()

@pytest.fixture
def product(db):
    return mixer.blend('products.Product')

def test_product_detail_authenticated(factory, product):
    
    path = reverse('detail', kwargs = {'pk':1})
    request = factory.get(path)
    request.user = mixer.blend(User)

    response = product_detail(request, pk =1)
    assert response.status_code == 200
    


def test_product_detail_unauthenticated(factory, product):
    mixer.blend('products.Product')
    path = reverse('detail', kwargs = {'pk':1})
    request = factory.get(path)
    request.user = AnonymousUser()

    response = product_detail(request, pk =1)
    assert 'accounts/login' in response.url
    