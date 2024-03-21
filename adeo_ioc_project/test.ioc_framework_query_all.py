import unittest
from unittest.mock import MagicMock
from ioc_framework.framework import IOCFramework
from ioc_framework.ioc import IP

class TestIOCFrameworkQueryAll(unittest.TestCase):
    def test_query_all(self):
        # IOCFramework sınıfını oluşturalım
        framework = IOCFramework()
        
        # İki adet IOC örneği oluşturalım
        ip1 = IP("91.203.193.91")
        ip2 = IP("192.168.1.1")
        
        # IOC örneklerinin query metodunu mocklayalım
        ip1.query = MagicMock()
        ip2.query = MagicMock()
        
        # IOC örneklerini IOCFramework'e ekleyelim
        framework.add_ioc(ip1)
        framework.add_ioc(ip2)
        
        # query_all metodunu çağıralım
        framework.query
