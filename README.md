# she-codes-crowdfunding-api-project-supremeoverlord-ofdoom
she-codes-crowdfunding-api-project-supremeoverlord-ofdoom created by GitHub Classroom
# Crowdfunding API Project: Gnome My Enemy 
​
"Gnome My Enemy" is a crowdfunding platform designed for individuals seeking to gnome someone. Gnoming is the act of placing a large number of gnomes in a particular area (commonly someone's garden), often as a form of creative expression and revenge. Our platform allows users to crowdfund the necessary resources to execute their gnome projects, whether it be as a form of retaliation or simply for personal enjoyment.

The target audience for "Gnome My Enemy" includes anyone who wants to gnome someone but lacks the funds to purchase the required gnomes. Our user-friendly interface makes it simple for individuals to raise money or donated gnomes for their projects and bring their gnome visions to life.

In conclusion, "Gnome My Enemy" is a unique platform that provides a means for individuals to express themselves through gnoming. Whether it's for revenge or for personal fulfillment, this platform offers a way for people to bring their gnome projects to fruition.
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
- none
​
​
## Part A Submission
​
- [X] A link to the deployed project.
- https://floral-wave-2596.fly.dev/projects/

- [X] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a token being returned.
- https://docs.google.com/document/d/1Flhez9Vm9QefuknHGGyvLhLcJNmaH3y6JHf-92WM-S8/edit?usp=sharing

- [X] Your refined API specification and Database Schema.
- https://docs.google.com/document/d/1JXM0Hmlw_aVDU9b-AmE9cT3Q4o9pw872nULi47lfP5c/edit?usp=sharing
​
### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
​
1. Create User
​
```shell
curl --request POST \
  --url http://localhost:8000/users/ \
  --header 'Authorization: Token c00thisisafaketoken' \
  --header 'Content-Type: application/json' \
  --data '{
	"email": "test_user@gnome.com",
  "username": "test_user",
	"password": "not_a_real_password"
}'

```
​
2. Sign in User
​
```shell
curl --request POST \
  --url http://localhost:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "test_user",
	"password": "not_a_real_password"
}'
```
​
3. Create Project
​
```shell
curl --request POST \
  --url http://localhost:8000/projects/ \
  --header 'Authorization: Token  c00thisisafaketoken' \
  --header 'Content-Type: application/json' \
  --data '{
	
"title": "Arch enemy gnoming",
		"description": "My one final nemesis has taken it too far and copied my artwork of a loaf of bread, so I need to get even - gnome style",
		"goal": 500,
		"image": "https://perthlocalguide.com/wp-content/uploads/2021/09/Gnomesville-Image-2.jpg",
		"is_open": true,
	"date_created": "2023-01-29T13:05:49.764Z"
}
'
```
