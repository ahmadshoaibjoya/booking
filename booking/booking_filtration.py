#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:39:30 2024

@author: ahmadshoaibjoya
"""
# This file will include a class with instance methods
# That will be responsible to interact with our webistes
# After we have some results to apply filteration


# WebDriver is imported for Python Type Hinting purpose
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    
    # The __init__ constructor receive in driver parameter an object of webdriver.Chrome from booking.py
    # The type of parameter(driver) is specified as WebDriver
    def __init__(self, driver:WebDriver):
        self.driver=driver
    # The star_value is an integer value and it specifies the rating of booking, Ex: 1 to 5 stars
    def apply_star_rating(self, star_value): 
        
        star_filtration_box=self.driver.find_element(By.CSS_SELECTOR,"div[data-filters-group='class']") 
        # Inside star filtration box, we are looking for 1-5 star elements
        star_element=star_filtration_box.find_element(By.CSS_SELECTOR,f"div[data-filters-item='class:class={star_value}']")
        star_element.click()
        
        

        
       
        
       
        
       
       
        
        