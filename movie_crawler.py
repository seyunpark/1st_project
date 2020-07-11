import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler


bot = telegram.Bot(token = '1391450532:AAH649LkqFFd-EsLfcVv8NOs0uxX8hXNBSA')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200711'


def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')

    if (imax):
        imax = imax.find_parent('div', class_='col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=1102663612, text=title + ' IMAX 예매가 열렸습니다.')
        sched.pause()
    # else:
    #     bot.sendMessage(chat_id=1102663612, text='IMAX 예매가 아직 열리지 않았습니다.')


sched = BlockingScheduler()
sched.add_job(job_function,'interval',seconds=30)
sched.start()