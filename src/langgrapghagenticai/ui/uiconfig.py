from configparser import ConfigParser

class Config:
    def __init__(self, config_file="/Users/muralim/Documents/AgenticAIWorkspace/LangGrapghProjects/src/langgrapghagenticai/ui/uiconfig.ini"):
        self.config=ConfigParser()
        self.config.read(config_file)

    # To get llm
    def get_llm_option(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(",")
    
    def get_usecae_option(self):
            return self.config["DEFAULT"].get("USECASE_OPTIONS").split(",")

    def get_groq_model_option(self):
            return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(",")
    #To get Title
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TILTE").split(",")