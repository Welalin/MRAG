import os
from git import Repo
import shutil  # Import shutil for directory removal


def removeDir(repo_dir):
   if os.path.exists(repo_dir):
      try:
      # Attempt to remove the existing directory
         shutil.rmtree(repo_dir)
         print(f"Existing directory '{repo_dir}' removed.")
      except OSError as e:
         print(f"Error removing directory '{repo_dir}': {e}")
   return  # Exit if removal fails

def create_test_repo(repo_dir, num_commits_per_branch, branch_names):
  """
  Creates a Git repository with multiple branches, commits, and merges.

  Args:
    repo_dir: The directory to create the repository in.
    num_commits_per_branch: The number of commits to create in each branch.
    branch_names: A list of branch names to create.
  """
  # Create the repository
  Repo.init(repo_dir)
  repo = Repo(repo_dir)
  readme_path = os.path.join(os.getcwd(), "test_repo", "README.md")

#   readme_path = os.path.join(repo_dir, "README.md")

  # Initial commit (optional)
  with open(readme_path, "w") as f:
    f.write("Initial content")
  repo.index.add([readme_path])
  repo.index.commit("Initial commit")

  # Generate base message
  base_message = "Added new file "

  for branch_name in branch_names:
    # Checkout a new branch
    repo.create_head(branch_name)
    repo.head.reference = branch_name

    # Generate filenames and commit messages
    filenames = [os.path.join(os.getcwd(), "test_repo", f"new_file{i+1}.txt") for i in range(num_commits_per_branch)]
    messages = [f"{base_message}{i+1}" for i in range(num_commits_per_branch)]

    # Create and commit files
    for filename, message in zip(filenames, messages):
      print(filename)
      with open(filename, "w") as f:
        f.write(f"Content for commit {message}")
      repo.index.add([filename])
      repo.index.commit(message)

    # Checkout back to main branch
    repo.head.reference = "master"

    # Merge all branches to main branch using GitPython >= 1.0
    if hasattr(repo, 'merge'):
        for branch_name in branch_names:
            try:
                repo.merge(branch_name)
            except GitCommandError as e:
                print(f"Error merging branch '{branch_name}': {e}")
    else:
        print("Warning: GitPython version may be older. Branch merging functionality might not be available.")

    print(f"Test repository created at: {repo_dir}")

  print(f"Test repository created at: {repo_dir}")


if __name__ == "__main__":
  # Set directory, number of commits per branch, and branch names
  repo_dir = "test_repo"
  removeDir(repo_dir)
  num_commits_per_branch = 2  # Adjust this value for desired number of commits per branch
  branch_names = ["feature1", "feature2", "feature3", "feature4", "feature5"]

  # Create the test repository
  create_test_repo(repo_dir, num_commits_per_branch, branch_names)

  print(f"Branches merged to main branch.")
