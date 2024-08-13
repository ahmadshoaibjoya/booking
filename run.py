#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:03:48 2024

@author: ahmadshoaibjoya
"""
from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currancy(currency="USD")



# inst=Booking()
# inst.land_first_page()