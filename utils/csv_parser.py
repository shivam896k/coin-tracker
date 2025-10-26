import csv

class CsvParser:
    def stream_to_csv(self, generator, filename):
        """
            Stream data from generator directly to CSV file

            Returns: Number of rows written
        """
        count = 0

        with open(filename, 'a', newline='', encoding='utf-8') as f:
            writer = None

            for row in generator:
                if writer is None:
                    writer = csv.DictWriter(f, fieldnames=row.keys())
                    writer.writeheader()

                writer.writerow(row)
                count += 1

                if count % 1000 == 0:
                    f.flush()

        return count
