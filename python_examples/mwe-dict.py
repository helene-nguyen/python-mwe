# dict_key = list({}.keys())
# value = dict_key[{}]
# another_dict = {}
# # another_dict[dict_key] = True

# is_working = another_dict.get(value) is None

# print(another_dict)

# state = {"last_run": "DATE"}
#
# print("state 1:", state)
#
# state.update({"last_successful": "TEST"})
# print("state 1:", state)


import json

alert = {
    "DisplayName": "Suspicious Login Attempt",
    "SystemAlertId": "ALERT-123456",
    "Status": "Active",
    "AlertSeverity": "High",

    "StartTime": "2025-05-27T12:00:00Z",
    "EndTime": "2025-05-27T12:30:00Z",
    "TimeGenerated": "2025-05-27T12:01:00Z",
    "Tactics": "Initial Access",
    "Description": "A suspicious login attempt was detected from an unusual location.",
    "RemediationSteps": json.dumps([
        "Reset the user's password.",
        "Review recent account activity.",
        "Enable multi-factor authentication."
    ])
}

incident_description = (
    f"**Display Name**: {alert.get('DisplayName')}  \n"
    f"**Alert ID**: {alert.get('SystemAlertId')}  \n"
    f"**Status**: {alert.get('Status')}  \n"
    f"**Severity**: {alert.get('AlertSeverity')}  \n"
    f"**Alert Type**: {alert.get('AlertType')}  \n"
    f"**Start Time (UTC)**: {alert.get('StartTime')}  \n"
    f"**End Time (UTC)**: {alert.get('EndTime')}  \n"
    f"**Time Generated (UTC)**: {alert.get('TimeGenerated')}  \n"
    f"**Tactics**: {alert.get('Tactics')}  \n"
    f"**Description**: {alert.get('Description')}  \n"
    f"**Remediation**:  \n{''.join([f"{step}  \n" for step in json.loads(alert.get('RemediationSteps', "[]"))])}  \n"
)

print(incident_description)