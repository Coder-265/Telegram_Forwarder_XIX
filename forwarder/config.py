from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5163576596:AAGqoKPu-HHaHaRkcfXmVQEKAr22idArFzM"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001617036243,-1001787061183,-1001261550869]# List of chat id's to forward messages from.
    TO_CHATS = [-1001293630641]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
