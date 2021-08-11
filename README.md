## listCalendar
List your incoming events and write them into a TODO.md to use as a checklist.
Every call to the command will overwrite the file and erase the previous list.

## TODO:

- [ ] Fix credentials file hardcoded and path to write TODO could be permanent?
- [ ] Make the cli interactive to permit the user decide some implementation decisions
- [ ] Fix installation guide 

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

- Finally, install it in your path

```sh
pip install .
```
