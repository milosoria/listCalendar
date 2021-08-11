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
