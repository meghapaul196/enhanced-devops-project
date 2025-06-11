import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import app


def test_home_route():
    test_app = app.app.test_client()
    response = test_app.get('/')
    assert response.status_code == 200

def test_predict_valid():
    test_app = app.app.test_client()
    response = test_app.post('/predict', data={'value': '5'})
    assert response.status_code == 200
    assert 'Predicted value' in response.data.decode()

def test_predict_invalid():
    test_app = app.app.test_client()
    response = test_app.post('/predict', data={'value': 'abc'})
    assert response.status_code == 400