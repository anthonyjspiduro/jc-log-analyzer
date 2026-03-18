# JumpCloud Activity Log Fields

This document lists all unique fields identified in the JumpCloud activity logs. The fields are grouped by their logical function.

## Core Fields
- `@version`: Version of the log format.
- `id`: Unique identifier for the log entry.
- `timestamp`: UTC timestamp of the event.
- `event_type`: The type of event (e.g., `ldap_srch`, `user_login_attempt`).
- `service`: The JumpCloud service involved (e.g., `ldap`, `sso`, `directory`).
- `organization`: The organization ID.
- `success`: Boolean indicating if the operation was successful.
- `error_code`: Numeric error code, if any.
- `error_message`: Human-readable error message.

## Initiator Information
- `initiated_by`: Object containing details about who/what started the event.
    - `initiated_by.type`: Type of initiator (e.g., `user`, `administrator`, `system`).
    - `initiated_by.id`: ID of the initiator.
    - `initiated_by.username`: Username of the initiator.
    - `initiated_by.email`: Email of the initiator.
    - `initiated_by.name`: Display name of the initiator.
- `client_ip`: IP address of the client.
- `username`: The username targeted or used in the event.
- `jc_initiated_by_id` / `jc_initiated_by_email`: Alternative fields for initiator info.

## Geolocation & User Agent
- `geoip`: Geographic information based on `client_ip`.
    - `geoip.country_code`, `geoip.region_name`, `geoip.city`, `geoip.latitude`, `geoip.longitude`, `geoip.timezone`.
- `useragent`: Details about the client's browser/OS.
    - `useragent.name`, `useragent.version`, `useragent.os`, `useragent.device`.

## Authentication & Security
- `auth_context`: Detailed authentication context.
    - `auth_context.auth_methods`: Methods used (password, TOTP, etc.) and their success status.
    - `auth_context.policies_applied`: Conditional access policies that were evaluated.
- `mfa`: Multi-factor authentication details.
- `tls_established`: Boolean for secure connection status.
- `start_tls`: Boolean for STARTTLS status.

## Resource & System Information
- `resource`: The resource being accessed or modified.
    - `resource.type`, `resource.id`, `resource.name`, `resource.hostname`.
- `application`: Application-specific details for SSO/SAML events.
    - `application.name`, `application.display_label`, `application.sso_url`.
- `system`: System-specific details for agent/device events.
    - `system.hostname`, `system.osFamily`, `system.id`.

## Operations & Changes
- `operation_type`: Type of operation (e.g., `SEARCH RESULT`, `UPDATE`).
- `changes`: List of changes made to an object.
    - `changes.field`, `changes.from`, `changes.to`.
- `association`: Details about object associations (e.g., adding a user to a group).
- `association.connection`: The 'from' and 'to' objects in the association.

## LDAP Specific
- `dn`: Distinguished Name used in LDAP queries.
- `filter`: The LDAP filter used.
- `scope`: LDAP search scope.
- `base`: LDAP base DN.
- `deref`: LDAP dereference policy.

## Miscellaneous
- `connection_id`: Unique ID for the network connection.
- `message`: General descriptive message.
- `windows_meta`: Metadata for Windows-specific events (e.g., logon type).
