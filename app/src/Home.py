##################################################
# This is the main/entry-point file for the 
# sample application for your project
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

# streamlit supports reguarl and wide layout (how the controls
# are organized/displayed on the screen).
st.set_page_config(layout = 'wide')

# If a user is at this page, we assume they are not 
# authenticated.  So we change the 'authenticated' value
# in the streamlit session_state to false. 
st.session_state['authenticated'] = False

# Use the SideBarLinks function from src/modules/nav.py to control
# the links displayed on the left-side panel. 
# IMPORTANT: ensure src/.streamlit/config.toml sets
# showSidebarNavigation = false in the [client] section
SideBarLinks(show_home=True)


# ***************************************************
#    The major content of this page
# ***************************************************

# set the title of the page and provide a simple prompt. 
logger.info("Loading the Home page of the app")
st.title('CoffeeStats')
st.write('\n\n')
st.write('### HI! As which user would you like to log in?')

# For each of the user personas for which we are implementing
# functionality, we put a button on the screen that the user 
# can click to MIMIC logging in as that mock user. 

# log in as Winston the system admin
if st.button('Act as Winston, System Administrator',
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'administrator'
    st.session_state['adminID'] = 16
    st.session_state['current_listing'] = 1
    st.switch_page('pages/A1_admin_home.py')

# log in as Catumbulo the co-op advisor
if st.button('Act as Catumbulo, an Northeastern Co-op Advisor', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'coop_advisor'
    st.session_state['first_name'] = 'Catumbulo'
    st.session_state['current_listing'] = 1
    st.session_state['adv_id'] = 41
    #For creating and deleting chats, lets assume Catumbulo has an id of 41
    st.switch_page('pages/10_CoopAdvisor_Home.py')

# log in as John the alumn
if st.button("Act as Jack, a Northeastern Alumnus", 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'alumnus'
    st.session_state['first_name'] = 'Jack'
    st.session_state['current_listing'] = 1
    st.switch_page('pages/AL_1_alumnus_profile.py')
    
# log in as Jennifer the HR contact
if st.button('Act as Jennifer, the HR contact for Bhlarma Advance', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'company'
    st.session_state['first_name'] = 'Jennifer'
    # For posting and accessing job listings, let's assume Jennifer represents the company with id 265
    # This should be Bhlarma Advance
    st.session_state['compID'] = 265
    st.session_state['current_listing'] = 1
    st.switch_page('pages/14_Company_Home.py')


# log in as Vinny the undergrad student
if st.button('Act as Vinny, a Northeastern Undergraduate Student',
            type='primary',
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'student'
    st.session_state['first_name'] = 'Vinny' 
    st.session_state['current_listing'] = 1
    st.session_state['studentID'] = 1
    st.switch_page('pages/22_Student_Dash.py')




