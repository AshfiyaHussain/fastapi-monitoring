# Python 3.9 Installation Guide

This guide provides instructions on how to install Python 3.9 on various operating systems.
You can choose any version of python thats compatible with the given packages in requirements.txt.

You can also checkout https://github.com/pyenv/pyenv to manage and install multiple versions of python

---

## 1. Windows

### Steps:

#### Download the Installer:

- Visit the [official Python downloads page](https://www.python.org/downloads/).
- Choose Python 3.9.x and download the installer for Windows.

#### Run the Installer:

1. Double-click the downloaded installer.
2. **Important**: Check `Add Python 3.9 to PATH` before proceeding.
3. Choose `Customize installation` if needed, or proceed with the default settings.

#### Verify Installation:

Open Command Prompt or PowerShell and type:

```bash
python --version
```

---

## 2. macOS

### Steps:

#### Use Homebrew (Recommended):

1. Install Homebrew if you haven’t already:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Python 3.9:
   ```bash
   brew install python@3.9
   ```

#### Verify Installation:

Check the version:

```bash
python3.9 --version
```

---

## 3. Linux

### Ubuntu/Debian

#### Update Package Lists:

```bash
sudo apt update
```

#### Install Python 3.9:

```bash
sudo apt install python3.9 python3.9-venv python3.9-dev -y
```

#### Verify Installation:

```bash
python3.9 --version
```

### CentOS/RHEL

#### Enable EPEL Repository:

```bash
sudo yum install epel-release -y
```

#### Install Python 3.9:

```bash
sudo yum install python39 -y
```

#### Verify Installation:

```bash
python3.9 --version
```

---

## Additional Notes

- For other distributions or advanced configurations, refer to the [official Python installation documentation](https://docs.python.org/3/using/index.html).
- Ensure you have administrative privileges to perform installations on your system.

# Virtual Environment Setup Guide

This guide outlines the steps to create and use a virtual environment for your Python project, including installing dependencies and running a FastAPI application.

---

## Prerequisites

- Python installed on your system
- `pip` (Python's package manager) installed

---

## Steps to Set Up and Use a Virtual Environment

### 1. Install `virtualenv` (if not already installed)

```bash
pip install virtualenv
```

Alternatively, use Python's built-in `venv` module:

```bash
python3 -m venv venv
(or)
python -m venv venv
```

---

### 2. Create a Virtual Environment

Navigate to your project directory and create a virtual environment named `venv`:

```bash
virtualenv venv
```

---

### 3. Activate the Virtual Environment

#### On Windows:

```bash
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
source venv/bin/activate
```

---

### 4. Install Dependencies in the Virtual Environment

Once the virtual environment is activated, install the necessary packages:

```bash
pip install -r requirements.txt
```

---

### 5. Run the Application in the Virtual Environment

With the virtual environment activated, run your FastAPI app:

```bash
uvicorn api:app --reload
```

---

## Additional Notes

- To deactivate the virtual environment, use the command:
  ```bash
  deactivate
  ```

Happy coding!
