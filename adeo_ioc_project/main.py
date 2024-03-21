from ioc_framework.ioc import IP, Domain
from ioc_framework.framework import IOCFramework
import requests
import json
import os

def main():

    framework = IOCFramework()

    ip = IP("91.203.193.91")
    domain = Domain("anydeskupdates.com")

    print("Welcome the ioc project.")

    platform = input("Select platform (1: VirusTotal, 2: UrlScan, 3: AbuseIPDB : ") #4: ThreatCrowd 

    if platform == "1":
        ip.endpoint = "https://www.virustotal.com/api/v3/ip_addresses/"
        framework.add_ioc(ip)
        print("Loading...")
        framework.query_all()
        framework.print_results_all()

        domain.endpoint = "https://www.virustotal.com/api/v3/domains/"
        framework.add_ioc(domain)
        print("Loading...")
        framework.query_all()
        framework.print_results_all()

        save_results = input(
            "Do you want to save and write the results to a file? (y/n): "
        )
        if save_results.lower() == "y":
            framework.write_results()
            print("Successfully file saved")
        else:
            print("Warning! File not saved.")

    elif platform == "2":
        ip.endpoint = "https://urlscan.io/api/v1/search/?q=ip:"
        framework.add_ioc(ip)
        framework.query_all()
        framework.print_results_all()

        domain.endpoint = "https://urlscan.io/api/v1/search/?q=domain:"
        framework.add_ioc(domain)
        framework.query_all()
        framework.print_results_all()

        save_results = input(
            "Do you want to save and write the results to a file? (y/n): "
        )
        if save_results.lower() == "y":
            framework.write_results()
            print("Successfully file saved")
        else:
            print("Warning! File not saved.")
            
    elif platform == "3":
        ip.endpoint = "https://abuseipdb.com/api/v2/check?ipAddress="
        framework.add_ioc(ip)
        framework.query_all()
        framework.print_results_all()

        domain.endpoint = "https://abuseipdb.com/api/v2/check-domain?domain="
        framework.add_ioc(domain)
        framework.query_all()
        framework.print_results_all()
        save_results = input(
            "Do you want to save and write the results to a file? (y/n): "
        )
        if save_results.lower() == "y":
            framework.write_results()
            print("Successfully file saved")
            
    # elif platform == "4":
            
    #         ip.endpoint = "https://www.threatcrowd.org/searchApi/v2/ip/report/?ip="
    #         framework.add_ioc(ip)
    #         framework.query_all()
    #         framework.print_results_all("ok")

    #         domain.endpoint = "https://www.threatcrowd.org/searchApi/v2/domain/report/?domain="
    #         framework.add_ioc(domain)
    #         framework.query_all()
    #         framework.print_results_all()

    #         # E-posta adresi için istek yapma ve sonuçları işleme
    #         email = "william19770319@yahoo.com"
    #         email_result = requests.get("https://www.threatcrowd.org/searchApi/v2/email/report/", params={"email": email})
    #         print(email_result.text)

    #         # JSON sonucunu işleme
    #         email_json = json.loads(email_result.text)
    #         if 'domains' in email_json:
    #             print(email_json['domains'][0])

    #         save_results = input("Do you want to save and write the results to a file? (y/n): ")
    #         if save_results.lower() == "y":
    #             framework.write_results()
    #             print("Successfully file saved")


    else:
        print("Invalid platform selection.")


if __name__ == "__main__":
    main()
