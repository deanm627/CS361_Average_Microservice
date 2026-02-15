import zmq

context = zmq.Context()

# Connect to server
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Sample data
nums = [1, 2.5, 5, 67, 33.4, 9.1, 0]
socket.send_json(nums)

# Print the response
response = socket.recv_json()
if response['code'] == 0:
    print(f"Average is: {response['avg']}")
else:
    print(f"An error occurred: {response['error']}")
