import zmq
import statistics

# Establish server and attach to port
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def average(nums):
    try:
        avg = statistics.mean(nums)
    except Exception as e:
        return e, 1
    else:
        return round(avg, 2), 0

def median(nums):
    try:
        med = statistics.median(nums)
    except Exception as e:
        return e, 1
    else:
        return med, 0

while True:
    # Wait for request
    print("Listening on 5555")
    # Obtain message and print to screen
    data = socket.recv_json()
    average, average_code = average(data)
    median, median_code = median(data)
    if average_code == 0 and median_code == 0:
        results = {'avg': average, 'median': median, 'code': 0}
    elif average_code == 1:
        results = {'error': average, 'median': median, 'code': 1}
    else:
        results = {'average': average, 'error': median, 'code': 1}
    # Compose and send response
    socket.send_json(results)