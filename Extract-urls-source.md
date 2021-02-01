Extract urls to comments source code

```
cat urls1 | html-tool comments | grep -oE '\b(https?|http)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]*[-A-Za-z0-9+&@#/%=~_|]' 

```

https://twitter.com/ofjaaah/status/1355926330890543106
