users = [{'login':'frog4gloss','password':'4380g76f'},{'login':'firefox777','password':'93847rgd'}]
def new_user(sourse,data,lenght):
    data.get('login',None)
    data.get('password',None)
    assert data['login'] != None and data['password']!= None
    assert len(data['password']) < lenght
    for i in sourse: 
        assert data['login'] != i['login']
    sourse.append(data)
    return sourse
print(new_user(users,{'login':'lesya','password':'3987dhd@'},9))