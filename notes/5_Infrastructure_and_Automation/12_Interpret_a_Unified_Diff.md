# Interpret a Unified Diff

```
$ diff -u file1.txt file2.txt
--- file1.txt   2020-01-01 13:37:11.10000000 +0400
+++ file2.txt   2020-01-01 15:41:33.20000000 +0400
@@ -1,5 +1,5 @@
 this is the original text
 line2
-line3
 line4
 happy hacking !
+GNU is not UNIX
```

- `---` metadata about the first specified file
- `+++` metadata about the second specified file
- `@@ -1,5 +1,5 @@` denotes the starting point and number of lines displayed from the original text
  - `-1,5` begin file1.txt at line 1 and display 5 lines
  - `+1,5` begin file2.txt at line 2 and display 5 lines

`-` line exists in first file but not the second
`+` line exists in second file but not the first

Diffs are also used in version control:

```
$ git diff file1.txt
```

In this example all of the above symbols mean the same thing, but instead of two different files it will compare the currently-committed version of the file with the file in the working directory (showing changes since last commit).
