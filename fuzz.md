```
cat sam.txt | xargs -I@ sh -c 'ffuf -w D:\dicc.txt -u @/FUZZ -replay-proxy http://127.0.0.1:8080'
```
