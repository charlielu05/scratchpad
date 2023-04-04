from datetime import datetime
from dataclasses import dataclass,field

@dataclass(order=True)
class trafficCount:
    sort_index: int = field(init=False, repr=False)
    
    time: datetime
    count: int
    
    def __post_init__(self):
        # sort by count
        self.sort_index = self.count

# read lines
with open('test-input.txt') as f:
    lines = f.readlines()
    
# pre-processing
dt = [entry.split() for entry in lines]

def convert_to_data(input: list[str,str]):
    return trafficCount(time = datetime.fromisoformat(input[0]) ,
                        count = int(input[1]))

# convert to data structure
data = [convert_to_data(x) for x in dt]

def return_total_cars(data = list[trafficCount])->int:
    return sum(tc.count
               for tc
               in data)
    
# sum of cars
total_cars = return_total_cars(data)
print(f"Total cars seen: {total_cars}")

# sum of cars for day
def day_sum(inputs: list[trafficCount]):
    output_dict = {}
    
    for input in inputs:
        date_string = input.time.strftime('%Y-%m-%d') 
        total = output_dict.get(date_string, 0) + input.count
        output_dict[date_string] = total
        
    return output_dict

total_cars_per_day = day_sum(data)

print("Date sum:")
for date, count in total_cars_per_day.items():
    print(date, count)

def return_top_three_half_hours(data: list[trafficCount])-> list[trafficCount]:
    return sorted(data, reverse=True)[:3]

# the top 3 half hours with most cars
top_3 = return_top_three_half_hours(data)

print("Top 3 half hours with most cars:")
for record in top_3:
    print(record.time.isoformat(), record.count)
    
# the 1.5 hours periods with least cars (3 contiguous half hour records)
# compare current to 2 idx ahead, if dif is not 1 hour, skip to 1 idx ahead
# else sum current to 2 idx ahead, compare to current least, if lower then overwrite else move 1 idx up
def least_cars_ninety_mins(inputs: list[trafficCount]):
    least_cars = float('inf')
    least_cars_timestamps = None
    
    for i in range(len(inputs) - 2):
        if inputs[i+2].time.timestamp() - inputs[i].time.timestamp() == 60 * 60:
            if (total_cars_in_ninety_mins := sum(tc.count for tc in inputs[i:i+3]))  < least_cars:
                least_cars = total_cars_in_ninety_mins
                least_cars_timestamps = list(tc.time.isoformat() for tc in inputs[i:i+3])
                
    return least_cars_timestamps, least_cars

print("1.5 hour period with least cars")
print(least_cars_ninety_mins(data))