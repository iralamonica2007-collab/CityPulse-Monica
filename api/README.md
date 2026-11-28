# JSON Fundamentals

This folder contains examples of JSON (JavaScript Object Notation).

## 1. JSON Object

A JSON object stores data in key-value pairs.

### Example

```json
{
    "name": "Monica Irala",
    "age": 19,
    "college": "Atria University",
    "course": "BS Engineering",
    "department": "Digital Transformation"
}
```

### Explanation

- `name` stores the student's full name.
- `age` stores the age as a number, so it has no quotes.
- `college` stores the college name.
- `course` stores the course being studied.
- `department` stores the department.

Each key is a string in double quotes, followed by `:` and its value.

---

## 2. JSON Object with Array

A JSON object can also hold an array as a value.

An array stores a list of values inside square brackets `[]`.

### Example

```json
{
    "name": "Monica Irala",
    "age": 19,
    "college": "Atria University",
    "skills": [
        "Linux",
        "Bash",
        "Git",
        "GitHub",
        "JSON"
    ],
    "hobbies": [
        "Hobby 1",
        "Hobby 2",
        "Hobby 3"
    ]
}
```

### Explanation

- `name`, `age` and `college` are normal key-value pairs.
- `skills` is an array holding several skills.
- `hobbies` is an array holding several hobbies.

---

## JSON Syntax

| Symbol | Purpose |
|---|---|
| `{ }` | Defines a JSON object |
| `[ ]` | Defines an array |
| `:` | Separates a key from its value |
| `,` | Separates properties or array items |
| `" "` | Defines strings (text) |

### Rules

- Keys must always be in double quotes.
- No comma after the last item.
- Comments are not allowed in JSON.

---

## Conclusion

JSON is a lightweight, easy-to-read format used to store data and send it between applications and APIs.
