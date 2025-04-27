# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

Aside from the functionality that was required to pass Boot.dev tests also added the following:

- Folder input possibility - If a folder is provided instead of a file, the script will look for ".txt" files in the specified folder and analyze all of them

- Somewhat graceful handling of exceptions (specific handling of FileNotFoundError, generally printing the exception message otherwise)
