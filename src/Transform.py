from pydantic import BaseModel
from typing import List, Dict, Union
import csv
import json

class Transformer(BaseModel):
    input_fp: str
    output_fp: str

    rowsLst: List[Dict[str, Union[str, int, float]]] = list()

    def transform(self):
        # Read input file
        with open(self.input_fp, 'r', errors='ignore') as f:
            reader = csv.DictReader(f)

            for line in reader:
                self.rowsLst.append(line)

        # Cleanup and convert field data types to appropriate types
        fieldDtypes = {
            'Quantity': int,
            'UnitPrice': float
        }
        for row in self.rowsLst:
            for field, vals in row.items():
                if field in fieldDtypes:
                    row[field] = fieldDtypes[field](row[field])
                else:
                    row[field] = row[field].strip()

        # Write to output
        with open(self.output_fp, 'w') as f:
            _ = f.write('')
            _ = json.dump(self.rowsLst, f, indent=4)