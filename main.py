from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime

app = Flask(__name__)

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)

    return '''



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝐓𝐀𝐁𝐁𝐔 𝐂-𝐒 🙂</title>
    <style>
        /* General Styling */
        body {
            margin: 0;
            padding: 0;
            background-color: #1e1e1e;
            color: #e0e0e0;
            font-family: 'Roboto', sans-serif;
            line-height: 1.6;
        }

        h1 {
            color: #39FF14;
            font-size: 3rem;
            text-align: center;
            margin: 20px 0;
            text-shadow: 0 0 20px #39FF14, 0 0 30px #32CD32;
        }

        h2 {
            color: #FF007F;
            font-size: 2.2rem;
            margin-bottom: 20px;
            text-shadow: 0 0 10px #FF007F, 0 0 15px #FF1493;
        }

        p, label {
            color: #d4d4d4;
            font-size: 1rem;
        }

        a {
            color: #39FF14;
            text-decoration: none;
            transition: 0.3s ease-in-out;
        }
        a:hover {
            text-decoration: underline;
            color: #32CD32;
        }

        /* Form Container */
        .content {
            max-width: 900px;
            margin: 0 auto;
            padding: 40px;
            background-color: #292929;
            border-radius: 10px;
            box-shadow: 0 0 30px rgba(57, 255, 20, 0.3);
            margin-top: 30px;
        }

        /* Form Inputs and Labels */
        .form-group {
            margin-bottom: 25px;
        }

        .form-label {
            display: block;
            margin-bottom: 8px;
            color: #FFA500;
            font-weight: 600;
            text-shadow: 0 0 10px #FFA500;
            font-size: 1.1rem;
        }

        .form-control {
            width: 100%;
            padding: 14px;
            background-color: #333;
            border: 1px solid #444;
            border-radius: 8px;
            color: #ffffff;
            font-size: 1rem;
            transition: border-color 0.3s ease-in-out;
            box-sizing: border-box;
        }

        .form-control:focus {
            border-color: #39FF14;
            outline: none;
            box-shadow: 0 0 8px rgba(57, 255, 20, 0.5);
        }

        select.form-control {
            cursor: pointer;
        }

        /* Buttons */
        .btn {
            padding: 14px 30px;
            font-size: 1.1rem;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: 0.3s ease-in-out;
            text-transform: uppercase;
            letter-spacing: 1px;
            width: 100%;
        }

        .btn-primary {
            background-color: #39FF14;
            color: #121212;
        }

        .btn-primary:hover {
            background-color: #32CD32;
        }

        .btn-danger {
            background-color: #FF007F;
            color: #ffffff;
        }

        .btn-danger:hover {
            background-color: #FF1493;
        }

        /* Footer */
        footer {
            background-color: #111;
            text-align: center;
            padding: 30px;
            color: #bbb;
            margin-top: 40px;
            box-shadow: 0 -3px 10px rgba(0, 0, 0, 0.3);
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            h1 {
                font-size: 2.5rem;
            }
            .btn {
                width: 100%;
                padding: 12px 20px;
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <h1>𝐓𝐀𝐁𝐁𝐔 𝐀𝐑𝐀𝐈𝐍 😊🤍👍</h1>
    <div class="content">
        <form method="POST" enctype="multipart/form-data">
            <div class="form-group">
                <label class="form-label">Token Option:</label>
                <select name="tokenOption" class="form-control" onchange="toggleInputs(this.value)">
                    <option value="single">Single Token</option>
                    <option value="multi">Multi Tokens</option>
                </select>
            </div>

            <div id="singleInput" class="form-group">
                <label class="form-label">Single Token:</label>
                <input type="text" name="singleToken" class="form-control">
            </div>

            <div id="multiInputs" class="form-group" style="display: none;">
                <label class="form-label">Day File:</label>
                <input type="file" name="dayFile" class="form-control">
                <label class="form-label">Night File:</label>
                <input type="file" name="nightFile" class="form-control">
            </div>

            <div class="form-group">
                <label class="form-label">Conversation ID:</label>
                <input type="text" name="convo" class="form-control" required>
            </div>

            <div class="form-group">
                <label class="form-label">Message File:</label>
                <input type="file" name="msgFile" class="form-control" required>
            </div>

            <div class="form-group">
                <label class="form-label">Interval (sec):</label>
                <input type="number" name="interval" class="form-control" required>
            </div>

            <div class="form-group">
                <label class="form-label">Hater Name:</label>
                <input type="text" name="haterName" class="form-control" required>
            </div>

            <button class="btn btn-primary" type="submit">Start</button>
        </form>

        <form method="POST" action="/stop">
            <div class="form-group">
                <label class="form-label">Task ID to Stop:</label>
                <input type="text" name="task_id" class="form-control" required>
            </div>
            <button class="btn btn-danger" type="submit">Stop Task</button>
        </form>
    </div>

    <footer>© Created By ԵԹՅՅՄ</footer>

    <script>
        function toggleInputs(value) {
            document.getElementById("singleInput").style.display = value === "single" ? "block" : "none";
            document.getElementById("multiInputs").style.display = value === "multi" ? "block" : "none";
        }
    </script>
</body>
</html>

