import os
from git import Repo

def create_test_repo(repo_dir, commit_messages):
  """
  Creates a Git repository with the specified directory and commits.

  Args:
    repo_dir: The directory to create the repository in.
    commit_messages: A list of commit messages for each commit.
  """
  # Create the repository
  Repo.init(repo_dir)
  repo = Repo(repo_dir)
  readme_path = os.path.join(repo_dir, "README.md")
  
  # Create initial file
  with open(readme_path, "w") as f:
    f.write("Initial content")
  repo.index.add(["README.md"])
  repo.index.commit("Initial commit")

  

  # Create subsequent commits
  for i, message in enumerate(commit_messages):
    with open(readme_path, "a") as f:
      f.write(f"\n\nAdded content for commit {i+1}")
    repo.index.add(["README.md"])
    repo.index.commit(message)

if __name__ == "__main__":
  # Set directory and commit messages
  repo_dir = "test_repo"
  commit_messages = ["Added feature X", "Fixed bug Y"]

  # Create the test repository
  create_test_repo(repo_dir, commit_messages)

  print(f"Test repository created at: {repo_dir}")
