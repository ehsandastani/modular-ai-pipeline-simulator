from pipeline import (
    DataLoader,
    Preprocessor,
    Analyzer,
    ReportGenerator,
    AIPipeline
)

if __name__ == "__main__":
    # --- Component Definitions ---
    loader = DataLoader()
    preprocessor = Preprocessor()
    basic_analyzer = Analyzer()
    reporter = ReportGenerator()
    input_filepath = "sample_data.txt"
    # --- Pipeline ---
    print("\n--- Running Pipeline ---")
    basic_pipeline = AIPipeline(loader, preprocessor, basic_analyzer)
    basic_results = basic_pipeline.run(input_filepath)
    reporter.print_to_console(basic_results)
    reporter.save_to_file(basic_results, "report.txt")