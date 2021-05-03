from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class PageTest(LiveServerTestCase):



	def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('id_table')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
      	               raise e                  
                   time.sleep(0.5)  
                 
	def setUp(self):
	 self.browser = webdriver.Firefox()

	def test_browser_title(self):
	 self.browser.get('http://localhost:8000/')
	 #self.browser.get(self.live_server_url)
	 self.assertIn('Owners Registration',self.browser.title)
	 header_text = self.browser.find_element_by_tag_name('h1').text
	 self.assertIn('Owners Registration', header_text)
	 
	 
	 
	
	 inputowner = self.browser.find_element_by_id('owner')
	 self.assertEqual(inputowner.get_attribute('placeholder'),'Enter your fullname')
	 inputowner.click()
	 time.sleep(1)
	 inputowner.send_keys('Leonalyn Maglines')
	 
	 time.sleep(1)
	 
	 
	 inputaddress = self.browser.find_element_by_id('address')
	 self.assertEqual(inputaddress.get_attribute('placeholder'),'Enter your complete address')
	 inputaddress.click()
	 time.sleep(1)
	 inputaddress.send_keys('Blk 13 lot 10 brgy Dimawari')
	 time.sleep(1)
	 btnContinue = self.browser.find_element_by_id('btnContinue')
	 btnContinue.click()
	 time.sleep(2)
	 
	 
	 inputpet = self.browser.find_element_by_id('pet')
	 self.assertEqual(inputpet.get_attribute('placeholder'),'Enter your pet name')
	 inputpet.click()
	 time.sleep(1)
	 inputpet.send_keys('Shana')
	 time.sleep(1)
	 
	
	 inputbreed = self.browser.find_element_by_id('breed')
	 self.assertEqual(inputbreed.get_attribute('placeholder'),'Type of breed')
	 inputbreed.click()
	 time.sleep(1)
	 inputbreed.send_keys('Puspin')
	 time.sleep(1)
	 
	 
	 inputday = self.browser.find_element_by_id('birthday')
	 self.assertEqual(inputday.get_attribute('placeholder'),'_ / _ / __')
	 inputday.click()
	 time.sleep(1)
	 inputday.send_keys('08/22/2013')
	 time.sleep(1)
	 
	 btnContinue = self.browser.find_element_by_id('btnContinue')
	 btnContinue.click()
	 time.sleep(2)
	 


	


'''	

if __name__=='__main__':
	 	unittest.main()
#this page should update and show two types of id on the list
	 Pet = self.browser.find_element_by_id('pet')
	 Pet.click()
	 time.sleep(1)
	 Pet.send_keys('Kuma')
	 time.sleep(1)
	 Breed = self.browser.find_element_by_id('breed')
	 Breed.click()
	 time.sleep(1)
	 Breed.send_keys('Pomeranian')
	 time.sleep(1)
	 Day = self.browser.find_element_by_id('birthday')
	 Day.click()
	 time.sleep(1)
	 Day.send_keys('05/25/2012')
	 btnContinue = self.browser.find_element_by_id('btnContinue')
	 btnContinue.click()
	 time.sleep(2)
	 #self.assertIn('1: Shana Puspin born on 08/22/2013',[row.text for row in rows])
	 #self.assertIn('1: Kuma Pomeranian born on 05/25/2012',[row.text for row in rows])
	 self.check_for_rows_in_list_table('1: Shana Puspin born on 08/22/2013')
	 self.check_for_rows_in_list_table("1: Kuma Pomeranian born on 05/25/2012")
	 table = self.browser.find_element_by_id('listTable')
	 rows = table.find_element_by_tag_name('tr')
'''
