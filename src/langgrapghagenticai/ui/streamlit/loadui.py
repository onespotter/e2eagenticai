import streamlit as st
import os
from datetime import date
from src.langgrapghagenticai.ui.uiconfig import Config


from langchain_core.messages import AIMessage, HumanMessage



class LoadStreamlitUI:
    def __init__(self):
        self.config= Config()
        self.user_controls = {}

    def initialize_session(self):
        return {
            "current_step": "requirements",
            "requirements": "",
            "user_stories":"",
            "po_feedbacks":"",
            "generated_code":"",
            "review_feedback":"",
            "decision": None
        }
    
    def render_requirements(self):
        st.markdown("## Requirements submission")
        st.session_state.state["requirements"] = st.text_area(
            "Enter your rwquirements:",
            height=200,
            key="req_input"
        )

        if st.button("Submit Requirements", key="submit_req"):
            st.session_state.state["current_step"] = "genearte_user_stories"
            st.session_state.IsSDLC = True

    def load_streamlit_ui(self):
        st.set_page_config(page_title=" "+str(self.config.get_page_title()), layout="wide")
        st.header(self.config.get_page_title())
        st.session_state.timeframe=''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False



        with st.sidebar:
            #Get options from config
            llm_options= self.config.get_llm_option()
            usercase_options= self.config.get_usecae_option()

            #LLM selction
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)
            if self.user_controls["selected_llm"] == 'Groq':
                #model selction
                model_options= self.config.get_groq_model_option()
                self.user_controls["selected+groq_model"] = st.selectbox("Select Model", model_options)
                #API Key input
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")
                #validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your GROQ api key to proceed.")


            #use case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select useecase", usercase_options)
            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
            #self.render_requirements() # right side window

        return self.user_controls







        