import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
        Manually scrape the information from the LinkedIn profile"""
    api_endpoint = 'https://gist.githubusercontent.com/Animesh27/fe549c65e254f6cd025058725ffaabd6/raw/ecfa95ed50330f371f1bdd0b21ffcd36559d3b0d/animesh-chaturvedi.json'
    response = requests.get(api_endpoint)
    data = response.json()
    data = {
        k: v
        for(k, v) in data.items()
        if v not in ("", [], None) and
           k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data
