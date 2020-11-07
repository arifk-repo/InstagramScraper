from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time
from bs4 import BeautifulSoup
from flaskr import excel_exporter
from flaskr.admin import LSTM

class ScrapePost:
    def __init__(self):
        self.data = []
        self.username = []
        self.comments = []
        self.image=[]
        self.result=[]
        self.valid=[]
        self.driver_path()
        return None

    def driver_path(self):
        self.login='https://www.instagram.com/accounts/login/'
        options = webdriver.ChromeOptions()
        path = 'flaskr'
        import os
        basepath = os.path.join(path, "driver", "chromedriver")
        self.driver = webdriver.Chrome(executable_path=basepath, options=options)

    def login_page(self,url,username,password):
        try:
            self.driver.get(self.login)
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='username']"))).send_keys(username)
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(password)
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(
                Keys.ENTER)
            time.sleep(5)
            return self.get_post(url)
        except TimeoutException:
            return False

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def check_verified_account(self,comments):
        for text in comments:
            if text != "Verified":
                self.data.append(text)

    def parse_text(self):
        for x in range(0,len(self.data)-1,2):
            self.username.append(self.data[x])
            self.comments.append(self.data[x+1])

    def identification(self):
        result = LSTM()
        valid=result.cek_valid(self.comments)
        for x in valid:
            self.valid.append(x)
        prediction=result.prediction()
        for x in prediction:
            self.result.append(x)

    def get_post(self,url):
        self.driver.get(url)
        while self.check_exists_by_xpath("//div/ul/li/div/button"):
            load_more_comments_element = self.driver.find_element_by_xpath("//div/ul/li/div/button")
            load_more_comments_element.click()
            time.sleep(0.2)

        time.sleep(2)
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        #mencari commentar dan username
        comms = soup.find_all('div', attrs={'class': 'C4VMK'})
        soup_2 = BeautifulSoup(str(comms), 'lxml')
        spans = soup_2.find_all('span')
        # mencari gambar
        image=soup.find_all('div',attrs={'class':'Jv7Aj'})
        soup_3=BeautifulSoup(str(image),'lxml')
        img=soup_3.find_all('img')
        for x in img:
            self.image.append(x["src"])
        if len(image)!=len(comms):
            self.image.pop(0)

        comments = [i.text.strip() for i in spans if i != '']
        self.check_verified_account(comments)
        self.parse_text()
        self.identification()
        hasil_label=[]
        for x in self.result:
            if x==0:
                hasil_label.append("Cyberbullying")
            elif x==1:
                hasil_label.append("Irrelevant")
            elif x==2:
                hasil_label.append("Netral")
            else:
                hasil_label.append("Non Cyberbullying")
        # excel_exporter.export(self.username,self.comments,self.image,self.valid,self.result,url)
        source=[]
        for x in range(len(hasil_label)):
            source.append(url)
        tuple = list(zip(source, hasil_label, self.comments, self.valid, self.username, self.image))
        self.driver.close()
        return tuple

#
# arif=ScrapePost()
# arif.login_page('https://www.instagram.com/p/CA1c8b4DIFA/','skyw.i','PassTemp123!')