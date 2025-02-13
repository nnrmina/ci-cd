# Pre-Commit Setup for Flask App

This repository contains a simple Flask application with pre-commit hooks to maintain code quality.

## Getting Started

### 1. Fork the Repository
1. Click the **Fork** button on the top-right corner of this repository.
2. This creates a copy of the repository under your GitHub account.
![fork_me.png](assets%2Ffork_me.png)
### 2. Clone the Forked Repository
```sh
# Replace <your-github-username> with your GitHub username
git clone https://github.com/<your-github-username>/ci-cd-primer.git
cd your-repo
```

### 3. Install Pre-Commit Locally
Make sure you have Python installed, then run:
```sh
pip install pre-commit
```

### 4. Enable Pre-Commit Hooks
Run the following command inside the cloned repository:
```sh
pre-commit install
```

This sets up pre-commit hooks to automatically check your code when you make a commit.

### 5. Test Pre-Commit
To verify that the hooks are working, run:
```sh
pre-commit run --all-files
```
This will run all checks on existing files.

### 6. Start Coding
Now you can modify and commit files. The pre-commit hooks will check your code before every commit.
```sh
git add .
git commit -m "Your message"
```
If any issues are found, pre-commit will warn you and suggest fixes.

### 7. Push Changes
Once all checks pass, push your changes to your forked repository:
```sh
git push origin main
```

Now you're ready to work with this Flask app using pre-commit hooks! 🚀
