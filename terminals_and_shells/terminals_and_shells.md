# Terminals and shells

## Unix fileshare permissions

A file where everyone has Read, Write, eXecute:
```
-rwxrwxrwx
```

The first 3 letter represent the "Owner's" permissions (creator of file)

The middle 3 letters represent the "Group's" permissions (can be assigned to a group of users)

The last 3 letters represent "Other", meaning everyone else

## Some examples:

### Everyone (including group and owner) has Read and Execute of a file

```
-r-xr-xr-x
```

###  Only owner has Read, Write, Execute of a file:

```
-rwx------
```

### A folder where everyone has Read, Write, eXecute:

```
drwxrwxrwx
```

### Chmod

To change permissions, use chmod:

```
sudo chmod -R u=rwx,g=rwx,o=rwx DIRECTORY
```

