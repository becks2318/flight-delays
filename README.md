# Capstone - Flight Delays

### Problem Statement


I will use machine learning to predict if a flight will be delayed using publicly available Bureau of Transportation data.

---


### Executive Summary

The goal of this project was to build a machine learning model to predict flight delays.

Data was collected from the Bureau of Transportation statistics and cleaned.

Four different models were run and evaluated with different hyperparameters:

Logistic Regression  
Random Forest  
XG Boost  
Neural Net (4 dense layers, early stopping at 34 epochs)  

The best model was: XG Boost with the following hyperparameters:

XG max_depth: 20  
XG n_estimators: 200  

With an accuracy score on unseen data of 67% and a precision score on unseen data of 63%

---

### File Directory

**datasets**  
airlines.csv: List of airlines used in the streamlit app  
airport_lat_long.csv: List of latitudes and longitudes of airports used in the streamlit app  
dest_airports.csv: List of the destination airports used in the streamlit app  
origin_airports.csv: List of the origin airports used in the streamlit app  

**code**  
flights_cleaning.ipynb: Notebook where the input data files were collected and cleaned  
flights_eda_delays.ipynb: Notebook where all of the EDA and analysis on the flight data was run  
flight_delays_logistic_regression.ipynb: Notebook where the logistic regression models were run  
flight_delays_random_forest.ipynb: Notebook where the random forest models were run  
flight_delays_xgboost.ipynb: Notebook where the xgboost models were run  
flight_delays_neural_net.ipynb: Notebook where the neural net models were run  
flights_maps.ipynb: Notebook containing the lat/long information for the airports  

**images**  
cities_per_airline.png  
delays_over_time.png  
flights_airline.png  
flights_airline_delayed.png  
flights_airline_delayed_average.png  
flights_airline_delayed_minutes.png  
flights_airline_delayed_percent.png  
flights_day.png  
flights_day_delay.png  
flights_day_delayed_average.png  
flights_day_delayed_minutes.png  
flights_dest_city.png  
flights_dest_city_delayed.png  
flights_dest_city_delayed_average.png  
flights_dest_city_delayed_minutes.png  
flights_month.png  
flights_month_delayed.png  
flights_month_delayed_average.png  
flights_month_delayed_minutes.png  
flights_origin_city.png  
flights_origin_city_delayed.png  
flights_origin_city_delayed_average.png  
flights_origin_city_delayed_minutes.png  

**models**  
log_reg_pipe.pkl: Logistic regression model for the streamlit app  
xgboost_pipe.pkl: XGBoost model for the streamlit app  

---


### Data Dictionary

Source for the data: https://www.transtats.bts.gov/DL_SelectFields.asp?gnoyr_VQ=FGJ

The following table contains the features that were used in the final model:

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**month**|_int_|Bureau of Transportation Statistics|Month of flight|
|**day_of_week**|_int_|Bureau of Transportation Statistics|Day of the week of flight|
|**op_carrier**|_object_|Bureau of Transportation Statistics|Airline code|
|**origin**|_object_|Bureau of Transportation Statistics|Code of origin airport|
|**dest**|_object_|Bureau of Transportation Statistics|Code of destination airport|
|**crs_dep_time**|_int_|Bureau of Transportation Statistics|Scheduled departure time (local time: hhmm)|
|**crs_arr_time**|_float_|Bureau of Transportation Statistics|Scheduled arrival time (local time: hhmm)|
|**crs_elapsed_time**|_float_|Bureau of Transportation Statistics|Scheduled flight time (minutes)|
|**distance**|_float_|Bureau of Transportation Statistics|Distance between airports (miles)|
|**flight_delay**|_int_|Derived Field| Whether the flight was delayed or not (0 or 1)|

---


### Data Modeling

The data was first collected and cleaned:

- Remove unnamed columns
- Clean up column values (ex. remove city from state)
- Fix data types of columns (ex. turn strings to ints)
- Split the delay and cancel files (cancel rows had many null values)
- Drop appropriate nulls
- Concatenate the separate months into one data frame
- Remove outliers

The target was **flight delay** so this was created based on whether the arrival delay minutes was greater than 0

A baseline model was first run to determine the percent of delayed flights:
- Not delayed: 0.647
- Delayed: 0.353

I ran and evaluated four different types of models to see which could produce the best results on unseen test data:

Logistic Regression
Random Forest
XG Boost
Neural Net

Each model was run at least 5 times with different hyperparameters.

---

### Conclusions and Recommendations

- While we were able to predict slightly above baseline, in general the model results were not as strong as we would have hoped:  
Accuracy on unseen data: 0.67  
Precision (class = 1) on unseen data: 0.63

- We found that XG Boost was slightly better than Logistic Regression and the Neural Net at predicting flight delays  
- Random Forest just labeled everything as ‘not delayed’  
- When analyzing the data, we did not find much variability between months or days to account for differences in flight delays  

---


### Future Research

- Set up a databricks cluster so that I could:
    - Run my model with many years worth of data
    - With more computing power, run more experiments and iterate faster
- Continued feature engineering around type/size of airport (looked at airport size and hub status but neither feature added any predictive power to my model)
- I would like to incorporate Covid data into the model and see what affect that has on the results
- Add additional data sources, e.g. weather reports
- Streamlit app: add in additional steps that only allow the user to enter actual flight parameters (for example, if Hawaiian airlines does not fly from Anchorage to Denver do not let the user enter that as a flight option)

---


### Streamlit App  

https://share.streamlit.io/becks2318/flight-delays/main/st_app.py