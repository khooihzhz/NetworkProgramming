from rocketchat_API.rocketchat import RocketChat
from pprint import pprint
from datetime import datetime

def main():
    # login with credentials and url here
    user = ''
    password = ''
    url = ''

    rocket = RocketChat(user, password, server_url=url)

    # room to get data from
    room_id = 'GENERAL'

    # get total message count
    total_messages_in_chat = rocket.channels_counters(room_id=room_id).json()['msgs']
    print('------Messages Count------')
    print(f'Current Total Message Count: {total_messages_in_chat}\n')

    # get user status
    total_members = rocket.channels_members(room_id=room_id).json()['members']

    user_status = {
        'online': 0,
        'away': 0,
        'busy': 0,
        'offline':0
    }
    for member in total_members:
        member_status = member['status']
        # add count if status matches
        if member_status in user_status:
            user_status[member_status] += 1

    print ("------User Status------") 
    for status, count in user_status.items():
        print(f'{status} : {count}')
        
    print()
    # function for user input
    while True:
        message = input("Enter Message: ")
        # user quit program
        if message.lower() == 'quit':   # ensure that any form of 'quit' will trigger
            print('quiting program.......')
            break
        else:
            # POST MESSAGE
            # get timestamp
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S -- ")
            rocket.chat_post_message(text=timestamp+message, room_id=room_id)


if __name__ == '__main__':
    main()
