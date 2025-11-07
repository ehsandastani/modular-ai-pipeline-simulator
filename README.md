# 🧠 Modular AI Pipeline Simulator

A simple modular text-processing pipeline implemented in Python.

## 📂 Project Structure
```bash
ai_pipeline_project/
│
├── pipeline.py # Core pipeline classes (DataLoader, Preprocessor, Analyzer, etc.)
├── main.py # Entry script to run the pipeline
├── sample_data.txt # Example input text (≥30 lines)
├── report.txt # Output analysis report
└── README.md
```

## ⚙️ Features
- **DataLoader:** reads text files safely  
- **Preprocessor:** cleans text (lowercase, remove punctuation, trim spaces)  
- **Analyzer:** computes total lines, average words per line, and unique word count  
- **ReportGenerator:** prints and saves formatted reports  
- **AIPipeline:** orchestrates all steps automatically  

## ▶️ Usage
```bash
python main.py
```

It will read sample_data.txt, analyze it, print the stats to the console,
and save them to report.txt.

## 🧑‍💻 Example Output
```bash
=== 🔎 Analysis Report 🔍 ===
total_lines: 30
avg_length: 8.1
unique_words: 166
```

## 🛠 Requirements
* Python 3.8 +
* No external libraries required (uses only the Python standard library)
