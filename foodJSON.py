with open('india.json') as data_file:
    data = json.load(data_file)
lis = []
for i in data:
    name = i.keys()[0]
    foodName = i[name]['foodName'][0]
    '''
    force = i[name]['Force']
    level = i[name]['Level']
    rating = i[name]['Your Rating']
    pic_right = i[name]['pic_right']
    guide = '\n'.join(i[name]['guide'])
    equipment = i[name]['Equipment']
    link = i[name]['link']
    pic_left = i[name]['pic_left']
    sport = i[name]['Sport']
    type_ = i[name]['Type']
    mech_type = i[name]['Mechanics Type']
    dic = json.loads(json.dumps({'name':name,'muscles_worked':muscle_worked,'force':force,'rating':rating,'level':level,'pic_right':pic_right,'mech_type':mech_type,'equipment':equipment,'link':link,'pic_left':pic_left,'Sport':sport,'type':type_,'guide':guide},indent=4))
   '''
   print foodName
