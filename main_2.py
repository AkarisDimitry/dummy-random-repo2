import git
import datetime
import random
import json
import os

# Set the repository URL with credentials
repository_url = "https://AkarisDimitry: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@github.com/AkarisDimitry/dummy-random-repo2.git"

# Set the repository path
repo_path = "."

# Initialize a Git repository
if not os.path.exists(os.path.join(repo_path, '.git')):
    repo = git.Repo.init(repo_path)
else:
    repo = git.Repo(repo_path)

# Remove existing remote repository if it exists
try:
    repo.remote("origin").url
    repo.delete_remote("origin")
except Exception as e:
    pass

# Add the remote repository
repo.create_remote("origin", repository_url)

# Push the changes to the remote repository and set the upstream branch
repo.git.push('--set-upstream', 'origin', 'master')

FILE_PATH = "./data.json"

def make_commit(n):
    if n == 0:
        repo = git.Repo('.')
        repo.git.push()
        return
    x = random.randint(0, 54*6)
    y = random.randint(0, 6)
    date = (datetime.datetime.now() - datetime.timedelta(days=365*7) + datetime.timedelta(days=1) + datetime.timedelta(weeks=x) + datetime.timedelta(days=y)).isoformat()
    data = {'date': date}
    print(date)
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
    repo = git.Repo('.')
    repo.git.add(FILE_PATH)
    repo.git.commit('-m', date, date=date)
    make_commit(n - 1)

make_commit(300)
