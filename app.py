from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = '7940438226:AAEqvu1U5ezSSk6txF_lgEWy1n3SDBB1bGo'
CHAT_ID = '740590041'  # Замените на ID вашего чата

@app.route('/')
def index():
       return render_template('index.html')

@app.route('/send-file/<file_name>', methods=['POST'])
def send_file(file_name):
       file_path = f'files/{file_name}'  # Путь к вашему файлу
       with open(file_path, 'rb') as file:
           response = requests.post(
               f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument',
               data={'chat_id': CHAT_ID},
               files={'document': file}
           )
       return jsonify({'status': 'success' if response.ok else 'failure'})

if __name__ == '__main__':
       app.run(debug=True)
   
