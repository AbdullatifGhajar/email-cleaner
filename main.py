from email_service.EmailManager import EmailManager

if __name__ == "__main__":
    with EmailManager() as email_importer:
        for email in email_importer.emails():
            print(email)
