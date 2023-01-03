import threading
import socket

class ZScan:
    def __init__(self, domain, subdomains):
        """
        It takes a domain and a list of subdomains, and returns a list of subdomains that are active
        
        :param domain: The domain you want to scan
        :param subdomains: A list of subdomains to scan
        """
        self.domain = domain
        self.subdomains = subdomains
        self.results = []
    
    def scan(self):
        """
        It creates a thread for each subdomain and starts it.
        """
        threads = []
        for subdomain in self.subdomains:
            thread = threading.Thread(target=self._is_subdomain_active, args=(subdomain,))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
    
    def _is_subdomain_active(self, subdomain):
        """
        It takes a subdomain as an argument, and if it can resolve the subdomain, it appends it to the
        results list
        
        :param subdomain: The subdomain to check
        """
        try:
            address = f"{subdomain}.{self.domain}"
            socket.gethostbyname(address)
            self.results.append(subdomain)
        except socket.error:
            pass
    
    def get_results(self):
        """
        The function get_results() returns the results of the search
        :return: The results of the search.
        """
        return self.results
