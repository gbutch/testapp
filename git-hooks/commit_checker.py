#!/usr/bin/python

import sys, os, re
from subprocess import call

print os.environ.get('EDITOR')

if os.environ.get('EDITOR') != 'none':
    editor = os.environ['EDITOR']
else:
    editor = "vim"

message_file = sys.argv[1]


def check_format_rules_for_line_1(line_number, line):
    def format_match(string):
        is_it_valid = re.match('^[Ss]tory[:;-][0-9]{1,4}[^.]+', string)
        if is_it_valid == None:
            return False
        else:
            return True
    real_line_number = line_number + 1
    if not line.startswith('#'):
        if not format_match(line):
            return "Error 'Line %d': Commit message must start with 'story:{number}'" \
                   % (real_line_number)
    return False

def generic_line_format_checks(line_number, line):
    real_line_number = line_number + 1
    if not line.startswith('#'):
        if len(line) > 50:
            return "Error %d: Line should be less than 50 characters " \
                   "in length." % (real_line_number,)

while True:
    commit_msg = []
    errors = []
    with open(message_file, 'r+') as commit_fd:
        for line_number, line in enumerate(commit_fd):
            commit_fd.write("Line number: %s, Line: %s" % (line_number, line))
            if line_number == 0:
                check_format_rules_for_line_1(line_number, line)
                commit_fd.write("Checking Line 1")
            if line_number != 0:
                generic_line_format_checks(line_number, line)
                real_line_number = line_number + 1
                commit_fd.write("Checking Line %d" % real_line_number)
# while True:
#     commit_msg = list()
#     errors = list()
#     with open(message_file) as commit_fd:
#         for line_number, line in enumerate(commit_fd):
#             stripped_line = line.strip()
#             if not line.startswith('#'):
#                 commit_msg.append(line)
#             if line_number == 0:
#                 e = check_format_rules_for_line_1(line_number, stripped_line)
#             if line_number != 0:
#                 e = generic_line_format_checks(line_number, stripped_line)
#             if e:
#                 errors.append(e)
#     if errors:
#         with open(message_file, 'w') as commit_fd
#             commit_fd.seek()
#             commit_fd.write('\n')
#             commit_fd.write('%s\n' % '# GIT COMMIT MESSAGE FORMAT ERRORS:')
#             for error in errors:
#                 commit_fd.write('#    %s\n' % (error,))
#             for line in commit_msg:
#                 commit_fd.write(line)
        commit_fd.close()
        re_edit = raw_input('Invalid git commit message format.  Press y to edit and n to cancel the commit. [y/n]')

        if re_edit.lower() in ('n', 'no'):
            sys.exit(1)
        call('%s %s' % (editor, message_file), shell=True)
        continue
    break
