import os

import requests
import json
from dotenv import load_dotenv
from datetime import datetime
from zoneinfo import ZoneInfo

load_dotenv()

NOTION_KEY = os.getenv("NOTION_KEY", None)
DATABASE_ID = os.getenv("DATABASE_ID", None)

headers = {
    "Authorization": f"Bearer {NOTION_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def create_page(title, content):
    create_url = "https://api.notion.com/v1/pages"

    date = datetime.now(ZoneInfo("America/Chicago")).isoformat()

    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name": {"title": [{"text": {"content": title}}]},
            "Date": {"date": {"start": date, "end": None}},
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": content,
                            },
                        }
                    ]
                },
            }
        ],
    }

    res = requests.post(create_url, headers=headers, json=payload)

    if res.status_code != 200:
        print(res.json())
        return False

    elif res.status_code == 200:
        return True


def get_latest_page():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    payload = {"page_size": 1}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    with open("db.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # get properties of your database
    get_latest_page()

    # match it with your data
    title = "Test Title"
    content = "Commodo adipisicing anim minim laborum cupidatat aute sit enim ut. Cupidatat occaecat ad labore eu. Officia minim elit labore mollit ea do proident elit cillum elit. Dolor minim culpa id incididunt elit deserunt eu. Commodo sint excepteur et magna duis magna fugiat reprehenderit."

    create_page(title, content)
