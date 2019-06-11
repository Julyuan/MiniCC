#masm32 environment

This is a simple masm32 environment.
But still, I suggest you to run in **Windows**.
if you hope to get set the actual environment, go to visit <a herf="10.71.45.100/bhh">Black White's Homepage</a>

to compile and link a assembly program, taking _helloworld.asm_ as an example, you should:
``` bash
ml /c /coff helloworld.asm
link /subsystem:console helloworld.obj
```
And this is the context in _masm_link.bat_, you can double click the __bat__ to rum these two commands.
If you hope to modify the context in _masm_link.bat_, right click the __bat__ and choose __Edit__
Then, we outht to have an __exe__ if there's no problem.
``` bash
helloworld
```
you can use this command to run it.