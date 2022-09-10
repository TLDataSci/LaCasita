import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import requests
import pickle
from geopy.geocoders import Nominatim

def convert_df(df):
    return df.to_csv()

header = st.container()
inputform = st.container()
evaluation = st.container()

propdetails = pd.read_csv('0909_OC_long_list_filtered.csv')
df_props = pd.DataFrame(propdetails)
oc_cities = ["Aliso Viejo","Anaheim","Brea","Buena Park","Costa Mesa","Cypress","Dana Point","Fountain Valley","Fullerton","Garden Grove","Huntington Beach","Irvine","La Habra","La Palma","Laguna Beach","Laguna Hills","Laguna Niguel","Laguna Woods","Lake Forest","Los Alamitos","Mission Viejo","Newport Beach","Orange","Placentia","Rancho Santa Margarita","San Clemente","San Juan Capistrano","Santa Ana","Seal Beach","Stanton","Tustin","Villa Park","Westminster","Yorba Linda"]

years = list(range(1900,2023))
years.reverse()


with open('model_pickle', 'rb') as f:
    model = pickle.load(f)

with header:
    st.title("Property Analyzer")
with inputform:
    st.header('Tell me about your real estate')
    inp_col, map_col = st.columns(2)

    #ML Model Input
    #yearsOld = inp_col.number_input('When was your house built?', min_value = 1, value = 1, help="Select a year.")
    yearsInput = inp_col.selectbox('In which year was your house built?', years)
    size_metric = inp_col.slider('How big is your living space in squaremeters?', min_value=50, max_value=1000, step=1,help="Please use the slider to enter your homes living space")
    bedrooms = inp_col.slider('How many bedrooms does your house have?', min_value=1, max_value=8, step=1,help='Please use the slider so select the number of bedrooms for your house.')
    bathrooms = inp_col.slider('How many bathrooms does your house have?', min_value=1, max_value=6, step=1,help='Please use the slider so select the number of bathrooms for your house.')
    #bedrooms = inp_col.number_input('How many bedrooms does your building have?', min_value = 1, value = 1)
    #bathrooms = inp_col.number_input('How many bathrooms does your building have?', min_value = 1, value = 1)
    hoi = inp_col.number_input('How much do you pay in homeowners insurance?', min_value = 1, value = 1)
    address_street = inp_col.text_input('Please enter your street & house number')
    address_city = inp_col.selectbox('Select your city', oc_cities)


    search_button = inp_col.button('Search')

    if search_button == True:
        #first get coordinates for the address using geopy / Nominatim
        address = address_street + ", " + address_city
        locator = Nominatim(user_agent='techlabs')
        location = locator.geocode(address)
        lat = location.latitude
        long = location.longitude
        #create dataframe from the returned longitude & latitude
        geodata = [[lat,long]]
        df_map = pd.DataFrame(geodata, columns = ['latitude', 'longitude'])
        map_col.map(df_map, 13)

        with evaluation:

            st.write('Your property is located in', address_city, ", CA")
            #Below we use the user input to feed our machine learning model
            age_building = 2022-yearsInput
            sqft = size_metric*10.76

            user_input = np.array([bedrooms, bathrooms,lat, hoi, age_building,size_metric])
            price_m2_modeled = model.predict(user_input.reshape(1,6))
            price_abs_modeled = int(price_m2_modeled[0]*size_metric)
            price_abs_modeled_str = str(price_abs_modeled)

            st.header("Here's what we found")
            df_col, map_df_col = st.columns(2)

            result_string='According to our model, your property should be worth around $' + price_abs_modeled_str
            df_col.subheader(result_string)

            df_col.caption('This table shows you some details about other properties in your area. You can compare prices, living area etc.')
            filtered_columns = [ 'address.streetAddress','address.city', 'price', 'livingArea','yearBuilt', 'resoFacts.hasPrivatePool', 'resoFacts.garageSpaces', 'resoFacts.hasFireplace', 'resoFacts.hasSpa','resoFacts.lotSize']

            comparables_filter= (df_props['address.city']==address_city) & (df_props['livingArea']<(sqft*1.3)) & (df_props['livingArea']>(sqft*0.7))
            comparables_filter2= (df_props['yearsOld']<(age_building+5)) & (df_props['yearsOld']>(age_building-5)) & (df_props['livingArea']<(sqft*1.2)) & (df_props['livingArea']>(sqft*0.8))
            df_props[filtered_columns].loc[comparables_filter2]

            st.map(df_props.loc[comparables_filter2])
            #df_props
