from firebase_admin import credentials, firestore, initialize_app
import pandas

cred = credentials.Certificate('ntpu-all-star-firebase-adminsdk-yq6fs-cda9dd2d3d.json')
initialize_app(cred)
db = firestore.client()


with pandas.ExcelWriter('result.xlsx') as writer:
    doc_ref = db.collection(u'basketball').document(u'male').collection(u'candidates')
    doc = doc_ref.get()
    d_list = []
    for d in doc:
        d_list.append(d.to_dict())
    df = pandas.DataFrame(eval(str(d_list)))
    df.sort_values(by='voteCount', inplace=True, ascending=False)
    df.to_excel(writer, sheet_name='男籃', columns=['username', 'voteCount', 'photoURL', 'introduction'])

    doc_ref = db.collection(u'basketball').document(u'female').collection(u'candidates')
    doc = doc_ref.get()
    d_list = []
    for d in doc:
        d_list.append(d.to_dict())
    df = pandas.DataFrame(eval(str(d_list)))
    df.sort_values(by='voteCount', inplace=True, ascending=False)
    df.to_excel(writer, sheet_name='女籃', columns=['username', 'voteCount', 'photoURL', 'introduction'])

    doc_ref = db.collection(u'volleyball').document(u'female').collection(u'edgeline')
    doc = doc_ref.get()
    d_list = []
    for d in doc:
        d_list.append(d.to_dict())
    df = pandas.DataFrame(eval(str(d_list)))
    df.sort_values(by='voteCount', inplace=True, ascending=False)
    df.to_excel(writer, sheet_name='女排邊線', columns=['username', 'voteCount', 'photoURL', 'introduction'])

    doc_ref = db.collection(u'volleyball').document(u'female').collection(u'setter')
    doc = doc_ref.get()
    d_list = []
    for d in doc:
        d_list.append(d.to_dict())
    df = pandas.DataFrame(eval(str(d_list)))
    df.sort_values(by='voteCount', inplace=True, ascending=False)
    df.to_excel(writer, sheet_name='女排舉球', columns=['username', 'voteCount', 'photoURL', 'introduction'])

    doc_ref = db.collection(u'volleyball').document(u'male').collection(u'edgeline')
    doc = doc_ref.get()
    d_list = []
    for d in doc:
        d_list.append(d.to_dict())
    df = pandas.DataFrame(eval(str(d_list)))
    df.sort_values(by='voteCount', inplace=True, ascending=False)
    df.to_excel(writer, sheet_name='男排邊線', columns=['username', 'voteCount', 'photoURL', 'introduction'])

    doc_ref = db.collection(u'volleyball').document(u'male').collection(u'setter')
    doc = doc_ref.get()
    d_list = []
    for d in doc:
        d_list.append(d.to_dict())
    df = pandas.DataFrame(eval(str(d_list)))
    df.sort_values(by='voteCount', inplace=True, ascending=False)
    df.to_excel(writer, sheet_name='男排舉球', columns=['username', 'voteCount', 'photoURL', 'introduction'])

    doc_ref = db.collection(u'volleyball').document(u'male').collection(u'spiker')
    doc = doc_ref.get()
    d_list = []
    for d in doc:
        d_list.append(d.to_dict())
    df = pandas.DataFrame(eval(str(d_list)))
    df.sort_values(by='voteCount', inplace=True, ascending=False)
    df.to_excel(writer, sheet_name='男排快攻', columns=['username', 'voteCount', 'photoURL', 'introduction'])

    doc_ref = db.collection(u'volleyball').document(u'male').collection(u'libero')
    doc = doc_ref.get()
    d_list = []
    for d in doc:
        d_list.append(d.to_dict())
    df = pandas.DataFrame(eval(str(d_list)))
    df.sort_values(by='voteCount', inplace=True, ascending=False)
    df.to_excel(writer, sheet_name='男排自由', columns=['username', 'voteCount', 'photoURL', 'introduction'])
