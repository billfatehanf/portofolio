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
├── README.md
└── research/
    ├── sources.md                     ← Master list of all 10 experts
    ├── linkedin-posts/
    │   ├── justin-welsh.md
    │   ├── chris-walker.md
    │   ├── dave-gerhardt.md
    │   ├── jason-lemkin.md
    │   ├── april-dunford.md
    │   ├── elena-verna.md
    │   ├── anthony-pierri.md
    │   ├── morgan-ingram.md
    │   ├── sangram-vajre.md
    │   └── kyle-poyar.md
    ├── youtube-transcripts/
    │   ├── justin-welsh.md
    │   ├── chris-walker.md
    │   ├── dave-gerhardt-exitfive.md
    │   ├── jason-lemkin-saastr.md
    │   ├── april-dunford.md
    │   ├── elena-verna.md
    │   ├── anthony-pierri.md
    │   ├── morgan-ingram.md
    │   ├── sangram-vajre.md
    │   └── kyle-poyar.md
    └── other/
        └── key-themes.md              ← Cross-expert synthesis
```

---

## 🔬 Research Project: LinkedIn Organic Content Strategy for B2B SaaS

### Why This Topic?

LinkedIn organic content strategy for B2B SaaS was chosen because:

1. **High practitioner density** — Unlike many marketing topics, LinkedIn B2B strategy has a large community of experts who *actively practice* what they teach, making it easy to find real-world evidence.
2. **Measurable impact** — LinkedIn organic content directly influences pipeline, recruiting, and brand in B2B SaaS, with experts openly sharing metrics and frameworks.
3. **Rapidly evolving** — The 2025–2026 landscape (AI commoditization, algorithm changes, the rise of "dark social") makes this a timely and dynamic research area.
4. **Cross-functional relevance** — The topic spans marketing, sales, product, and leadership — providing diverse expert perspectives.

### Experts Selected (10)

| # | Expert | Role / Company | Primary Focus |
|---|--------|---------------|---------------|
| 1 | **Justin Welsh** | Solopreneur | LinkedIn systems, content repurposing, personal branding |
| 2 | **Chris Walker** | CEO, Passetto | Demand generation, dark social, anti-MQL movement |
| 3 | **Dave Gerhardt** | Founder, Exit Five | Founder-led marketing, community building, B2B playbooks |
| 4 | **Jason Lemkin** | Founder, SaaStr | SaaS scaling, AI transformation, organic as competitive moat |
| 5 | **April Dunford** | Positioning Consultant | Product positioning, sales narratives, messaging frameworks |
| 6 | **Elena Verna** | Growth Advisor | Growth loops, PLG, product-led sales, trust as moat |
| 7 | **Anthony Pierri** | Co-Founder, FletchPMM | Homepage messaging, positioning execution, use-case anchoring |
| 8 | **Morgan Ingram** | Founder, AMP Creative | Social selling, LinkedIn video, content-driven prospecting |
| 9 | **Sangram Vajre** | CEO, GTM Partners | ABM/ABX, GTM operating system, community-led growth |
| 10 | **Kyle Poyar** | Solopreneur (ex-OpenView) | PLG pricing, data-driven content, personal brand portability |

**Selection criteria:** Each expert was chosen because they *actively practice* LinkedIn organic content strategy — not just write about it. They have built audiences, companies, and revenue streams primarily through LinkedIn organic content.

### Data Collected

| Category | Count | Details |
|----------|-------|---------|
| **LinkedIn Posts** | 50 posts | 5 curated posts per expert × 10 experts |
| **YouTube Transcripts** | 20 videos | 2 videos per expert × 10 experts |
| **Key Themes Synthesis** | 10 themes | Cross-expert analysis identifying common patterns |

### Key Findings

The top 10 themes that emerged across all experts:

1. **People follow people, not brands** — Personal profiles outperform company pages
2. **Demand creation > lead capture** — Ungated content builds pipeline; MQLs are dying
3. **Positioning comes first** — All content must flow from clear strategic positioning
4. **Consistency compounds** — Multi-year daily posting creates exponential returns
5. **Zero-click content wins** — Full value within posts; no external links
6. **Content systems > one-off creation** — Repurpose one source into many posts
7. **Trust is the ultimate moat** — Authentic human content beats AI-generated content
8. **LinkedIn is a full-stack tool** — Serves pipeline, recruiting, research, and more
9. **Data + specificity outperform** — Real numbers and examples beat generic advice
10. **Content-community loop** — LinkedIn + community creates a self-reinforcing flywheel

For detailed analysis, see [`research/other/key-themes.md`](research/other/key-themes.md).

---

## 📅 Setup Date

> April 13, 2026

## 📅 Research Date

> April 14, 2026

---

## 👤 Bill Fatehan Fathoni

Personal portfolio repository — set up as part of the developer environment configuration process. Research project on LinkedIn organic content strategy for B2B SaaS.
