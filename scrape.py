from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/usr/local/bin/chromedriver", options=options)

driver.get("https://www.pokernow.club/games/sUjNoZXmgGYBCmzwbXZKhJ5Qt")
sleep(1)
players = {} 

while True:
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')

    new_players = {}

    player_info = soup.find_all('div', class_="table-player-infos-ctn")
    for player in player_info:
        name = player.find('p', class_='table-player-name').get_text()
        stack = player.find('p', class_='table-player-stack').get_text()

        if '+' in stack:
            to_add = stack.split('+')
            stack = int(to_add[0]) + int(to_add[1])
        else:
            stack = int(stack)

        new_players[name] = stack

    if players != new_players:
        players = new_players
        print(players)