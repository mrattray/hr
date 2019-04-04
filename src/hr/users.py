import subprocess
import sys
import pwd

from .helpers import user_names

def add_user(user_info):
    print(f"Adding a user with the name {user_info['name']}")
    try:
        subprocess.call(
            ['useradd', 
            "-p",
            user_info["password"],
            "-G",
            "i".join(user_info["groups"] or []),
            user_info["name"]
        ])
    except:
        print(f"Error adding user")
        sys.exit(1)

def update_user(user_info):
    print(f"Updating user with the name {user_info['name']}")
    try:
        subprocess.call(
            ['usermod'            
            "-p",
            user_info["password"],
            "-G",
            "i".join(user_info["groups"] or []),
            user_info["name"]
        ])
    except:
        print(f"Error updating user")
        sys.exit(1)

def remove_user(user):
    print(f"Removing a user with the name {user}")
    try:
        subprocess.call(
            ['userdel',
            '-r',
            user])
    except:
        print(f"Error removing user")
        sys.exit(1)

def sync(all_users):
    all_local_users = user_names()
    user_names = [user['name'] for user in all_users]
    for user in all_users:
        if user['name'] not in all_local_users:
            add_user(user)
        elif user['name'] in all_local_users:
            update_user(user)

    for user in all_local_users:
        if user not in user_names:
            remove_user(user)
        

