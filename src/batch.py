import argparse,csv
from collections import defaultdict
from pathlib import Path
def run(input_path,output_dir):
 out=Path(output_dir);(out/"raw").mkdir(parents=True,exist_ok=True);(out/"marts").mkdir(parents=True,exist_ok=True); metrics=defaultdict(lambda:[0,0.0])
 with open(input_path,newline="") as f:
  for row in csv.DictReader(f):
   fare=float(row["fare"])
   if fare < 0: continue
   day=row["pickup_ts"][:10];metrics[day][0]+=1;metrics[day][1]+=fare
   with open(out/"raw"/(day+".csv"),"a",newline="") as part: csv.DictWriter(part,fieldnames=row.keys()).writerow(row)
 with open(out/"marts/daily_trips.csv","w",newline="") as f:
  w=csv.writer(f);w.writerow(["pickup_date","trips","fare_revenue"])
  for day,(trips,revenue) in sorted(metrics.items()):w.writerow([day,trips,round(revenue,2)])
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--input",required=True);p.add_argument("--output",required=True);run(**vars(p.parse_args()))
