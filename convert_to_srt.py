import json
import argparse

def milliseconds_to_srt_time(milliseconds):
    """Convert milliseconds to srt time format: hh:mm:ss,ms"""
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def json_to_srt(data):
    """Convert JSON data to SRT format"""
    srt_entries = []
    for index, entry in enumerate(data['events'], start=1):
        start_time = milliseconds_to_srt_time(entry['start'])
        end_time = milliseconds_to_srt_time(entry['end'])
        srt_entries.append(f"{index}\n{start_time} --> {end_time}\n{entry['text']}\n")
    return "\n".join(srt_entries)

def convert_json_to_srt(input_json_path, output_srt_path):
    """Load a JSON file and convert it to SRT format"""
    with open(input_json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    srt_content = json_to_srt(data)
    with open(output_srt_path, 'w', encoding='utf-8') as file:
        file.write(srt_content)

def main():
    parser = argparse.ArgumentParser(description="Convert JSON to SRT format")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--output", required=True, help="Path to output SRT file")
    
    args = parser.parse_args()
    convert_json_to_srt(args.input, args.output)

if __name__ == "__main__":
    main()
    
