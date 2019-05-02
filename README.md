```sh
$ python3 -m http.server --cgi --bind localhost 10080
```

```sh
% curl -X POST localhost:10080/cgi-bin/up.cgi -F file=@/etc/hosts
% curl -X POST localhost:10080/cgi-bin/msg.cgi --data-urlencode "textcontent=$( ls -l /etc/ )"
```
