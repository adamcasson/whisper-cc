import argparse
from typing import List, Literal

import whisper


### written by ChatGPT ###
def seconds_to_srt_timestamp(seconds: float) -> str:
    """Convert a given number of seconds to a timestamp in the format used in SRT files.

    Args:
        seconds (float): The number of seconds to convert to a timestamp.

    Returns:
        str: A timestamp in the format used in SRT files.
    """
    hours = int(seconds / 3600)
    minutes = int((seconds % 3600) / 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return "{:02d}:{:02d}:{:02d},{:03d}".format(hours, minutes, secs, millis)


def create_srt_segment(
    segment_number: int, start_time: float, end_time: float, text: str
) -> str:
    """Create a segment of an SRT file given the the segment number, start and end times, and the text.

    Args:
        segment_number (int): The number of the segment.
        start (float): The start time of the segment in seconds.
        end (float): The end time of the segment in seconds.
        text (str): The text of the segment.

    Returns:
        str: A string representing the segment of an SRT file.
    """
    start_timestamp = seconds_to_srt_timestamp(start_time)
    end_timestamp = seconds_to_srt_timestamp(end_time)
    return (
        f"{segment_number}\n{start_timestamp} --> {end_timestamp}\n{text.strip()}\n\n"
    )


def create_srt_file(segments: List[str]) -> str:
    """Create an SRT file by combining multiple segments.

    Args:
        segments (List[str]): A list of segments to combine into an SRT file.

    Returns:
        str: A string representing the combined segments as an SRT file.
    """
    srt_file = ""
    for segment in segments:
        srt_file += segment
    return srt_file


def save_srt_file(srt_file, filename):
    """Save an SRT file to disk with the ".srt" file extension.

    Args:
        srt_file (str): A string representing the contents of the SRT file.
        filename (str): A string representing the name of the file to be saved, including the ".srt" file extension.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(srt_file)
    print("File saved successfully!")


######


### written by my ###
def main(filename: str, model_size: Literal["tiny", "small", "medium", "large"]):
    model = whisper.load_model(model_size)
    result = model.transcribe(filename)

    segments = []
    for i, s in enumerate(result["segments"]):
        segments.append(create_srt_segment(i + 1, s["start"], s["end"], s["text"]))
    srt_file = create_srt_file(segments)

    save_srt_file(srt_file, "../outputs/subtitles.srt")


######


if __name__ == "__main__":

    ### written by ChatGPT ###
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("filename", type=str, help="name of the file to be processed")
    parser.add_argument(
        "--size",
        type=str,
        choices=["tiny", "small", "medium", "large"],
        default="small",
        help="model size",
    )
    args = parser.parse_args()

    print(f"File name: {args.filename}")
    print(f"Model size: {args.size}")
    ######

    main(filename=args.filename, model_size=args.size)
