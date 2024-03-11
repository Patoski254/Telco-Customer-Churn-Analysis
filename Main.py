import streamlit as st

# Function to create session state
def create_session_state():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

# Function to authenticate user
def authenticate(username, password):
    if username == "maranga" and password == "password":
        st.session_state.logged_in = True
    else:
        st.error("Incorrect username or password. Please try again.")

# Function to display home page
def home():
    st.markdown("<h-7><i>Welcome Patrick Maranga Moturi</i></h-7>", unsafe_allow_html=True)

    st.markdown("<h18><b>Attrition Meter:</b></h18>", unsafe_allow_html=True)
    st.markdown("<small>This app shows whether or not an employee will leave the company based on certain determined demographic and job-related questions.</small>", unsafe_allow_html=True)

    # View Data section
    st.markdown("<h18><b>Key Features:</b></h18>", unsafe_allow_html=True)
    st.markdown("<ul>"
                "<li><h20>View Data:</h20> <small>Allows you to access the data in a remote database via connection</small></li>"
                "<li><h20>Dashboard:</h20> <small>Contains Data Visualization</small></li>"
                "<li><h20>Predict:</h20> <small>Allows you to view predictions in real time</small></li>"
                "</ul>", unsafe_allow_html=True)

    st.markdown("<h18><b>User Benefits:</b></h18>", unsafe_allow_html=True)
    st.markdown("- Make data-driven decisions effortlessly\n"
                "- Harness the power of machine learning without the complexity")

    st.markdown("<h18><b>Machine Learning Integration:</b></h18>", unsafe_allow_html=True)
    st.markdown("- You have access to select between 3 models for prediction\n"
                "- Simple integration and user-friendly interface\n"
                "- Save data to a database for future use\n"
                "- Get probability of predictions")

    st.markdown("<h18><b>Need Help?</b></h18>", unsafe_allow_html=True)
    st.write('Contact me at marangap@gmail.com for collaborations. All rights reserved.')
    st.markdown('[GitHub](https://github.com)')
    st.markdown('[Medium](https://medium.com/@marangap/title-building-an-interactive-machine-learning-application-with-streamlit-dc53a28b8af5)')

# Main fun')ction
def main():
    create_session_state()

    if not st.session_state.logged_in:
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        submit_button = st.sidebar.button("Login")

        if submit_button:
            authenticate(username, password)
    else:
        home()
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False

if __name__ == '__main__':
    main()
git status
