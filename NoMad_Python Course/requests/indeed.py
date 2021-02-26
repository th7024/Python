import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&sort=&psf=advsrch&from=advancedsearch&limit={LIMIT}"

def extract_indeed_pages():
  result=requests.get(URL)

  soup = BeautifulSoup(result.text,"html.parser")

  pagination = soup.find("ul", {"class":"pagination-list"})


  pages = pagination.find_all('span')

  spans = []

  for page in pages[:-2]:
    spans.append(page.string)

  max_spans = int(spans[-1])
  return max_spans

def extract_indeed_jobs(last_page):
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    print(result.status_code)
