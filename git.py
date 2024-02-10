def fetch_user_info():
    response = requests.get('https://api.github.com/user', headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        print("User login:", user_info['login'])
        print("User name:", user_info.get('name'))
    else:
        print("Failed to fetch user information")

fetch_user_info()
