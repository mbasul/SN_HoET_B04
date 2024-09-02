# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

cnx = st.connection("snowflake")
session = cnx.session()

st.title("ZENA's Amazing Athleisure Catalog")

colors_df = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.SWEATSUITS").select(col('COLOR_OR_STYLE'), col('PRICE'))
st.dataframe(data=colors_df, use_container_width=True)

st.selectbox('Pick a sweatsuit color or style:', 
             colors_df
         )


# name_on_order = st.text_input('Name on Smoothie:')

# session = get_active_session()
# my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
# #st.dataframe(data=my_dataframe, use_container_width=True)

# ingredients_list = st.multiselect(
    # 'Cooose up to 5 ingredients: '
    # , my_dataframe
    # , max_selections = 5
# )

# if ingredients_list:
    # st.write(ingredients_list)
    # st.text(ingredients_list)

    # ingredients_string = ''
    # for f in ingredients_list:
        # ingredients_string += f + ' '

    # #st.write(ingredients_string)
    
    # time_to_insert = st.button('Submit Order')
    # if time_to_insert:
        # my_insert_stmt = """ insert into smoothies.public.orders(NAME_ON_ORDER, INGREDIENTS)
            # values ('""" + name_on_order + """', '"""+ ingredients_string + """')"""
        # # st.write(my_insert_stmt)
        # # st.stop()

        # if ingredients_string:
            # session.sql(my_insert_stmt).collect()
            # st.success('Your Smoothie is ordered, '+name_on_order+'!', icon="✅")
