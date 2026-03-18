# Plan: Guided Analysis & Preset Searches

## Goal
Transform the log analyzer from a raw data viewer into a guided investigation tool. Non-technical users should be able to identify a subject (user) and then ask common "Plain English" questions to filter the logs instantly.

## 1. User Experience Flow
1.  **Subject Selection**: After log upload, the user selects a "Subject of Interest" (e.g., `kristen.emond`) from a prominent dropdown or the "Top Users" list.
2.  **Guided Questions**: Once a user is selected, a "What are you looking for?" section appears with preset, human-readable buttons.
3.  **Instant Filtering**: Clicking a preset applies a complex multi-field filter and updates the table/stats immediately.

## 2. Proposed Preset Mappings (Plain English to Log Logic)

| Button Label | Logic (Event Type / Service) | Description |
| :--- | :--- | :--- |
| **Group Changes** | `event_type: association_change` | Shows when the user was added to or removed from groups/apps. |
| **Login Activity** | `event_type: *login*` OR `*auth*` | Shows all successful and failed sign-in attempts. |
| **Password Updates** | `event_type: *password_update*` | Tracks when the user changed or reset their password. |
| **App Access** | `event_type: sso_auth` | Lists every SSO application the user launched. |
| **Admin Actions** | `initiated_by.type: admin` (as initiator) | If the subject is an admin, show actions they performed on others. |
| **Lockouts/Failures** | `success: false` | Focuses purely on where the user ran into trouble. |

## 3. UI/UX Changes
- **"The Investigation Hub"**: A new UI component below the stats cards that activates once a user is selected.
- **Preset "Pills"**: Visual buttons for the presets listed above.
- **Active Filter Breadcrumbs**: Clear indicator of what is currently being filtered (e.g., "Showing **Group Changes** for **kristen.emond**") with an "X" to clear.

## 4. Technical Implementation Strategy
- **Centralized Preset Registry**: A JavaScript object mapping labels to filter functions.
- **Query Parameter Support**: (Optional) Allow the URL to store the search state so an investigation can be shared.
- **Enhanced Search Engine**: Update `applyFilters()` to handle "OR" logic and partial matches for the presets (e.g., matching both `user_login_attempt` and `sso_login_success` under "Login Activity").

## 5. Metadata Enrichment
- When a preset is active, the "Plain English" explanation should highlight the specific data relevant to that search (e.g., for "Group Changes", bold the group name).

---
*Prepared by Gemini CLI - March 17, 2026*
