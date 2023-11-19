import unittest
from unittest.mock import patch
from cloudflare import cloudflare


class TestCloudflareModule(unittest.TestCase):

    @patch('requests.get')
    def test_list_zones(self, mock_get):
        # Configurar la respuesta simulada
        mock_response = mock_get.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"result": [{"id": "zone1", "name": "example.com"}]}

        # Llamar a la función
        response = cloudflare.list_zones()

        # Verificar que la respuesta es la esperada
        self.assertEqual(response, {"result": [{"id": "zone1", "name": "example.com"}]})

    @patch('requests.post')
    def test_create_dns_record(self, mock_post):
        # Configurar la respuesta simulada
        mock_response = mock_post.return_value
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"success": True}

        # Llamar a la función
        response = cloudflare.create_dns_record("zone123", "A", "example.com", "1.2.3.4")

        # Verificar que la respuesta es la esperada
        self.assertTrue(response['success'])

    @patch('requests.delete')
    def test_delete_dns_record(self, mock_delete):
        # Configurar la respuesta simulada
        mock_response = mock_delete.return_value
        mock_response.raise_for_status.return_value = None

        # Llamar a la función y verificar que no se lanza excepción
        cloudflare.delete_dns_record("zone123", "record123")


if __name__ == '__main__':
    unittest.main()
