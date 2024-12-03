from crewai import Agent, Task, Crew
import yaml

def load_config():
    with open('config/agents.yaml', 'r') as f:
        agents_config = yaml.safe_load(f)
    with open('config/tasks.yaml', 'r') as f:
        tasks_config = yaml.safe_load(f)
    return agents_config, tasks_config

def main():
    agents_config, tasks_config = load_config()
    # Configuração básica do crew
    crew = Crew(
        agents=[],
        tasks=[],
    )
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    main()
