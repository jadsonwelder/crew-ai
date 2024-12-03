from crewai import Crew
from typing import List
from .config import load_config

class CrewManager:
    def __init__(self):
        self.agents_config, self.tasks_config = load_config()
        
    def build_crew(self):
        return Crew(
            agents=[],
            tasks=[],
        )
