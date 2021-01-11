xargs -a domain -I@ -P500 sh -c 'shuffledns -d "@" -silent -w words.txt -r resolvers.txt' | httpx -silent -threads 1000 | nuclei -t /root/nuclei-templates/ -o re1
