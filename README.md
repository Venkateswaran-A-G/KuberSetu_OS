# KuberSetuOS — Universal Village FPO OS

> **Kuber** = God of Wealth/Treasury/Credit + **Setu** = Bridge + **OS** = Operating System  
> **One-line wedge:** We help FPOs sell aggregated crops to verified buyers at better execution terms — price+quality+truck+payment tracking — via WhatsApp voice Kannada<br>
>**Writer:** Venkateswaran A G<br>
>**Theme:** Kisan / FPO OS — One product for every village

---

## Problem Statement

Small and marginal farmers (60-70% of produce) face:

- **MSP not accessible:** Karnataka maize MSP ₹2400 vs market ₹1600-1800, moong MSP ₹8768 vs ₹5400, 32 lakh MT surplus, ethanol plants bypass farmers
- **Price volatility:** 2x in a year (mustard, peppermint), no farm-to-table linkage
- **Trust & logistics:** Transport corruption, cold storage owned by big firms, no quality grading, no payment tracking
- **Digital divide:** Smartphone 4G in town, 2G or no internet in village for 2 days, feature phone users need proxy, need WhatsApp voice Kannada not English app
- **Data mess:** FPO secretary has Tally zip / CSV with missing land, duplicate ids, no consent tracking, phone numbers stored as plain text (DPDP violation)

Result: FPO cannot aggregate and sell at better price, farmer gets low price.

## Solution

**One-line wedge:** We help FPOs sell aggregated crops to verified buyers at better execution terms — price+quality+truck+payment tracking — via WhatsApp voice Kannada

**How it works:**
1. **FPO Secretary** imports members via CLI: `--import members.csv` or `--import-tally-zip tally.zip` (offline-first)
2. **System** cleans data: handles duplicate id, missing land queued to `offline_queue`, CROP_CATEGORY dict (ragi→Millets), consent verified filter (DPDP), phone_hash not phone
3. **Export** `clean.json` → becomes bureau input W20 for verified financial profile 0-100
4. **Future weeks:** Quality grading photo + eWayBill + logistics + Bank AA payment tracking + dispute + fraud detection (circular trading graph + price outlier) + WhatsApp voice loop + IVR/SMS fallback + GGUF offline

**Universal Village Ready:** 
- Smartphone 4G → real-time
- 2G / no internet 2 days → queued to `offline_queue.json` retry when internet comes
- Feature phone → field officer proxy via CLI

## Tech Stack

**Week 1 (Current):**
- Python 3.11+
- CSV (DictReader) — Tally export compatibility
- JSON — clean.json bureau input
- argparse — CLI for field officer
- hashlib / hash() — DPDP phone_hash
- pytest — 5 tests

**Upcoming Weeks:**
- Pandas, FastAPI, SQLite
- RAG: LangChain, FAISS / Pinecone, Embeddings
- Vision: Photo grading, OCR
- Voice: WhatsApp API, STT/TTS Kannada, IVR/SMS
- Transaction: Bank Account Aggregator, eWayBill API
- Fraud: NetworkX graph, price outlier
- Offline: GGUF, llama.cpp
- Deploy: Docker, Cloud

## Why This Tech Stack

| Tech | Why We Used It |
|------|----------------|
| **Python** | Easy for FPO field officers to read, huge ecosystem, works offline, no compilation needed in village laptop |
| **CSV DictReader** | Tally exports CSV, secretary already has it, no need for Excel dependency, handles every village reality |
| **JSON clean.json** | Bureau input W20 needs structured data, easy to share, language independent, becomes verified profile later |
| **argparse** | Field officer can run `python starter.py --import members.csv --search ragi` without editing code, --help self-documenting |
| **hash(phone) not phone** | DPDP Act 2023 — cannot store phone as plain text, hash for privacy, no Aadhaar storage |
| **CROP_CATEGORY dict** | `{'ragi':'Millets',...}.get(crop.lower(),"Other")` handles caps RAGI and unknown tomato→Other, O(1) lookup |
| **List comprehension + lambda** | `search_by_crop` list comp and `filter_land>2` lambda — Pythonic, fast, readable for small FPO 8-10k members |
| **offline_queue list** | Every village without internet — don't crash on missing land or FileNotFound, queue row dict and retry later, JSON serializable |
| **pytest** | 5 tests ensure load 8, ragi 3, land>2 4, consent 6, dues ₹3000, offline queue 2 dirty + 1 notfound, duplicate stays 8 |
| **Sublime + GitHub Desktop** | No AI autocomplete — learn properly, GitHub Desktop helps commit without git+vim complexity |

## Weekly Progress — Auto-Updating

This table is auto-updated by `python scripts/update_readme.py`. It scans `week1..week24` folders for code + tests.

<!-- WEEKLY_PROGRESS_START -->
| Week | Theme | Status | Detail | Deliverable |
|------|-------|--------|--------|-------------|
| W01 | FPO Member Organizer CLI | ✅ DONE | 8 members | clean.json bureau W20 ✅ |
| W02 | Verified Financial Profile 0-100 | ⬜ Not Started | — | profile 0-100 + PDF |
| W03 | Quality Grading Photo + eWayBill | ⬜ Not Started | — | grading + eWayBill json |
| W04 | WhatsApp Voice Kannada + IVR/SMS | ⬜ Not Started | — | voice bot demo |
| W05 | Transaction + Payment Tracking | ⬜ Not Started | — | transaction API |
| W06 | Scheme RAG + Compliance RAG | ⬜ Not Started | — | RAG prototype |
| W07 | VectorDB + Cost/Latency | ⬜ Not Started | — | cost/latency dashboard |
| W08 | Fraud Detection Graph | ⬜ Not Started | — | fraud graph |
| W09 | RAG Eval Faithfulness | ⬜ Not Started | — | eval report |
| W10 | Tool Calling + MCPs | ⬜ Not Started | — | MCP server |
| W11 | CrewAI Agents | ⬜ Not Started | — | 3 agents flow |
| W12 | FastAPI + Docker + Cloud | ⬜ Not Started | — | API live URL |
| W13 | GGUF Offline | ⬜ Not Started | — | offline model |
| W14 | MLOps + Monitoring | ⬜ Not Started | — | MLOps pipeline |
| W15 | SQL + Scale | ⬜ Not Started | — | scale test 10k |
| W16 | WhatsApp Transaction Loop | ⬜ Not Started | — | end-to-end txn |
| W17 | Verified Buyer + Trust | ⬜ Not Started | — | buyer verification |
| W18 | Cost Optimization | ⬜ Not Started | — | cost <₹0.50/txn |
| W19 | Security + DPDP Audit | ⬜ Not Started | — | audit report |
| W20 | Live URLs + Demo | ⬜ Not Started | — | live app |
| W21 | Polish + Docs | ⬜ Not Started | — | docs |
| W22 | System Design | ⬜ Not Started | — | design doc |
| W23 | Final Metrics | ⬜ Not Started | — | metrics dashboard |
| W24 | Launch + 1% Monetization | ⬜ Not Started | — | 1% txn live |

**Progress: 1/24 weeks (4.2%) | Last Updated: 2026-10-04 14:46 IST | Auto-updated by `scripts/update_readme.py`**

<!-- WEEKLY_PROGRESS_END -->

## How to Run

### Week 1 Demo (No Args)
```bash
cd week1
python starter.py
```
Expected:
```
✅ Loaded 8 members, 0 queued offline
Loaded 8 members
Search ragi: 3
Land>2: 4
Consent: 6
Dues: ₹3000.0
RAGI -> Millets, tomato -> Other
Exported 8 to clean.json — bureau input W20
```

### CLI for Field Officer
```bash
python starter.py --import members_v2.csv --search ragi --filter-land 2 --dues --export clean.json
python starter.py --import members_v2.csv --search RAGI
python starter.py --import dirty.csv
python starter.py --import notfound.csv
python starter.py --import-tally-zip tally.zip --export clean.json
```

### Run Tests
```bash
pip install pytest
pytest -v
# 5 passed
```

### Update README Tracker
```bash
python scripts/update_readme.py
# or
python update_readme.py
```

## How Auto-Update Works

1. Script `scripts/update_readme.py` scans `week1..week24` and `KuberSetuOS/week*` for `starter.py`, `test_*.py`, `clean.json`
2. Status: No folder = Not Started, Has code = In Progress, Has code + tests = DONE
3. It updates only between the special markers in this README (do not delete them)
4. Auto on push: `.github/workflows/update-readme.yml` runs on every push to main

---

**Writer:** Venkateswaran A G  
**Project:** KuberSetuOS — Wealth Bridge OS for Every Village  
**Location:** Bengaluru, Karnataka, IN
