import requests
from time import sleep
url = "https://www.nhsportspage.com/news_article/show/1047982"

sess = requests.session()

sess.get(url)

formdata = {
    "utf8": "✓",
    "answer_id": "156070",
    "commit": "Vote"
}

while True:
    post_url = "https://www.nhsportspage.com/poll/cast_vote_element/37871"
    res = sess.post(post_url, data=formdata)
    if res.status_code == 200:
        text = res.text
        pos = text.find('Votes: ')
        print("Total %s" % text[pos:pos + 13])
    sleep(1)
