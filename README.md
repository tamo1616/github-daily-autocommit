# GitHub Daily Auto-Commit Repository

This repository automatically commits once daily at a specified time using GitHub Actions.

## Why Use This?

On GitHub, many developers contribute their code and work every day. Many of users has the highest days streaks. A streak is a feature that tracks the number of consecutive days a developer contributes at least one commit. Streaks can be a powerful motivator, encouraging developrs to practice regularly and avoid breaking their streak. However, sometimes due to family reasons or other busy works, a user may forget or be unable to contribute. For this, you can use this auto-commit repository to ensure that you will not lose your streaks in any way. 

This repository can automatically make daily commits for you and you can enjoy your days and vacations without any worries.

By using the service below, you can track your total contributions, current streak,and longest streak and display them on your GitHub profile README.

- [GitHub Readme Streak Stats](https://streak-stats.demolab.com/)
 


## How it works?

- A GitHub Action runs on a scheduled cron job
- Python script updates commit and streak logs
- All commits are permanently stored in `commits.json`
- Daily streak progress is tracked in `streaks.json`
- Time is displayed in your configured timezone (PKT/IST/UTC)

## Data Files

- **`commits.json`**

Stores all commits with timestamps, no deletion after any number of commits.

- **`streaks.json`**  

Tracks daily streak progress with format: "Day X: [TIME]"

## Timezone Configuration

Change the timezone in `update_activity.py`:
```python
TIMEZONE = 'Asia/Karachi'  # For PKT
TIMEZONE = 'UTC'           # For UTC
```

The cron schedule uses UTC time. Here are some examples for different times:

- `'0 0 * * *'` - 12:00 AM UTC (Midnight)
- `'0 12 * * *'` - 12:00 PM UTC (Noon)
- `'30 18 * * *'` - 6:30 PM UTC
- `'0 6 * * *'` - 6:00 AM UTC

**For Pakistan Time (PKT = UTC+5):**
- For 12:00 AM PKT, use `'0 19 * * *'` (7:00 PM UTC)
- For 6:00 AM PKT, use `'0 1 * * *'` (1:00 AM UTC)

---

*This repository maintains consistent GitHub activity through automated commits.*
