import math
import whois
import requests
from datetime import datetime
from collections import Counter
from urllib.parse import urlparse

class url_crawler:
    def __init__(self, url):
        self.url = url
        self.domain = url.split('//')[-1].split('/')[0]
        self.urlparse = urlparse(self.url)
        
        try:
            self.whois = whois.whois(self.urlparse.netloc)
        except:
            self.whois = None
            
        self.check_http = self._get_http()
        self.check_https = self._get_https()
        self.url_response = self._get_url_response()
        self.registration_date = self._get_registration_date()
        self.expiry_date = self._get_expiry_date()
        self.intended_lifespan = self._get_intended_lifespan()
        self.registrar = self._get_registrar()
        self.registered_country = self._get_registered_country()
        self.dot_count = self._get_dot_count()
        self.digit_count = self._get_digit_count()
        self.url_length = self._get_url_length()
        self.fragments_count = self._get_fragments_count()
        self.entropy = self._get_entropy()
        self.check_encoding = self._get_encoding()
        self.check_client = self._get_check_client()
        self.check_admin = self._get_check_admin()
        self.check_server = self._get_check_server()
        self.check_login = self._get_check_login()
        self.check_ports = self._get_check_ports()
    
    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __repr__(self):
        return "%s" % (self.url)

    def __str__(self):
        return "%s" % (self.url)
 
    ## URL Domain Based Features
    def _get_http(self) -> bool:
        return True if 'http:' in self.url else False
    
    def _get_https(self) -> bool:
        return True if 'https:' in self.url else False
    
    def _get_url_response(self) -> bool:
        try:
            response = requests.get(self.url)
            return True if response.ok else False
        except:
            return False
    
    def _get_registration_date(self) -> int:
        if self.whois and self.whois['creation_date']:
            try:
                creationDate = self.whois.creation_date
                return abs((creationDate.date()-datetime.now().date()).days)
            except:
                creationDate = self.whois.creation_date[0]
                return abs((creationDate.date()-datetime.now().date()).days)
            return None
        else:
            return None
        
    def _get_expiry_date(self) -> int:
        if self.whois and self.whois['expiration_date']:
            try:
                expiryDate = self.whois.expiration_date
                return abs((expiryDate.date()-datetime.now().date()).days)
            except:
                expiryDate = self.whois.expiration_date[0]
                return abs((expiryDate.date()-datetime.now().date()).days)
            return None
        else:
            return None
        
    def _get_intended_lifespan(self) -> int:
        try:
            return abs((self.getExpiryDate() - self.getRegistrationDate())).days
        except:
            return None
        
    def _get_registrar(self) -> str:
        return self.whois.get('registrar', None)
    
    def _get_registered_country(self) -> str:
        return self.whois.get('country', None)
    
    ## URL string Based Features
    def _get_dot_count(self) -> int:
        y = Counter(x for x in self.url if x == '.')
        return y['.']
    
    def _get_digit_count(self) -> int:
        return sum(digit.isdigit() for digit in self.url)
    
    def _get_url_length(self) -> int: 
        return len(self.url)
    
    def _get_fragments_count(self) -> int:
        fragments = self.urlparse.fragment
        y = Counter(x for x in fragments if x == '#')
        return y['#']
    
    def _get_entropy(self) -> float:
        url_string = self.url.strip()
        probs = [float(url_string.count(c)) / len(url_string) for c in dict.fromkeys(list(url_string))]
        entropy = sum([(p * math.log(p) / math.log(2.0)) for p in probs])
        return entropy
    
    def _get_encoding(self) -> bool:
        return True if '%' in self.url else False
    
    def _get_check_client(self) -> bool:
        return True if 'client' in self.url else False
    
    def _get_check_admin(self) -> bool:
        return True if 'admin' in self.url else False
    
    def _get_check_server(self) -> bool:
        return True if 'server' in self.url else False
    
    def _get_check_login(self) -> bool:
        return True if 'login' in self.url else False
    
    def _get_check_ports(self) -> bool:
        return True if self.urlparse.port != None else False
    
if __name__ == '__main__':
    url_crawler(url)