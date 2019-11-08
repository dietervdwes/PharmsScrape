#Tacrolimus levels: SA03452243 (UCT Private)
#Urine drugs of abuse: SA03450896 (2 Military Hospital lab)

import requests, bs4
from bs4 import BeautifulSoup
from lxml import html


from selenium.webdriver.chrome.options import Options
from selenium import webdriver


driver = webdriver.Chrome()

#If you do not know how to use Selenium, here is a quick overview:

driver.get("http://10.184.55.233:8080") #Browser goes to pharms.westerncape.gov.ac.za
#Finding elements: Use either the ELEMENTS or ELEMENT method. Examples:

#driver.find_element_by_css_selector("#IWEDITUSERNAME") #Find your country in Google. (singu
#sitename = driver.find_element_by_css_selector("#IWLABELLOGINDESCRIPTION")

#print(sitename.text)



assert "Pharmacology" in driver.title
#COMPLETE THE USERNAME AND PASSWORD FIELDS
#Find the username field by its id in the HTML markup (e.g. id="uid) and the password by the name attribute (e.g. name="pwd")

username = driver.find_element_by_id("IWEDITUSERNAME")
username.clear()
username.send_keys("WARD")

password = driver.find_element_by_id("IWEDITPASSWORD")
password.clear()
password.send_keys("WARD")

#CLICK THE LOGIN BUTTON
#Now we need to submit the login credentials by clicking the submit button
driver.find_element_by_id("IWBUTTONLOGIN").click()

#CLICK A LINK ON THE PAGE BASED ON THE LINK TEXT
#This is handy where you know the text of the link you want to target, but there's no unique identifier reliably grip onto in the mark up. Here, we're simply looking for a link with the text: "Grumpy cats".
#####    driver.find_element_by_link_text("Grumpy cats").click()

'''

#To log into the homepage:
#import requests

# Fill in your details here to be posted to the login form.
headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'Origin': 'http://10.184.55.233:8080',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://10.184.55.233:8080',
    'Accept': 'text/html, */*; q=0.01',
}

payload = {
  'IWEDITUSERNAME': 'WARD^',
  'IWEDITPASSWORD': 'WARD^',
  }

# The following is the older requests scrape code

"""
# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('http://10.184.55.233:8080', headers=headers, data=payload, verify=False)
    # print the html returned or something more intelligent to see if it's a successful login page.
    soup = BeautifulSoup(p.text, 'lxml')
    print(soup.prettify())

    # An authorised request.
    r = s.get('http://10.184.55.233:8080/$')
    #print(r.BeautifulSoup(r.text, 'lxml')

#print(soup.get_text)
#print(soup.prettify())





cookies = {
    'IW_CookieCheck_': 'Enabled',
    'IW_CustomTrackID': '0cse19b15u30qf1bkqfu017cta6q',
    'IntraWeb_WWDisa': '0cse19b15u30qf1bkqfu017cta6q_',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://10.184.55.233:8080',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 OPR/64.0.3417.61',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://10.184.55.233:8080/$',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
  'IWLISTBOXPERIOD': '0^',
  'IWLISTBOXWARD': '0^',
  'IWLISTBOXLOCATION': '3^',
  'Name3': '^',
  'name1': 'IWRadioButtonExact^',
  'Name2': '^',
  'IWEDITFILENO': '^',
  'IWEDITNAME': '^',
  'IWEDITINITS': '^',
  'IWEDITAGE': '^',
  'IWEDITSEX': '^',
  'IWEDITDOB': '^',
  'IWEDITID': 'SA03452243^',
  'IWEDITTESTS': '^',
  'IWBUTTONSEARCH': '^',
  'IWBUTTONRESET': '^',
  'IWGRIDMYPATIENTS': '^',
  'IWEDIT1': '^',
  'IW_Action': 'IWLISTBOXLOCATION^',
  'IW_ActionParam': '^',
  'IW_FormName': 'MyPatientsForm^',
  'IW_FormClass': 'TMyPatientsForm^',
  'IW_width': '843^',
  'IW_height': '757^',
  'IW_TrackID_': '13'
}

response = requests.post('http://10.184.55.233:8080/$', headers=headers, cookies=cookies, data=data, verify=False)

soup = response.text



webpagehtml = bs4.BeautifulSoup(response.text)



print(webpagehtml.prettify())






##########            This is the curl when logging in  #################
import requests

cookies = {
    'IW_CookieCheck_': 'Enabled',
    'IW_CustomTrackID': '0cse19b15u30qf1bkqfu017cta6q',
    'IntraWeb_WWDisa': '0cse19b15u30qf1bkqfu017cta6q_',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://10.184.55.233:8080',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 OPR/64.0.3417.61',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://10.184.55.233:8080/^$',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
  'IWEDITUSERNAME': 'WARD^',
  'IWEDITPASSWORD': 'WARD^',
  'IWBUTTONLOGIN': '^',
  'IWBUTTONCHANGE': '^',
  'IWBUTTONCANCEL': '^',
  'IWEDITERROR': '^',
  'IW_Action': 'IWEDITPASSWORD^',
  'IW_ActionParam': '^',
  'IW_FormName': 'LoginForm^',
  'IW_FormClass': 'TLoginForm^',
  'IW_width': '843^',
  'IW_height': '757^',
  'IW_TrackID_': '26'
}

response = requests.post('http://10.184.55.233:8080/%5E$', headers=headers, cookies=cookies, data=data, verify=False)


#################### This is the curl for the search page after having logged in  ############## 
import requests

cookies = {
    'IW_CookieCheck_': 'Enabled',
    'IW_CustomTrackID': '0cse19b15u30qf1bkqfu017cta6q',
    'IntraWeb_WWDisa': '0cse19b15u30qf1bkqfu017cta6q_',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://10.184.55.233:8080',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 OPR/64.0.3417.61',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://10.184.55.233:8080/$',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
  'IWLISTBOXPERIOD': '0^',
  'IWLISTBOXWARD': '0^',
  'IWLISTBOXLOCATION': '3^',
  'Name3': '^',
  'name1': 'IWRadioButtonExact^',
  'Name2': '^',
  'IWEDITFILENO': '^',
  'IWEDITNAME': 'Monwabisi^',
  'IWEDITINITS': '^',
  'IWEDITAGE': '^',
  'IWEDITSEX': '^',
  'IWEDITDOB': '^',
  'IWEDITID': '^',
  'IWEDITTESTS': '^',
  'IWBUTTONSEARCH': '^',
  'IWBUTTONRESET': '^',
  'IWGRIDMYPATIENTS': '^',
  'IWEDIT1': '^',
  'IW_Action': 'IWLISTBOXLOCATION^',
  'IW_ActionParam': '^',
  'IW_FormName': 'MyPatientsForm^',
  'IW_FormClass': 'TMyPatientsForm^',
  'IW_width': '843^',
  'IW_height': '757^',
  'IW_TrackID_': '13'
}

response = requests.post('http://10.184.55.233:8080/%5E$', headers=headers, cookies=cookies, data=data, verify=False)

####################### This is the curl for the patient page:
import requests

cookies = {
    'IW_CookieCheck_': 'Enabled',
    'IW_CustomTrackID': '0cse19b15u30qf1bkqfu017cta6q',
    'IntraWeb_WWDisa': '0cse19b15u30qf1bkqfu017cta6q_',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://10.184.55.233:8080',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 OPR/64.0.3417.61',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://10.184.55.233:8080/^$',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'If-Modified-Since': 'Tue, 8 Oct 2019 12:38:34 GMT',
}

data = {
  'IWGRIDHISTORY': '^',
  'IWBUTTONSAVEPDF': '^',
  'IWTABCONTROL1_input': '1^',
  'IW_Action': 'IWTABCONTROL1^',
  'IW_ActionParam': '^',
  'IW_FormName': 'AccessForm^',
  'IW_FormClass': 'TAccessForm^',
  'IW_width': '1307^',
  'IW_height': '1021^',
  'IW_TrackID_': '23'
}

response = requests.post('http://10.184.55.233:8080/%5E$', headers=headers, cookies=cookies, data=data, verify=False)

"""



