# she-codes-crowdfunding-api-project-supremeoverlord-ofdoom
she-codes-crowdfunding-api-project-supremeoverlord-ofdoom created by GitHub Classroom
# Crowdfunding API Project: Gnome My Enemy 
​
{{ a paragraph detailing the purpose and target audience }}
​
## Features
​
### User Accounts
​
- [X] Username
- [X] Email Address
- [X] Password
​
### Project
​
- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [] Destroy - projects cannot be deleted (to avoid problems), the owner can edit them to be closed for pledges
- Pledge
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
- User
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [ ] Destroy - users cannot be deleted (to avoid problems)
​
### Implement suitable permissions
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [X] Limit who can create
  - [ ] Limit who can retrieve - not necessary to restrict this currently
  - [X] Limit who can update
  - [X] Limit who can delete
- Pledge
  - [X] Limit who can create
  - [X] Limit who can retrieve - pledges asscoiated to a user
  - [X] Limit who can update
  - [X] Limit who can delete
- User
  - [X] Limit who can retrieve - user detail view is restricted to the logged in user
  - [X] Limit who can update
  - [X] Limit who can delete
​
### Implement relevant status codes
​
- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404
​
### Handle failed requests gracefully 
​
- [X] 404 response returns JSON rather than text
​
### Use token authentication
​
- [X] impliment /api-token-auth/
​
## Additional features
​
- [X] {List of pledges assoicated with project}
​
{{ All pledges are listed under the Project Detail }}
​
- [X] {List of user's pledges}
​
{{ All user's pledges are listed in the User Detail, this view is restricted to the logged in user to keep anonymous pledges anonymous (otherwise people could see who anonymous  pledges are linked to) }}
​
- [X] {Current total funded}
​
{{ Total amolunt raised from pledges is calulcated }}
​
- [X] {Change password}
​
{{ User password can be changed (as long as you remember the current password}}
​
### External libraries used
​
- [ ] none
​
​
## Part A Submission
​
- [X] A link to the deployed project.
- https://floral-wave-2596.fly.dev/projects/
- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a token being returned.
- [ ] Your refined API specification and Database Schema.
​
### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
​
1. Create User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"email": "not@myemail.com",
	"password": "not-my-password"
}'
```
​
2. Sign in User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"password": "not-my-password"
}'
```
​
3. Create Project
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/projects/ \
  --header 'Authorization: Token 5b8c82ec35c8e8cb1fac24f8eb6d480a367f322a' \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "Donate a cat",
	"description": "Please help, we need a cat for she codes plus, our class lacks meows.",
	"goal": 1,
	"image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Dollar_bill_and_small_change.jpg",
	"is_open": true,
	"date_created": "2023-01-28T05:53:46.113Z"
}'
```
