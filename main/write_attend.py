from librabries import *
def markAttendance(name):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(r"utils\attendance-372917-e9d66492d3da.json", scope)
    gc = gspread.authorize(credentials)
    spreadsheet_key = "1IQ72i3bkEhQ3xp1B-VcWN40vKUaemYrYAjbxIVbLL8M"
    d = {"NARLA_VENKATA_ANAND_SAI_KUMAR":[9921004497,2],"AMAN_KUMAR":[99210042123,2],"GAYAM_SWARNA_LATHA":[99210041988,2],"GUBBA_V_SESHA_SAI_KRISHNA_VINEETH":[9921004803,2],"KARE_GANESH_VARMA":[9921004322,1],"GOPAL_KUMAR":[9921008061,1],"ACHUTHA_ HEMASAI":[9921004005,1],"MAREM_UMA_MAHESWAR_REDDY":[9921004436,2],"MENTHEM_POOJITH_REDDY":[9921004449,2],"MIRYALA_LAKSHMI":[9921004920,1],"NALLAMEKALA_SYAM_SUNDAR":[9921004489,2],"PARIMAL_SESHA_SAI":[992100,1],"SABBINENI_JASWANTH":[9921004620,1],"YADAVALLI_NITHIN":[99210041304,1],"GORLA_SARATH_KUMAR":[99210041937,2],"BOBBA_KUMAR_SRINIVAS":[99210041514,1]}
    if 'Unknown' in name:
            name.remove('Unknown')
    p={}
    for i in name:
        if i in d:
            p[i]=d[i]
    print(p)
    lt=[]
    lt1=[]
    lt2=[]
    for i in p:
        lt.append(i)
        lt1.append(p[i][0])
        lt2.append(p[i][1])
    
    k={"Name":lt,"Reg-NO":lt1,"cluster":lt2}
    k = pd.DataFrame(k)
    today = date.today()
    dt = today.strftime("%m/%d/%y")
    print("wait 3 to 5 minutes for completion")
    d2g.upload(k, spreadsheet_key, dt, credentials=credentials, row_names=True)
    print("complete")
