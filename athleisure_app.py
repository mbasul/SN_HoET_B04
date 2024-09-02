# Import python packages
import streamlit as st
import pandas as pd
#from snowflake.snowpark.context import get_active_session

from snowflake.snowpark.functions import col

#session = get_active_session()
cnx = st.connection("snowflake")
session = cnx.session()


st.title("ZENA's Amazing Athleisure Catalog")

colors_df = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE").select(col('COLOR_OR_STYLE'), col('PRICE'), col('FILE_URL'), col('SIZE_LIST'), col('UPSELL_PRODUCT_DESC'))
st.dataframe(data=colors_df, use_container_width=True)

option = st.selectbox('Pick a sweatsuit color or style:', 
             colors_df
         )
st.write('-- Step 3: '+option)

choice_df = colors_df.filter((col("COLOR_OR_STYLE") == option))
choice_df.show()
#price_df = choice_df.select(col('PRICE'))
price = choice_df.select(col('PRICE')).to_pandas().iloc[0]["PRICE"]
st.write('Price: '+str(price))
#url = choice_df.select(col('FILE_URL')).to_pandas().iloc[0]["FILE_URL"]
#st.write('URL '+str(url))
size_list = choice_df.select(col('SIZE_LIST')).to_pandas().iloc[0]["SIZE_LIST"]
st.write('Sizes available:  '+str(size_list))
upsell = choice_df.select(col('UPSELL_PRODUCT_DESC')).to_pandas().iloc[0]["UPSELL_PRODUCT_DESC"]
st.write(upsell)

