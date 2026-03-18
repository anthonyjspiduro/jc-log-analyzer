# JumpCloud Log Analyzer

A secure, local-only web application for analyzing JumpCloud Activity Logs. This tool parses JSON or NDJSON log files entirely in your browser—no data ever leaves your machine.

## 🚀 Features

-   **Two Viewing Modes**:
    -   **Basic Mode (Default)**: Translates complex JSON log data into plain English sentences with location, device, and IP context.
    -   **Advanced Mode**: Shows the raw JSON structure for deep technical investigation.
-   **Guided Analysis (Investigation Hub)**: Select a user to unlock preset "Plain English" searches:
    -   👥 **Group Changes**: Track additions/removals from groups and apps.
    -   🔐 **Login Activity**: Monitor all sign-in attempts and methods.
    -   🚀 **App Access**: See exactly which SSO applications a user launched.
    -   ⚠️ **Lockouts/Failures**: Quickly identify why a user is having trouble.
-   **Smart Success Detection**: Correctly identifies successes in complex SSO events (`sso_auth`).
-   **Local & Secure**: 100% client-side. No server-side processing or data storage.

## 📁 Project Structure

-   `src/`: Contains the core application logic and assets.
    -   `jc-analyzer.html`: The main web application.
    -   `extract_keys.py`: A utility script to identify all unique fields in a log file.
-   `docs/`: Documentation on log fields and project plans.
-   `sample/`: (Optional) Directory for storing your JumpCloud log files.

## 🛠️ Usage

### Web Analyzer
1.  Open `src/jc-analyzer.html` in any modern web browser.
2.  Drag and drop your JumpCloud Activity Log (JSON or NDJSON) into the drop zone.
3.  Use the "Top Users" list or search bar to find a subject.
4.  Click any row to see the "Plain English" explanation of the event.

### Key Extractor (CLI)
If you need to see every unique field present in a large log file:
```bash
python3 src/extract_keys.py sample/your_log_file.json
```

## ⚖️ License
This project is licensed under the MIT License - see the `LICENSE` file for details.

---
*Developed for MTS Pro Services | Talos Fleet Management*
