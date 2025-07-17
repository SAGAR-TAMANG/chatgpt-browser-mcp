# ChatGPT Browser MCP

This project provides an MCP (Model-Client-Protocol) server that allows an AI model, like Claude, to control a local Chrome browser to interact with ChatGPT. It exposes a `run_chatgpt` tool that can be called by an MCP client to get responses directly from the ChatGPT web interface.

This is useful for tasks that require interacting with the most up-to-date version of ChatGPT or for leveraging its capabilities within a larger automated workflow controlled by an AI agent.

-----

## 🎥 Video Tutorial

Coming Soon..
<!-- For a complete walkthrough of the setup, configuration, and usage, please watch the video tutorial below.

[![Watch the video tutorial](https://img.youtube.com/vi/tzenr4y6Cp0/0.jpg)](http://www.youtube.com/watch?v=tzenr4y6Cp0) -->

-----

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed:

1.  **Python 3.8+**
2.  **[uv](https://github.com/astral-sh/uv)**: An extremely fast Python package installer and resolver.
    ```shell
    # Install uv on macOS and Linux
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # Install uv on Windows
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
3.  **Google Chrome**: A standard installation of the Google Chrome browser.

-----

## 🚀 Setup and Installation

Follow these steps to get the server up and running.

### 1\. Clone the Repository

First, clone this repository to your local machine.

```shell
git clone https://github.com/SAGAR-TAMANG/chatgpt-browser-mcp.git
cd chatgpt-browser-mcp
```

### 2\. Install Dependencies

Use `uv` to create a virtual environment and install the required Python packages. If you do not have uv, install it.

```shell
# Create and activate a virtual environment
uv venv
.venv\Scripts\activate

# Install dependencies
uv pip install .
```

### 3\. Configure File Paths

This is the most important step. You **must** edit the `main.py` file to point to your local Chrome installation and user profile.

Open `main.py` and modify the following configuration variables:

```python
# --- Config ---

# ⚠️ UPDATE THIS: Path to your Google Chrome executable
browser_1 = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# ⚠️ UPDATE THIS: Path to a directory for user data.
# Using a temporary or secondary profile is recommended.
profile_dir = "C:/Users/YOUR_USERNAME/Documents/MyChromeProfile"

# ⚠️ UPDATE THIS: The name of the profile to use within the profile_dir.
profile_name = "Profile 1"
```

**How to find these paths:**

  - **`browser_1` (Chrome Executable)**:
      - **Windows**: Usually `C:/Program Files/Google/Chrome/Application/chrome.exe`.
      - **macOS**: `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`.
  - **`profile_dir` & `profile_name`**:
      - Find your Chrome profile path by navigating to `chrome://version` in your browser and looking for the "Profile Path" field.
      - It's highly recommended to create a new, separate folder for `profile_dir` to avoid interfering with your main browser profile.

> [!CAUTION]
> Latest Chrome versions **require** you to create a separate copy of your profile_dir.

-----

## 🔌 Connecting to Claude Desktop Client

With the server running, you can connect to Claude MCP Client.

```
uv run mcp install main.py
```
This will add the this MCP to config.json of Claude Desktop App.

-----

## ⚠️ Important Notes

  - **Fragile Automation**: This tool relies on fixed `asyncio.sleep()` timers and finding UI elements on the ChatGPT website. If ChatGPT updates its user interface, this script may break and will require updates.
  - **Clipboard Usage**: The response is retrieved by clicking the "Copy" button and reading from the system clipboard via `pyperclip`. This means that if you copy other text while the tool is running, it may interfere with the result.
  - **Security**: The tool controls a browser that may be logged into your personal accounts. Be aware of the security implications of allowing a script this level of access.

-----

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.
