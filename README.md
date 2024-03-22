#### Installion

Intallion requires [Python](https://python.org/) v3.6+

```sh
python3 -m venv venv
touch .env
pip install -r requirements.txt
python main.py

```

#### Project Structure
        ioc.py:
             Bu dosya IOC (Indicator of Compromise) sınıflarını içerir. 

            IOC adlı bir temel sınıf tanımlanır. Diğer IOC sınıfları bu sınıftan türetilir ve query ve print_results metodlarını uygular. Bu kod, IOC (Indicators of Compromise - Tehdit Belirteçleri) analizi yapmak için kullanılır. Belirli bir SHA256 değeri kullanarak belirli bir endpoint'e bir HTTP GET isteği gönderir ve yanıtı işler. Ayrıca, farklı IOC türleri için ayrı sınıflar sağlar (IP, Domain, SHA256).    
## Kullanım
            Kod, IOC sınıflarından birini başlatarak ve ardından `query` yöntemini çağırarak kullanılır.
            IP, Domain ve SHA256 adlı IOC alt sınıfları tanımlanır. Her biri farklı tipte IOC'leri temsil eder ve query metoduyla ilgili platformlardan IOC sorgularını gerçekleştirir.
            IOC sınıfları, verilen değerlerle oluşturulduğunda ilgili platforma sorgu yapmak için HTTP istekleri kullanır ve sonuçları results listesine kaydeder.


        # framework.py

        Bu kod, IOC (Tehdit Belirteci) analizi için bir çerçeve oluşturur. IOCFramework sınıfı, çeşitli IOC türlerini (IP, Domain, SHA256 vb.) içeren bir listeyi yönetir. IOC eklemek, tüm IOCs'yi sorgulamak, sonuçları yazdırmak ve dosyaya yazmak gibi temel işlevleri sağlar.  add_ioc metoduyla IOC'leri ekleyebilir ve query_all metoduyla eklenen tüm IOC'leri sorgulayabilirsiniz. print_results_all metoduyla tüm IOC'lerin sonuçlarını yazdırabilirsiniz.
        write_results metofu ile de sonuçları bir txt dosyasına yazdırabilirsiniz.

## Kullanım

        1. IOCFramework sınıfından bir örnek oluşturun:

        ```python
        ioc_framework = IOCFramework()

        main.py
        Bu kod, IOC (Indicators of Compromise - Tehdit Belirteçleri) analizi yapmak için kullanılır. Belirli bir SHA256 değeri kullanarak belirli bir endpointe bir HTTP GET isteği gönderir ve yanıtı işler. Ayrıca, farklı IOC türleri için ayrı sınıflar sağlar IP, Domain, SHA256.
    ## Kullanım

        Ana uygulama, main.py  dosyasında bulunur. Bu dosya, IOCleri sorgulayan ve sonuçlarını işleyen bir main fonksiyon içerir.
