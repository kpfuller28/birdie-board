# Birdie Board

A simple Django-powered golf scorecard app. This project uses a `Makefile` to simplify common development tasks, and assumes a feature branch Git workflow for collaboration.

## Setup Instructions

Follow the steps below to get your development environment ready:

### 1. Clone the Repository

Clone the GitHub repository to your local machine.

    git clone https://github.com/kpfuller28/birdie-board.git
    cd birdie-board

### 2. Create a Virtual Environment (only required the first time)

    make venv

### 3. Install Python Dependencies

    make install

### 4. Run Migrations

    make migrate

### 5. Start the Development Server

    make run

## Optional Virtual Environment Use

The Makefile commands temporarily activate the virtual environment just for each command. If you prefer to work within a persistent virtual environment session (such as when running multiple commands or using the Python shell), activate it manually:

- On macOS/Linux:

      source venv/bin/activate

- On Windows (Git Bash or Command Prompt):

      venv\Scripts\activate

You can exit the virtual environment anytime using:

    deactivate

## Development Workflow (Feature Branches)

1. Create a new feature branch:

       git checkout -b your-feature-name

2. Work on your changes.

3. Stage and commit changes:

       git add .
       git commit -m "Your descriptive commit message"

4. Push your feature branch:

       git push origin your-feature-name

5. Open a Pull Request on GitHub and request a review.

## Keeping Your Feature Branch Updated with Main

When working on a feature branch, it’s important to keep it up to date with the latest changes from the `main` branch. This ensures that you’re working with the most current version of the codebase and helps prevent difficult merge conflicts later.

Follow these steps periodically while working on your feature branch:

### 1. Commit your work
Before switching branches, make sure your work is committed:
```
git add .
git commit -m "WIP: your message here"
```

### 2. Switch to the main branch
```
git checkout main
```

### 3. Pull the latest changes from GitHub into main
This brings your local `main` branch up to date:
```
git pull origin main
```

### 4. Switch back to your feature branch
```
git checkout your-feature-branch
```

### 5. Merge updated main into your feature branch
```
git merge main
```

If you get merge conflicts here, Git will tell you which files need to be resolved. After resolving, commit the changes:
```
git add .
git commit -m "Resolve merge from main"
```

### Notes
- `git merge main` is preferred over `git merge origin/main` because it uses your local up-to-date `main`.
- Always ensure `main` is current by pulling from origin before merging.

Repeat this process regularly during long-running work on a feature branch.

---
