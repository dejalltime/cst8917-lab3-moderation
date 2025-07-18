import logging, re, json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing message…")
    try:
        data = req.get_json()
    except ValueError:
        return func.HttpResponse("Invalid JSON", status_code=400)

    html = data.get("message","")
    text = re.sub(r'<[^>]+>','', html).strip().lower()

    result = {
        "message": text,
        "teamId":   data.get("teamId"),
        "channelId":data.get("channelId"),
        "user":     data.get("user"),
        "messageId":data.get("messageId")
    }
    return func.HttpResponse(json.dumps(result),
                             status_code=200,
                             mimetype="application/json")
