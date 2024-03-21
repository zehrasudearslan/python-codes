from ioc_framework.ioc import IP, Domain
from ioc_framework.framework import IOCFramework

def display_menu():
    print("Welcome to the IOC project.")
    print("Select platform:")
    print("1. VirusTotal")
    print("2. UrlScan")
    print("3. AbuseIPDB")

def main():
    framework = IOCFramework()

    display_menu()
    platform = input("Enter your choice: ")

    ip = IP("91.203.193.91")
    domain = Domain("anydeskupdates.com")

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

        save_results = input("Do you want to save and write the results to a file? (y/n): ")
        if save_results.lower() == "y":
            framework.write_results()
            print("Successful. Goodbye :D")
        else:
            print("Goodbye")

    elif platform == "2":
        ip.endpoint = "https://urlscan.io/api/v1/search/?q=ip:"
        framework.add_ioc(ip)
        framework.query_all()
        framework.print_results_all()

        domain.endpoint = "https://urlscan.io/api/v1/search/?q=domain:"
        framework.add_ioc(domain)
        framework.query_all()
        framework.print_results_all()

        save_results = input("Do you want to save and write the results to a file? (y/n): ")
        if save_results.lower() == "y":
            framework.write_results()
            print("Successful. Goodbye :D")
        else:
            print("Goodbye")
    
    elif platform == "3":
        ip.endpoint = "https://abuseipdb.com/api/v2/check?ipAddress="
        domain.endpoint = "https://abuseipdb.com/api/v2/check-domain?domain="
    else:
        print("Invalid platform selection.")

if __name__ == "__main__":
    main()
