import json
import pandas as pd


def filter_task_ids(
    csv_file,
    run_type,
    reasoning_difficulty=None,
    visual_difficulty=None,
    overall_difficulty=None,
):
    # Load the CSV file
    df = pd.read_csv(csv_file)

    # Filter based on run type
    filtered_df = df[df[run_type] == "PASS"]

    # Further filtering based on difficulty levels if specified
    if reasoning_difficulty is not None:
        filtered_df = filtered_df[
            filtered_df["reasoning_difficulty"] == reasoning_difficulty
        ]

    if visual_difficulty is not None:
        filtered_df = filtered_df[filtered_df["visual_difficulty"] == visual_difficulty]

    if overall_difficulty is not None:
        filtered_df = filtered_df[
            filtered_df["overall_difficulty"] == overall_difficulty
        ]

    # Get the list of task_ids
    task_ids = filtered_df["task_id"].tolist()
    return task_ids


# Example usage
categories = ["classifieds", "reddit", "shopping"]
for category in categories:
    csv_file = "results/jy_results/{}_results.csv".format(
        category
    )  # Replace with your CSV file path
    run_type = "GPT-4V + SoM"  # Replace with your specific run type
    task_ids = filter_task_ids(
        csv_file,
        run_type,
        # reasoning_difficulty="easy",
        # visual_difficulty="easy",
        overall_difficulty="easy",
    )

    task_ids = [str(int(task_id)) for task_id in task_ids]
    with open("results/jy_results/{}_successful_tasks.json".format(category), "w") as f:
        json.dump(task_ids, f)
