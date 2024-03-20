from flask import Flask, request, jsonify

app = Flask(__name__)

WINDOW_SIZE = 10  # Maximum number of values in the window
window_state = []  # List to store window elements

@app.route("/calculate", methods=["POST"])
def calculate_average():
  data = request.get_json()
  number = data.get("number")
  if number is None:
    return jsonify({"error": "Missing number in request body"}), 400

  # Add number to window and calculate average if window is full
  if len(window_state) < WINDOW_SIZE:
    window_state.append(number)
  else:
    window_state.pop(0)  # Remove oldest number
    window_state.append(number)
  average = sum(window_state) / len(window_state)

  return jsonify({"average": average})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
