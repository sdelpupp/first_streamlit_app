import streamlit 
import pandas as pd
from urllib.error import URLError
import requests
import snowflake.connector 


streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado toast') 

def get_fruityvice_data(this_fruit_choice):
    #streamlit.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice )
    # write your own comment -what does the next line do? 
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    # write your own comment - what does this do?
    return fruityvice_normalized
  


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
fruit_select = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index) , [my_fruit_list.index[0],my_fruit_list.index[1]] )

streamlit.dataframe(my_fruit_list.loc[fruit_select])

streamlit.header('Frityvice header')


try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data( fruit_choice )
    streamlit.dataframe( back_from_function )
except URLError as e:
  streamlit.error()

  
  




streamlit.header("The fruit load list contains:")

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()    

#Add a button to load the fruit 
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets)
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe( my_data_rows )

#streamlit.text("The fruit load list contains:")
#streamlit.text(my_data_row)
streamlit.stop()

add_my_fruit = streamlit.text_input("Add another fruit:")
my_cur.execute("INSERT INTO fruit_load_list VALUES ('from streamlit');")






