import pandas as pd


def json_to_csv_with_pandas(json_files, categories, csv_file):
    # Create an empty DataFrame to store all data
    all_data = pd.DataFrame()

    for i in range(len(json_files)):
        json_file = json_files[i]
        # Read each JSON file into a DataFrame
        data = pd.read_json(json_file, orient="index").reset_index()
        # Rename columns to more descriptive names
        data.columns = ["Task ID", "Task Success"]
        data["Task ID"] = data["Task ID"].str.extract("(\d+)").astype(int)
        # Append the data to the main DataFrame
        data["Category"] = categories[i]

        all_data = all_data._append(data, ignore_index=True)

    # Write the DataFrame to a CSV file
    all_data.to_csv(csv_file, index=False)


# List of JSON files to be converted
categories = ["classifieds", "reddit", "shopping"]
template = "results/no_text_observation_1/successful_{}_gpt4_som/results.json"
json_files = [template.format(category) for category in categories]

# CSV file to be created
csv_file = "results/no_text_observation_2/successful_gpt4_som_no_text_observation.csv"

# Call the function
json_to_csv_with_pandas(json_files, categories, csv_file)
