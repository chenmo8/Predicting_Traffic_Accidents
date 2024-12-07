import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
import datetime
from sklearn.model_selection import train_test_split
import math
import datetime
from datetime import timedelta

date_format = '%m/%d/%Y %I:%M:%S %p'

# Generate 24-hour intervals
def generate_input_24_hour_intervals(increment_in_hours, date_start_obj, date_end_obj):
    i=0
    # Initialize the list to store 24-hour intervals
    twenty_four_hour_intervals = {}
    current_start = date_start_obj
    while current_start + timedelta(hours=24) <= date_end_obj:
        current_end = current_start + timedelta(hours=24)
        twenty_four_hour_intervals.update({i:[current_start, current_end]})
        current_start = current_start+timedelta(hours=increment_in_hours)  # Move to the next 24-hour interval
        i+=1
    twenty_four_hour_intervals_list = list(twenty_four_hour_intervals.values())
    return twenty_four_hour_intervals_list, twenty_four_hour_intervals

def generate_output_1_hour_intervals(twenty_four_hour_intervals_output):
    twenty_four_intervals_dict = twenty_four_hour_intervals_output[1]
    predicted_hour_interval = {}
    for k in twenty_four_intervals_dict:
        interval = twenty_four_intervals_dict[k]
        test_end = interval[1] + timedelta(hours=1)  # Add 1 hour to the end of the 24-hour interval
        predicted_hour_interval.update({k:[interval[1], test_end]}) 
    predicted_hour_interval_list = list(predicted_hour_interval.values())
    return predicted_hour_interval_list

def generate_latitude_longitude_intervals(max_lat, min_lat, max_long, min_long, divisor):
    lat_intvs, long_intvs = (max_lat-min_lat)/divisor, (max_long-min_long)/divisor
    latitude_intervals, longitude_intervals = [], []
    lat_start=min_lat
    long_start=min_long
    while lat_start < max_lat:
        latitude_intervals.append([lat_start, lat_start+lat_intvs])
        lat_start+=lat_intvs

    while long_start<max_long:
        longitude_intervals.append([long_start, long_start+long_intvs])
        long_start+=long_intvs

    return latitude_intervals, longitude_intervals

def map_time_to_interval(time_intervals, current_time):
    #print(current_time)
    for i, (start, end) in enumerate(time_intervals):
        #print(type(start), type(end))
        #print(start, current_time)
        if start <= current_time <= end:  # Check if current time is in the interval
            return i, [start, end]  # Return the index and the interval
    #print('none')
    return None

def find_interval(intervals, current_number):
    for i, (start, end) in enumerate(intervals):
        if start <= current_number <= end:
            return i, (start, end)