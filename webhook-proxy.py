from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/subdomain/domain/com/<path:webhook_path>', methods=['POST'])
def translate_webhook(webhook_path):
    # Extract the webhook URL from the request
    webhook_url = request.url
    
    # Trigger the webhook by making a POST request to the URL in format B
    requests.post(f'https://subdomain.domain.com/{webhook_path}', json=request.json)
    
    return 'Webhook triggered successfully', 200

if __name__ == '__main__':
    app.run()