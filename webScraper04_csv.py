import requests
from bs4 import BeautifulSoup as bs
import csv
all_jobs=[]

def get_pages(url):
    response = requests.get(url)
    soup = bs(response.content,"html.parser")
    buttons = len(soup.find("div",
                    class_="pagination").find_all("span",class_="page"))
    return buttons
    

def scrape_page(url):
    url = url
    response = requests.get(url)

    soup = bs(
        response.content,
        "html.parser"
    )

    jobs = soup.find("section",
                    class_ = "jobs"
                    ).find_all("li")[0:-1]

    

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

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

file = open("jobs.csv","w")
writter = csv.writer(file)
writter.writerow(
    [
        "title",
        "company",
        "position",
        "region",
        "url",
     ]
)

for job in all_jobs:
    writter.writerow(job.values())
file.close()