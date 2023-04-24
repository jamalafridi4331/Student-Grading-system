
########################################import packages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
import streamlit as st
from streamlit.components.v1 import html
from base64 import b64encode
import plotly.graph_objs as go
import pydeck as pdk


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

############################################# front image
text = "Students Grading and Monitoring System"
color = 'green'
font_size = '70px'
styled_text = f'<span style="color:{color};font-size:{font_size}">{text}</span>'
st.write(styled_text, unsafe_allow_html=True)
image = Image.open("C:\\Users\\Jamaludeen\\Downloads\\grading.jfif")
st.image(image,width=800)

############################################################LOGIN PAGE

import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Simple Login App"""

	st.title("Login For Student Details")

	menu = ["Home","Login","SignUp"]
	choice = st.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.text_input("User Name")
		password = st.text_input("Password",type='password')
		if st.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				a = st.success("Logged In as {}".format(username))

				task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
				if task == "Add Post":
					st.subheader("Add Your Post")

				elif task == "Analytics":
					st.subheader("Analytics")
				elif task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")
                





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			b = st.success("You have successfully created a valid Account")
			c = st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()


#################################################data loading

data = pd.read_csv('C:\\Users\\Jamaludeen\\Documents\\RADOME\\SCHOOL MARKSHEET.csv')
data1 =  pd.read_csv(r"C:\Users\Jamaludeen\Documents\RADOME\school marksheet_11a.csv")
data2 = pd.read_csv(r"C:\Users\Jamaludeen\Documents\RADOME\school marksheet_11B.csv")

####################################################subheaders with bolding
text = "RESULTS"
color = 'green'
font_size = '50px'
styled_text = f'<span style="color:{color};font-size:{font_size}">{text}</span>'
st.write(styled_text, unsafe_allow_html=True)

text = "STEPS"
color = 'green'
font_size = '35px'
styled_text = f'<span style="color:{color};font-size:{font_size}">{text}</span>'
st.write(styled_text, unsafe_allow_html=True)

st.write("Step 1 :  SELECT THE CLASS OF THE STUDENT")
st.write("Step 2 : ENTER THE REGISTER NUMBER")

#############################create a custom CSS style for the box
highlight_style = """
<style>
div.stDataFrame {
    border: 2px solid #f63366;
    border-radius: 8px;
    padding: 10px;
}
</style>
"""
st.markdown(highlight_style, unsafe_allow_html=True)


#################################################### select box

option = st.selectbox('SELECT THE CLASS', ('SSLC', 'HSC +1'))

if option == "SSLC":    
    option_1 = st.selectbox("SELECT THE SECTION",("SSLC - A" , "SSLC - B"))
    
if option == "HSC +1":
    option_1 = st.selectbox("SELECT THE SECTION",("HSC_1 - A" , "HSC_1 - B"))
    
    
#################################################### taking results
               
roll_no = st.number_input('Enter your Register Number',min_value=1020000, max_value=10000000000)
roll_num = int(roll_no)
st.write('Student Roll number   : ', roll_no)


if roll_no >= 1020001 and roll_no <= 1020019:
    df_result = data[data["REGISTER NUMBER"] ==  roll_num]
    st.write(df_result)
        
    
if roll_no >= 11200001 and roll_no <= 11200020:
    df1_result = data1[data1["REGISTER NUMBER"] ==  roll_num]
    df1_result            
    
if roll_no >= 11210001 and roll_no <= 11210001:
    df2_result = data2[data2["REGISTER NUMBER"] ==  roll_num]
    df2_result
    

    
######################subjects
    
if option =='SSLC':
    st.subheader("THE SUBJECTS ARE")
    st.write("Tamil")
    st.write("English")
    st.write("Mathematics")
    st.write("Science")
    st.write("Social Science")

if option_1 =='HSC_1 - B' :
    st.subheader("THE SUBJECTS ARE")
    st.write("Tamil")
    st.write("English")
    st.write("Mathematics")
    st.write("Chemisty")
    st.write("Physics")
    st.write("Biology")
    
if option_1 =='HSC_1 - A':
    st.subheader("THE SUBJECTS ARE")
    st.write("Tamil")
    st.write("English")
    st.write("Mathematics")
    st.write("Chemisty")
    st.write("Physics")
    st.write("Computer Science")
    

################################ MARK STATEMENT
st.subheader("THE MARK STATEMENT")
st.markdown (""" <style>.big-font { font-size:30px !important; } </style> """, unsafe_allow_html=True)
st.markdown ('<p class="big-font">LINE CHART FOR STUDENT SCORE</p>', unsafe_allow_html=True)


################################################### LINE CHART 
if option =='SSLC':
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['TAMIL'], mode='lines'))
    fig.update_layout(title='Student Mark Levels', xaxis_title='EXAMINATIONS',yaxis_title='MARKS SCORED')
    fig.update_layout(margin=dict(l=20, r=30, t=20, b=20), width=800, height=500)
    st.plotly_chart(fig)
    

if option_1 =='HSC_1 - A':
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data1.index, y=data1['TAMIL'], mode='lines'))
    fig.update_layout(title='Student Mark Levels', xaxis_title='EXAMINATIONS',yaxis_title='MARKS SCORED')
    fig.update_layout(margin=dict(l=20, r=30, t=20, b=20), width=800, height=500)

    st.plotly_chart(fig)

if option_1 =='HSC_1 - B':
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data2.index, y=data2['TAMIL'], mode='lines'))
    fig.update_layout(title='Student Mark Levels', xaxis_title='EXAMINATIONS',yaxis_title='MARKS SCORED')
    fig.update_layout(margin=dict(l=20, r=30, t=20, b=20), width=800, height=500)
    st.plotly_chart(fig)
    
st.write("From the above lone chart your kids marks are shown and the marks in each examinations are iven by the graphical structures.")

################################################PIE CHART
st.markdown (""" <style>.big-font { font-size:30px !important; } </style> """, unsafe_allow_html=True)
st.markdown ('<p class="big-font">PIE CHART FOR MARK INCREASING LEVELS</p>', unsafe_allow_html=True)


if option =='SSLC':
    fig_1 = go.Figure()
    fig_1.add_trace(go.Pie(values=data["ENGLISH"], labels=data.index))
    fig_1.update_layout(title='Student Mark Level Increasing')
    fig.update_layout(margin=dict(l=20, r=30, t=20, b=20), width=800, height=500)
    st.plotly_chart(fig_1)
 
if option_1 =='HSC_1 - A':
    fig_1 = go.Figure()
    fig_1.add_trace(go.Pie(values=data1["COMPUTER SCIENCE"], labels=data.index))
    fig.update_layout(margin=dict(l=20, r=30, t=20, b=20), width=800, height=500)
    fig_1.update_layout(title='Student Mark Level Increasing')
    st.plotly_chart(fig_1)

if option_1 =='HSC_1 - B':
    fig_1 = go.Figure()
    fig_1.add_trace(go.Pie(values=data1["TAMIL"], labels=data.index))
    fig.update_layout(margin=dict(l=20, r=30, t=20, b=20), width=600, height=400)
    fig_1.update_layout(title='Student Mark Level Increasing')
    st.plotly_chart(fig_1)

st.write("The above PIE CHART is giving the students marks is increasing or decreasing and the exact prediction for the fure marks.")
    
################################### bar chart
st.markdown (""" <style>.big-font { font-size:30px !important; } </style> """, unsafe_allow_html=True)
st.markdown ('<p class="big-font">BAR CHART FOR MARK LEVELS</p>', unsafe_allow_html=True)

if option =='SSLC':
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data['TAMIL'], y=data['MATHEMATICS'], name='MARKS IN FIRST MID TERM EXAMS'))
    fig.add_trace(go.Bar(x=data['TAMIL'], y=data['SCIENCE'], name='MARKS IN HALF YEARLY'))
    fig.update_layout(barmode='group', xaxis_title='EXAMS', yaxis_title='MARKS')
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), width=800, height=500)
    st.plotly_chart(fig)
    
if option_1 =='HSC_1 - A':
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data1['TAMIL'], y=data1['COMPUTER SCIENCE'], name='MARKS IN FIRST MID TERM EXAMS'))
    fig.add_trace(go.Bar(x=data1['TAMIL'], y=data1['PHYSICS'], name='MARKS IN HALF YEARLY'))
    fig.update_layout(barmode='group', xaxis_title='EXAMS', yaxis_title='MARKS')
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), width=800, height=500)
    st.plotly_chart(fig)
    
if option_1 =='HSC_1 - B':
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data2['TAMIL'], y=data2['MATHEMATICS'], name='MARKS IN FIRST MID TERM EXAMS'))
    fig.add_trace(go.Bar(x=data2['TAMIL'], y=data2['BIOLOGY'], name='MARKS IN HALF YEARLY'))
    fig.update_layout(barmode='group', xaxis_title='EXAMS', yaxis_title='MARKS')
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20), width=800, height=500)
    st.plotly_chart(fig)
st.write("The above BAR CHART is giving the comparision between the examinations.")


###################################################### maping

text = "STUDENT MONITOR"
color = 'BROWN'
font_size = '60px'
styled_text = f'<span style="color:{color};font-size:{font_size}">{text}</span>'
st.write(styled_text, unsafe_allow_html=True)


layer = pdk.Layer(
    "ScatterplotLayer",
    data="https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv?accessType=DOWNLOAD",
    get_position=["longitude", "latitude"],
    get_radius=100,
    get_color=[150, 155, 100],
    pickable=True,
)

# Create a pydeck view
view = pdk.ViewState(
    latitude=11.6643,
    longitude=78.1460,
    zoom=20,
    pitch=50,
)

# Create a pydeck deck object
r = pdk.Deck(
    layers=[layer],
    initial_view_state=view,
    map_style= 'mapbox://styles/mapbox/outdoors-v11'
)

# Render the pydeck deck in Streamlit
st.pydeck_chart(r)

latitude = 11.6643
longitude = 78.1460


from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="my_app")

# Reverse geocode the latitude and longitude to get the address
location = geolocator.reverse(f"{latitude}, {longitude}")
st.subheader("THE CURRENT LOCATION IS    : ")
st.write(location.address)


# Define the location of interest
location = [longitude, latitude]

# Define the Pydeck map
view = pdk.ViewState(latitude=latitude, longitude=longitude, zoom=10)

# Define the Pydeck layer for the location of interest
location_layer = pdk.Layer('ScatterplotLayer', data=[{'lon': location[0], 'lat': location[1]}], get_position='[lon, lat]', get_color='[255, 0, 0, 255]', get_radius=100)

# Define the Pydeck layer for the data points
data_layer = pdk.Layer('ScatterplotLayer', data=data, get_position='[lon, lat]', get_color='[200, 30, 0, 160]', get_radius=10000)

# Define the Pydeck tooltip
tooltip = {'html': '{name}', 'style': {'backgroundColor': 'white', 'color': 'black'}}

# Create the Pydeck map with both layers
map = pdk.Deck(layers=[data_layer, location_layer], initial_view_state=view, tooltip=tooltip)

# Display the Pydeck map with Streamlit
st.pydeck_chart(map)

st.write("The above maps gives you the exact student location and activity details.")

text = "LINKS for Notes :"
color = 'red'
font_size = '50px'
styled_text = f'<span style="color:{color};font-size:{font_size}">{text}</span>'
st.write(styled_text, unsafe_allow_html=True)

st.write("GOOGLE homepage :")
st.markdown("![Google logo](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png)\
             Click [here](https://www.google.com) to go to Google's homepage.")

st.write("SSLC notes :")
st.markdown("Click [here](https://www.padasalai.net/2021/01/SSLC-10th-Standard-All-Subjects-Full-Guides-Full-Notes-PDF-Download.html) to go SSLC notes page.")

st.write("HSC notes :")
st.markdown("Click [here](https://www.kalvikavi.com/2021/03/12th-standard-study-materials-important.html) to go HSC notes page.")

text = "Visit Our University Website for More Informations"
color = 'blue'
font_size = '30px'
styled_text = f'<span style="color:{color};font-size:{font_size}">{text}</span>'
st.write(styled_text, unsafe_allow_html=True)
st.markdown("Click [here](https://www.periyaruniversity.ac.in/)to go UNIVERSITY website.")


text = " .....THANK YOU.....            "
color = 'GREEN'
font_size = '25px'
styled_text = f'<span style="color:{color};font-size:{font_size}">{text}</span>'
st.write(styled_text, unsafe_allow_html=True)

###########################################################
#####################################################
#############################################sidebar
text = "About Our Institution"
color = 'purple'
font_size = '50px'
styled_text = f'<span style="color:{color};font-size:{font_size}">{text}</span>'
st.sidebar.write(styled_text, unsafe_allow_html=True)

###########################################################log in page


        
        
#############################################################

with st.sidebar:
    image_univ = Image.open(r"C:\Users\Jamaludeen\Pictures\univ logo.jpg")
    st.image(image_univ,use_column_width = True)
    st.markdown("Click [here](https://www.periyaruniversity.ac.in/)to go UNIVERSITY website.")



selectbox = st.sidebar.selectbox('DETAILS',
    ('About School','Faculty','Infrastructure', 'Contacts'))



if selectbox == "About School":
    with st.sidebar:
      st.write("A school is an educational institution designed to provide learning spaces and learning environments for the teaching of students under the direction of teachers. Most countries have systems of formal education, which is sometimes compulsory.[2] In these systems, students progress through a series of schools. The names for these schools vary by country (discussed in the Regional terms section below) but generally include primary school for young children and secondary school for teenagers who have completed primary education. An institution where higher education is taught is commonly called a university college or university.")
      image = Image.open("C:\\Users\\Jamaludeen\\Downloads\\OIP.jfif")
      st.image(image,use_column_width = True)

      image = Image.open("C:\\Users\\Jamaludeen\\Downloads\\OIP (1).jfif")
      st.image(image,use_column_width = True)
      
      image = Image.open("C:\\Users\\Jamaludeen\\Downloads\\OIP (2).jfif")
      st.image(image,use_column_width = True)




if selectbox == "Faculty":
    with st.sidebar:
      st.write("Mr.JAMALUDEEN")
      st.write("Mr.BALAJI")
      st.write("Mrs.PRIYADHARSHINI")
      st.write("Mrs.SHALINI")
      
      image = Image.open("C:\\Users\\Jamaludeen\\Documents\\certificates\\p1.jfif")
      st.image(image,caption="MR.JAMALUDEEN",use_column_width = True)

      image = Image.open("C:\\Users\\Jamaludeen\\Documents\\certificates\\p2.jfif")
      st.image(image,caption="MR.BALAJI",use_column_width = True)
      
      image = Image.open("C:\\Users\\Jamaludeen\\Documents\\certificates\\p3.jfif")
      st.image(image,caption="MRS.PRIYADHARSHINI",use_column_width = True)

      image = Image.open("C:\\Users\\Jamaludeen\\Documents\\certificates\\p4.jfif")
      st.image(image,caption="SHALINI",use_column_width = True)

if selectbox == "Infrastructure":
    with st.sidebar:
      st.write("Having a good infrastructure helps the school management getting more student admission, ensuring student satisfaction, and much more. Having a good infrastructure with good amenities and facilities helps the students in focusing more on the studies. Teachers also feel good when they work in a safe, clean, healthy, and positive school environment. Here are a few things that the school management shall keep in mind while designing the school infrastructure")
      image = Image.open("C:\\Users\\Jamaludeen\\Downloads\\OIP.jfif")
      st.image(image,use_column_width = True)

      image = Image.open("C:\\Users\\Jamaludeen\\Downloads\\OIP (1).jfif")
      st.image(image,use_column_width = True)
      
      image = Image.open("C:\\Users\\Jamaludeen\\Downloads\\OIP (2).jfif")
      st.image(image,use_column_width = True)
      
if selectbox == "Contacts":
    with st.sidebar:
        st.write("TELEPHONE : 0462 - 7788990")
        st.write("periyaruniversity@gmail.com")


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

with st.sidebar:
    user_input = st.text_input("Please enter your Mail ID ")
    st.write("You mail ID is : ", user_input)

    phone_number = st.text_input("Please enter your phone number")
    st.write("Your Mobile Number is : ", phone_number)
    if len(phone_number) < 10 or len(phone_number) > 10 :
        st.write (" You entered wrong number....please check.!")

    
with st.sidebar:
    add_radio = st.radio(
        "Review For School",
        ("Very Good", "Good" , "Moderate")
    )

with st.sidebar:
    add_radio = st.radio(
        "School Infrastructure",
        ("Very Good", "Good" , "Moderate")
    )
with st.sidebar:
    add_radio = st.radio(
        "Teaching Method",
        ("Very Good", "Good" , "Moderate")
    )
with st.sidebar:
    add_radio = st.radio(
        "Extra Curricular Activities",
        ("Very Good", "Good" , "Moderate")
    )
with st.sidebar:
    add_radio = st.radio(
        "Sport Activities",
        ("Very Good", "Good" , "Moderate")
    )

################################  STUDY TIPS
with st.sidebar:
    st.subheader("Good study habits to develop")
    st.write("Find a good place to study.")
    st.write("Minimize distractions.")
    st.write("Take breaks.")
    st.write("Space out your studying.")
    st.write("Set study goals for each session.")
    st.write("Reward yourself.")
    st.write("Study with a group.")
    st.write("Take practice tests.")
    st.write("Use your own words.")
    st.write("Take care of yourself.")


























