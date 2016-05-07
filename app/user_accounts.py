import json
from app import *
from models import DBconn
from flask.ext.httpauth import HTTPBasicAuth
from flask import request
import re
import hashlib
from flask import jsonify
from spcalls import SPcalls


def store_user(data):

    # data = json.loads(request.data)
    # print "my data is ", data
    username = data['username']
    email = data['email']
    spcalls = SPcalls()
    print "spcall", spcalls

    check_username_exist = spcalls.spcall('check_username', (username,))

    check_email_exist = spcalls.spcall('check_mail', (email,))

    if check_username_exist[0][0] == 'OK' and check_email_exist[0][0] == 'OK':

        check_mail = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

        if check_mail is not None:
            fname = data['fname']
            mname = data['mname']
            lname = data['lname']
            password = data['password']
            role_id = data['role_id']

            if fname is not '' and mname is not '' and lname is not '' and username is not '' and password is not '' and role_id is not None:
                """
                PASSWORD HASHING
                source: https://pythonprogramming.net/password-hashing-flask-tutorial/

                import hashlib
                password = 'pa$$w0rd'
                h = hashlib.md5(password.encode())
                print(h.hexdigest())

                """
                pw_hash = hashlib.md5(password.encode())

                store_user = spcalls.spcall('store_user', (fname, mname, lname, username, pw_hash.hexdigest(), email, role_id), True)

                if store_user[0][0] == 'OK':
                    return jsonify({'status': 'OK', 'message': 'Successfully add ' + str(fname)})

                elif store_user[0][0] == 'Error':
                    return jsonify({'status': 'failed', 'message': 'failed to add ' + str(fname)})

                else:
                    return jsonify({'ERROR': '404'})

            else:
                return jsonify({'status': 'failed', 'message': 'Please input required fields!'})

        else:
            return jsonify({'status': 'failed', 'message': 'Invalid email input!'})

    elif check_username_exist[0][0] == 'EXISTED':
        return jsonify({'status ': 'failed', 'message': 'username already exist'})

    elif check_email_exist[0][0] == 'EXISTED':
        return jsonify({'status ': 'failed', 'message': 'email already exist'})

    else:
        return jsonify({'failed': 'failed'})

def show_user_id(id):
    spcalls = SPcalls()
    print "spcall", spcalls
    #when you have only one parameter you need to user "," comma.
    #example: spcals('show_user_id', (id,) )
    user_id = spcalls.spcall('show_user_id', (id,))
    data = [] 

    if len(user_id) == 0: 
        return jsonify({"status": "FAILED", "message": "No User Found", "data": []})

    else:
        r = user_id[0]
        data.append({"fname": r[0],
                     "mname":r[1],
                     "lname":r[2],
                     "email":r[3],
                     "username":r[4],
                     "role_id":r[5]})
        return jsonify({"status": "OK", "message": "OK", "data": data})





