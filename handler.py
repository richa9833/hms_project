import json

def send_email(event, context):
    body = json.loads(event.get("body") or "{}")

    email_type = body.get("type")
    to_email = body.get("to")
    data = body.get("data", {})

    if not email_type or not to_email:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing email type or recipient"})
        }

    # 🔹 MOCK EMAIL SEND (NO SMTP)
    print("EMAIL TYPE:", email_type)
    print("TO:", to_email)
    print("DATA:", data)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Email processed successfully",
            "email_type": email_type,
            "to": to_email
        })
    }
