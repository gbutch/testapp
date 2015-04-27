#!/usr/bin/python

import sys, os, re
from subprocess import call

print os.environ.get('EDITOR')

if os.environ.get('EDITOR') != 'none':
    editor = os.environ['EDITOR']
else:
    editor = "vim"

message_file = sys.argv[1]


def check_format_rules(line_number, line):
    def format_match(string):
        is_it_valid = re.match('^[Ss]tory[:;-][0-9]{1,4}[^.]+', string)
        if is_it_valid == None:
            return False
        else:
            return True

    real_line_number = line_number + 1
    if not line.startswith('#'):
        if len(line) > 50:
            return "Error %d: First line should be less than 50 characters " \
                   "in length." % (real_line_number,)
        if not format_match(line):
            return "Error %d: Commit message must start with 'story:{number}'" \
                   % (real_line_number)

    return False


while True:
    commit_msg = []
    errors = list()
    with open(message_file) as commit_fd:
        for line_number, line in enumerate(commit_fd):
            stripped_line = line.strip()
            commit_msg.append(line)
            e = check_format_rules(line_number, stripped_line)
            if e:
                errors.append(e)
    if errors:
        with open(message_file, 'w') as commit_fd:
            commit_fd.write('%s\n' % '# GIT COMMIT MESSAGE FORMAT ERRORS:', \n, commit_fd)
            for error in errors:
                commit_fd.write('#    %s\n' % (error,))
            for line in commit_msg:
                commit_fd.write(line)
        re_edit = raw_input('Invalid git commit message format.  Press y to edit and n to cancel the commit. [y/n]')
        if re_edit.lower() in ('n', 'no'):
            sys.exit(1)
        call('%s %s' % (editor, message_file), shell=True)
        continue
    break
