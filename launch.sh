socat tcp-l:53699,reuseaddr,fork,crlf exec:./script.py,pty,ctty,echo=0;
