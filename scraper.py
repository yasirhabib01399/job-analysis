from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

def scrape_indeed_jobs():
    options = Options()
    options.add_argument(r"user-data-dir=C:\Users\Yasir\flask\chrome-profile")  
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    job_titles = []
    job_links = []

    try:
        url = "https://www.indeed.com/jobs?q=python+developer&l=Pakistan"
        print(f"Accessing: {url}")
        driver.get(url)

        time.sleep(10)

        jobs = driver.find_elements(By.CSS_SELECTOR, "div.job_seen_beacon")

        if not jobs:
            print("⚠️ No job data found.")
            return

        for job in jobs:
            try:
                title_elem = job.find_element(By.CSS_SELECTOR, "h2.jobTitle")
                link_elem = job.find_element(By.CSS_SELECTOR, "a")
                title = title_elem.text.strip()
                link = link_elem.get_attribute("href")
                
                job_titles.append(title)
                job_links.append(link)

            except Exception:
                continue

        # Save to CSV
        df = pd.DataFrame({
            "title": job_titles,
            "link": job_links
        })

        df.to_csv("jobs.csv", index=False)
        print("✅ Data saved to jobs.csv")

    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_indeed_jobs()