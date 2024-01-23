import requests

i = 0
activites = []
while True:
    activity = requests.get('https://www.boredapi.com/api/activity').json()
    print(activity['activity'])
    user_answer = input('Yes/No ')
    if user_answer == 'Yes':
        i += 1
        activites.append(activity['activity'])
    if i == 3:
        print(activites)
        break