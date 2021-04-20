from optparse import OptionParser
import re
import sys


def release_type(filename):
    with open(filename,'r+') as f:
        text = f.read()
        regex_minor = ["feature/", "(feat)"]
        release = "patch"
        for reg in regex_minor if re.search(reg, text):
            release = "minor"

        return release


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

def bump_file_versions(version):
    filename = "./openpypeCItest/version.py"
    regex = "(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(-((0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(\.(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(\+([0-9a-zA-Z-]+(\.[0-9a-zA-Z-]+)*))?"
    version = sys.argv[1]
    file_regex_replace(filename, regex, version)

    # bump pyproject.toml
    filename = "pyproject.toml"
    regex = "version = \"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(-((0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(\.(0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(\+([0-9a-zA-Z-]+(\.[0-9a-zA-Z-]+)*))?\" # OpenPype"
    version = f"version = \"{sys.argv[1]}\" # OpenPype"
    file_regex_replace(filename, regex, version)


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("--logfile", dest="logfile", action="store",
                      type="string", help="read data from FILENAME")
    parser.add_option("--version",
                      action="store", type="string", dest="version")

    (options, args) = parser.parse_args()

    if options.logfile:
        print(release_type(options.logfile))

    if options.version:
        print(bump_file_versions(options.version))


if __name__ == "__main__":
    main()