import csv,tempfile,unittest
from pathlib import Path
from src.batch import run
class BatchTests(unittest.TestCase):
 def test_aggregates(self):
  with tempfile.TemporaryDirectory() as d:
   run(Path(__file__).parents[1]/"data/trips.csv",d)
   with open(Path(d)/"marts/daily_trips.csv") as f:self.assertEqual(list(csv.reader(f))[1][1],"2")
