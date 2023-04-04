from traffic import convert_to_data, trafficCount, return_total_cars, day_sum, least_cars_ninety_mins
import datetime

MOCK_INPUT = ['2021-12-01T05:00:00', '5']
MOCK_DATA = [trafficCount(time=datetime.datetime(2021, 12, 1, 5, 0), count=5),
            trafficCount(time=datetime.datetime(2021, 12, 1, 5, 30), count=2),
            trafficCount(time=datetime.datetime(2021, 12, 1, 6, 0), count=3),
            trafficCount(time=datetime.datetime(2021, 12, 2, 6, 0), count=3),
            trafficCount(time=datetime.datetime(2021, 12, 2, 5, 0), count=3),
            trafficCount(time=datetime.datetime(2021, 12, 3, 5, 30), count=1),
            trafficCount(time=datetime.datetime(2021, 12, 3, 6, 0), count=1),
            trafficCount(time=datetime.datetime(2021, 12, 3, 6, 30), count=1),
            ]

def test_convert_to_data():
    assert convert_to_data(MOCK_INPUT) == trafficCount(time=datetime.datetime(2021, 12, 1, 5, 0), count=5)
    
def test_return_total_cars():
    assert return_total_cars(MOCK_DATA) == 19
    
def test_day_sum():
    assert day_sum(MOCK_DATA) == {'2021-12-01': 10, '2021-12-02': 6, '2021-12-03': 3}

def test_least_cars_ninety_mins():
    assert least_cars_ninety_mins(MOCK_DATA) == (['2021-12-03T05:30:00', '2021-12-03T06:00:00', '2021-12-03T06:30:00'], 3)