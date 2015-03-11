'''
Created on 23.02.2015

@author: constantin
'''
from urllib.parse import urlparse, urljoin
from models.url import Url

'''
Pagehandling and Scanning2
'''
class DomainHandler():
    def __init__(self, domain):
        o = urlparse(domain)
        self.domain = o.netloc
        self.scheme = o.scheme
        
        
    def create_url(self, url, requested_url=None, depth_of_finding=None):
        if requested_url is not None:
            try:
                url = url.toString()
            except AttributeError:
                url = url
            new_url = urljoin(requested_url, url)
        else:
            new_url = url
        res = Url(new_url)
        res.depth_of_finding = depth_of_finding
        return res 
    
    def is_in_scope(self, url):
        url_splits = url.toString().split(".")
        end_of_url = url_splits[len(url_splits) - 1]
        if end_of_url in ['png', "jpg"]:
            return False
        parsed_url = urlparse(url.toString())
        if parsed_url.netloc.find(self.domain) != -1 and parsed_url.fragment == "":
            return True
        else:
            return False
        
    def create_url_from_domain(self, domain):
        return "http://" + domain

    def has_urls_same_structure(self, url1, url2):
        if url1.__class__ != url2.__class__:
            raise ValueError("Both must be Url...")
        
        if url1.toString() == url2.toString():
            return True
        
        if url1.domain != url2.domain or url1.path != url2.path or len(url1.params) != len(url2.params):
            return False
          
        for key in url1.params:
            if key not in url2.params:
                return False
            
        for key in url2.params:
            if key not in url1.params:
                return False
        
        return True

    def complete_urls(self, web_page):

        if web_page.base_url is not None:
            base_url = web_page.base_url
        else:
            base_url = web_page.url

        for link in web_page.links:
            link.url = self.create_url(link.url, web_page.url, web_page.current_depth)

        for request in web_page.timeming_requests:
            request.url = urljoin(base_url, request.url)
        for form in web_page.forms:
            form.action = urljoin(base_url, form.action)

        try:
            for ajax in web_page.ajax_requests:
                ajax.url = urljoin(base_url, ajax.url)
        except AttributeError:
            pass

        return web_page