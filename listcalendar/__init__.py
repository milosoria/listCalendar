#!/usr/bin/env python3
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    root_dir = os.path.split(os.path.relpath(__file__))[0]
    token_path = os.path.join(root_dir,'token.json')
    credentials_path = os.path.join(root_dir,'credentials.json')
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.\n Exiting program')
        exit(0)

    start_dict = {}
    valid_path = False

    while not valid_path:
        todo_path = input('Path to write TODO.md (use ~ or equivalent): ').split('/')
        todo_path = os.path.expanduser(os.path.join(*todo_path))
        if os.path.isdir(todo_path):
            valid_path = True 
        else:
            print('Please enter a valid path')

    with open(f'{todo_path}/TODO.md', 'w') as f:
        f.write("##TODO :feelsgood: :\n\n")
        for event in events:
            start = event['start'].get('dateTime',
                    event['start'].get('date')).split("T")[0]
            if start in start_dict.keys():
                start_dict[start].append(event['summary'])
            else:
                start_dict[start] = [event['summary']]
        for key, summaries in start_dict.items():
            f.write(f"\t- Date {key}:\n\t\t")
            for summary in summaries:
                f.write(f"- [ ] :boom: Summary: {summary}\n")

if __name__ == '__main__':
    main()
