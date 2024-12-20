# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st




#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Homepage", icon="🏠")

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="ℹ️")

def ExploreListingsNav():
    st.sidebar.page_link("pages/17_All_Listings.py", label="Explore Listings", icon="🚀")

#### ------------------------ System Admin Role ------------------------
def AdminDash():
    st.sidebar.page_link(
        "pages/A1_admin_home.py", label="Dashboard", icon="📊"
    )
def AdminChange():
    st.sidebar.page_link(
        "pages/A2_admin_changes.py", label="Changes", icon="✏️"
    )
def AdminUsage():
    st.sidebar.page_link(
        "pages/A3_admin_analytics.py", label="Usage Analytics", icon="📈"
    )

#### ------------------------ HR Contact Role ------------------------
def CreateListing():
    st.sidebar.page_link("pages/15_Create_Listing.py", label="Create Job Listing", icon="➕")

def MyListings():
    st.sidebar.page_link("pages/18_My_Listings.py", label="My Job Listings", icon="👁️")

def CompanyNav():
    st.sidebar.page_link("pages/14_Company_Home.py", label="Company Home", icon="👤")

#### ------------------------ Student Role ------------------------
def StudentDash():
    st.sidebar.page_link("pages/22_Student_Dash.py", label="Student Dashboard", icon="🗂️")

def StudentLinks():
    st.sidebar.page_link("pages/26_Student_Links.py", label="Useful Links", icon="📎")

# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    st.markdown(
        """
        <style>
            [data-testid="stSidebar"] {
                width: 250px;  /* Adjust sidebar width */
                min-width: 250px; /* Ensure it doesn't shrink below this width */
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # add a logo to the sidebar always
    st.sidebar.image("assets/Coffee_stats_logo.png", width=200)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        HomeNav()
        st.switch_page("Home.py")
        

    # Always show the Home page and show the About page at the bottom of the list of links
    AboutPageNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # All authenticated users get to use the Explore page
        if st.session_state["authenticated"]:
            ExploreListingsNav()

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "administrator":
            st.sidebar.write("### Administrator Links")
            AdminDash()
            AdminChange()
            AdminUsage()

        # If the user is an HR Contact, give them access to the company pages
        if st.session_state["role"] == "company":
            st.sidebar.write("### Company Links")
            CreateListing()
            MyListings()
            CompanyNav()

        # If the user is a student, give them access to student pages
        if st.session_state["role"] == "student":
            st.sidebar.write("### Student Links")
            StudentDash()
            StudentLinks()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")

    else:
        HomeNav()