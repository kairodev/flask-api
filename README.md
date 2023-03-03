# Flask API ![Badge](https://img.shields.io/static/v1?label=Flask&message=Python&color=green&style=&logo=FLASK)
> API developed in Flask/Python for studies. This API consists of dummy data with routes to view/change/delete

### Functionalities  

- [X] Addition
- [X] Visualization
- [X] Edition
- [X] Exclusion

### Installation

```python
pip install flask
pip install pandas
python app.py
```

### Routes
> GET /data
- list all users

> GET /specific/data/{id}
- List the details of a specific user

> DELETE /reset
- Reset the dummy database,

> DELETE /delete/{id}
- Delete a specific user

> POST /change/{id}
- Change data for a specific user
- The username and password fields must be sent in formdata format, indicating the new username and password

> POST /add
- Create a new user
- The username and password fields must be sent in formdata format, indicating the username password
