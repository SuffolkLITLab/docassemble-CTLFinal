from docassemble.base.util import log
from mechanize import Browser
import re
def ct_prop_search(firstName, lastName):
  br = Browser()    
  br.set_handle_robots(False)   # ignore robots
  br.set_handle_refresh(False)  # can sometimes hang without this
  br.addheaders = [('User-agent', 'Firefox')] 	  
  br.open("http://civilinquiry.jud.ct.gov/PartySearch.aspx") 
  br.select_form(id="aspnetForm")
  br["ctl00$ContentPlaceHolder1$txtFirstName"] = firstName
  br["ctl00$ContentPlaceHolder1$txtLastName"] = lastName
  response = br.submit()  
  cleanResponse = response.read().decode("utf-8") #get rid of bytes-type error and white space
  cleanResponse = cleanResponse.replace('<!DOCTYPE html>','')
  case_names = re.findall("(\w+\D\s\w+\D\w+\s(?:V|v)\D\s\w+\D\s\w+)", cleanResponse)
  #log( case_name.groups()[0] , 'console' )
  docket_numbers = re.findall("(\w{8}\W\w{3}\D\w{2}\D\d{2}\D\d{7}\D\w{1})", cleanResponse)
  return case_names, docket_numbers
    
#parse the output with HTMLParser
#from html.parser import HTMLParser
#class HTMLFilter(HTMLParser):
#  def __init__(self):
#    HTMLParser.__init__(self)
#    self.recording = 0
#    self.text = ""
#    self.data = []
#
#  def handle_starttag(self, tag, attributes):
#    if tag != 'div':
#      return
#    if self.recording:
#      self.recording += 1
#      return
#    for name, value in attributes:
#      if name == 'class' and value == 'article':
#        break
#    else:
#      return
#    self.recording = 1
#
#  def handle_endtag(self, tag):
#    if tag == 'div' and self.recording:
#      self.recording -= 1
#
#  def handle_data(self, data):    
#    if self.recording:      
#      self.text += data       