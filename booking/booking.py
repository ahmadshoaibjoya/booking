#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:06:54 2024

@author: ahmadshoaibjoya
"""

import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

from booking.booking_filter import BookingFiltration


class Booking(webdriver.Chrome):
    
    # For Windows we need to specify the Selenium path
    # def __init__(self, driver_path=r"C:\user\desktop\SeleniumDrivers")
    #     self.driver_path=driver_path
    #     os.environ["path"]+=self.driver_path
    
    def __init__(self, teardown=False):
        
        self.teardown=teardown
        
        # This line will instantiate an instance of webdriver.chrome
        super().__init__()
        self.implicitly_wait(5)
        self.maximize_window()
        
        
        # This __exit__() is in the concept of "Context Manager" in Python, it close the file after finishing the process.
    def __exit__(self, exc_type, exc, traceback):
        
        if self.teardown:
            self.quit()
        
        
    
    def land_first_page(self):
        
        self.get(const.BASE_URL)
 
    
 
    def manage_cookie(self):
        
        try:
            cookie=self.find_element(By.ID,"onetrust-accept-btn-handler")
            cookie.click()
            
        except:
            print("Cookies buttons not exist!")          
        
        
    def dismiss_signin(self):
        
        try:            
            dismiss=self.find_element(By.CSS_SELECTOR,"Button[aria-label='Dismiss sign-in info.']")
            dismiss.click()
        except:
            print("Dismiss Button of Signin Dialog box is not exist!")
        
        
    
    def change_currancy(self, currency="EUR"):
        
        currency_element=self.find_element(By.CSS_SELECTOR,"button[data-testid='header-currency-picker-trigger']")
        
        if not currency_element.text==currency:
            
            currency_element.click()
            
            try:
                
                select_currency_element=self.find_element(
                    By.XPATH,
                    f"//button[@data-testid='selection-item']//div//div//span//div[normalize-space(text())='{currency}']"
                    )
                
            except:
                print("Your currency name is incorrect, please check the booking.com and select the correct currency name.")
                
            else:

                select_currency_element.click()
                
     
    
    def select_a_place(self, place):
        
        place_element=self.find_element(By.CSS_SELECTOR,"input[placeholder='Where are you going?']")
        place_element.clear()
        place_element.send_keys(place)
        time.sleep(1)
        select_place=self.find_element(By.ID, "autocomplete-result-0")
        select_place.click()
       
    
    def select_dates(self, checkin_date, checkout_date):
        checkin=self.find_element(By.CSS_SELECTOR,f"span[data-date='{checkin_date}']")
        checkin.click()
        checkout=self.find_element(By.CSS_SELECTOR,f"span[data-date='{checkout_date}']")
        checkout.click()
        
        
    def select_adults_children_rooms(self, adults_count=1, child_count=0, room_count=1):
        
        # Click on the Adults, Children, Rooms toggle button.
        toggle_btn=self.find_element(By.CSS_SELECTOR,"button[data-testid='occupancy-config']")
        toggle_btn.click()
        
        # ===== Add the number of Adults =====       
        # Get the default value of the Adults number
        adults_value_element=self.find_element(By.ID, "group_adults")
        adults_value=int(adults_value_element.get_attribute("value"))
        
        # Find the decrease button of adults
        decrease_adults=self.find_element(
            By.CSS_SELECTOR,
            "div[data-testid='occupancy-popup'] div div:first-child div:nth-child(3) button:first-child"
            )
        
        # Find the increase button of the adults
        increase_adults=self.find_element(
            By.CSS_SELECTOR,
            "div[data-testid='occupancy-popup'] div div:first-child div:nth-child(3) button:nth-child(3)"
            )
        
        # The default value of adults is 2 in booking.com, if the number of adults is 1, then we decrease it.
        if adults_count < adults_value:
            
            decrease_adults.click()
            
        # Increasing the number of adults  
        elif adults_count > adults_value:
            
            count=adults_count-adults_value           
            for _ in range(count):          
                increase_adults.click()
                
                
                
             
        # ===== Add the number of Children =====
        # This section will be done in next commits
        
        
        
        # ===== Add the number of Rooms =====
        # This section will be done in next commits     
        
        
        # Click the Done button, after adding the number of Adults, Childern and Rooms
        done_btn=self.find_element(By.CSS_SELECTOR,"div[data-testid='occupancy-popup'] button:nth-child(2) span")
        done_btn.click()
        
        
        
        # element=WebDriverWait(self, 10).until(                            
        #     expected_conditions.presence_of_element_located(
        #         # (By.CSS_SELECTOR,"div[data-testid='occupancy-popup'] button span")
        #         (By.CSS_SELECTOR,"div[data-testid='occupancy-popup'] button:nth-child(2) span")               
        #         )
        #     )         
        # self.execute_script("arguments[0].style.border='3px solid red'", element)
        
        
        
        
    def click_search(self):
        search_btn=self.find_element(By.CSS_SELECTOR,"button[type='submit']")
        search_btn.click()
     
    
    
    def apply_filtrations(self):
        # The self(webdriver.Chrome) object is passed as an argument to the class
        filtration=BookingFiltration(driver=self)
        # In arguments filtering the 1 to 5 stars booking.
        filtration.apply_star_rating(2,3)
        time.sleep(2)
        filtration.sort_lowest_price()
        
    
        
        
        
        