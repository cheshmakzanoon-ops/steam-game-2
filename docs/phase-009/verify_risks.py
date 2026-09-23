#!/usr/bin/env python3
import csv,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def verify():
    m=json.loads((ROOT/"RISK_MODEL.json").read_text())
    with (ROOT/"LIVING_RISK_REGISTER.csv").open(newline="") as f: rows=list(csv.DictReader(f))
    n=0
    def yes(c,msg):
        nonlocal n;n+=1
        if not c: raise AssertionError(msg)
    yes(m["schema_version"]==1,"schema");yes(m["phase"]==9,"phase")
    yes(len(rows)==len(m["register_expected_ids"])==26,"risk count")
    yes([r["id"] for r in rows]==m["register_expected_ids"],"risk IDs/order")
    for r in rows:
        p,i,d=map(int,(r["probability"],r["impact"],r["detectability"]))
        yes(1<=p<=5 and 1<=i<=5 and 1<=d<=5,f"score range {r['id']}")
        score=p*i*d
        yes(int(r["priority_score"])==score,f"score {r['id']}")
        expected="CRITICAL" if score>=60 else "HIGH" if score>=40 else "MEDIUM" if score>=20 else "LOW"
        yes(r["band"]==expected,f"band {r['id']}")
        yes(bool(r["owner"].strip()),f"owner {r['id']}")
        yes(bool(r["evidence_gate"].strip()),f"evidence {r['id']}")
    yes(m["prototype"]["cohort_min"]==8,"prototype cohort")
    yes(m["prototype"]["command_thesis_min"]==6,"prototype comprehension")
    yes(m["readability"]["cohort_min"]==10,"readability cohort")
    yes(m["readability"]["urgent_scan_median_seconds_max"]==2,"scan target")
    yes(m["fair_loss"]["score_min"]==14 and m["fair_loss"]["category_zero_max"]==0,"fair loss")
    yes(m["performance_targets"]["baseline_fps_min"]==60,"fps target")
    yes(m["performance_red_lines"]["sustained_fps_min"]==30,"fps red line")
    yes(m["art_throughput"]["green_dev_days_max"]==15 and m["art_throughput"]["amber_dev_days_max"]==20,"throughput")
    yes(m["schedule"]["green_reserve_fraction_min"]==0.20,"reserve threshold")
    yes(m["formal_reviews"]==[10,30,40,70,100,107,112,114],"review phases")
    yes(m["demo"]["cohort_min"]==12 and m["demo"]["retry_plan_min"]==8,"demo threshold")
    return n,m,rows
def main():
    n,m,rows=verify()
    print(f"PASS: {n} Phase 009 risk-policy checks; {len(rows)} scored risks; {len(m['formal_reviews'])} formal review gates")
    if "--self-test" in sys.argv:
        bad=json.loads((ROOT/"RISK_MODEL.json").read_text());bad["prototype"]["command_thesis_min"]=9
        try:
            if bad["prototype"]["command_thesis_min"]>bad["prototype"]["cohort_min"]: raise AssertionError("impossible threshold")
        except AssertionError: print("PASS: impossible prototype threshold rejected")
        else: raise AssertionError("negative self-test unexpectedly passed")
if __name__=="__main__": main()
