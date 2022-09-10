Disclaimer: The data which is used, has been fetched via a API from Zillow.com. The live version however does not include a live connection to Zillow.com, due to the fact that a specfic API code and password is required that cannot be stored on publicy. Therefore the model contains data that has been retrieved in July/August of 2022 in order to have a working product. 

# LaCasita 🏡
We want to make it easier for people to find their own home. Therefore we thought about issues people face nowadays and two of the biggest pain points seem to be the missing transparency as well as the missing knowledge whether a property is fair valued and how the price is driven. In that manner we want to contribute to: The transparent housing market of the future - LaCasita! 

## Purpose & Project goal 🏁 
The project goal is to enable people to understand a property valuation by a breakdown into the features, that creates the most value for homes. Even though it can be used to also increase the selling price, but understanding what brings more value, the focus is on the home buyers:
- Property value estimation
- Recommendation system, that eases the process of finding a suitable property (incl. recommendations on how to find a better property, when defining the requirements, such as area, price or number of bathrooms)
- Display the information in a user friendly way

## Project Outline ℹ️
Starting the project the focus was on creating a product for the german market, but we quickly realized that the amount and quality of available data was dissatisfactory. As the focus was more on creating a working product than on collecting data, we switched to the US market. There the data is accessible and easier to retrieve. In our case we retireved the data via RapidAPI, which retrieved a list of search results including detailed property information, as well as similar properties, which where recetly sold and a Walk & Transit Score for each property.

## How users can get started with the project 🚀
1. [Click here to start Streamlit](https://monnes16-lacasita-streamlit-54ador.streamlitapp.com/)

2. Fill out all datafields (as adress you can use e.g. 10 Dominguez Street)

3. Click on 'Search' and a price estimation for your property will be provided as well as comparable properties. 

## Required tools 🔧 & packages 📦
- RapidAPI for fetching property data from Zillow.com (no live connection included in the product, but with stored data)
- Python environment (e.g. Colabs or Jupyter notebooks)
- Streamlit
- numpy
- pandas
- matplotlib.pyplot
- seaborn
- pickle
- geopy

## The Contributors ⌨️
- Timon Beyen
- David Brüninghoff
- Steffen Frye
- Johannes Mokry
- Philipp Sybon
- Robin Wershoven

- Aakash Dhekane (Mentor)
