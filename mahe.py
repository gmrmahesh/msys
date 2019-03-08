from git import Repo

repo_dir = '/home/ubuntu/Docker/'
repo = Repo(repo_dir)
file_list = [
    'text.py'
]
commit_message = 'Add simple regression analysis'
repo.index.add(file_list)
repo.index.commit(commit_message)
origin = repo.remote('origin')
origin.push()
