import requests
import pytest
from settings import LOGIN, PASSWORD, COMPANY_ID, base_url

#Тест для метода [POST]/api-v2/projects:


def test_create_project():
    url = base_url
    headers = {
            'Autorization' : 'Bearer Ddi2RkZ1HBGfEcpaF4Das6+pNnhLRymo25WZY6EQ11LMiPtk4t2iJvaCg1W+Z4DO',
            'Content-Type': 'application/json'
        }
    data = {
        "title": "Тестирование ресурса YuoGile"
        }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201
    assert id in response.json()

#Тест для метода [GET]/api-v2/projects:


def test_get_projects():
    url = base_url
    headers = {
            'Autorization' : 'Bearer Ddi2RkZ1HBGfEcpaF4Das6+pNnhLRymo25WZY6EQ11LMiPtk4t2iJvaCg1W+Z4DO',
            'Content-Type': 'application/json'
        }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert 'projects' in response.json()

#Тест для метода [PUT]/api-v2/projects/{id}:


def test_update_project():
    project_id = 'f5c59ecd-71f9-4b93-a5c8-597bd9460de0'
    headers = {
            'Autorization' : 'Bearer Ddi2RkZ1HBGfEcpaF4Das6+pNnhLRymo25WZY6EQ11LMiPtk4t2iJvaCg1W+Z4DO',
            'Content-Type': 'application/json'
        }
    # Заменить на существующий ID проекта
    url = f"https://ru.yougile.com/api-v2/projects/{project_id}"
    data = {
        "title": "Тестирование_YuoGile_1"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200


#Тест для метода [GET]/api-v2/projects/{id}:

def test_get_project_by_id():
    project_id = 'f5c59ecd-71f9-4b93-a5c8-597bd9460de0'
    headers = {
            'Autorization' : 'Bearer Ddi2RkZ1HBGfEcpaF4Das6+pNnhLRymo25WZY6EQ11LMiPtk4t2iJvaCg1W+Z4DO',
            'Content-Type': 'application/json'
        }
    # Заменить на существующий ID проекта
    url = f"https://ru.yougile.com/api-v2/projects/{project_id}"
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert 'name' in response.json()
