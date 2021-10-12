# Super simple file operations

Are you tired of doing this each time to just modify a part of a json file?
```python
with open(filepath, 'r') as file:
    fd = json.load(file)

fd[key] = 'new value'

with open(filepath, 'w') as file:
    json.dump(fd, file)
```

Don't worry! Now you can do it just like this! - 

```python
fd = fileops.read_json(filepath)
fd[key] = 'new value'
fileops.write_json(filepath, fd)
```

**No hassle of context managers, or saving files, just do things simpler!**