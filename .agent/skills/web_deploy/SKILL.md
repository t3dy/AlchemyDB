---
name: Deploy Website
description: Automates the full deployment of the AlchemyDB website to GitHub Pages, ensuring database updates are propagated.
---

# Deploy Website Skill

This skill allows you to reliably update the live AlchemyDB website (https://t3dy.github.io/AlchemyDB/) with the latest code and database content.

## When to Use
Use this skill whenever the user asks to:
- "Update the website"
- "Deploy changes"
- "Push to github" (if they imply updating the live site)
- "Fix the dashboard"

## Instructions

1.  **Run the Deployment Script:**
    Execute the following command in the terminal:
    ```powershell
    ./scripts/deploy_website.ps1
    ```

2.  **Monitor Output:**
    - Ensure the database export succeeds.
    - Ensure the npm build succeeds.
    - Ensure the git push to `gh-pages-manual` succeeds.

3.  **Verify Deployment:**
    - Wait 30-60 seconds after the script finishes.
    - Run a curl check to verify the new build is serving:
      ```powershell
      Invoke-WebRequest -Uri "https://t3dy.github.io/AlchemyDB/" -UseBasicParsing | Select-Object -ExpandProperty Content | Select-String -Pattern "index-.*\.js"
      ```

4.  **Notify User:**
    - Confirm success.
    - Remind them to **HARD REFRESH** (Ctrl+Shift+R) their browser.
    - Provide the link: https://t3dy.github.io/AlchemyDB/

## Troubleshooting
- If `gh-pages-manual` push fails, check if the remote URL is correct.
- If the live site shows old data, ask the user to clear their cache explicitly.
