import os
import requests
from dotenv import load_dotenv

from ies_mail_sender import send_mail
from ies_sms_sender import send_sms

load_dotenv()

# HTTP status code
http_status_codes = {
    400: "Bad Request - მომსახურება ვერ ამუშავებს მოთხოვნას.",
    401: "Unauthorized - ავტორიზაცია საჭიროა.",
    403: "Forbidden - მოთხოვნა აღიარებულია, მაგრამ უარის თქმა.",
    404: "Not Found - რესურსი ვერ მოიძებნა.",
    500: "Internal Server Error - ზოგადი შეცდომა.",
    503: "Service Unavailable - მომსახურება არ არის ხელმისაწვდომი.",
}

#magti url shemowmeba
def check_magti_url():
    magti_url = os.getenv('MAGTI_URL')  # Get the Magti URL from .env

    try:
        response = requests.get(magti_url, timeout=30)
        if not response.ok:
            status_description = http_status_codes.get(response.status_code, "უცნობი სტატუსი")
            message = f"Magti URL სტატუს კოდი: {response.status_code} - {status_description}."
            print_and_log(message)
            send_mail(emails, subject, message)
            send_sms(message=message, numbers=numbers)
   
    except Exception as ex:
        message = f"შეცდომა Magti URL არ მუშაობს: {str(ex)}"
        print_and_log(message)

if __name__ == "__main__":
    check_magti_url()