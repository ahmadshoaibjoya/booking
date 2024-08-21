#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:03:48 2024

@author: ahmadshoaibjoya
"""
from booking.booking import Booking


with Booking() as bot:
    
    bot.land_first_page()
    
    bot.manage_cookie()
    
    bot.dismiss_signin()
    
    bot.change_currancy(currency="EUR")
    
    bot.dismiss_signin()
    
    bot.select_a_place("Berlin")
    
    bot.select_dates(checkin_date="2024-08-25", checkout_date="2024-08-30")
    
    bot.select_adults_children_rooms(adults_count=1)
    
    bot.click_search()
    
    bot.dismiss_signin()
    
    bot.apply_filtrations()

