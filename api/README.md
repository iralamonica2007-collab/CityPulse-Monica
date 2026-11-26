# JSON Basics

JSON (JavaScript Object Notation) is a simple text format for storing data and sending it between apps and APIs.

## 1. JSON Object

An object holds data as `key: value` pairs inside `{ }`.

```json
{
  "name": "Monica",
  "college": "Atria University",
  "course": "<your course>",
  "year": 2
}
```

- `name`: the student's name (text)
- `college`: the college name (text)
- `course`: the course being studied (text)
- `year`: the current year of study (number, so no quotes)

## 2. JSON Object with Arrays

A value can also be an array: a list of items inside `[ ]`.

```json
{
  "name": "Monica",
  "skills": ["Linux", "Git", "Bash", "HTML"],
  "hobbies": ["<hobby 1>", "<hobby 2>"]
}
```

- `skills`: an array of skills
- `hobbies`: an array of hobbies

## JSON Syntax

| Symbol | Meaning |
| --- | --- |
| `{ }` | An object |
| `[ ]` | An array (list) |
| `:` | Separates a key from its value |
| `,` | Separates items |
| `" "` | Text (a string). Keys always use double quotes |

Rules to remember: keys must be in double quotes, there is no comma after the last item, and comments are not allowed.
