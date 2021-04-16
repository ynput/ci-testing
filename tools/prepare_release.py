import re
import sys

def file_regex_replace(filename, regex, version):
    with open(filename,'r+') as f:
        text = f.read()
        text = re.sub(regex, version, text)
        print(20*"#")
        print(f"NEW VERSION INSERTED into {filename}")
        print(text)
        f.seek(0)
        f.write(text)
        f.truncate()

# bump version.py
filename = "./openpypeCItest/version.py"
regex = "(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(-((0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(\.(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(\+([0-9a-zA-Z-]+(\.[0-9a-zA-Z-]+)*))?"
version = sys.argv[1]
file_regex_replace(filename, regex, version)

# bump pyproject.toml
filename = "pyproject.toml"
regex = "version = \"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(-((0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(\.(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(\+([0-9a-zA-Z-]+(\.[0-9a-zA-Z-]+)*))?\" # OpenPype"
version = f"version = \"{sys.argv[1]}\" # OpenPype"
file_regex_replace(filename, regex, version)