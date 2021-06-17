# League of Spin

League of Spin is a management system for running a table tennis league consisting of teams.

## Getting started
```
docker build -t league-of-spin
docker run -p 8000:8000 -it --rm league-of-spin
```

Example league table at http://localhost:8000/leagues/table/1

Access the admin interface at https://localhost:8000/admin

The default super user is **admin** and the password is **changeit**
