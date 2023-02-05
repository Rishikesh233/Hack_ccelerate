import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import plotly.express as px
from PIL import Image
import time
import webbrowser

st.set_page_config(page_title = 'Data-Visualisation', page_icon = "📊",layout="wide")  # For setting wide page configuration
st.markdown(""" <style>
#MainMenu {visibility: hidden;}        #For hiding the menu bar
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

with st.spinner('Data Visualisation is being done!'):
    time.sleep(8)  # Loading spinner call so that user does not get bored

st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/eddc84b6-ba91-4454-982d-2ea514cc92ae/d2u3quu-041237b6-45ea-497e-a8d4-3a0ca25de4f7.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2VkZGM4NGI2LWJhOTEtNDQ1NC05ODJkLTJlYTUxNGNjOTJhZVwvZDJ1M3F1dS0wNDEyMzdiNi00NWVhLTQ5N2UtYThkNC0zYTBjYTI1ZGU0ZjcuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.lwoFMVm-aJrVTGN46U7DE1ZF6vtfkJtTuEeMPhO5W0E",width = 250)
#image ontop of header

# Reading the data that has been cleaned through Jupyter Notebook
data = pd.read_csv(
    "Cleaned Engage Car.csv")
# An extra column needed to be dropped
data.drop('Unnamed: 0', inplace=True, axis=1)
st.title("DATA VISUALISATION:")


# A function that defines the features of plot such as plot size , title name , x-y label size and name.
def plot_feat(x, y, z, a, b):
    plt.figure(figsize=(x, y))
    plt.xticks(fontsize=22)
    plt.yticks(fontsize=22)
    plt.xlabel(a, fontsize=24)
    if (b == ' '):  # For count plot the y label would be count so this function would now work for every kind of plot
        plt.ylabel('Count', fontsize=26)
    else:
        plt.ylabel(b, fontsize=26)
    plt.title(z, fontsize=(x+5))


def plot_call():   # A function defined for calling plot
    plt.show()
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)  # This is called for sorting an error.


st.subheader("""This app provides an interactive feature for playing with data set used.""")
st.subheader("""Based on complexity of plots, there are two types : Simple and Complex.""")

numeric_columns = data.select_dtypes(
    ['float64', 'int64', 'float32', 'int32']).columns    
list_numeric_columns = (list(numeric_columns))   #list of columns that have numeric values

menu_list = ["Simple Plots", "Complex Plots"]
menu = st.radio("Menu", menu_list)             #this gives user to choose graph on basis of complexity

if (menu == 'Complex Plots'):
    st.header('Welcome to Data Visualisation Interface for Complex Plots') #For user input of complex plots

    option2 = st.selectbox(
        'Options for Complex Plot :',          #5 options are provided and stored in variable option2
        ('3-D Scatter Plot', 'Histogram Plot', 'Scatter Plot', '3-D Line Plot', 'Area Plot', 'Strip Plot'))

    if (option2 == 'Histogram Plot'):
        option7 = st.selectbox('X - Label :', list(data.columns))
        option8 = st.selectbox('Y - Label:', list_numeric_columns)
        option12 = st.number_input('Number of bins:', 20, 100, step=5)                         
        fig2 = px.histogram(data, x=data.groupby(option7)[option8].mean().index, y=data.groupby(option7)[
                            option8].mean() ,nbins=option12 , text_auto = True , title = 'Histogram' , width = 1200 , height = 750)
        # for histogram the data is grouped by and then mean is taken for the y axis so that the data representation must be very clear.                    
        st.write(fig2) #Showing the plot
    
    if (option2 == 'Strip Plot'):
        option7 = st.selectbox('X - Label :', list(data.columns))
        option8 = st.selectbox('Y - Label:', list_numeric_columns) # one input must be numeric
        option12 = st.selectbox('Characterization Feature :', (
            'Manufacturer', 'Body_Type', 'Gear_Type', 'Fuel_Type', 'Drivetrain')) #For deciding color of markers on basis of data categorisation
        fig3 = px.strip(data, x = option7 , y = option8, color = option12 , width = 1200 , height = 750)
        st.write(fig3)

    if (option2 == '3-D Scatter Plot'):
        st.write("For a 3-D Plot, there should be 3 parameters and all those should be numeric."

                 " So only options for numeric features is there in the multibox.")

        option3 = st.multiselect(
            'Select the three features', list_numeric_columns) #multi inputs are taken 
        option3_array = np.array(option3) #since input were in multi input formatt so i thought of storing them in array and then accessing them through indexing
        if (len(option3_array) != 3):    #If a user select either less than 3 or more than 3 input so error should be displayed
            st.error('**_This plot requires exactly 3 features_**.')

        option4 = st.selectbox('Select the characterization feature :',
                               ('Manufacturer', 'Body_Type', 'Gear_Type', 'Fuel_Type', 'Drivetrain')) #Markers color will be based on characterisation feature which will help user in evaluating more better
        option6 = st.selectbox(
            'Do you want animated feature in your plot?', ('No', 'Yes')) #A timeline based on user input will be open which will help user to analyse data based on another feature using an animation
        if (option6 == 'Yes'):
            option5 = st.selectbox(
                'Animation Feature for Timeline :', list_numeric_columns)
            fig2 = px.scatter_3d(data, x=option3_array[0], y=option3_array[1], z=option3_array[2],       #array indexing used to get input values of multibox
                                 animation_frame=option5, color=option4, width=900, height=1000, title='3-D Scatter Plot')
        else:
            fig2 = px.scatter_3d(data, x=option3_array[0], y=option3_array[1], z=option3_array[2],  #If user does not want animation frame
                                 color=option4, width=900, height=1000, title='3-D Scatter Plot')
        st.write(fig2)

    if(option2 == 'Scatter Plot'):                                   
        st.write("For scatter plot, both should be numeric.")         #If user wants scatter plot then both onput needs to be numeric
        option7 = st.selectbox('X - Label :', list_numeric_columns)
        option8 = st.selectbox('Y - Label:', list_numeric_columns)
        option14 = st.selectbox('Characterization Feature :', (
            'Manufacturer', 'Body_Type', 'Gear_Type', 'Fuel_Type', 'Drivetrain')) #More this more creative by defining two more features:
        option15 = st.selectbox(                                                  #1. Color of marker based on charaterization feature and
            'Size of marker categorisation :', list_numeric_columns)              #2. Size of marker on another feature
        fig3 = px.scatter(data, x=option7, y=option8,                #Visualization 4 features in a 2-D plot makes it more awesome
                          size=option15, color=option14)
        st.write(fig3)

    if(option2 == '3-D Line Plot'):         
        st.write("For scatter plot, both should be numeric.")           
        option7 = st.selectbox('X - Label :', list_numeric_columns)    #Input is similar to 3D Scatter Plot but instead of using array I have used three input variable
        option8 = st.selectbox('Y - Label :', list_numeric_columns)
        option16 = st.selectbox('Z - Label :', list_numeric_columns)
        option14 = st.selectbox('Characterization Feature :', (
            'Manufacturer', 'Body_Type', 'Gear_Type', 'Fuel_Type', 'Drivetrain')) #For categorising data
        option17 = st.selectbox(
            'Do you want animated feature in your plot?', ('No', 'Yes')) 
        if (option17 == 'Yes'):
            option15 = st.selectbox(
                'Variable Feature for animation :', list_numeric_columns)
            fig3 = px.line_3d(data, x=option7, y=option8, z=option16, animation_frame=option15,  #For those who choose animation feature to be true
                              color=option14, width=1200, height=700, title='3-D Line Plot')
            st.write(fig3)
        else:
            fig3 = px.line_3d(data, x=option7, y=option8, z=option16,
                              color=option14, width=1200, height=700, title='3-D Line Plot') #code for line 3d plot
            st.write(fig3)

    if (option2 == 'Area Plot'):    #For area plot choosen by user
        option7 = st.selectbox('First Feature:', list_numeric_columns) #taking input from user 
        option8 = st.selectbox('Second Feature:', list(data.columns))
        option14 = st.selectbox('Characterization Feature :', (
            'Manufacturer', 'Body_Type', 'Gear_Type', 'Fuel_Type', 'Drivetrain')) #Categorising feature
        option15 = st.selectbox('Line Group Category :', ('Manufacturer',
                                'Body_Type', 'Gear_Type', 'Fuel_Type', 'Drivetrain', 'Model')) #Feature by which we would group lines together
        option11 = st.selectbox('Numeric Features:', list_numeric_columns)
        option13 = st.selectbox(
            'Which kind of bar You need to plot?', ('Horizontal', 'Vertical')) #Plot might be vertical or horizontal
        if(option13 == 'Horizontal'):     #Using a simple swap to plot graph horizontal or vertical
            temp = option7    
            option7 = option8
            option8 = temp
        fig3 = px.area(data, x=option7, y=option8, color=option14, #code for plotting area plot based on different input
                       line_group=option15, height=700, width=1200, title='Area Plot')
        st.write(fig3)

if (menu == 'Simple Plots'): #Now if user want to see simplex plots
    st.header('Welcome to Data Visualisation Interface for Simple Plots') #For user input of complex plots it will be shown in the screen
    option9 = st.selectbox('Which kind of plot you want?',
                           ('Histogram Plot', 'Box Plot', 'Count Plot', 'Scatter Plot', 'Bar Plot',
                            'Strip Plot', 'KDE Plot', 'Violin Plot', 'Swarm Plot')) #Choice under simple plots
    if(option9 == 'Scatter Plot'):
        st.write("Both input features should be numeric.") #For scatter plot both options should be numeric 
        option10 = st.selectbox(
            'Feature in X-axis :', list_numeric_columns)
        option11 = st.selectbox(
            'Feature in Y-axis :', list_numeric_columns)
        if (option10 == option11):
            st.error(
                "You have choosen same input. Please select one different!") #For both input to be same scatter plot would be a straight line so we showed error od both input same
        option12 = st.selectbox('Characterization Feature:', (
            'Manufacturer', 'Body_Type', 'Gear_Type', 'Fuel_Type', 'Drivetrain')) #Color of markers in plot would be categorised on these basis.
        plot_feat(16, 11, option9, option10, option11) # calling function for plot features
        sns.scatterplot(data=data, x=option10, y=option11,
                        hue=option12, palette='viridis', alpha=.89, s=120) #code for scatter plot
        plot_call()

    if(option9 == 'Count Plot'):
        st.write(
            "For many features, there is large numer even in X-axis so those features have been excluded.")
        option10 = st.selectbox('Feature in X-axis :', ('Fuel_Type', 'Airbags',                #categorisation for count plot
                                'Gear_Type', 'Drivetrain', 'Doors', 'Seats', 'Body_Type'))
        option11 = st.select_slider('Select a color of the bars',
                                    options=['red', 'orange', 'yellow',
                                             'green', 'blue', 'indigo', 'violet'])   # color of bars can be seleted using a slider
        if(option10 == 'Body_Type'): # Since x label for body type are so many so x axis should be stretched
            x = 90
            y = 40
        else:
            x = 30
            y = 20
        plot_feat(x, y, option9, option10, ' ') #calling plot_feat
        sns.countplot(data=data, x=option10, alpha=0.6, color=option11) #code for count plot
        plot_call() # call plot_call for showing up the plot

    if(option9 == 'Box Plot'):
        st.write("One input should be numeric at least")
        option10 = st.selectbox(
            'Feature in X-axis :', list_numeric_columns) #Taking input for a box plot
        option11 = st.selectbox(
            'Feature in Y-axis :', ('Manufacturer', 'Body_Type', 'Fuel_Type', 'Gear_Type', 'Drivetrain'))
        option13 = st.selectbox(
            'Which kind of bar You need to plot?', ('Horizontal', 'Vertical')) #Plot might be vertical or horizontal
        if(option13 == 'Horizontal'):     #Using a simple swap to plot graph horizontal or vertical
            temp = option10
            option10 = option11
            option11 = temp
        plot_feat(30, 20, option9, option10, option11)
        sns.boxplot(data=data, x=option10, y=option11, palette='viridis')
        plot_call()

    if(option9 == 'KDE Plot'):
        st.write("None of the input should be categorical.")
        option10 = st.selectbox(
            'Feature in X-axis :', list_numeric_columns)
        option11 = st.selectbox(
            'Feature in Y-axis :', list_numeric_columns) #for option10 == option11 , there would exist a singular matrix so it shows error
        if(option10 == option11): #for soting that error thing so that user does not put same features
            st.error("Both input features can not be same!")
        plot_feat(30, 20, option9, option10, option11) #for features of plot
        sns.kdeplot(data[option10], data[option11],
                    shade=True, cmap="Purples_d", cbar=True) #code for kde plot
        plot_call()

    if(option9 == 'Violin Plot'): #If user wants a Violin plot
        st.write("One of the input should be categorical.")
        option10 = st.selectbox('Categorical Features :', (
            'Drivetrain', 'Fuel_Type', 'Gear_Type', 'Body_Type', 'Airbags', 'Doors', 'Seats')) #taking input features
        option11 = st.selectbox('Numeric Features:', list_numeric_columns)
        plot_feat(50, 20, option9, option10, option11) #features of plot is being called
        sns.violinplot(option10, option11, data=data, palette=[
            "lightblue", "violet"], split=False)   #code for violin plot
        plot_call()

    if(option9 == 'Swarm Plot'): #All the process is similar to Violin plot
        st.write("One of the input should be categorical.")
        option10 = st.selectbox('Categorical Features :', (
            'Drivetrain', 'Fuel_Type', 'Gear_Type', 'Body_Type', 'Airbags', 'Doors', 'Seats'))
        option11 = st.selectbox('Numeric Features:', list_numeric_columns)
        option12 = st.color_picker('Pick Color for Histograms', '#00f900')
        plot_feat(50, 20, option9, option10, option11)
        sns.swarmplot(option10, option11, data=data,
                      color=option12, size=8)
        plot_call()

    if(option9 == 'Strip Plot'): #All the process is similar to Violin plot
        st.write("One of the input should be categorical.")
        option10 = st.selectbox('Categorical Features :', (
            'Drivetrain', 'Fuel_Type', 'Gear_Type', 'Body_Type', 'Airbags', 'Doors', 'Seats'))
        option11 = st.selectbox('Numeric Features:', list_numeric_columns)
        plot_feat(50, 20, option9, option10, option11)
        sns.stripplot(option11, option10, data=data, jitter=True, size=10)
        plot_call()

    if(option9 == 'Bar Plot'): #For histogram plot
        st.write("One of the input should be categorical.")
        option13 = st.selectbox(
            'Which kind of bar You need to plot?', ('Horizontal', 'Vertical')) #Taking input features
        option10 = st.selectbox('Categorical Features :', (
            'Drivetrain', 'Fuel_Type', 'Gear_Type', 'Body_Type', 'Airbags', 'Doors', 'Seats'))
        option11 = st.selectbox('Numeric Features:', list_numeric_columns)
        if(option13 == 'Horizontal'): #For plot to be horizontal use swapping
            temp = option10
            option10 = option11
            option11 = temp
        plot_feat(50, 20, option9, option10, option11)
        sns.barplot(x=option10, y=option11, data=data) #feature calling and code for bar plot
        plot_call()

    if(option9 == 'Histogram Plot'): #For Histogram plot , process is same as count plot
        st.write("One of the input should be categorical.")
        option10 = st.selectbox('Categorical Features :', ('Manufacturer', 'Drivetrain',
                                'Fuel_Type', 'Gear_Type', 'Body_Type', 'Airbags', 'Doors', 'Seats'))
        option11 = st.color_picker('Pick Color for Histograms', '#00f900')
        if(option10 == 'Manufacturer'):
            x = 100
        else:
            x = 25

        plot_feat(x, 20, option9, option10, ' ')
        sns.histplot(data=data, x=option10, color=option11)
        plot_call()

st.balloons() #calling ballons when process is executed
