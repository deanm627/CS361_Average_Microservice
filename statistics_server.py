from statistics import StatisticsError

import zmq
import statistics

# Establish server and attach to port
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def average(nums):
    try:
        avg = statistics.mean(nums)
    except TypeError as e:
        return "Error computing average. " + str(e), 1
    except StatisticsError as e:
        return "Error computing average: " + str(e), 1
    except Exception as e:
        return "An unexpected error occurred: " + str(e), 1
    else:
        return round(avg, 2), 0

def median(nums):
    try:
        med = statistics.median(nums)
    except TypeError as e:
        return "Error computing median: " + str(e), 1
    except StatisticsError as e:
        return "Error computing median: " + str(e), 1
    except Exception as e:
        return "An unexpected error occurred: " + str(e), 1
    else:
        return med, 0

while True:
    # Wait for request
    print("Listening on 5555")
    # Get data from client
    data = socket.recv_json()
    # Compute average and median
    avg, average_code = average(data)
    med, median_code = median(data)
    # Compose response
    if average_code == 0 and median_code == 0:
        results = {'avg': avg, 'median': med, 'code': 0}
    else:
        results = {'avg': avg, 'median': med, 'code': 1}
    # Send response
    socket.send_json(results)