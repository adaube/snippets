Original list of files:
```
49G Mar 19 10:04 C0010.MP4
777 Mar 19 09:36 C0010M01.XML
```

Why split the MP4 up?
  1. File is large
    - We want to be able to track progress easily as well as mitigate potential data loss
  2. OneDrive currently limits to 10GB max single upload

Let's use a built-in command that comes with the Linux kernel to split the original file:

    split -b 150M C0010.MP4 bdj.

This creates 333 files with the bdj. prefix in parts `aa-mu` from the original file.

We can find the number of files in the directory with the command:

    ls -1 | wc -l
 
Combining the files is done with the command:

    cat bdj.?? > C0010.MP4

Try this with any size file by changing the `150M` parameter, or read up with `man split` in your terminal for some use cases.
