# function that prints out time every 15 mins from 12:00 am to 11:45 pm

mins = ["00", "15", "30", "45"]
hours = ["12", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]
am_pm_list = ["am", "pm"]

def every_15_mins():
    for am_pm in am_pm_list:
        for hour in hours:
            for minute in mins:
                print(f"{hour}:{minute} {am_pm}")
        
if __name__ == "__main__":
    every_15_mins()