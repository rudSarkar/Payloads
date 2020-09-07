## Duplicate item

```
root@kali:~/hek$ cat domain
example.com
example.com
hackerone.com
hackerone.com
bugcrowd.com
google.com
mail.google.com
mail.google.com
```

## Unique Item
```
root@kali:~/hek$ sort domain | uniq
bugcrowd.com
example.com
google.com
hackerone.com
mail.google.com
```
