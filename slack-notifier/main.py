import functions_framework
import requests
from flask import abort

@functions_framework.http
def slack_notifier(request):
    webhook_url = 'https://hooks.slack.com/services/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'
    try:
        data = request.get_json(silent=True)
        message = data.get('message', 'Deployment completed!') if data else 'Deployment completed!'
    except Exception:
        message = 'Deployment completed!'

    payload = {'text': message}
    response = requests.post(webhook_url, json=payload)

    if response.status_code != 200:
        abort(500, f"Slack webhook failed: {response.text}")

    return {'status': response.status_code}