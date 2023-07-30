import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-d0bc0-default-rtdb.firebaseio.com/"
 
})
 
ref = db.reference('Students')
 
data={
    "321654":
    	{
            "name":"Ranoj Bhowmik",
            "major":"InfoTech",
            "starting_year":2020,
            "total_attendance":6,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2023-03-31 00:30:30"
        },
    "852741":
    	{
            "name": "Kasat Ishan Rajesh",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "S",
            "year": 4,
            "last_attendance_time": "2023-03-31 00:20:30"
        },
    "963852":
    	{
            "name": "Dhruv Umesh Sompura",
            "major": "Robotics",
            "starting_year": 2020,
            "total_attendance": 8,
            "standing": "S",
            "year": 4,
            "last_attendance_time": "2023-03-31 00:10:30"
    	}
}
 
for key, value in data.items():
	ref.child(key).set(value)
