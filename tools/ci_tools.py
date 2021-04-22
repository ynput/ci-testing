from optparse import OptionParser
import re
import sys


def release_type(filename):
    with open(filename,'r+') as f:
        text = f.read()
        regex_minor = ["feature/", "(feat)"]
        regex_patch = ["bugfix/", "fix/", "(fix)"]
        for reg in regex_minor:
            if re.search(reg, text):
                return "minor"
        for reg in regex_patch:
            if re.search(reg, text):
                return "patch"
        return "skip"


def file_regex_replace(filename, regex, version):
    with open(filename,'r+') as f:
        text = f.read()
        text = re.sub(regex, version, text)
        print(20*"#")
        print(f"NEW VERSION {version} INSERTED into {filename}")
        f.seek(0)
        f.write(text)
        f.truncate()

def bump_file_versions(version):
    filename = "./openpypeCItest/version.py"
    regex = "(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(-((0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(\.(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(\+([0-9a-zA-Z-]+(\.[0-9a-zA-Z-]+)*))?"
    file_regex_replace(filename, regex, version)

    # bump pyproject.toml
    filename = "pyproject.toml"
    regex = "version = \"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(-((0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(\.(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(\+([0-9a-zA-Z-]+(\.[0-9a-zA-Z-]+)*))?\" # OpenPype"
    replace_version = f"version = \"{version}\" # OpenPype"
    file_regex_replace(filename, regex, replace_version)


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("--logfile", dest="logfile", action="store",
                      type="string", help="read data from FILENAME")
    parser.add_option("--version", dest="version",
                      action="store", type="string")

    (options, args) = parser.parse_args()

    if options.logfile:
        print(release_type(options.logfile))

    if options.version:
        print(bump_file_versions(options.version))


if __name__ == "__main__":
    main()