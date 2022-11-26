Python app in Docker with two endpoints and testing. One for creating an entity, and another for listing them by different criteria.

### INSTRUCTIONS:
Clone this repository, install docker and get this running with docker-compose. In your terminal, go to the root where docker-compose.yml is and execute<br>
> $ docker-compose up

<br>For any doubts on the installation and execution on Docker, check the official docker documentation here:<br>
https://docs.docker.com/get-docker/

In */volumes/external_media/*, you should have the following files:
- banana1.txt
- banana2.txt
- banana3.txt

If not there, just create them with anything or nothing in it. These will be used for testing. As you use or test the app, folders are going to be created inside /volumes/external_media/. Since their permissions can be funny, should you wish to delete them, chances are you'll have to prune the docker volumes, or alternatively, sudo rm them, ***but do be careful***.

### ENDPOINTS:
- /
- /new/
- /fetch/

### ENDPOINT DOCS:
You can see the docs at http://localhost:8000/docs

### TESTS:
You can manually execute the tests with on your bash terminal. No need to enter inside the docker since this will work from your terminal.<br>
>$ docker exec -ti tips-app pytest

### KNOWN BUGS:
- Chances are two Tips of the same user for the same match shouldn't coexist, so mongo should be set with that constraint in mind.
- Working with media items gets broken between docker uptime sessions.

### TECHNICAL OBSERVATIONS:
- The architecture is based on hexagonal-onion-clean principles of decoupling and separating Domain, Application and Infrastructure. It is not entirely this way since it seems a bit overkill for a simple app, so for example, there are no interfaces that automagically instantiate into implementations.
- The framework is fastapi since everyone is using it and it's lightweight.
- The chosen persistence implementation is with mongodb, since entities are not relational to each other and I wanted to practice with this DB.

### THINGS I'VE LEARNED:
- Got to practice hexagonal architecture once more, and the first time from scratch. It's now finally coming intuitively to me. Hopefully I haven't made many glaring mistakes.
- Docker from scratch. Although I'm pretty sure I built a docker in the past, perhaps from scratch, it wasn't anything like this. What a painful learning process this has been.
- Using a framework from scratch, albeit a lightweight one.
- Programmatic integration testing from scratch.
- A bit more of mongodb, nothing major.
- OpenAPI is cool.
- Life is suffering.

### THINGS TO IMPROVE UPON:
- My back posture.
- Crack down on hexagonal architecture and solve some of the doubts I still have. It's finally starting to come together.
- Could've used Pydantic modelling more. Mainly at the Controller level, which I bet would've helped with the API docs, since /fetch is not correct. I could've also gone more ORM on the database.
- TDD. Turns out programmatic testing can be a real pain in the ass, so I should've had the config in order from the very start. I initially did some tests, but soon the config failed and I manually tested with Postman. By the time I got around to do the testing solution offered by fastapi, was already tired of it all.
- Setting up mongo programatically, since I used mongoexpress to help me with that bit.
- Using docker env variables.
- I don't know how to make containers unacessible from outside and at this point I'm too afraid to ask.
- Use GET for fetching, not POST.
- Setting up the project the python3 way, not python2-style like it is now.


If you read this far, consider hiring me. I learn from my mistakes, just like Tony Stark.
