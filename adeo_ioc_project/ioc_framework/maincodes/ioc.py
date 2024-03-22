import requests
import os

headers = {
    "accept": "application/json",
    "x-apikey": os.getenv("API_KEY"),
}


# Base class
class IOC:
    def __init__(self, value):
        self.value = value
        self.results = []
        self.endpoint = ""

    # Eğer query çalışmıuyorsa istisna olarak bu hata fırlatılır.
    def query(self):
        raise NotImplementedError(
            "Implement Error !, Query method must be implemented in classes."
        )

    def print_results(self):
        if self.results:
            print(f"Results for {self.__class__.__name__} - {self.value}:")
            for result in self.results:
                print(result)
        else:
            print(f"No results for {self.__class__.__name__} - {self.value}.")


# İp ioc analiz işlemi
class IP(IOC):
    def query(self):
        url = self.endpoint + self.value
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.text
            self.results.append(data)
        else:
            self.results.append(f"Error occurred while querying {self.endpoint}.")

# Domain ioc analiz işlemi
class Domain(IOC):
    def query(self):
        url = self.endpoint + self.value
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.text
            self.results.append(data)
        else:
            self.results.append(f"Error occurred while querying {self.endpoint}.")




class SHA256(IOC):
    def query(self):
        url = self.endpoint + self.value
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data:
                self.results = data


sha256 = SHA256("ed01ebfbc9eb5bbea545af4d01bf5f1071661840480439c6e5babe8e080e41aa")


 
# Bu kod bir SHA256 değerini kullanarak belirli bir endpoint'e bir HTTP GET isteği yapmayı sağlar. Genel olarak, bu kodun amacı aşağıdaki işlevleri yerine getirmektir:

# Belirli bir endpoint ile birleştirilmiş bir SHA256 değeri içeren bir URL oluşturmak.
# Oluşturulan URL'ye bir HTTP GET isteği göndermek.
# Sunucudan başarılı bir yanıt alındığında, bu yanıtın JSON biçiminde olduğunu varsayarak bu yanıtı işlemek ve içindeki veriyi almak.
# Alınan veriyi sınıfın results özelliğine atamak.