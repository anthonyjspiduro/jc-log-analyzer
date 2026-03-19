# JumpCloud Log Analyzer

A secure, local-only web application for analyzing JumpCloud Activity Logs. This tool parses JSON or NDJSON log files entirely in your browser—no data ever leaves your machine.

## 🌐 Live Version
Access the analyzer directly in your browser:  
**[Open JumpCloud Log Analyzer](https://anthonyjspiduro.github.io/jc-log-analyzer/src/jc-analyzer.html)**
## 🚀 Features

-   **Activity Trend Chart**: Visualizes event volume and failure rates over the last 24 active hours to instantly spot spikes or system anomalies.
-   **Geolocation Summary**: Identifies top cities and countries of origin for all activity to detect anomalous geographic access.
-   **Deep-Dive Analytics**: Select a specific user to view a dedicated investigation dashboard featuring their top locations, action types, and resource interaction history.
-   **Global Discovery (Quick Filters)**: Instantly filter the entire log file or specific users with preset "Plain English" searches:
    -   👥 **Group Changes**: Track additions/removals from groups and apps.
    -   🔐 **Login Activity**: Monitor all sign-in attempts and methods.
    -   🚀 **App Access**: See exactly which SSO applications were launched.
    -   🔄 **Provisioning**: Track automated user access changes in connected apps (SCIM).
    -   ⚠️ **Lockouts/Failures**: Quickly identify why a user is having trouble.
-   **Smart Noise Reduction**: Toggle "Hide Service Accounts" to automatically filter out high-volume LDAP bind noise (`svc-ldap-bind`, etc.).
-   **Ultra-Wide Layout**: Optimized for 4K and large displays to view long log events without truncation.
-   **Two Viewing Modes**:
    -   **Basic Mode (Default)**: Translates complex JSON log data into plain English sentences with location, device, and IP context.
    -   **Advanced Mode**: Shows the raw JSON structure for deep technical investigation.
-   **Local & Secure**: 100% client-side. No server-side processing or data storage.

## 📁 Project Structure
    -   `jc-analyzer.html`: The main web application.
    -   `extract_keys.py`: A utility script to identify all unique fields in a log file.
-   `docs/`: Documentation on log fields and project plans.
-   `sample/`: (Optional) Directory for storing your JumpCloud log files.

## 🛠️ Usage

### Web Analyzer
1.  **Live**: [Open the JumpCloud Log Analyzer](https://anthonyjspiduro.github.io/jc-log-analyzer/src/jc-analyzer.html) directly in your browser.
2.  **Local**: Open `src/jc-analyzer.html` from this repository in any modern web browser.
3.  Drag and drop your JumpCloud Activity Log (JSON or NDJSON) into the drop zone.
4.  Use the "Top Users" list or search bar to find a subject.
5.  Click any row to see the "Plain English" explanation of the event.

### Key Extractor (CLI)
If you need to see every unique field present in a large log file:
```bash
python3 src/extract_keys.py sample/your_log_file.json
```

## ⚖️ License
This project is licensed under the MIT License - see the `LICENSE` file for details.

---
*Developed for MTS Pro Services | Talos Fleet Management*
