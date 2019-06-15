## a small C-subset compiler
``` bash
python3 genmid.py parsetree.txt|python3 mid2masm32.py
```
genmid.py reads from parsetree.txt and its output will be the input of mid2masm32.py
mid2masm32.py reads and print the code in **stdout**
File redirection is allowed by both.
