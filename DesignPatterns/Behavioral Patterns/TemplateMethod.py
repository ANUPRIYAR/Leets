from abc import ABC, abstractmethod

class ReportGenerator(ABC):
    @abstractmethod
    def collect_data(self):
        pass

    @abstractmethod
    def process_data(self, data):
        pass

    @abstractmethod
    def format_report(self, data):
        pass

    def print_report(self, report):
        print(report)

    def generate_report(self):
        data = self.collect_data()
        processed_data = self.process_data(data)
        report = self.format_report(processed_data)
        self.print_report(report)


class CSVReportGenerator(ReportGenerator):
    def collect_data(self):
        return "CSV Data"

    def process_data(self, data):
        return "Processed " + data

    def format_report(self, processed_data):
        return "CSV Report: " + processed_data


# Similar classes for HTMLReport Generator and PDFReportGenerator

# Test the implementation
csv_report = CSVReportGenerator()
csv_report.generate_report()
# Similarly for other report types

# Output
# CSV Report: Processed CSV Data