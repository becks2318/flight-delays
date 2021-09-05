# Capstone - Flight Delays

### Problem Statement


I will use machine learning to predict if a flight will be delayed using publicly available Bureau of Transportation data.

---


### Executive Summary



---

### File Directory

**datasets**  


**code**  


**images**  

---


### Data Dictionary

Source for the data: https://www.transtats.bts.gov/DL_SelectFields.asp?gnoyr_VQ=FGJ

The following table contains the features that were used in the final model:

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**year**|_int_|Bureau of Transportation Statistics|Year of flight|
|**month**|_int_|Bureau of Transportation Statistics|Month of flight|
|**day_of_week**|_int_|Bureau of Transportation Statistics|Day of the week of flight|
|**fl_date**|_object_|Bureau of Transportation Statistics|Date of flight|
|**op_carrier**|_object_|Bureau of Transportation Statistics|Airline code|
|**op_carrier_fl_num**|_int_|Bureau of Transportation Statistics|Flight number|
|**origin_airport_id**|_int_|Bureau of Transportation Statistics|ID of origin airport|
|**origin**|_object_|Bureau of Transportation Statistics|Code of origin airport|
|**origin_city_name**|_object_|Bureau of Transportation Statistics|City of origin airport|
|**origin_state_nm**|_object_|Bureau of Transportation Statistics|State of origin airport|
|**dest_airport_id**|_int_|Bureau of Transportation Statistics|ID of destination airport|
|**dest**|_object_|Bureau of Transportation Statistics|Code of destination airport|
|**dest_city_name**|_object_|Bureau of Transportation Statistics|City of destination airport|
|**dest_state_nm**|_object_|Bureau of Transportation Statistics|State of destination airport|
|**crs_dep_time**|_int_|Bureau of Transportation Statistics|Scheduled departure time (local time: hhmm)|
|**dep_time**|_float_|Bureau of Transportation Statistics|Actual departure time (local time: hhmm)|
|**dep_delay_new**|_float_|Bureau of Transportation Statistics|Difference between scheduled and actual departure time (minutes)|
|**crs_arr_time**|_int_|Bureau of Transportation Statistics|Scheduled arrival time (local time: hhmm)|
|**arr_time**|_float_|Bureau of Transportation Statistics|Actual arrival time (local time: hhmm)|
|**arr_delay_new**|_float_|Bureau of Transportation Statistics|Difference between scheduled and actual arrival time (minutes)|
|**cancelled**|_float_|Bureau of Transportation Statistics|Flag if the flight was cancelled|
|**crs_elapsed_time**|_float_|Bureau of Transportation Statistics|Scheduled flight time (minutes)|
|**actual_elapsed_time**|_float_|Bureau of Transportation Statistics|Actual flight time (minutes)|
|**distance**|_float_|Bureau of Transportation Statistics|Distance between airports (miles)|
|**carrier_delay**|_float_|Bureau of Transportation Statistics|Flag if the delay was from carrier|
|**weather_delay**|_float_|Bureau of Transportation Statistics|Flag if the delay was from weather|
|**nas_delay**|_float_|Bureau of Transportation Statistics|Flag if the delay was from National Air System|
|**security_delay**|_float_|Bureau of Transportation Statistics|Flag if the delay was from security|
|**late_aircraft_delay**|_float_|Bureau of Transportation Statistics|Flag if the delay was from late aircraft|


---


### Data Modeling



---

### Conclusions and Recommendations



---


### Future Research

