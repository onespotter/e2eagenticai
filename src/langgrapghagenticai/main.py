import streamlit as st
import json
from src.langgrapghagenticai.ui.streamlit.loadui import LoadStreamlitUI
from src.langgrapghagenticai.LLMS.groqllm import GroqLLM
from src.langgrapghagenticai.graph.graph_builder import GraphBuilder


#main function start

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with streamlit UI.
    This function initializes the UI, handles user input, configures the LLM models,
    sets up the graph based on the selcted use case,and displays th eoutput while implementing exception handling for robustness.
    """

    #Load UI
    ui = LoadStreamlitUI()
    user_input= ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: failed to load user input from th eUI.")
        return
    
    #Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    elif st.session_state.IsSDLC:
        user_input = st.session_state.state
    else:
        user_input = st.chat_input("Enter your message") 


    if user_message:
        try:
            #configure LLM
            obj_llm_conbfig= GroqLLM(user_controls_input=user_input)
            model = obj_llm_conbfig.get_llm_model()

            if not model:
                st.error("Error: LLM model could not initialized.")
                return
            #Initialize and set up the GROQ based on use case
            usecase=user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No use case selected.")
                return
            
            # Graph builder
            builder = GraphBuilder(model)
            try:
                graph=builder.setup_graph(usecase)
            except Exception as e:
                st.error("Erros: Graph setup failed {e}")
                return
                

        except Exception as e:
            raise ValueError(f"Error occurred with Exception: {e}")

