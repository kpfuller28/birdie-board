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

       git checkout -b feature/your-feature-name

2. Work on your changes.

3. Stage and commit changes:

       git add .
       git commit -m "Your descriptive commit message"

4. Push your feature branch:

       git push origin feature/your-feature-name

5. Open a Pull Request on GitHub and request a review.

---