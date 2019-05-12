#!/usr/bin/env python3
#
# ./generate_usernames.py users.txt

import collections
import sys


ID, FORENAME, MIDDLE_NAME, SURNAME, DEPARTMENT = range(5)

User = collections.namedtuple("User", "username forename middlename surname id")


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(
              sys.argv[0]))
        sys.exit()

    user_names = set()
    users = {}
    for filename in sys.argv[1:]:
        with open(filename, encoding="utf8") as file:
            for line in file:
                line = line.rstrip()
                if line:
                    user = process_line(line, user_names)
                    users[(user.surname.lower(), user.forename.lower(),
                            user.id)] = user
    print_users(users)


def process_line(line, user_names):
    fields = line.split(":")
    username = generate_username(fields, user_names)
    user = User(username, fields[FORENAME], fields[MIDDLE_NAME],
                fields[SURNAME], fields[ID])
    return user


def generate_username(fields, user_names):
    username = ((fields[FORENAME][0] + fields[MIDDLE_NAME][:1] +
                 fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in user_names:
        username = "{0}{1}".format(original_name, count)
        count += 1
    user_names.add(username)
    return username


def print_users(users):
    name_width = 32
    username_width = 9

    print("{0:<{nw}} {1:^6} {2:{uw}}".format(
          "Name", "ID", "Username", nw=name_width, uw=username_width))
    print("{0:-<{nw}} {0:-<6} {0:-<{uw}}".format(
          "", nw=name_width, uw=username_width))

    for key in sorted(users):
        user = users[key]
        initial = ""
        if user.middlename:
            initial = " " + user.middlename[0]
        name = "{0.surname}, {0.forename}{1}".format(user, initial)
        print("{0:.<{nw}} ({1.id:4}) {1.username:{uw}}".format(
              name, user, nw=name_width, uw=username_width))


main()
