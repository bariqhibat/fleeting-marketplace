from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

import time
import requests
from bs4 import BeautifulSoup
import re


class CarousellScrapper:
    def __init__(self):
        self.time = time 

        self.chrome_options = Options()
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(),
            options=self.chrome_options
        )

    def get_recent_products(self):
        URL = f"https://www.carousell.sg/search/?addRecent=false&canChangeKeyword=false&includeSuggestions=false&sort_by=time_created%2Cdescending"
        self.driver.get(URL)

        i = 0
        while i < 2:
            try:
                loadmore = self.driver.find_element_by_xpath(
                    '//button[normalize-space()="Load more"]'
                )
                loadmore.click()
                self.time.sleep(5)
                i += 1
            except NoSuchElementException:
                print("Reached bottom")
                break

        isAscending = False

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        regex = re.compile(".*D_cM D_ip D_iz.*")

        likes = soup.find_all(
            "span",
            {
                "class": "D_bn M_bI D_bw M_bR D_b_ M_bV D_bC M_bY D_bG M_cb D_bI M_ce D_bK M_cg D_bk"
            },
        )
        items = soup.find_all("div", {"class": regex})

        li = []
        for like, item in zip(likes, items):
            img = item.find("img")

            if img:
                img = img.get("src")
            else:
                img = None

            user_id = (
                item.find("a", {"class": "D_iH M_iq D_bg M_bq"})
                .get("href")
                .split("/")[1]
            )
            title = item.find(
                "p",
                {
                    "class": "D_bn M_bI D_bw M_bR D_b_ M_bV D_bC M_bY D_bF M_ca D_bI M_ce D_bL M_ch D_bk"
                },
            ).text
            time = item.find(
                "p",
                {
                    "class": "D_bn M_bI D_bw M_bR D_b_ M_bV D_bC M_bY D_bF M_ca D_bI M_ce D_bK M_cg D_iU M_iC D_bl"
                },
            )
            price = item.find(
                "p",
                {
                    "class": "D_bn M_bI D_bw M_bR D_b_ M_bV D_bC M_bY D_bF M_ca D_bI M_ce D_bK M_cg D_bj"
                },
            ).text

            if time:
                time = time.text

            texts = item.findAll(
                "p",
                {
                    "class": "D_bn M_bI D_bw M_bR D_b_ M_bV D_bC M_bY D_bF M_ca D_bI M_ce D_bK M_cg D_bk"
                },
            )

            if len(texts) == 5 and "Carouseller" in texts[0].text:
                new_carouseller = texts[0].text
                description = texts[1].text
                condition = texts[2].text
            elif len(texts) == 4:
                description = texts[0].text
                condition = texts[1].text

            if new_carouseller:
                new_carouseller = True
            else:
                new_carouseller = False

            li.append(
                {
                    "title": title,
                    "description": description,
                    "image": img,
                    "price": price,
                    "user_id": user_id,
                    "likes": like.text,
                    "time": time,
                    "condition": condition,
                    "new_seller": new_carouseller,
                }
            )

        return li

