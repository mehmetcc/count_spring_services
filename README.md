#count_spring_services

Walk each and every file and search for a keyword. Searches subdirectories as well.

Usage is pretty simple, either edit globals.py, or run cli.py. You can configure the path, the keyword and the extension as well.
There is also a Command Line Interface, to access it use the following command:

```shell
python3 cli.py --path GIVEN_PATH --keyword GIVEN_KEYWORD --extension GIVEN_EXTENSION
```

For example, to search for how many Java files contains the keyword @Service, the arguments should be entered as such:
```shell
python3 cli.py --path your/project/path --keyword @Service --extension .java
```
