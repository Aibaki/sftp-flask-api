from flask import Flask, request
import subprocess
import json

app = Flask(__name__)
uid = 1003

@app.route("/create_user", methods=['POST'])
def create_user():
    """
        Method to run a server-side script to create a user using payload information

        :returns Response from Server Script Call
    """
    global uid
    
    credentials = request.get_json(request.data)
    username = credentials['credentials']['username']
    password = credentials['credentials']['password']

    # Primary key in db; incremental
    # gid=0 for root gid=100 for normal users
    uid_current = uid
    gid = 100
    path = credentials['sftp_details']['path']

    # The above variables form part of the arguments used by the script to create a user
    arguments = username + ':' + password + ':' + str(uid) + ":" + str(gid) + ':' + path

    # Calling the server-side script in this format: create-sftp-user username:Password:uid:gid:upload-folder
    ret = subprocess.call("create-sftp-user.py " + arguments, shell=True)
    uid+=1
    return str(uid)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
