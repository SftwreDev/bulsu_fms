import base64

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def email_verify_template(link):
    html = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
            </head>
            <body>
                <div class="flex items-center justify-center min-h-screen p-5 bg-blue-100 min-w-screen">
                    <div class="max-w-xl p-8 text-center text-gray-800 bg-white shadow-xl lg:max-w-3xl rounded-3xl lg:p-12">
                        <h3 class="text-2xl">Thanks for signing up for Barangay Natatas Online Services!</h3>
                        <div class="flex justify-center">

                        <p>To continue using our system, please click the button below to verify</p>
                        <div class="mt-4">
                            <a href="{link}"  class="px-2 py-2 text-blue-200 bg-blue-600 rounded button button1"
                            style="background-color: #6366f1;border: none;color: white;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;cursor: pointer;padding: 10px 24px;">Click to Verify Email</a>
                        </div>
                    </div>
                </div>
            </body>
        </html>
    """.format(link=link)
    return html


def reset_password_template(link):
    html = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet">
            </head>
            <body>
                <div class="flex items-center justify-center min-h-screen p-5 bg-blue-100 min-w-screen">
                    <div class="max-w-xl p-8 text-center text-gray-800 bg-white shadow-xl lg:max-w-3xl rounded-3xl lg:p-12">
                        <h3 class="text-2xl">To reset your password, click the button below.</h3>
                        <div class="flex justify-center">
                        <div class="mt-4">
                            <a href="{link}"  class="px-2 py-2 text-blue-200 bg-blue-600 rounded button button1"
                            style="background-color: #6366f1;border: none;color: white;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;margin: 4px 2px;cursor: pointer;padding: 10px 24px;">Reset my password</a>
                        </div>
                    </div>
                </div>
            </body>
        </html>
    """.format(link=link)
    return html


def send_email_verify(email):
    encoded_email = encode_base64(email)
    link = f"https://onlineservicesapp.up.railway.app/verify-email/{encoded_email}"
    message = Mail(
        from_email='natatas.tanauan@gmail.com',
        to_emails=email,
        subject='Online Services | Email Verification',
        html_content=email_verify_template(link))
    try:
        sg = SendGridAPIClient(
            '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')
        sg.send(message)
    except Exception as e:
        print(e.message)


def send_reset_link(email):
    encoded_email = encode_base64(email)
    link = f"https://onlineservicesapp.up.railway.app/reset-password/{encoded_email}"
    message = Mail(
        from_email='natatas.tanauan@gmail.com',
        to_emails=email,
        subject='Online Services | Password Reset',
        html_content=reset_password_template(link))
    try:
        sg = SendGridAPIClient(
            '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')
        sg.send(message)
    except Exception as e:
        print(e.message)


def encode_base64(str):
    str_bytes = str.encode('ascii')
    base64_bytes = base64.b64encode(str_bytes)
    base64_str = base64_bytes.decode("ascii")
    return base64_str


def decode_base64(str):
    base64_bytes = str.encode("ascii")
    decoded_string_bytes = base64.b64decode(base64_bytes)
    decoded_string = decoded_string_bytes.decode("ascii")
    return decoded_string
