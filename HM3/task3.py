import re
class RegexValidator(object):

    def __init__(self, regex, message):
        self.regex = regex
        self.massage = message


    def __call__(self, text):
        self.text = text
        if not re.match(self.regex, self.text):
            print (self.massage)
        else:
            print (self.text + ' is valid')

validator = RegexValidator(regex='^[A-Z]$', message='Ouch! your input is not valid!')
validator('F')
validator('q')
validator('$')

class EmailValidatior(RegexValidator):
    def __init__(self):
        RegexValidator.__init__(self, regex='[\w.]+[@][\w.][a-z]', message='Enter a valid email')

email_validator = EmailValidatior()
email_validator('jira@name.com')
email_validator('my@name.com')
email_validator('myname.com')
