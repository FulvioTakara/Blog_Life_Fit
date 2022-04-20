import requests
from wsgiref import headers


class TestCategorys:
    headers = {'Authorization': 'Token b01d7fe3282f94a32b6debe2a047ded07bcec45d'}
    urls_base_category = 'http://127.0.0.1:8000/api/v2/categorys/'

    def test_get_categorys(self):
        response = requests.get(url=self.urls_base_category, headers=headers)

        assert response.status_code == 200

    def test_get_category(self):
        response = requests.get(
            url=f'{self.urls_base_category}/pk/', headers=headers)

        assert response.status_code == 200

    def test_post_category(self):
        new = {
            "name_cat": "NovaCategoria"
        }

        response = requests.post(
            url=f'{self.urls_base_category}/5/', headers=headers, data=new)

        assert response.status_code == 201

    def test_put_category(self):
        updated = {
            "name_cat": "NovaCategoriaAtualizado"
        }

        response = requests.put(
            url=f'{self.urls_base_category}/5/', headers=headers, data=updated)

        assert response.status_code == 200
        assert response.json()['name_cat'] == updated['name_cat']

    def test_delete_category(self):
        response = requests.delete(
            url=f'{self.urls_base_category}/5/', headers=headers,)

        assert response.status_code == 200 and len(response.text) == 0


class testPublications:
    headers = {'Authorization': 'Token b01d7fe3282f94a32b6debe2a047ded07bcec45d'}
    urls_base_publication = 'http://127.0.0.1:8000/api/v2/publications/'

    def test_get_publications(self):
        response = requests.get(
            url=self.urls_base_publication, headers=headers)

        assert response.status_code == 200

    def test_get_publication(self):
        response = requests.get(
            url=f'{self.urls_base_publication}/pk/', headers=headers)

        assert response.status_code == 200

    def test_post_publication(self):
        new = {
            "title": "Nova Publicação",
            "author": "Fulvio",
            "contents": "Testando publicações novas",
            "excerpt": "Testando metodo POST",
        }

        response = requests.post(
            url=f'{self.urls_base_publication}/5/', headers=headers, data=new)

        assert response.status_code == 201

    def test_put_publication(self):
        updated = {
            "title": "Atualização da Publicação",
            "author": "Fulvio",
            "contents": "Testando atualização da publicação nova",
            "excerpt": "Testando metodo PUT",
        }

        response = requests.put(
            url=f'{self.urls_base_publication}/5/', headers=headers, data=updated)

        assert response.status_code == 200
        assert response.json()['title'] == updated['title']

    def test_delete_publication(self):
        response = requests.delete(
            url=f'{self.urls_base_publication}/5/', headers=headers,)

        assert response.status_code == 200 and len(response.text) == 0


class testComments:
    headers = {'Authorization': 'Token b01d7fe3282f94a32b6debe2a047ded07bcec45d'}
    urls_base_comment = 'http://127.0.0.1:8000/api/v2/comments/'

    def test_get_comments(self):
        response = requests.get(url=self.urls_base_comment, headers=headers)

        assert response.status_code == 200

    def test_get_comment(self):
        response = requests.get(
            url=f'{self.urls_base_comment}/pk/', headers=headers)

        assert response.status_code == 200

    def test_post_comment(self):
        new = {
            "name": "Novo Comentário",
            "email": "fulvio@takara.com",
            "coments": "Testando comentários novos",
            "publication": "Testando metodo POST",
            "author": "fulvio",
        }

        response = requests.post(
            url=f'{self.urls_base_comment}/15/', headers=headers, data=new)

        assert response.status_code == 201

    def test_put_comment(self):
        updated = {
            "name": "Atualização Comentário",
            "email": "fulvio@takara.com",
            "coments": "Testando comentários atualizados",
            "publication": "Testando metodo PUT",
            "author": "fulvio",
        }

        response = requests.put(
            url=f'{self.urls_base_comment}/15/', headers=headers, data=updated)

        assert response.status_code == 200
        assert response.json()['name'] == updated['name']

    def test_delete_comment(self):
        response = requests.delete(
            url=f'{self.urls_base_comment}/15/', headers=headers,)

        assert response.status_code == 200 and len(response.text) == 0
