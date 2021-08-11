## listCalendar
List your incoming events and write them into a TODO.md to use as a checklist.
Every call to the command will overwrite the file and erase the previous list.

#Installation

- Install the dependencies to run the program

```sh
pip install
```
- Create a credentials file to be allow the program to retreive your events, name it credentials.json
and place it in listCalendar directory (credentials)[https://developers.google.com/workspace/guides/create-credentials].

- When you use listCalendar for the first time, a OAauth will be needed, follow the instructions prompted and your tokens
will be saved into a token.json file. When the tokens expire, you will need to repeat the authentification process.

#To use it as a terminal command

- Make the script an executable

```sh
chmod +x listCalendar.py
```

- Finally, install it in your path, wether placing on your bin directory (usually /usr/bin/) or creating a folder in your $HOME directory, placing the script in it and adding the path to $PATH.

Fix credentials file hardcoded and path to write TODO could be permanent:
    Traceback (most recent call last):
      File "/home/camilo/.local/bin/listcalendar", line 11, in <module>
        load_entry_point('listcalendar', 'console_scripts', 'listcalendar')()
      File "/home/camilo/projects/listcalendar/listcalendar/__init__.py", line 28, in main
        flow = InstalledAppFlow.from_client_secrets_file(
      File "/home/camilo/.local/lib/python3.8/site-packages/google_auth_oauthlib/flow.py", line 203, in from_client_secrets_
    file
        with open(client_secrets_file, "r") as json_file:
    FileNotFoundError: [Errno 2] No such file or directory: 'credentials.json'
