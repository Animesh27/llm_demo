from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import os

from agents.linkedin_lookup_agent import lookup_agent as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

os.environ["OPENAI_API_KEY"] = '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'

if __name__ == '__main__':
    print("Hello World")

    summary_template = """
     given the information {information} about a person from I want you to create :
      1. a short summary
      2. two interesting facts about them
      """
    linkedin_profile_url = linkedin_lookup_agent(name="Animesh Chaturvedi Walmart")
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = OpenAI(temperature=0, model_name="text-ada-001")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)
    print(chain.run(information=linkedin_data))
