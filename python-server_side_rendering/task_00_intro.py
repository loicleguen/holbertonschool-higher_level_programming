#!/usr/bin/env python3
"""
task_00_intro.py
A script to generate personalized invitation files from a given template and list of attendees.
"""

import os


def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template and a list of attendee dictionaries."""

    try:
        # --- Input type validation ---
        if not isinstance(template, str):
            print("Error: Invalid template type. Expected a string.")
            return
        if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
            print("Error: Invalid attendees type. Expected a list of dictionaries.")
            return

        # --- Handle empty inputs ---
        if not template.strip():
            print("Template is empty, no output files generated.")
            return
        if not attendees:
            print("No data provided, no output files generated.")
            return

        # --- Process each attendee ---
        for index, attendee in enumerate(attendees, start=1):
            try:
                # Replace placeholders with actual data or "N/A" if missing
                personalized = template
                for key in ["name", "event_title", "event_date", "event_location"]:
                    value = attendee.get(key)
                    if value is None or str(value).strip() == "":
                        value = "N/A"
                    personalized = personalized.replace("{" + key + "}", str(value))

                # Define output filename
                output_filename = f"output_{index}.txt"

                # Check if file already exists
                if os.path.exists(output_filename):
                    print(f"Warning: {output_filename} already exists and will be overwritten.")

                # Write the personalized invitation to a file
                with open(output_filename, "w", encoding="utf-8") as file:
                    file.write(personalized)

                print(f"Generated: {output_filename}")

            except Exception as e:
                print(f"Error processing attendee #{index}: {e}")

    except Exception as main_error:
        print(f"Unexpected error: {main_error}")
