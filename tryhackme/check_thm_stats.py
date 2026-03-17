import argparse
import json
import re
import time
from collections import namedtuple

import requests

# Define a named tuple to store room information
Room = namedtuple("Room", ["name", "url", "points", "difficulty"])


def fetch_raw_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch data: HTTP {response.status_code}")


def parse_rooms(raw_data):
    rooms = []
    # Find the start of the room table
    table_start = raw_data.find("| Room Name | Room URL | Points | Difficulty |")
    if table_start == -1:
        raise Exception("Room table not found in the README")

    # Extract the table content
    table_content = raw_data[table_start:]

    # Parse the table
    pattern = r"\| (.*?) \| (https://tryhackme\.com/room/.*?) \| (\d+) \| (.*?) \|"
    matches = re.findall(pattern, table_content)

    for match in matches:
        name, url, points, difficulty = match
        rooms.append(Room(name, url, int(points), difficulty.strip()))

    return rooms


def get_completed_rooms(user_id, limit=20):
    rooms = []
    page = 1
    while True:
        url = f"https://tryhackme.com/api/v2/public-profile/completed-rooms?user={user_id}&limit={limit}&page={page}"
        response = requests.get(url)
        data = response.json()

        if not data["data"]["docs"]:
            break

        rooms.extend(data["data"]["docs"])
        page += 1

        print(f"Fetched page {page-1}, total rooms so far: {len(rooms)}")
        time.sleep(2)

    return rooms


def main(user_id):
    try:
        # Fetch and parse room data from GitHub
        github_url = "https://raw.githubusercontent.com/pentestfunctions/thm-room-points/refs/heads/main/README.md"
        raw_data = fetch_raw_data(github_url)
        all_rooms = parse_rooms(raw_data)

        # Get user's completed rooms
        print("Fetching completed rooms...")
        completed_rooms_data = get_completed_rooms(user_id)
        print(f"Total completed rooms: {len(completed_rooms_data)}")

        # Create a set of completed room codes
        completed_room_codes = set(room["code"] for room in completed_rooms_data)

        # Separate completed and uncompleted rooms
        completed = []
        uncompleted = []
        total_points_gained = 0

        for room in all_rooms:
            room_code = room.url.split("/")[-1]
            if room_code in completed_room_codes:
                completed.append(room)
                total_points_gained += room.points
            else:
                uncompleted.append(room)

        # Sort uncompleted rooms by points (descending)
        uncompleted.sort(key=lambda x: x.points, reverse=True)

        # Write results to files
        with open("completed_rooms.txt", "w") as f:
            for room in completed:
                f.write(
                    f"{room.name} | {room.url} | {room.points} | {room.difficulty}\n"
                )
            f.write(f"\nTotal points gained: {total_points_gained}\n")

        with open("rooms_to_complete.txt", "w") as f:
            for room in uncompleted:
                f.write(
                    f"{room.name} | {room.url} | {room.points} | {room.difficulty}\n"
                )

        print(f"Results written to 'completed_rooms.txt' and 'rooms_to_complete.txt'")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="THM Room Data Scraper and Analyzer")
    parser.add_argument("user_id", help="TryHackMe user ID hash")
    args = parser.parse_args()

    main(args.user_id)
