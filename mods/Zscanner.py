import threading
import socket

class ZScan:
    def __init__(self, domain, subdomains):
        self.domain = domain
        self.subdomains = subdomains
        self.results = []
    
    def scan(self):
        threads = []
        for subdomain in self.subdomains:
            thread = threading.Thread(target=self._is_subdomain_active, args=(subdomain,))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
    
    def _is_subdomain_active(self, subdomain):
        try:
            address = f"{subdomain}.{self.domain}"
            socket.gethostbyname(address)
            self.results.append(subdomain)
        except socket.error:
            pass
    
    def get_results(self):
        return self.results
