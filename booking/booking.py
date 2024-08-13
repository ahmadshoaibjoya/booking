#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:06:54 2024

@author: ahmadshoaibjoya
"""

import booking.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# import os


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
        
        
        
    def __exit__(self, exc_type, exc, traceback):
        
        if self.teardown:
            self.quit()
        
        
    
    def land_first_page(self):
        
        self.get(const.BASE_URL)
 
    
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
                
     
       

        
        
        
        
        
        
        
        
        
        
        