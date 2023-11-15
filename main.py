import requests, json, time

print("TheBigThing.txt Creator - Created by: sevenworks.eu.org")
print("Harvesting is now running in the background, to avoid errors please create ids.txt with level ids seperated by newlines. This scrapes pretty fast and may cause duplicates so use the clean tool.")

def harvest(joemama):
    with open("thebigthing.txt", "a") as file:
        for level in joemama:
            try:
                for page in range(1, 195 + 1):
                    url = f"https://gdbrowser.com/api/comments/{level}?count=100&page={page}"
                    response = requests.get(url)

                    if response.status_code == 200:
                        comments = response.json()

                        for comment in comments:
                            username = comment.get("username")
                            account_id = comment.get("accountID")

                            if username and account_id:
                                line = f"{username}:{account_id}\n"
                                file.write(line)
                    else:
                        pass
            except:
                pass

                time.sleep(0.7)

joemama = [line.strip() for line in open("ids.txt")]
harvest(joemama)