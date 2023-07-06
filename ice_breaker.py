from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import os

from agents.linkedin_lookup_agent import lookup_agent as linkedin_lookup_agent
from output_parsers import person_intel_parser, PersonIntel
from third_parties.linkedin import scrape_linkedin_profile


def llm_demo(name: str) -> PersonIntel:
    summary_template = """
         given the Linkedin information {linkedin_information} and twitter {twitter_information} about a person from I want you to create:
         1. a short summary
         2. two interesting facts about them
         3. A topic that may interest them
         4. 2 creative Ice breakers to open a conversation with them
         \n{format_instructions}
     """
    linkedin_profile_url = linkedin_lookup_agent(name=name)
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template,
                                             partial_variables={
                                                 "format_instructions": person_intel_parser.get_format_instructions()})
    llm = OpenAI(temperature=0, model_name="text-ada-001")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url)
    result = chain.run(information=linkedin_data)
    return person_intel_parser.parse(result)


if __name__ == '__main__':
    llm_demo("Animesh Chaturvedi")
