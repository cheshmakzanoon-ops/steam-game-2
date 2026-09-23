#!/usr/bin/env python3
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def verify(m):
    n=0
    def yes(c,msg):
        nonlocal n;n+=1
        if not c: raise AssertionError(msg)
    yes(m["schema_version"]==1,"schema")
    yes(m["baseline_name"]=="preproduction-v1","baseline name")
    yes(m["decision"]=="GO_FOUNDATION_ONLY","decision")
    yes(m["next_phase"]==11,"next phase")
    yes(list(m["phase_closure_blobs"].keys())==[f"{i:03d}" for i in range(1,10)],"closure phases")
    yes(all(len(v)==40 for v in m["phase_closure_blobs"].values()),"closure blob hashes")
    b=m["locked_baselines"]
    yes(b["core_rules_version"]=="1.0.0","rules")
    yes(b["gdd_version"]=="1.0","gdd")
    yes(b["normal_run_minutes"]==[35,50],"run target")
    yes((b["watches"],b["acts"])==(15,3),"run structure")
    yes(b["principal_modes"]==1 and b["principal_biomes"]==1,"mode/biome")
    yes(b["doctrines"]==4 and b["bosses"]==3,"content")
    yes(b["prelaunch_planned_dev_days"]==165,"planned days")
    yes(b["protected_contingency_dev_days"]==75,"reserve")
    yes(b["productive_prelaunch_dev_days"]==240,"capacity")
    yes(b["safety_ceiling_months"]==18,"safety ceiling")
    c=m["conditions"]
    yes(c["external_spending_authorized"] is False,"spend deferred")
    yes(c["full_time_schedule_commitment"] is False,"schedule not promised")
    yes(c["personal_runway_stored"] is False,"runway privacy")
    yes(c["public_title_cleared"] is False,"title provisional")
    yes(c["mandatory_online_dependency"] is False,"offline")
    yes(c["phase_011_authorized"] is True,"phase 11 authorization")
    yes(m["tag_intent"]=="preproduction-v1","tag intent")
    return n
def main():
    m=json.loads((ROOT/"PREPRODUCTION_BASELINE_MANIFEST.json").read_text())
    n=verify(m)
    print(f"PASS: {n} Phase 010 baseline checks; decision={m['decision']}; next_phase={m['next_phase']:03d}")
    if "--self-test" in sys.argv:
        bad=json.loads(json.dumps(m));bad["conditions"]["mandatory_online_dependency"]=True
        try: verify(bad); raise AssertionError("negative case unexpectedly passed")
        except AssertionError as e:
            if str(e)=="negative case unexpectedly passed": raise
            print("PASS: mandatory-online negative case rejected")
if __name__=="__main__": main()
