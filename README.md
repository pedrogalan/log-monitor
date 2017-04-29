# Log monitor
A very simple service that monitors your log files and sends you an email if something goes wrong.

## Configuration
There is a number of configuration parameters that are required by the service to work:

- `mail.smtp.host` - The SMTP server that will be used to send the e-mail alerts.
- `mail.smtp.username` - The username to authenticate in the SMTP server.
- `mail.smtp.password` - The password to authenticate in the SMTP server.
- `mail.receiver` - The e-mail address where the alerts will be sent.
- `mail.sender` - The sender of the alert e-mails.
- `log.file.locations` - The comma-separated list of locations of the log files to be monitored.

All these configuration parameters are mandatory and must be present in a file called `.log-monitor`, in the user's home directory. If the file does not exist it will be created with a set of default (useless) values.

## How does it work?
When the service is run, it simply reads the configured log files and looks for the string `[ERROR]`. If a log file contains the word, then the service sends the content of the file by email to the configured receiver. After this, it **deletes the content** of the file.

## What is the purpose
This is a personal project, and I use it to monitor some services that I have running in my NAS. I am too lazy to check the logs of these services in a regular basis, so I came up with this solution.

If one of the services fails, it will write a `[ERROR]` trace to its log file. Then, the _Log Monitor_ service, that runs every hour, will find the trace and send me an email with the content of the file. I decided to delete the content of the file after sending the email because I don't really need it anymore.
