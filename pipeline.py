from abc import ABC, abstractmethod
from typing import Any, List
import re


class PipelineStep(ABC):
    """
    An abstract base class representing a single step in a processing
    pipeline.
    """
    @abstractmethod
    def process(self, data: Any) -> Any:
        """
        Processes the input data and returns the result.
        This method must be implemented by all concrete subclasses.
        """
        pass


class DataLoader(PipelineStep):
    """
    Loads data from a text file, returning a list of lines.
    """
    def process(self, filepath: str) -> List[str]:
        """
        Reads a file from the given filepath and returns its lines as a
        list of strings.
        Handles FileNotFoundError and other potential exceptions.
        """
        try:
            with open(filepath, "rt", encoding="utf-8") as file:
                lines = file.readlines()
            
            # strip newline characters from each line.
            cleaned_lines = [line.strip() for line in lines]
            return cleaned_lines

        except FileNotFoundError:
            print(f"File not found: {filepath}")
            return []

        except Exception as e:
            print(f"Error while reading file: {e}")
            return []
   

class Preprocessor(PipelineStep):
    """
    Cleans a list of text strings by converting to lowercase, removing
    punctuation,
    and stripping extra whitespace.
    """
    def __init__(self, punctuation_to_remove: str = r'[^\w\s]'):
        self.punctuation_pattern = re.compile(punctuation_to_remove)


    def process(self, data: List[str]) -> List[str]:
        """
        Applies cleaning steps to each string in the input list.
        """
        cleaned_data = []
        for line in data:
            line = line.lower()
            line = self.punctuation_pattern.sub("", line)
            line = re.sub(r"\s+", " ", line).strip()
            cleaned_data.append(line)

        return cleaned_data
    

class Analyzer(PipelineStep):
    """
    Analyzes the text data to compute basic statistics.
    """
    def process(self, data: List[str]) -> dict:
        """
        Calculates total lines, average words per line, and number of
        unique words.
        """
        if not data:
            return {
                "total_lines": 0,
                "avg_length": 0.0,
                "unique_words": 0
            }

        total_lines = len(data)

        unique = set()

        total_word = 0
        for line in data:
            words = line.split()
            total_word += len(words)
            unique.update(words)

        avg_length = total_word / total_lines
        unique_words = len(unique)

        return {
            "total_lines": total_lines,
            "avg_length": avg_length,
            "unique_words": unique_words
        }


class ReportGenerator:
    """
    Generates and outputs reports from the analysis statistics.
    """
    def print_to_console(self, stats: dict):
        """
        Prints the statistics in a formatted way to the console.
        """
        print("=== 🔎 Analysis Report 🔍 ===")
        for key, value in stats.items():
            print(f"{key}: {value}")


    def save_to_file(self, stats: dict, filepath: str):
        """
        Saves the statistics in a formatted way to a text file.
        """
        try:
            with open(filepath, "wt", encoding="utf-8") as file:
                file.write("=== 🔎 Analysis Report 🔍 ===\n")
                for key, value in stats.items():
                    file.write(f"{key}: {value}\n")

        except Exception as e:
            print(f"Error while writing in file: {e}")


class AIPipeline:
    """
    Orchestrates a series of pipeline steps to process data.
    """
    def __init__(self, *steps: PipelineStep):
        self.steps = steps


    def run(self, initial_input: Any) -> Any:
        """
        Executes all steps in the pipeline sequentially.
        """
        data = initial_input
        for step in self.steps:
            data = step.process(data)
        
        return data

