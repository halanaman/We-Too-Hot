from libdw import pyrebase

dburl = "https://what-the-hack-2022-default-rtdb.asia-southeast1.firebasedatabase.app/"
email = "test1@test123.com"
password = "testing"
apikey = "AIzaSyDGUnEQH9BNpPHWa46602PvfRlH8aonVzM"
authdomain = dburl.replace("https://","")

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()
user = auth.refresh(user['refreshToken'])

def get_receipt(rfid):
    userdata = db.child(rfid).get(user['idToken'])
    return userdata.val()

def set_receipt(rfid,userdata):
    db.child(rfid).set(userdata, user['idToken'])
