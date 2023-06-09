LINUX_TO_WINDOWS = {
    "touch": "type nul >",
    "mkdir": "mkdir",
    "rm": "del",
    "rmdir": "rmdir",
    "cp": "copy",
    "mv": "move",
    "ls": "dir",
    "pwd": "cd",
    "grep": "findstr",
    "cat": "type",
    "echo": "echo",
    "chmod": "icacls",  
    "chown": "takeown",  
    "df": "fsutil volume diskfree",
    "du": "dir /s",  
    "ps": "tasklist",
    "kill": "taskkill", 
    "top": "tasklist", 
    "clear": "cls",
}