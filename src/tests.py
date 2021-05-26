from fastapi.testclient import TestClient

from main import app
from models import NPIMAGE_ERRORS

client = TestClient(app)


def test_read_image_invalid_type():
    response = client.post(
        '/images/',
        json={'image': '[0, 1, 2, 3]'},
    )
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == NPIMAGE_ERRORS['INVALID_TYPE_ON_JSON_PARSE']


def test_read_image_invalid_ndims():
    response = client.post(
        '/images/',
        json={'image': [0, 1, 2, 3]},
    )
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == NPIMAGE_ERRORS['INVALID_NDIMS']


def test_read_image_invalid_nchannels():
    response = client.post(
        '/images/',
        json={'image': [[[0, 1, 2, 3]]]},
    )
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == NPIMAGE_ERRORS['INVALID_NCHANNELS']


def test_read_image():
    response = client.post(
        '/images/',
        json={'image': [[[0, 1, 2]]]},
    )
    assert response.status_code == 200
    assert response.json() == {'image_shape': '(1, 1, 3)'}
