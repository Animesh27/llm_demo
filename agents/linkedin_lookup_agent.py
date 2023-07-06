from langchain import PromptTemplate
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.tools import Tool

from tools.tools import get_profile_url


def lookup_agent(name: str) -> str:
    llm = OpenAI(temperature=0, model_name="text-ada-001")
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                              Your answer should contain only a URL"""
    tools_for_agent = [Tool(name="Crawl Google 4 LinkedIn Profile Page", func=get_profile_url,
                            description="useful for when you need get the Linkedin Page URL")]
    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )
    agent = initialize_agent(tools_for_agent, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    linkedin_username = agent.run(prompt_template.format_prompt(name_of_person=name))
    return linkedin_username
