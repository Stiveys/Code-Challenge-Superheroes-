# Code-Challenge-Superheroes-
SA.:Phase 4 Code Challenge: Superheroes - Compulsory
Due No due date Points 15 Submitting a website url Attempts 0 Allowed attempts 8
Instructions
For this assessment, you'll be working on an API for tracking heroes and their superpowers.
Setup
Create a new PRIVATE repository, and add your TM as a collaborator. Push your solution to this repository and submit for grading.
You have been provided a Postman collection Download Postman collection. This collection contains all the endpoints that you are required to create with this API. You can download and import it into your Postman application to test that your app works correctly.
How to import postman collection.

Select `Upload Files`, navigate to this repo folder, and select `challenge-2-superheroes.postman_collection.json` as the file to import.
Before you submit! Save and run your code to verify that it works as you expect.
You MUST have a well-written README in your repository. Ensure your markdown renders correctly before submission. You can use Visual Studio Code Markdown preview to see how it would appear on your GitHub repository.
Resources
How to write a good README.


Deliverables
Your job is to build out the Flask API to add the functionality described in the deliverables below.

Models
You will implement an API for the following data model:



Now you can implement the relationships as shown in the ER Diagram:

- A `Hero` has many `Power`s through `HeroPower`
- A `Power` has many `Hero`s through `HeroPower`
- A `HeroPower` belongs to a `Hero` and belongs to a `Power`

Since a `HeroPower` belongs to a `Hero` and a `Power`, configure the model to cascade deletes.

Set serialization rules to limit the recursion depth.
Run the migrations and seed the database
If you aren't able to get the provided seed file Download seed fileworking, you are welcome to generate your own seed data to test the application.

Validations

Add validations to the `HeroPower` model:

- `strength` must be one of the following values: 'Strong', 'Weak', 'Average'

Add validations to the `Power` model:

- `description` must be present and at least 20 characters long

Routes

Set up the following routes. Make sure to return JSON data in the format specified along with the appropriate HTTP verb.

Recall you can specify fields to include or exclude when serializing a model instance to a dictionary using to_dict() (don't forget the comma if specifying a single field).

a. GET /heroes
Return JSON data in the format below:
[
 {
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel"
 },
 {
  "id": 2,
  "name": "Doreen Green",
  "super_name": "Squirrel Girl"
 },
 {
  "id": 3,
  "name": "Gwen Stacy",
  "super_name": "Spider-Gwen"
 },
 {
  "id": 4,
  "name": "Janet Van Dyne",
  "super_name": "The Wasp"
 },
 {
  "id": 5,
  "name": "Wanda Maximoff",
  "super_name": "Scarlet Witch"
 },
 {
  "id": 6,
  "name": "Carol Danvers",
  "super_name": "Captain Marvel"
 },
 {
  "id": 7,
  "name": "Jean Grey",
  "super_name": "Dark Phoenix"
 },
 {
  "id": 8,
  "name": "Ororo Munroe",
  "super_name": "Storm"
 },
 {
  "id": 9,
  "name": "Kitty Pryde",
  "super_name": "Shadowcat"
 },
 {
  "id": 10,
  "name": "Elektra Natchios",
  "super_name": "Elektra"
 }
]

b. GET /heroes/:id
If the `Hero` exists, return JSON data in the format below:
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
     {
       "hero_id": 1,
       "id": 1,
       "power": {
              "description": "gives the wielder the ability to fly through the skies at supersonic speed",
              "id": 2,
              "name": "flight"
        },
       "power_id": 2,
       "strength": "Strong"
        }
   ]
}
If the `Hero` does not exist, return the following JSON data, along with the appropriate HTTP status code:
{
  "error": "Hero not found"
}

c. GET /powers
Return JSON data in the format below:
[
 {
    "description": "gives the wielder super-human strengths",
    "id": 1,
    "name": "super strength"
 },
 {
    "description": "gives the wielder the ability to fly through the skies at supersonic speed",
    "id": 2,
    "name": "flight"
 },
 {
    "description": "allows the wielder to use her senses at a super-human level",
    "id": 3,
    "name": "super human senses"
 },
 {
    "description": "can stretch the human body to extreme lengths",
    "id": 4,
    "name": "elasticity"
 }
]

d. GET /powers/:id
If the `Power` exists, return JSON data in the format below:
{
  "description": "gives the wielder super-human strengths",
  "id": 1,
  "name": "super strength"
}
If the `Power` does not exist, return the following JSON data, along with the appropriate HTTP status code:
{
  "error": "Power not found"
}
e. PATCH /powers/:id
This route should update an existing `Power`. It should accept an object with the following properties in the body of the request:
{
 "description": "Valid Updated Description"
}
If the `Power` exists and is updated successfully (passes validations), update its description and return JSON data in the format below:
{
  "description": "Valid Updated Description",
  "id": 1,
  "name": "super strength"
}
If the `Power` does not exist, return the following JSON data, along with the
appropriate HTTP status code:
{
 "error": "Power not found"
}
If the `Power` is **not** updated successfully (does not pass validations), return the following JSON data, along with the appropriate HTTP status code:
{
 "errors": ["validation errors"]
}
f. POST /hero_powers
This route should create a new `HeroPower` that is associated with an existing `Power` and `Hero`. It should accept an object with the following properties in the body of the request:
{
 "strength": "Average",
 "power_id": 1,
 "hero_id": 3
}
If the `HeroPower` is created successfully, send back a response with the data related to the new `HeroPower`:
{
 "id": 11,
 "hero_id": 3,
 "power_id": 1,
 "strength": "Average",
 "hero": {
    "id": 3,
    "name": "Gwen Stacy",
    "super_name": "Spider-Gwen"
 },
 "power": {
    "description": "gives the wielder super-human strengths",
    "id": 1,
    "name": "super strength"
 }
}
If the `HeroPower` is **not** created successfully, return the following JSON data, along with the appropriate HTTP status code:
{
 "errors": ["validation errors"]
}
Rubric
Phase 4 Flask CC Rubric (1)
Phase 4 Flask CC Rubric (1)
Criteria	Ratings	Pts
This criterion is linked to a learning outcomeModels, Relationships, and Validations
5 Pts
5
All specified models, relationships, and validations are complete and correct. Validations are used when appropriate. Variable and method names are intention-revealing.
4 Pts
4
All models, relationships, and validations are complete and correct, save minor mistakes in advanced deliverables. Advanced validations are complete and add informative error messages.
3 Pts
3
Models, relationships, and validations mostly complete and correct per the deliverables. Advanced validations and methods may be incomplete. May have unused or unnecessary code, possibly including duplication. May have written validations instead of using appropriate built-in validations. May implement advanced query methods with iterators instead of using built-in methods.
2 Pts
2
Models, relationships, and validations attempted but incomplete or have errors. Relationships may construct the wrong relationships. Validations may be missing or applied to the wrong models. Advanced query methods incomplete or have errors.
1 Pts
1
Models, relationships, and validation not started or have errors that prevent the application from running. Missing validations, or validation syntax is incorrect. May have introduced models outside the specified domain.
5 pts
This criterion is linked to a learning outcomeRoutes and REST
5 Pts
5
All routes deliverables work as described in the instructions. Routing follows REST naming conventions.
4 Pts
4
Nearly all routing deliverables completed, possibly with minor errors in advanced deliverables. Routing follows REST conventions.
3 Pts
3
Most routing logic working as specified. Some advanced deliverables may be incomplete. Routing follows REST convention.
2 Pts
2
Some routing logic implemented, but incompletely or incorrectly. May have routes actions not included in the deliverables.
1 Pts
1
Routes missing, naming does not follow REST.
5 pts
This criterion is linked to a learning outcomeResponse Structure
5 Pts
5
Includes correct JSON response body with nested data where indicated. All routes return the appropriate HTTP status code for successful requests as well as unsuccessful requests. Uses a serializer to structure data.
4 Pts
4
Includes correct JSON response body with nested data where indicated. All routes return the appropriate HTTP status code for successful requests as well as unsuccessful requests.
3 Pts
3
Includes appropriate top-level JSON data in response as specified. May have missing nested data structures. Includes the correct HTTP status code for successful requests. May be missing response body or status code for unsuccessful requests (not found or invalid data).
2 Pts
2
Includes correct responses for some (but not all) of the routes required in the deliverables. May have missing nested data structures.
1 Pts
1
Missing response or returns JSON data other than what is specified in the deliverables.
5 pts
Total points: 15
