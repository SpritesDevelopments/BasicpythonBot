TOKEN = ''

LOG_CHANNEL_ID = None

def get_log_channel_id():
    global LOG_CHANNEL_ID
    return LOG_CHANNEL_ID

def set_log_channel_id(channel_id):
    global LOG_CHANNEL_ID
    LOG_CHANNEL_ID = channel_id
