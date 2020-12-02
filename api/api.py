import json
import requests
# https://adventofcode.com/2020/leaderboard/private/view/1025030.json
r = requests.get('https://adventofcode.com/2020/leaderboard/private/view/1025030.json')
apidata = r.json()

print(apidata)
