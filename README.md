# FitbitInterface


## How to make it work?

### Create an account

If not already in possession of a Fitbit account, create one here: https://accounts.fitbit.com/signup

### Register a app though Fitbit website

To use the API, we need to have an app registered (the API has been build for third-party app developers). 

To do this, go to https://dev.fitbit.com/apps.

For our purposes right now, it will be a dummy app. Therefore, the content of only
two fields matter (for the rest, enter whatever you'd like to): 

* `Redirect URL`. The value has to be `http://127.0.0.1:8080/` 
(if you change that, you'll need to update the script `obtain_token.py`).
For the rest.
* `OAuth 2.0 Application Type`. The value as to be set to `Personal`.

What we need is to get in the end is a 
`OAuth 2.0 Client ID` and `Client Secret`. Once you complete the registration, you should have access to those.


### Install the Python Wrapper for the Fitbit API

Depending on your Python installation, it can vary but should look like:

    pip3 install fitbit


### Create a `credentials.py` in the repo.

Create a `credentials.py` at the root of the repo.

Use the `OAuth 2.0 Client ID` that you obtained to create a variable `CLIENT_ID`.

Use the `Client Secret` that you obtained to create a variable `CLIENT_SECRET`.

The `credentials.py` should look something like:

    CLIENT_ID = '<your client id>'
    CLIENT_SECRET = '<your client secret>'

### Run `obtain_token.py`

    python3 obtain_token.py
