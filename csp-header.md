```
curl -v -silent https://$1 --stderr - | awk '/^content-security-policy:/' | grep -Eo "[a-zA-Z0-9./?=_-]*" |  sed -e '/\./!d' -e '/[^A-Za-z0-9._-]/d' -e 's/^\.//' | sort -u
```

CC: [Geeknik’s Farm @geeknik](https://twitter.com/geeknik/status/1312496701966413826)
