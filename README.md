Arkest
======

INSTALL
-------

API
---

### GET /dinosaurs/list:
    Return the list of the race of the dinosaurs present in the database.

```json
{
    "count": 2,
    "races":
        [
            "Sabertooth",
            "Direwolf"
        ]
}
```

### GET /dinosaurs/list/<**_kind_**>:
    Return the list of all dinosaurs of race `kind`, Sabertooth for example. If
    there is no dinosaurs of this race in the database, the array is empty.

```json
{
    "count": 1,
    "dinosaurs":
        [
            {
                "id": 0,
                "race": "Sabertooth",
                "name": "SuperSaber",
                "owner": "Namarand",
                "tribe": "My Awesome Tribe",
                "acquired": "Breeded", //Can be Tamed or Breeded
                "effectiveness": 89, //This field is ommited in case of a Tamed dino
                "status": "Alive", //Can be Alive or Dead
                "sexe": "Male", //Can be Male or Female
                "health": 14,
                "stamina": 4,
                "oxygen": 24,
                "food": 25,
                "weight": 5,
                "damage": 7,
                "speed": 5,
                "level": 14
            }
        ]
}
```

### GET /dinosaurs/get:
    Get all information about a list of specific dinosaurs. The request must
    have an attached body with an array of *ids* following this format:

```json
{
    "count": 2,
    "ids":
        [
            5,
            7
        ]
}
```

    The response will follow the same structure of the previsous function, but
    with an error case:

```json
{
    "count": 2,
    "dinosaurs":
        [
            {
                "id": 5,
                ...
                "speed": 5,
                "level": 14
            },
            {
                "id": 7,
                "error": "no such dinosaurs"
            }
        ]
}
```

### POST /dinosaurs/new:
    Create new dinosaur. The request must have an attached body with all data
    about the new dinosaur. The body must follow this format:

```json
{
    "race": "Sabertooth",
    "name": "SuperSaber2"
    "owner": "Namarand",
    "tribe": "My Awesome Tribe",
    ...
    "speed": 5,
    "level": 14
}
```
    On success, you'll receive a json with the *id* of the new dinosaur. On
    failure, you'll receive a json with an error message.

```json
//success
{
    "id" : 5
}
//failure
{
    "error": "invalid value for 'speed'"
}
```

### PUT /dinosaurs/update/<**_id_**>:
    Update fields for a specific dinosaur. The request must have an attached
    body with only the field that have to be updated. It must follow this
    format:

```json
{
    "level": 54,
    "stamina": 12
}
```
    On failure, you'll receive a json with an error message.

```json
{
    "error": "invalid value for 'speed'"
}
```

### DELETE /dinosaurs/delete/<**_id_**>:
    Delete a specific dinosaur.

### POST /parents/new:
    Add a parent to a dinosaur. The request must have an attached body with the
    id of the two parent. It must follow this format:

```json
{
    "id": 0,
    "father": 2,
    "mother": 48
}
```

    On failure, you'll receive a json with an error message.

```json
{
    "error": "father is not a male"
}
```

### PUT /parents/update/<**_id_**>:

    Update parents for a child. The request must have an attached
    body with only the field that have to be updated. It must follow this
    format:

```json
{
    "father" : 5
}
```
    On failure, you'll receive a json with an error message.

```json
{
    "error": "father is not a male"
}
```

### DELETE /parents/delete/<**_id_**>:

    Delete a specific relations.

### GET /parents/get:

    Get all information about a list of specific relations. The request must
    have an attached body with an array of *ids* following this format:

```json
{
    "count": 3,
    "ids":
        [
            5,
            3,
            7
        ]
}
```
    The response will return an array of response, with parents or error:

```json
{
    "count": 3,
    "parents":
        [
            {
                "id": 5,
                "father": 3,
                "mother": 2
            },
            {
                "id": 3,
                "father": 4,
                "mother": 2
            },
            {
                "id": 7,
                "error: "no such dinosaur"
            }
        ]
}
```
