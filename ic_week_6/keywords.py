from datetime import datetime, timedelta

SPECIAL_KEYWORDS = {
    "today": datetime.today(),
    "tomorrow": datetime.today() + timedelta(days=1),
    "next week": datetime.today() + timedelta(days=7)
}

