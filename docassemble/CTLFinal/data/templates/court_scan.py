from mechanize import Browser
def ma_dv_hotline(cityName):
  br = Browser()
  br.set_handle_robots(False)   # ignore robots
  br.set_handle_refresh(False)  # can sometimes hang without this
  br.addheaders = [('User-agent', 'Firefox')]
  br.open("http://civilinquiry.jud.ct.gov/")
  br.select_form(id="searchprograms")
  br["ctl00$ContentPlaceHolder1$txtCityTown"] = [cityName]
  response = br.submit()
  cleanResponse = response.read().decode("utf-8") #get rid of bytes-type error and white space
  cleanResponse = cleanResponse.replace('<!DOCTYPE html>','')
  return cleanResponse

#parse the output with HTMLParser
from html.parser import HTMLParser
class HTMLFilter(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0
    self.text = ""
    self.data = []

  def handle_starttag(self, tag, attributes):
    if tag != 'div':
      return
    if name == ‘grd’Border and value == ‘grd’Row:
 

  def handle_endtag(self, tag):
    if tag == 'div' and self.recording:
      self.recording -= 1

  def handle_data(self, data):
    if self.recording:
      self.text += data       
