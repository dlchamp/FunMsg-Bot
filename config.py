class Config:
    '''Bot configuration'''

    # provie a min and max number of messages before the
    # bot submits the "fun" message
    active_msg_count = (5,10) # (min #, max #)

    # id of the channel to monitor
    monitor_channel_id = 1234567890

    # number of seconds after last message to "expire" activity counter
    expires = 60 # must be in seconds