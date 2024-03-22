import unittest
from adeo_ioc_project.ioc_framework.maincodes.framework import IOCFramework
from ioc_framework.ioc import IP

class TestIOCFrameworkAddIOC(unittest.TestCase):
    def test_add_ioc(self):
        # IOCFramework sınıfını oluşturalım
        framework = IOCFramework()
        # Bir IP örneği oluşturalım
        ip = IP("91.203.193.91")
        # add_ioc metoduyla IP örneğini ekleyelim
        framework.add_ioc(ip)
        # iocs listesinin doğru şekilde güncellendiğini kontrol edelim
        self.assertIn(ip, framework.iocs)  # Eklenen IOC öğesinin iocs listesinde olup olmadığını kontrol edelim

if __name__ == '__main__':
    unittest.main()
