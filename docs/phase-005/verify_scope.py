#!/usr/bin/env python3
import json, sys
from pathlib import Path
MODEL=Path(__file__).with_name("SCOPE_CEILINGS.json")
def verify(d):
    n=0
    def eq(a,b,m):
        nonlocal n;n+=1
        if a!=b: raise AssertionError(f"{m}: {a!r} != {b!r}")
    def le(a,b,m):
        nonlocal n;n+=1
        if a>b: raise AssertionError(f"{m}: {a} > {b}")
    eq(d["schema_version"],1,"schema");eq(d["phase"],5,"phase")
    for k,v in {"noncombat_structures":24,"combat_structures":9,"standard_enemies":15,"bosses":3,"doctrines":4,"run_upgrades":45,"systemic_events":24,"oaths":6,"principal_biomes":1,"principal_modes":1}.items():eq(d["content"][k],v,k)
    for k,v in {"doctrines":1,"total_structures":10,"standard_enemies":6,"bosses":1,"upgrades":12,"events":4,"watches":5,"minutes_min":20,"minutes_max":40}.items():eq(d["demo"][k],v,"demo "+k)
    le(d["art"]["allocated_color_frames"],d["art"]["hard_color_frame_cap"],"frame cap");eq(d["art"]["hard_color_frame_cap"],400,"frame ceiling")
    eq(d["text"]["launch_source_words_cap"],12000,"text cap");le(d["text"]["demo_source_words_cap"],d["text"]["launch_source_words_cap"],"demo words")
    le(d["audio"]["music_pieces_target"],d["audio"]["music_pieces_cap"],"music target");eq(d["audio"]["cue_identities"],76,"cue ids")
    eq(d["performance"]["baseline_fps_min"],60,"fps");le(d["performance"]["installed_build_mb_max"],1800,"install")
    c=d["cash"]
    for a,b in [(c["lean_total_usd"],c["lean_ceiling_usd"]),(c["base_total_usd"],c["base_ceiling_usd"]),(c["stretch_total_usd"],c["stretch_ceiling_usd"])]:le(a,b,"cash")
    eq(c["living_runway"],None,"runway unset");eq(c["available_cash"],None,"cash unset")
    s=d["schedule"];eq(s["target_months"],15,"months");le(s["target_months"],s["safety_ceiling_months"],"safety");eq(s["allocated_prelaunch_hours"]+s["unallocated_prelaunch_hours"],s["productive_prelaunch_hours"],"hours")
    n+=1
    if s["reserve_fraction"]<0.20: raise AssertionError("15-month reserve below 20%")
    n+=1
    if not s["twelve_month_reserve_fraction"]<0.20: raise AssertionError("12-month case must be amber")
    flat=[]
    for lo,hi in d["milestone_phase_ranges"]:
        n+=1
        if lo>hi: raise AssertionError("invalid range")
        flat.extend(range(lo,hi+1))
    eq(flat,list(range(1,121)),"phase coverage")
    return n
def main():
    d=json.loads(MODEL.read_text())
    print(f"PASS: {verify(d)} Phase 005 scope-ceiling checks")
    if "--self-test" in sys.argv:
        bad=json.loads(json.dumps(d));bad["content"]["doctrines"]=5
        try:verify(bad)
        except AssertionError:print("PASS: invalid extra-doctrine case rejected")
        else:raise AssertionError("negative self-test unexpectedly passed")
if __name__=="__main__":main()
