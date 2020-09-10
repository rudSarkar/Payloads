If you're not sure that which type of extenstion are avialable in your waybackurs you can use the `egrep`

```
root@kali:~/hek/domains/example$ cat example-target-wayback-list.txt | egrep -i -E -o "\.{1}\w*$" | sort -su
.
.0
.03
.1
.10
.11
.15
.2
.3
.32
.4
.5
.6
.681
.7
.8
.9
.action
.atom
.com
.css
.eot
.gif
.ico
.jpeg
.jpg
.JPG
.js
.json
.mp4
.otf
.php
.png
.PNG
.rss
.svg
.ttf
.txt
.woff
.woff2
.x
.xml

```

It will print all the available extenstions of your waybackurls lists.
