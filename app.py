from otomate import ScrapePost as instagram
import os

if __name__ == '__main__':
    print("login required")
    username = input("Input Your Username : ")
    password = input("Input Your Password : ")
    url = input("Input the url ")
    print(f'your username is {username} and your password is {password}')
    print("running scraping.......")
    instagram().login_page(url=url,username=username,password=password)