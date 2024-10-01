# Message Reader Bot

A Slack bot that reads messages in a channel and can react to them.

## Slack Instructions

1. Go to [Slack API](https://api.slack.com/) and click **Create an App** for the workspace you are in.

2. Click **Create from Manifest** and enter the manifest code below:

    ```json
    {
        "display_information": {
            "name": "Message Reader",
            "description": "Read messages in a channel",
            "background_color": "#4A154B"
        },
        "features": {
            "bot_user": {
                "display_name": "Message Reader",
                "always_online": true
            }
        },
        "oauth_config": {
            "scopes": {
                "user": [
                    "chat:write"
                ],
                "bot": [
                    "channels:history",
                    "channels:read",
                    "chat:write",
                    "reactions:read",
                    "reactions:write"
                ]
            }
        },
        "settings": {
            "event_subscriptions": {
                "bot_events": [
                    "message.channels"
                ]
            },
            "interactivity": {
                "is_enabled": true
            },
            "org_deploy_enabled": false,
            "socket_mode_enabled": true,
            "token_rotation_enabled": false
        }
    }
    ```

3. Click **Install App** and choose the workspace.

4. Click **Allow** to install the app to your workspace.

5. Copy the **Bot User OAuth Token** and paste it into the `.env` file as `SLACK_BOT_TOKEN`.

6. Go to **User Token Scopes** under the **OAuth & Permissions** tab and add the following scope:
   - `chat:write`

7. Click **Install to Workspace**.

8. Copy the **User OAuth Token** and paste it into the `.env` file as `SLACK_USER_TOKEN`.

9. Copy your **User ID** and paste it into the `.env` file as `SLACK_USER_ID`.

10. Go to **Basic Information** and navigate to **App-Level Tokens**. Click **Generate Token and Scopes**.

11. Add a name for the token and assign the following scopes:
   - `connections:write`
   - `authorizations:read`

12. Copy the generated token and paste it into the `.env` file as `SLACK_APP_TOKEN`.

## Code Instructions

1. Install the dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

2. Create a `.env` file in the root directory with the following variables:

    ```
    SLACK_APP_TOKEN=<Your App-Level Token>
    SLACK_BOT_TOKEN=<Your Bot User OAuth Token>
    SLACK_USER_TOKEN=<Your User OAuth Token>
    SLACK_USER_ID=<Your User ID>
    ```

3. Run the app:

    ```bash
    python app.py
    ```