import pytest
from app import db, app

@pytest.fixture
def client():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_login(client):    
    data = '{"usuario":"admin", "senha":"admin"}'
    response = client.post(
        ('/api/login'),
        data=data, content_type='application/json', charset='UTF-8'
    )

    assert response.status_code == 200

def test_post_not_admin(client):
    data = '{"titulo":"teste1", "corpo":"teste1_corpo"}'
    response = client.post(
        ('/api/informes'),
        data=data, content_type='application/json', charset='UTF-8'
    )
    assert response.status_code == 401

def test_post_admin(client):
    #loga admin
    data = '{"usuario":"admin", "senha":"admin"}'
    response = client.post(
        ('/api/login'),
        data=data, content_type='application/json', charset='UTF-8'
    )
    #posta
    data = '{"titulo":"teste1", "corpo":"teste1_corpo"}'
    response = client.post(
        ('/api/informes'),
        data=data, content_type='application/json', charset='UTF-8'
    )
    assert response.status_code == 200
    #confirma se o post está mesmo lá
    response = client.get(
        ('/api/informes?limite=1')
    )
    assert response.status_code == 200
    assert len(response.json['conteudo']) == 1
    assert response.json['conteudo'][0]['titulo'] == 'teste1'
