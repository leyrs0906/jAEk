'''
Copyright (C) 2015 Constantin Tschuertz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


from models.webpage import WebPage

class DeltaPage(WebPage):
    
    def __init__(self, id, url = None, html = None, cookiesjar = None, depth = None, generator = None, parent_id = None, delta_depth = None, base_url = None):
        WebPage.__init__(self, id, url, html, cookiesjar, depth, base_url=base_url)
        self.generator = generator
        self.generator_requests = []
        self.parent_id = parent_id
        self.delta_depth = delta_depth
        
    def toString(self):
        msg = "[ Page: " + str(self.url) + " - ID: " + str(self.id) + " - Depth:" + str(self.current_depth) +" \n"
        msg += "Parent-ID: " + str(self.parent_id) + " - Generator: " + self.generator.toString() + " - Delta Depth: " + str(self.delta_depth) + " \n"
        if len(self.generator_requests) > 0:
            msg += "Generator AsyncRequests: \n"
            for r in self.generator_requests:
                msg += " - " + r.toString() + " \n"
        if len(self.clickables) > 0: 
            msg += "Clickable: \n"
            for elem in self.clickables:
                msg += elem.toString() + " \n"
        if len(self.timing_requests) > 0:
            msg += "Timingrequests: \n"
            for elem in self.timing_requests:
                msg += elem.toString() + " \n"
        if len(self.links) > 0: 
            msg += "Static Links: \n"
            for link in self.links:
                tmp = link.toString()
                msg += tmp + " \n"
        if len(self.forms) > 0: 
            msg += "Forms: \n"
            for elem in self.forms:
                msg += elem.toString() + " \n"
        return msg + "]"    
    

