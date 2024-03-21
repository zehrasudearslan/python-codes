import unittest
from ioc_framework.framework import IOCFramework

class TestIOCFrameworkInit(unittest.TestCase):
    def test_iocs_initialized_empty(self):
        # IOCFramework sınıfını oluşturalım
        framework = IOCFramework()
        # iocs özelliğinin varlığını ve boş bir liste olduğunu kontrol edelim
        self.assertTrue(hasattr(framework, 'iocs'))  # iocs özelliğinin varlığını kontrol et
        self.assertIsInstance(framework.iocs, list)  # iocs özelliğinin bir liste olup olmadığını kontrol et
        self.assertEqual(len(framework.iocs), 0)  # iocs listesinin boş olduğunu kontrol et

if __name__ == '__main__':
    unittest.main()
