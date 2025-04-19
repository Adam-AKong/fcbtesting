<h1>API Specifications</h1>

<p>Project Members: Adam Kong, Brian Kaplan, Vic Grigoryev</p>

<h5>Cal Poly Email: aakong@calpoly.edu, bhkaplan@calpoly.edu, vgrigory@calpoly.edu</h5>

<h3> Endpoint 1</h3>

## GET /character/{character_id}

**Description:**  
Returns the character information of the id provided

**Response Example:**

Note: some of these fields are subject to change
```json
[
  {
    "character_id": 1,
    "name": "Superman",
    "description": "a comic book character from the planet Krypton. He can fly, has super strength, and has laser eyes",
    "rating": 8.6,
    "strength": 10
    "speed": 9,
    "health": 100
  }
]
```
<h3> Endpoint 2</h3>

## POST /character/review/{character_id}

**Description:**  
Allows a user to post a review of the character

**Response Example:**

Note: some of these fields are subject to change
```json
[
  {
    "character_id": 1,
    "name": "Superman",
    "rating": 9,
    "comments": "Superman is a really cool character that I really like because he is Super!"
  }
]
```
<h3> Endpoint 3</h3>

## POST /battle/characters/{character_1}/{character_2}

**Description:**  
Allows a user to get the results of a battle between 2 selected characters

**Response Example:**

Note: some of these fields are subject to change
```json
[
  {
    "character_id": 1,
    "name": "Superman"
  },
 {
    "character_id": 2,
    "name": "Batman"
  }
]
```
<h3> Endpoint 4</h3>

## POST /battle/vote/{battle_id}/{selected_character}

**Description:**
Allows the user to vote for a character during a battle

**Response Example:**

Note: some of these fields are subject to change
```json
[
  {
    "battle_id": 1,
    "character_vote": 1
  }
]
```
<h3> Endpoint 5</h3>

## POST /character/make/{user_id}/{character_id}

**Description:**
Allows the user to create a character that is linked to their user id

**Response Example:**

Note: some of these fields are subject to change
```json
[
  {
    "character_id": 2,
    "user_id": 1,
    "description": "A wealthy guy who patrols the streets of Gotham at night for justice. He is very strong and smart and will stop at nothing to achieve his goals.",
    "strength": 7,
    "speed": 6,
    "health": 100
  }
]
```
<h3> Endpoint 6</h3>

## GET /character/{user_id}

**Description:**
Allows the user to get a list of characters created based on a user's id

**Response Example:**

Note: some of these fields are subject to change
```json
[
  {
    "character_id": 1
  }
  {
    "character_id": 2
  }
]
```
<h3> Endpoint 7</h3>

<h3> Endpoint 8</h3>
