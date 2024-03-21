import unittest
from unittest.mock import MagicMock
from ioc_framework.framework import IOCFramework
from ioc_framework.ioc import IP

class TestIOCFrameworkPrintResultsAll(unittest.TestCase):
    def test_print_results_all(self):
        # IOCFramework sınıfını oluşturalım
        framework = IOCFramework()
        
        # İki adet IOC örneği oluşturalım
        ip1 = IP("91.203.193.91")
        ip2 = IP("192.168.1.1")
        
        # IOC örneklerinin print_results metodunu mocklayalım
        ip1.print_results = MagicMock()
        ip2.print_results = MagicMock()
        
        # IOC örneklerini IOCFramework'e ekleyelim
        framework.add_ioc(ip1)
        framework.add_ioc(ip2)
        
        # print_results_all metodunu çağıralım
        framework.print_results_all()
        
        # IOC örneklerinin print_results metodunun çağrıldığını kontrol edelim
        ip1.print_results.assert_called_once()
        ip2.print_results.assert_called_once()

if __name__ == '__main__':
    unittest.main()
