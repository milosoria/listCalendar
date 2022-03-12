#!/usr/bin/env python3

# std
import datetime
import os.path
import sys
from collections import OrderedDict
from typing import Any

# third party modules
from dateutil.relativedelta import relativedelta

# google
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.errors import UnknownApiNameOrVersion


class Lister:
    def __init__(self, n_months: int,  format: str) -> None:
        self.scopes = ['https://www.googleapis.com/auth/calendar.readonly']
        self.months = {
            "01": "January",
            "02": "Febraury",
            "03": "March",
            "04": "April",
            "05": "May",
            "06": "June",
            "07": "July",
            "08": "August",
            "09": "September",
            "10": "October",
            "11": "November",
            "12": "December",
        }
        self.n_months = n_months
        self.format = format

    def authenticate(self) -> Any:
        creds = None
        root_dir = os.path.split(os.path.relpath(__file__))[0]
        token_path = os.path.join(root_dir, 'token.json')
        credentials_path = os.path.join(root_dir, 'credentials.json')

        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(
                token_path, self.scopes)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path, self.scopes)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open(token_path, 'w') as token:
                token.write(creds.to_json())
        try:
            service = build('calendar', 'v3', credentials=creds)
        except HttpError or UnknownApiNameOrVersion as e:
            sys.stdout.write(
                "An error ocurred when building service object: {e}\n".format(
                    e))
            exit(e)

        return service

    def call_api(self, service: Any) -> None:
        # Call the Calendar API
        time_now = datetime.datetime.utcnow()
        time_now_plus_month_offset = time_now + relativedelta(months=self.n_months)
        time_now_formatted = time_now.isoformat(
        ) + 'Z'  # 'Z' indicates UTC time

        events_result = service.events().list(
            calendarId='primary',
            timeMin=time_now_formatted,
            timeMax=time_now_plus_month_offset.isoformat() + 'Z',
            singleEvents=True,
            orderBy='startTime').execute()

        self.events = events_result.get('items', [])

    def write_events(self) -> None:
        def write_it(writer: Any) -> None:
            writer.write("Incoming Events:\n")
            hasEnd = False
            for key, infos in start_dict.items():
                if key.find("+") != -1:
                    startDate, endDate = key.split("+")
                    year, month, day = startDate.split("-")
                    eyear, emonth, eday = endDate.split("-")
                    hasEnd = True
                else:
                    year, month, day = key.split('-')
                writer.write(
                    f"\t* {day} of {self.months[month]} of {year}:\n"
                ) if not hasEnd else writer.write(
                    f"\t* {day} of {self.months[month]} of {year} until {eday} of {self.months[emonth]} of {eyear} :\n"
                )
                for info in infos:
                    writer.write(f"\t\t- [ ] '{info}'\n")
                hasEnd = False


        start_dict = OrderedDict()
        end_dict = OrderedDict()
        if self.events:
            for event in self.events:
                start = event['start'].get(
                    'dateTime', event['start'].get('date')).split("T")[0]

                end = event['end'].get('dateTime',
                                       event['end'].get('date')).split("T")[0]

                if start in start_dict.keys():
                    if end != start:
                        start = start + "+" + end
                    start_dict[start].append((event['summary']))
                else:
                    if end != start:
                        start = start + "+" + end
                    start_dict[start] = [event['summary']]

            if self.format != "list":
                file = open(f"events.{self.format}", "a")
                write_it(file)
                sys.stdout.write(
                    f"File events.{self.format} written in path {os.path.abspath(f'events.{self.format}')}\n"
                )
                file.close()
            else:
                write_it(sys.stdout)
        else:
            sys.stdout.write("No incoming events for the flags specified\n")
            exit(0)
