from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

twitter_url = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXIST Twitter 
(name TEXT, retrieved INTEGER, friends INTEGER)''')

#Ignore ssl certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter a Twitter account, or Quit: ')
    if(acct == 'Quit'): break
    if (len(act) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print('No un retrieved accounts found')
            continue
    url = twurl.argumnt(twitter_url, {'screen_name':acct, 'count':'5'})
    print('Retrieving', url)
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.header())

    print('Remaining', headers['x--rate-limit-remaining'])
    js = json.loads(data)

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE NAME = ?',(acct, ))

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend,))

        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ? ',(count+1, friend))
        except:
            cur.execute('INSERT INTO Twitter (name, retrieved, friends) VALUES (?, 0, 1)', (friend,))

    print('New accounts= ',countnew, 'revisited= ', countold)
    conn.commit()
cur.close()

