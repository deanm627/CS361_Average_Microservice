import zmq

context = zmq.Context()

# Connect to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Sample data
nums = [1, 5, 6, 7, 8, 10, 22]
socket.send_json(nums)

# Get and print the response
response = socket.recv_json()
if response['code'] == 0:
    print(f"Average: {response['avg']}")
    print(f"Median: {response['median']}")
else:
    print(f"An error occurred:")
    print(f"Average: {response['avg']}")
    print(f"Median: {response['median']}")
