from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
p = sync_playwright().start()

browser = p.chromium.launch(headless=False)
page = browser.new_page()

page.goto("https://www.wanted.co.kr/")

time.sleep(4)

page.click("button.Aside_searchButton__rajGo")

time.sleep(7)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(5)

page.keyboard.down("Enter")

time.sleep(7)

page.click("a#search_tab_position")

time.sleep(5)

for x in range(3):
    page.keyboard.down("End")
    time.sleep(5)
    
content = page.content()
soup = BeautifulSoup(content,'html.parser')

jobs = soup.find_all("div",class_="JobCard_content__jt_Jf")
job_list=[]
for job in jobs:
    biz = job.find("strong",class_="JobCard_title__HBpZf")
    company_name = job.find("span",class_="JobCard_companyName__N1YrF")
    reword = job.find("span",class_="JobCard_reward__cNlG5")
    job ={
        "biz":biz.text,
        "company_name":company_name.text,
        "reword":reword.text,
    }
    job_list.append(job)
    
print(job_list)
p.stop()