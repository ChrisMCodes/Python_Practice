def format_duration(seconds):
    years = seconds // 31_536_000 
    seconds = seconds % 31_536_000
    days = seconds // 86_400
    seconds = seconds % 86_400
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    
    iter_time = [years, days, hours, minutes, seconds]
    time_names = ["year", "day", "hour", "minute", "second"]
    
    message_len = 0
    for i in iter_time:
        if i > 0:
            message_len += 1
            
    message = str()
    idx = 0
    
    for i in iter_time:
        if i > 0:
            message = message + str(i) + " {}".format(time_names[idx])
            message_len -= 1
            if i > 1:
                message += "s"
            if message_len > 1:
                message += ", "
            if message_len == 1:
                message += " and "
        idx += 1    
    return message
