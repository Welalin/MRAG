import os
from git import Repo

def create_test_repo(repo_dir, num_commits, base_message="Added new file "):
  """
  Creates a Git repository with the specified directory and commits.

  Args:
    repo_dir: The directory to create the repository in.
    num_commits: The number of commits to create.
    base_message: The base message for commit messages (can be customized).
  """
  # Create the repository
  Repo.init(repo_dir)
  repo = Repo(repo_dir)

  # Initial commit (optional)
  with open("README.md", "w") as f:
    f.write("Initial content")
  repo.index.add(["README.md"])
  repo.index.commit("Initial commit")
 
  # Generate filenames and commit messages
  filenames = [f"new_file{i+1}.txt" for i in range(num_commits)]
  messages = [f"{base_message}{i+1}" for i in range(num_commits)]

  # Create and commit files
  for filename, message in zip(filenames, messages):
    with open(filename, "w") as f:
      f.write(f"Content for commit {message}")
    repo.index.add([filename])
    repo.index.commit(message)

if __name__ == "__main__":
  # Set directory and number of commits
  repo_dir = "test_repo"
  num_commits = 100

  # Create the test repository
  create_test_repo(repo_dir, num_commits)

  print(f"Test repository created at: {repo_dir}")
