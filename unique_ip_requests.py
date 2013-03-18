import os
import sys

from subprocess import Popen, PIPE, STDOUT

def main(filename):
    if not os.path.isfile(filename):
        usage("File: %s cannoot be opened" %filename)
        sys.exit(1)

    cmd = "cat %s | cut -d ' ' -f1 | sort | uniq -c" %filename
    p = Popen(
            cmd,
            shell=True,
            stdin=PIPE,
            stdout=PIPE,
            stderr=STDOUT,
            close_fds=True)

    output = p.stdout.read()
    request_count = {}
    for line in output.split('\n'):
        line = line.strip()
        if ' ' in line:
            count, ip = line.split()
            request_count[ip] = count

    return request_count

def usage(msg):
    print """
    Error: %s

    Usage:
    python unique_ip_requests.py <path-to-apache-access-logs>
    """ %msg

if __name__=="__main__":
    if len(sys.argv) == 2:
        print main(sys.argv[1])
    else:
        usage("Pass in only filename as a command line argument")
