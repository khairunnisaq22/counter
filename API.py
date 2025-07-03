from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/logreceiver', methods=['POST'])
def receive_log():
    data = request.json
    print("Log data received:", data)  
    
   
    with open("received_logs.txt", "a") as file:
        file.write(str(data) + "\n")

    return jsonify({"status": "success", "message": "Log received"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    

