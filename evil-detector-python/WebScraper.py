import requests
from bs4 import BeautifulSoup
import urllib.parse
import re

class WebScraper:

    def __init__(self, url):
        self.url = url
        self.soup = self.get_soup()
        self.poxies = {
            "http": "http://",
            "https": "https://"
        }


    def get_soup(self):
        headers = {

                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 ",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
            } 
        response = requests.get(self.url, headers=headers)
        return BeautifulSoup(response.text, 'html.parser')

    def is_ip_in_url(self):
        """
        This function checks if the given URL contains an IPv4 address rather than a domain name.
        
        Parameters:
        url (str): The input URL string that needs to be checked.

        Returns:
        int: Returns 1 if the URL contains an IPv4 address, otherwise returns 0.
        
        Example:
        Input: "http://192.168.1.1"
        Output: 1
        
        Input: "http://www.example.com"
        Output: 0
        """

        ipv4_regex = re.compile(
            r'http[s]?://'          # Matches the scheme (http or https)
            r'((?:\d{1,3}\.){3}\d{1,3})'  # IPv4 pattern (e.g., 192.168.1.1)
            r'(?::\d+)?'            # Optional port number (e.g., :8080)
            r'(?:/?|[/?]\S+)$',     # Matches the rest of the URL
            re.IGNORECASE           # Case-insensitive matching
        )
        return 1 if re.match(ipv4_regex, self.url) else 0

    def get_long_url(self):
        """
        This function checks whether the length of the URL held by the current object instance is greater than 75 characters.
        
        Returns:
        int: Returns 1 if the URL length is greater than 75 characters, otherwise returns 0.
        
        """

        return 1 if len(self.url) > 75 else 0

    def get_at_symbol_in_url(self):
        """
        This function checks whether the URL contains the @ symbol.

        Returns:
        int: Returns 1 if the URL contains the @ symbol, otherwise returns 0.
        
        """

        return 1 if '@' in self.url else 0

    def get_domain_prefix_suffix(self):
        
        """
        This function checks whether the domain has a prefix or suffix separated by a hyphen.

        Returns:
        int: Returns 1 if the domain name is separated by a hyphen, otherwise returns 0.
        """

        pass

    def get_sub_domain_count(self):
        parsed_url = urllib.parse.urlparse(self.url)
        return len(parsed_url.netloc.split('.')) - 1

    def get_anchor_url(self):
        # Your scraping logic here
        pass

    def get_abnormal_url(self):
        # Your scraping logic here
        pass

    def get_links_in_tags(self):
        return len(self.soup.find_all(['a', 'img']))

    def get_webpage_title(self):
        return self.soup.title.string if self.soup.title else None

    def get_meta_description(self):
        meta = self.soup.find('meta', attrs={'name': 'description'})
        return meta['content'] if meta else None

    def get_redirect_page(self):
        # Your scraping logic here
        pass

    def get_active_content_presence(self):
        # Your scraping logic here
        pass

    def get_technology_stack_info(self):
        # Your scraping logic here
        pass

    def get_http_header_info(self):
        headers = requests.get(self.url).headers
        return headers

    def get_privacy_policy_presence(self):
        # Your scraping logic here
        pass

    def get_mobile_responsiveness(self):
        # Your scraping logic here
        pass

    def get_external_links_count(self):
        return len(self.soup.find_all('a', href=True))

    def scrape_features(self):
        features = {
            "IP_Address_Usage": self.get_ip_address_usage(),
            "Long_URL": self.get_long_url(),
            "At_Symbol_In_URL": self.get_at_symbol_in_url(),
            "Domain_Prefix_Suffix": self.get_domain_prefix_suffix(),
            "Sub_Domain_Count": self.get_sub_domain_count(),
            "Request_URL": self.url,
            "Anchor_URL": self.get_anchor_url(),
            "Abnormal_URL": self.get_abnormal_url(),
            "Links_In_Tags": self.get_links_in_tags(),
            "Webpage_Title": self.get_webpage_title(),
            "Meta_Description": self.get_meta_description(),
            "Redirect_Page": self.get_redirect_page(),
            "Active_Content_Presence": self.get_active_content_presence(),
            "Technology_Stack_Info": self.get_technology_stack_info(),
            "HTTP_Header_Info": self.get_http_header_info(),
            "Privacy_Policy_Presence": self.get_privacy_policy_presence(),
            "Mobile_Responsiveness": self.get_mobile_responsiveness(),
            "External_Links_Count": self.get_external_links_count()
        }
        return features

if __name__ == "__main__":
    url = input("Enter the URL: ")
    scraper = WebScraper(url)
    features = scraper.scrape_features()
    print(features)
