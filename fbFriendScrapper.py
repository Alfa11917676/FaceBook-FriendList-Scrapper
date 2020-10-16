import time
from bs4 import BeautifulSoup
from selenium import webdriver
browser=webdriver.Chrome('C:\\Users\\ARNAB RAY\\Desktop\\python\\chromedriver_win32\\chromedriver.exe')

browser.get("https://www.facebook.com")
user_id="Enter your id name"
password="Enter your password"


element=browser.find_element_by_id("email")
element.send_keys(user_id)

passwor=browser.find_element_by_id("pass")
passwor.send_keys(password)
time.sleep(10)





clicker=browser.find_element_by_xpath('//a[@class="_2s25 _606w"]')
clicker.click()

time.sleep(6)
friend=browser.find_element_by_xpath('//ul[@class="_6_7 clearfix"]/li[3]/a')
friend.click()

while True:
	browser.execute_script('window.scrollTo(0,document.body.scrollHeight);')
	time.sleep(0.1)
	browser.execute_script('window.scrollTo(0,0);')
	time.sleep(0.1)
	try:
		exit_command=browser.find_element_by_xpath("//*[contains(text(),'More about you')]")
		break
	except:
		continue

source_page=browser.page_source

soup=BeautifulSoup(source_page,'html.parser')
amigo=[]
friendList=soup.find('div',{'class':'_3i9'})
for i in friendList.findAll('a'):
	amigo.append(i.text)

fried_list=[]
for name in amigo:
	if(name=='FriendFriends'):
		continue
	if('friends' in amigo):
		continue
	if(name==''):
		continue
	else:
		fried_list.append(name)
print(fried_list)
