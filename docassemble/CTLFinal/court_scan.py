from docassemble.base.util import log
from mechanize import Browser
import re
def case_search(firstName, lastName):
  br = Browser()    
  br.set_handle_robots(False)   # ignore robots
  br.set_handle_refresh(False)  # can sometimes hang without this
  br.addheaders = [('User-agent', 'Firefox')] 	  
  br.open("http://civilinquiry.jud.ct.gov/PartySearch.aspx") 
  br.select_form(id="aspnetForm")
  br["ctl00$ContentPlaceHolder1$txtFirstName"] = firstName
  br["ctl00$ContentPlaceHolder1$txtLastName"] = lastName
  br.find_control(name="ctl00$ContentPlaceHolder1$ddlLastNameSearchType", kind="list").value = ["Is Equal To"]
  response = br.submit()  
  cleanResponse = response.read().decode("utf-8") #get rid of bytes-type error and white space
  cleanResponse = cleanResponse.replace('<!DOCTYPE html>','')
  # regex
  case_names = re.findall("(?<=(?:td><td align=\"left\">)).*\s(?:V|v)(?:.*)(?=<\/td>)", cleanResponse)
  docket_numbers = re.findall("((?<=DocketNo\=)\w{3}\D\w{2}\D\d{2}\D\d{7}\D\w{1})", cleanResponse)
  table =  "Case Name | Docket Number\n- | -" #heading row 
  for x in range(len(case_names)): 
    table = "\n"+ table +  "\n" + case_names[x] + " | " + docket_numbers[x]
  return table
  














