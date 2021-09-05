import streamlit as st
import pandas as pd
import numpy as np
import math
import pickle
import time
import datetime
import altair as alt
import pydeck as pdk
from datetime import datetime, date, time
from vega_datasets import data
from PIL import Image

page = st.sidebar.selectbox(
    'Select a page:',
    ('Home', 'Flight Delay App')
)


if page == 'Home':
    st.title('Predicting Flight Delays')

    image = Image.open('st-images/airplanes.jpeg')
    st.image(image, caption='source: https://www.shutterstock.com/image-photo/commercial-airplane-flying-above-clouds-dramatic-493536652')

    st.markdown('''
    ## **Problem Statement**
    Flight delays are incredibly costly. It is estimated that in 2019, flight delays cost the airline industry 33 billion dollars
    in the US alone*.
    They are also disruptive to passengers forcing schedule changes that can have ripple effects throughout the entire travel industry.
    The goal of this application is to allow a user to enter details about their upcoming flight and then predict the likelihood of
    whether or not this flight will be delayed giving the user information to adjust their plans accordingly.

    \* https://www.faa.gov/data_research/aviation_data_statistics/media/cost_delay_estimates.pdf
    ''')

    st.markdown('''
    ## **Methodology**
    Four different machine learning models were built and evaluated on accuracy and precision to identify the best method
    to predict a flight delay.
    ''')

    st.markdown("## **Data & Code**")
    st.markdown('''All data was taken from the Bureau of Transportation Statistics (https://www.transtats.bts.gov/Fields.asp?gnoyr_VQ=FGJ)
    \n The code can be found on the [github repo](https://github.com/becks2318/flight-delays)''')


if page == 'Flight Delay App':
    st.title("Flight Delay App")
    st.write('''Please select the parameters for your flight from the dropdown options below:''')

    # Read in the airlies list to create dropdown
    airlines_df = pd.read_csv('./data/airlines.csv')
    airlines_list = list(airlines_df.iloc[:, 0])
    sorted_airlines = airlines_list.sort()

    # Read in the origin airport list to create the origin dropdown
    origins_df = pd.read_csv('./data/origin_airports.csv')
    origins_list = list(origins_df.iloc[:, 0])
    sorted_origins = origins_list.sort()

    # Read in the destination airport list to create the destination dropdown
    dest_df = pd.read_csv('./data/dest_airports.csv')
    dest_list = list(dest_df.iloc[:, 0])
    sorted_dests = dest_list.sort()

    # Create the form to input the data
    with st.form(key='columns_in_form'):
        col1, col2, col3, col4 = st.columns(4)
        col5, col6 = st.columns(2)
        date_choice = col1.date_input('Select travel date')
        airline_choice = col2.selectbox('Select airline', airlines_list)
        origin_choice = col3.selectbox('Select origin', origins_list, index = 9)
        dest_choice = col4.selectbox('Select destination', dest_list, index = 87)
        origin_time_choice = col5.time_input('Select departure time')
        dest_time_choice = col6.time_input('Select arrival time')
        submitted = st.form_submit_button('Submit')

    # Read in the model
    with open('./models/log_reg_pipe.pkl', mode='rb') as pickle_in:
            pipe = pickle.load(pickle_in)

    # Pull out the month and day of the week from the date
    month_number = date_choice.month
    day_number = date_choice.weekday() + 1

    # Build value to predict on
    result = [[month_number, day_number, airline_choice, origin_choice, dest_choice,
    origin_time_choice, dest_time_choice]]

    # Update the results column to say 'Not Cancelled' or 'Cancelled'
    prob = pipe.predict_proba(result)[:,1]
    prob_format = (np.round(prob[0], 2) * 100)

    st.write(f'This flight has a {prob_format}% chance of being delayed.')

    maps = pd.read_csv('data/airport_lat_long.csv')

    longitude_1 = maps[maps['iata_code'] == origin_choice].get(key = 'longitude').item()
    longitude_2 = maps[maps['iata_code'] == dest_choice].get(key = 'longitude').item()
    latitude_1 = maps[maps['iata_code'] == origin_choice].get(key = 'latitude').item()
    latitude_2 = maps[maps['iata_code'] == dest_choice].get(key = 'latitude').item()


    flight_dict = [{'path': [[longitude_1, latitude_1], [longitude_2, latitude_2]], 'color': (255, 0, 0)}]
    flight_df = pd.DataFrame(flight_dict)

    ICON_URL = 'https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678111-map-marker-512.png'
    icon_dict = {
            'url': ICON_URL,
            'width': 242,
            'height': 242,
            'anchorY': 242
    }

    AIRPLANE_URL = 'https://cdn2.iconfinder.com/data/icons/old-traditional-heritage/50/25-1024.png'
    airplane_icon_dict = {
        'url': AIRPLANE_URL,
        'width': 100,
        'height': 100
    }

    location_list = [{'coordinates': [longitude_1, latitude_1], 'icon': icon_dict},
                    {'coordinates': [longitude_2, latitude_2], 'icon': icon_dict}]

    airplane_data = [{'coordinates': [(longitude_1 + longitude_2)/2, (latitude_1 + latitude_2)/2],
                    'icon': airplane_icon_dict}]

    view_state = pdk.data_utils.compute_view([[longitude_1, latitude_1], [longitude_2, latitude_2]])

    layer = pdk.Layer(
        type = 'PathLayer',
        data = flight_df,
        pickable = True,
        get_color = 'color',
        width_scale = 20,
        width_min_pixels = 2,
        get_path = 'path',
        get_width = 5
    )

    icon_layer = pdk.Layer(
        type = 'IconLayer',
        data = location_list,
        pickable = True,
        get_icon = 'icon',
        get_position = 'coordinates',
        get_size = 4,
        size_scale = 15,
        id = 'map_icon'
    )

    airplane_layer = pdk.Layer(
        type = 'IconLayer',
        data = airplane_data,
        pickable = True,
        get_icon = 'icon',
        get_position = 'coordinates',
        get_size = 4,
        size_scale = 10,
        id = 'airplane_icon'
    )

    r = pdk.Deck(layers = [layer, icon_layer, airplane_layer], initial_view_state = view_state, map_style = 'light', map_provider = 'mapbox')

    st.pydeck_chart(r)
