## Create your own wordlist.
```
echo "http://api.uber.com" | waybackurls | cut -d "/" -f 4,5 | sed 's/?.*//' | sort -u
```

CC: [King Of Tips](https://twitter.com/KingOfBugbounty/status/1311074172475498497)
