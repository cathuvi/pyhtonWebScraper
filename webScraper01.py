import requests
from bs4 import BeautifulSoup as bs

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

soup = bs(
    response.content,
    "html.parser"
)

jobs = soup.find("section",
                 class_ = "jobs"
                 ).find_all("li")[0:-1]

all_jobs=[]

for job in jobs:
    title = job.find("span",class_="title")
    company,position, region  = job.find_all("span",class_="company")
    #url = job.find_all("a")[1]["href"]
    url = job.find("div",class_="tooltip--flag-logo").next_sibling["href"]
    job_data = {
        "title":title.text,
        "company":company.text,
        "position":position.text,
        "region":region.text,
        "url":f"https://weworkremotely.com{url}",
    }
    all_jobs.append(job_data)


print(all_jobs)

