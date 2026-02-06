# Dictionary as condition Rreplacement
person = {"name": "Alice",
           "age": 30}

print(person.get("name", "Unknown"))  # Output: Alice
print(person.get("gender", "Unknown"))  # Output: Unknown

actions = {
    "start": "Game started",
    "stop": "Game stopped",
    "pause": "Game paused"
}

actions2={
    "arun":"good boy",
    "prakash":"smart boy",
    "ponmozhi":"good mom"
}

# command = "arin"
command = "start"
command2="ponmozhi"
print(actions.get(command, "Unknown command"))
print(actions2.get(command2, "Unknown command"))    