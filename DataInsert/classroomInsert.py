from Client.connectMongo import connectDB

collection = connectDB(Collection = "usableClassroom")
classroomInfo = {
    'className':'A101',
    'seat1':{
        'time1':{
            '是否被占用':False,
            '使用人员':''
        }
    },

    'seat2': {
        'time1': {
            '是否被占用':False,
            '使用人员':''
        }
    },

    'seat3': {
        'time1': {
            # '是否被占用': True,
            # '使用人员': '464555168'
            '是否被占用':False,
            '使用人员':''
        }
    },

    'seat4': {
        'time1': {
            '是否被占用': False,
            '使用人员': ''
        }
    }
}

# collection.insert_one(classroomInfo)
collection.insert_one(classroomInfo)