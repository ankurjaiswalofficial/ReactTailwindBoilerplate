import time
from git import Repo
import requests


def commit_changes(repo_dir, commit_msg):
    branch_name = ""
    success = False
    try:
        print("Debug: Came Here")
        repo = Repo(repo_dir)
        index = repo.git
        # Add all changes to the index
        branch_name = repo.active_branch.name
        index.add(A = True)

        # Commit changes with the specified message
        index.commit(m=commit_msg)
        print(f"Changes committed with message: {commit_msg}")
        origin = repo.remote(name='origin')
        origin.push()
        success = True
    except Exception as e:
        print(f"Error committing changes: {e}")
    return (branch_name, success)


if __name__ == "__main__":
    repo_directory = "."
    commit_message = "Updated Code"

    print("Auto Commit Program Started \n")
    while True:
        branch_name, success = commit_changes(repo_directory, commit_message)
        time.sleep(0.2)
