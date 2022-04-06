
import string
string.whitespace
string.punctuation
blurt = "What the...!!?"
print(blurt.strip(string.punctuation))
prospector = "What in tarnation ...!!!?"
print(prospector.strip(string.whitespace + string.punctuation))
