from icecream import ic
from langdetect import detect

from email_service import Email, EmailManager
from llama.LlamaModel import LlamaModel

NUMBER_OF_EMAILS_TO_ANALYSE = 1


def preprocess_text(text: str):
    # remove '\n' and '\r'
    return text.replace("\n", " ").replace("\r", " ")


def is_english(email: Email):
    try:
        lang = detect(email.body)
        return lang == "en"
    except Exception:
        return False  # If the language is not detectable, assume it's not English


if __name__ == "__main__":
    with EmailManager() as email_manager:
        for email in email_manager.emails():
            body = preprocess_text(email.body)
            ic(body)
            ic(LlamaModel().generate_response_with_context())
            break
