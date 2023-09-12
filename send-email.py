from azure.communication.email import EmailClient
#adding the connection string from the azure communication service
connection_string = "endpoint=https://service-ra.unitedstates.communication.azure.com/;accesskey=ZrLEhs4yKkF9Q/PHhIn65SLH/wjOzlrQmXm4miaCzUtyp+0VX6HPY9l2iau35NTUV6JMRlM8lZtb5cQaaG6SUA=="
#provide sender address
sender_address = "DoNotReply@ee56ee44-f9d7-464f-a34e-f1c5b55bda27.azurecomm.net"
#provide receiver address
recipient_address = "chanjal.nc@rockwellautomation.com"

POLLER_WAIT_TIME = 10

message = {
    "senderAddress": sender_address,
    "recipients":  {
        "to": [{"address": recipient_address}],
    },
    "content": {
        "subject": "Test email from Python Sample",
        "plainText": "This is plaintext body of test email.",
        "html": "<html><h1>This is the html body of test email.</h1></html>",
    }
}

try:
    client = EmailClient.from_connection_string(connection_string)

    poller = client.begin_send(message);

    time_elapsed = 0
    while not poller.done():
        print("Email send poller status: " + poller.status())

        poller.wait(POLLER_WAIT_TIME)
        time_elapsed += POLLER_WAIT_TIME

        if time_elapsed > 18 * POLLER_WAIT_TIME:
            raise RuntimeError("Polling timed out.")

    if poller.result()["status"] == "Succeeded":
        print(f"Successfully sent the email (operation id: {poller.result()['id']})")
    else:
        raise RuntimeError(str(poller.result()["error"]))
    
except Exception as ex:
    print(ex)