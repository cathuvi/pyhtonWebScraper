
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup as bs
import requests
url = "https://remoteok.com"
p = sync_playwright().start()

browser = p.chromium.launch(headless=False)
page = browser.new_page()
page.set_extra_http_headers({
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://remoteok.com/'
})

page.goto(url)

time.sleep(5)
#fbMan1 > div > label > input[type=checkbox]
# page.loca

time.sleep(20)



# header = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
#     } 
# cookie = {
#     "cf_clearance" :"4ocuGx0njq3DdPRoWW5EYw.fT8e7kHt8_11Wl_zz2l0-1729845686-1.2.1.1-Ts6KxDY93aUk7O4t4P.uKURVaVXWm1GIyEOGjaYrowh26nDRz7QCnG.QXSnZEqG.tx4NdCFMStlgvhzieNQD0H8V_wI6v7FV4YqmCzQvfX7KHmyJ_kHzqgTwl8GJiUdhpy5MX7q1I709cy9lhfhW8MT9.LjuBFin9YhbDMl57cmL6vPsBXl25MRNlkeUn6ZhV4I7aU6G_y0gju6.oJHIU0Oiu7ol19krVAfNwVgIEC5o6hHWTwNLsuZmfdDdJ8RoX0UALXa2ykpqb8ce19NNuw7oIQGzG2u3VpKTmiPr3dC6dmRE4FMSeyfxn4ifADejQ7chnAfOEQ79yjgpEMBoql.3OmuTwh7sPNzckBfMTiwV5OcyKHkNeYC7Mw1QsnSGjNpkjZ2RGK2GdIoYo8O607JGCaJEIguv7iG0dU2CSQwIeWe..LX3bDpHKlNx6ysF; visit_count=7; adShuffler=1"
# }

# r = requests.get("https://remoteok.com/",headers=header,cookies=cookie)


