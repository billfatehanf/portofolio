# Portfolio Project Setup

## 🛠️ Tools Installed

### 1. Cursor IDE
- **Source:** [https://cursor.com/](https://cursor.com/)
- **Type:** AI-powered code editor (fork of VS Code)
- **Version:** Latest stable release
- **Purpose:** Primary development environment for writing and editing code with AI assistance

### 2. Claude Code (Cursor Extension)
- **Source:** Cursor Extensions Marketplace (search: "Claude Code")
- **Type:** AI coding assistant add-on
- **Purpose:** Integrates Anthropic's Claude AI directly into Cursor for code generation, review, and pair programming

### 3. Codex (Cursor Extension)
- **Source:** Cursor Extensions Marketplace (search: "Codex")
- **Type:** AI coding assistant add-on
- **Purpose:** Provides OpenAI Codex-powered code completions and suggestions within Cursor

---

## ✅ Steps Completed

### Step 1 — Install Cursor IDE
1. Visited [https://cursor.com/](https://cursor.com/) and downloaded the Linux installer (`.AppImage` / `.deb` package).
2. Installed Cursor and launched it successfully.
3. Completed initial setup (theme, keybindings, etc.).

### Step 2 — Add Claude Code Extension
1. Opened the Extensions panel in Cursor (`Ctrl+Shift+X`).
2. Searched for **"Claude Code"** in the marketplace.
3. Clicked **Install** and waited for the extension to activate.
4. Logged in to the Claude account via the extension's authentication flow.

### Step 3 — Add Codex Extension
1. Opened the Extensions panel in Cursor (`Ctrl+Shift+X`).
2. Searched for **"Codex"** in the marketplace.
3. Clicked **Install** and waited for the extension to activate.
4. Logged in / provided API credentials as required by the extension.

### Step 4 — Create a Public GitHub Repository
1. Navigated to [https://github.com/](https://github.com/billfatehanf) and logged in (account was already created).
2. Clicked **New Repository**.
3. Set the repository name, added a description, and set visibility to **Public**.
4. Initialized the repository with a `README.md`.
5. Copied the repository URL for cloning.

### Step 5 — Open the Repository in Cursor
1. Cloned the repository locally using the terminal:
   ```bash
   git clone https://github.com/billfatehanf/portofolio.git
   ```
2. Opened Cursor and used **File → Open Folder** to open the cloned repository directory.
3. Confirmed the project was loaded correctly in the Explorer panel.

---

## ⚠️ Issues Encountered & Solutions

### Issue 1 — Cursor Installation on Linux
- **Problem:** The downloaded `.AppImage` file was not executable by default on Linux.
- **Solution:** Made it executable via terminal:
  ```bash
  chmod +x cursor-*.AppImage
  ./cursor-*.AppImage
  ```

### Issue 2 — Claude Code Extension Login
- **Problem:** The authentication window did not open automatically after installation.
- **Solution:** Triggered login manually via the Command Palette (`Ctrl+Shift+P`) → searched for **"Claude: Sign In"** and followed the browser-based OAuth flow.

### Issue 3 — Codex Extension API Key Setup
- **Problem:** The Codex extension required an OpenAI API key which was not immediately obvious from the UI.
- **Solution:** Opened extension settings (`Ctrl+,` → searched "Codex") and pasted the API key in the designated field. Restarted Cursor to apply the changes.

### Issue 4 — Git Not Configured
- **Problem:** Running `git clone` produced a warning about missing global git configuration (`user.name` and `user.email`).
- **Solution:** Configured git globally before proceeding:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your@email.com"
  ```

---

## 📁 Project Structure

```
Portofolio/
└── README.md        ← This file
```

---

## 📅 Setup Date

> April 13, 2026

---

## 👤 Bill Fatehan Fathoni

Personal portfolio repository — set up as part of the developer environment configuration process.
