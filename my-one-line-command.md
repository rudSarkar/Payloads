## Amass
amass passive scan and grab title and status of the subdomain.
```
amass enum --passive -d example.com | httpx -title -status-code | anew
```
