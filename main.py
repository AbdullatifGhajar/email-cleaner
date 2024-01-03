from email_service.EmailImporter import EmailImporter

if __name__ == "__main__":
    with EmailImporter() as email_importer:
        for email in email_importer.emails():
            print(email)
