import pandas as pd
from handleGoogle import uploadCandidates, getSheet

volleyballMap = {
    '舉球員': 'setter',
    '邊線攻擊手': 'edgeline',
    '中間手': 'spiker',
    '自由球員': 'libero'
}

getSheet()

# 女籃
print('Handling basketball girl.')
df = pd.read_excel('bg.xlsx', usecols=['姓名', '系級', '學號', '背號', '自我介紹', '能認出本人的照片'])
for row in range(df.shape[0]):
    row_data = df.iloc[row]
    player = {}
    player['name'] = row_data['姓名']
    player['photoURL'] = str(row_data['能認出本人的照片']).removeprefix('https://drive.google.com/open?id=')
    player['introduction'] = row_data['自我介紹']
    player['grade'] = row_data['系級']
    player['back_number'] = int(row_data['背號'])

    uploadCandidates(player, 'female', 'basketball', '')
print('Basketball girl done.-----------------')

# 排球
print('Handling volleyball.')
df = pd.read_excel('v.xlsx', usecols=['姓名', '排球水水還是暖男呢？', '系級', '報名的位置(女生)', '報名的位置(男生)', '自我介紹~要用心打喔', '大頭貼 (最帥最好看的那張)'])
for row in range(df.shape[0]):
    row_data = df.iloc[row]
    player = {}
    player['name'] = row_data['姓名']
    player['photoURL'] = str(row_data['大頭貼 (最帥最好看的那張)']).removeprefix('https://drive.google.com/open?id=')
    player['introduction'] = row_data['自我介紹~要用心打喔']
    player['grade'] = row_data['系級']
    if row_data['排球水水還是暖男呢？'] == '男排':
        role = volleyballMap[row_data['報名的位置(男生)']]
        uploadCandidates(player, 'male', 'volleyball', role)
    else:
        role = volleyballMap[row_data['報名的位置(女生)']]
        uploadCandidates(player, 'female', 'volleyball', role)
print('Volleyball girl done.-----------------')

# 男籃
print('Handling basketball boy.')
df = pd.read_excel('bb.xlsx', usecols=['姓名', '系級／學號', '自我介紹', '大頭照'])
for row in range(df.shape[0]):
    row_data = df.iloc[row]
    player = {}
    player['name'] = row_data['姓名']
    player['photoURL'] = str(row_data['大頭照']).removeprefix('https://drive.google.com/open?id=')
    player['introduction'] = row_data['自我介紹']
    player['grade'] = row_data['系級／學號']
    uploadCandidates(player, 'male', 'basketball', '', )
print('Basketball boy done.-----------------')
