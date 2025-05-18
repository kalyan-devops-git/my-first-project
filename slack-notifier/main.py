import functions_framework
import requests

@functions_framework.http
def notify_slack(request):
    webhook_url = 'https://hooks.slack.com/services/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'
    message = request.get_json().get('message', 'Deployment completed!')
    
    payload = {'text': message}
    response = requests.post(webhook_url, json=payload)
    
    return {'status': response.status_code}