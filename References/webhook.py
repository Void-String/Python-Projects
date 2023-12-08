import requests
url = "https://discord.com/api/webhooks/860010213401559040/Yow5jrRdlBzQ8uawZFCIQO2KW2_vb4bfp_2zSW0z0g5XX4zOU38eefY-A4CJTznfawO1"

data = {
    "content" : "TEST",
    "username" : "TESTUSERNAME"
}

result = requests.post(url, json = data)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(err)
else:
    print("Payload delivered successfully, code {}.".format(result.status_code))