import streamlit as st 
import pandas as pd
import numpy as np


st.title('📆 Glenfiddich Events Register 📋')

# convert csv to dataframe
df = pd.read_csv('new_data.csv', skiprows=0, names =["CLIENT ONBOARDING SESSION 20220505", "POWERHOUSE SENDS EDM 6AM-1PM 20220511", "POWERHOUSE SENDS EDM 5PM-11PM 20220511", "RUNWAY EVENT 12AM-2PM-20220512", "RUNWAY EVENT 10PM-11:59PM 20220512", "LATE REGISTRATIONS 20220513"])
df = df.dropna() # drop rows with NaN values

# count the number of strings of each column in the dataframe
df['CLIENT ONBOARDING SESSION 20220505'] = df['CLIENT ONBOARDING SESSION 20220505'].astype(str)
df['POWERHOUSE SENDS EDM 6AM-1PM 20220511'] = df['POWERHOUSE SENDS EDM 6AM-1PM 20220511'].astype(str)
df['POWERHOUSE SENDS EDM 5PM-11PM 20220511'] = df['POWERHOUSE SENDS EDM 5PM-11PM 20220511'].astype(str)
df['RUNWAY EVENT 12AM-2PM-20220512'] = df['RUNWAY EVENT 12AM-2PM-20220512'].astype(str)
df['RUNWAY EVENT 10PM-11:59PM 20220512'] = df['RUNWAY EVENT 10PM-11:59PM 20220512'].astype(str)
df['LATE REGISTRATIONS 20220513'] = df['LATE REGISTRATIONS 20220513'].astype(str)

# save the number of strings in each column to a new dataframe
df_count = pd.DataFrame(df['CLIENT ONBOARDING SESSION 20220505'].str.split(' ').apply(len))
df_count['POWERHOUSE SENDS EDM 6AM-1PM 20220511'] = df['POWERHOUSE SENDS EDM 6AM-1PM 20220511'].str.split(' ').apply(len)
df_count['POWERHOUSE SENDS EDM 5PM-11PM 20220511'] = df['POWERHOUSE SENDS EDM 5PM-11PM 20220511'].str.split(' ').apply(len)
df_count['RUNWAY EVENT 12AM-2PM-20220512'] = df['RUNWAY EVENT 12AM-2PM-20220512'].str.split(' ').apply(len)
df_count['RUNWAY EVENT 10PM-11:59PM 20220512'] = df['RUNWAY EVENT 10PM-11:59PM 20220512'].str.split(' ').apply(len)
df_count['LATE REGISTRATIONS 20220513'] = df['LATE REGISTRATIONS 20220513'].str.split(' ').apply(len)

# show bar chart value in percentage out of 123
df_count['CLIENT ONBOARDING SESSION 20220505'] = df_count['CLIENT ONBOARDING SESSION 20220505']/123*100
df_count['POWERHOUSE SENDS EDM 6AM-1PM 20220511'] = df_count['POWERHOUSE SENDS EDM 6AM-1PM 20220511']/123*100
df_count['POWERHOUSE SENDS EDM 5PM-11PM 20220511'] = df_count['POWERHOUSE SENDS EDM 5PM-11PM 20220511']/123*100
df_count['RUNWAY EVENT 12AM-2PM-20220512'] = df_count['RUNWAY EVENT 12AM-2PM-20220512']/123*100
df_count['RUNWAY EVENT 10PM-11:59PM 20220512'] = df_count['RUNWAY EVENT 10PM-11:59PM 20220512']/123*100
df_count['LATE REGISTRATIONS 20220513'] = df_count['LATE REGISTRATIONS 20220513']/123*100

# save events name in a list
events = ['CLIENT ONBOARDING SESSION 20220505', 'POWERHOUSE SENDS EDM 6AM-1PM 20220511', 'POWERHOUSE SENDS EDM 5PM-11PM 20220511', 'RUNWAY EVENT 12AM-2PM-20220512', 'RUNWAY EVENT 10PM-11:59PM 20220512', 'LATE REGISTRATIONS 20220513']
# save number of attendees in a list
attendees = [4 , 4, 19, 57, 27, 12]
# convert list to dataframe
df_pct = pd.DataFrame(attendees, index=events, columns=['attendees'])
# show the dataframe
st.write(df_pct)
st.bar_chart(df_pct, use_container_width=True, height=600)
# calculate the attendance percentage
df_new = df_pct.copy()
df_new['attendees'] = df_new['attendees']/123*100
# show the dataframe
st.write(df_new)
st.bar_chart(df_new, use_container_width=True, height=600)


# # calculate each events attendance percentage and save to a new dataframe
# df_percentage = pd.DataFrame(df_count.sum(axis=0)/123*100)

# # show the percentage of each events attendance
# st.write(df_percentage)

# st.bar_chart(df_percentage, use_container_width=True , height=600)



# # plot and only show the percentage of each column in the dataframe
# st.bar_chart(df_count, use_container_width=True)

