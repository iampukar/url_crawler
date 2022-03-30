import unittest
from src.url_crawler.url_crawler import url_crawler

class Test(unittest.TestCase):
    def test_cases(self):
        """
        Test Case1: https://neptunemutual.com
        """
        package_details = url_crawler('https://neptunemutual.com')

        self.assertEqual(package_details.url, 'https://neptunemutual.com')
        self.assertEqual(package_details.domain, 'neptunemutual.com')
        self.assertEqual(package_details.check_http, False)
        self.assertEqual(package_details.check_https, True)
        self.assertEqual(package_details.url_response, True)
        self.assertEqual(package_details.dot_count, 1)
        self.assertEqual(package_details.digit_count, 0)
        self.assertEqual(package_details.url_length, 25)
        self.assertEqual(package_details.fragments_count, 0)
        self.assertEqual(package_details.check_encoding, False)
        self.assertEqual(package_details.check_client, False)
        self.assertEqual(package_details.check_admin, False)
        self.assertEqual(package_details.check_server, False)
        self.assertEqual(package_details.check_login, False)
        self.assertEqual(package_details.check_ports, False)
        
if __name__ == '__main__':
    unittest.main()
