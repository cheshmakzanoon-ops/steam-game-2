#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
MODEL=ROOT/"ROADMAP_MODEL.json"
CSV=ROOT/"PHASE_ESTIMATES.csv"

def verify(model, rows):
    checks=0
    def yes(cond,msg):
        nonlocal checks
        checks += 1
        if not cond: raise AssertionError(msg)
    yes(model["schema_version"]==1,"schema")
    yes(model["phase"]==8,"phase")
    yes(len(rows)==120,"must contain 120 phases")
    phases=[int(r["phase"]) for r in rows]
    yes(phases==list(range(1,121)),"phase IDs")
    for i,r in enumerate(rows,1):
        pred=r["hard_predecessor"]
        yes((i==1 and pred=="") or (i>1 and int(pred)==i-1),f"predecessor {i}")
        yes(float(r["estimate_dev_days"])>0,f"positive estimate {i}")
        yes(int(r["acceptance_weight_points"])==round(float(r["estimate_dev_days"])*4),f"AWP {i}")
    pre=sum(float(r["estimate_dev_days"]) for r in rows if int(r["phase"])<=116)
    post=sum(float(r["estimate_dev_days"]) for r in rows if int(r["phase"])>=117)
    yes(abs(pre-165)<1e-9,"prelaunch days")
    yes(abs(post-10)<1e-9,"postlaunch days")
    cap=model["capacity"]
    yes(cap["planned_prelaunch_dev_days"]==165,"model prelaunch")
    yes(cap["productive_prelaunch_dev_days"]==240,"capacity days")
    yes(cap["unallocated_contingency_dev_days"]==75,"reserve days")
    yes(sum(x["dev_days"] for x in model["contingency_blocks"])==75,"reserve block sum")
    milestones={x["phase"] for x in model["milestones"]}
    for p in (30,40,100,111,112,114,116): yes(p in milestones,f"milestone {p}")
    reviews={x["phase"] for x in model["stop_reviews"]}
    for p in (10,30,40,70,100,107,112,114): yes(p in reviews,f"review {p}")
    total=sum(int(r["acceptance_weight_points"]) for r in rows)
    yes(total==model["burndown"]["total_points"]==700,"total AWP")
    yes(model["burndown"]["prelaunch_points"]==660,"prelaunch AWP")
    yes(model["staffing"]["agent_multiplier"]==1.0,"agent multiplier")
    return checks

def main():
    model=json.loads(MODEL.read_text())
    with CSV.open(newline="") as f: rows=list(csv.DictReader(f))
    n=verify(model,rows)
    print(f"PASS: {n} Phase 008 roadmap checks; 120 phases; 165 prelaunch planned days; 75 contingency days")
    if "--self-test" in sys.argv:
        bad=json.loads(json.dumps(model))
        bad["capacity"]["unallocated_contingency_dev_days"]=74
        try: verify(bad,rows)
        except AssertionError: print("PASS: invalid reserve case rejected")
        else: raise AssertionError("negative self-test unexpectedly passed")

if __name__=="__main__":
    main()
