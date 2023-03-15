
def get_hours_mins_secs(total_secs: int)->str:
    if total_secs == 0:
        return '0s'
    
    time_string = ''
   
    # hours
    hours = int(total_secs / 3600)
    if hours != 0:
        time_string += f"{str(hours)}h "
    
    # mins
    mins = int(total_secs / 60 % 60)
    if mins != 0:
        time_string += f"{str(mins)}m "
        
    # seconds
    seconds = int(total_secs % 60)
    if seconds != 0:
        time_string += f"{str(seconds)}s"
        
    return time_string.rstrip()

assert get_hours_mins_secs(3600) == "1h"
assert get_hours_mins_secs(3661) == '1h 1m 1s'