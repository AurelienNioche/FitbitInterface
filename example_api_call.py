from fitbit import Fitbit
import json
from credentials import CLIENT_ID, CLIENT_SECRET


def main():

    try:
        with open('credentials_user.json', 'r') as f:
            user_credentials = json.load(f)
            access_token = user_credentials['access_token']
            refresh_token = user_credentials['refresh_token']

    except FileNotFoundError:
        print("Your should run `obtain_toke.py` first")

    fb = Fitbit(access_token=access_token, refresh_token=refresh_token,
                client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

    print(fb.intraday_time_series('activities/heart', detail_level='1sec',
                                  start_time='16:30', end_time='16:32', ))

    # rsp = fb.make_request("https://api.fitbit.com/1/user/-/activities/heart/date/today/1d/1sec/time/16:30/16:32.json")
    # print(rsp)


if __name__ == "__main__":
    main()