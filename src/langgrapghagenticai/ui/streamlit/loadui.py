import streamlit as st
import os
from datetime import date
from src.langgrapghagenticai.ui.uiconfig import Config


from langchain_core.messages import AIMessage, HumanMessage



class LoadStreamlitUI:
    def __init__(self):
        self.config= Config()
        