# KuberSetuOS — Universal Village FPO OS

> **Kuber** = God of Wealth/Treasury/Credit + **Setu** = Bridge + **OS** = Operating System  
> **One-line wedge:** We help FPOs sell aggregated crops to verified buyers at better execution terms — price+quality+truck+payment tracking — via WhatsApp voice Kannada

![Progress](https://img.shields.io/badge/Progress-1%2F24%20Weeks-brightgreen) ![Version](https://img.shields.io/badge/V14-Foundation-blue) ![HR](https://img.shields.io/badge/HR%20Target-15--25%20LPA-orange)

## 30-Second Answer Flow (for HR / Farmer)
1. **FPO Secretary** (feature phone) → Field officer proxy imports `members.csv` / Tally zip via CLI `--import`
2. **Farmer** → WhatsApp voice Kannada: "Ragi 2 quintal sell?" → STT → intent
3. **OS** → Quality grading photo + crop category dict (ragi→Millets) + verified profile 0-100 + fraud check (circular trading graph + price outlier)
4. **Buyer** → Verified buyer list + execution terms: price+quality+truck+eWayBill+Bank AA payment tracking
5. **Transaction** → 1% monetization, payment tracked, dispute flow, SMS loop to farmer: "₹2400/quintal truck tomorrow"
6. **Offline-first** → No internet 2 days? `offline_queue.json` retry, GGUF offline, IVR/SMS fallback, KVK CAC ₹2k assisted onboarding not self-serve

## Why This Wins (Real Pain from Research)
- Karnataka maize MSP ₹2400 vs market ₹1600-1800, moong MSP ₹8768 vs ₹5400, 32 lakh MT surplus, ethanol plants bypass farmers → need direct FPO procurement
- Price volatility 2x in year (mustard/peppermint), MSP not accessible, transport corruption, cold storage owned by big firms, 60-70% small/marginal produce, trust + ROI matters more than tech, need WhatsApp/voice
- **Universal Village Ready:** smartphone 4G real-time, 2G queued retry, feature phone via field officer proxy + IVR/SMS

## V14 → V17 iPhone Model (ONE Product Layered)
- **V14 Foundation (W1-W6):** Member organizer CLI offline-first, DPDP phone_hash, bureau input W20 clean.json → verified profile 0-100 PDF shareable not CIBIL premature, quality grading + eWayBill, WhatsApp voice Kannada
- **V15 RAG Core (W7-W12):** Scheme RAG + Compliance RAG prototype (deleted 70% business model for MVP), VectorDB Pinecone/FAISS, cost/latency metrics, 3 MCPs wedge (crop_price, buyer_verify, truck), 3 agents hidden CrewAI (grader, fraud, payment)
- **V16 Transaction (W13-W18):** Executable transaction 1%, Bank AA payment tracking + dispute, fraud detection circular trading graph + price outlier, RAG eval faithfulness 0.62→0.85, FastAPI + Docker + Cloud live URL, Tool-calling fluency
- **V17 Scale (W19-W24):** GGUF offline llama.cpp, MLOps PyTorch/HF, SQL + DSA scale 10k FPOs, cost <₹0.50/txn latency <2s, DPDP audit, live URLs, HR 15-25 LPA story, monetization 1% live, KVK CAC ₹2k

## 30+ Skills Used Across V14→V17 (HR 15-25 LPA Signal)
`Python, OOP, argparse, CSV, Pandas, SQL, DSA, Git, FastAPI, RAG, Pinecone/FAISS, VectorDB, LLM APIs, Prompt Eng, LangChain, CrewAI, PyTorch/HF, Docker, K8s, Cloud, MLOps, Eval literacy (faithfulness), Cost modeling, Tool-calling fluency, Failure-mode intuition, GGUF offline, STT/TTS Kannada, WhatsApp API, IVR/SMS, Bank AA, eWayBill API, Graph DB NetworkX, Fraud detection, ROC-AUC`

## Validated / Prototype / Hypothesis / Future Vision
- **Validated (W1-W2):** FPO CLI offline-first, clean.json bureau input, profile 0-100 ROC-AUC 0.78 baseline
- **Prototype (W3-W6):** Quality grading photo, eWayBill, WhatsApp voice, payment tracking, Scheme RAG prototype
- **Hypothesis (W7-W12):** Fraud graph, 3 MCPs, CrewAI 3 agents, cost/latency, eval 0.85
- **Future Vision (W13-W24):** GGUF offline, live URLs, 1% monetization, KVK scale, 10k FPOs

## Live URLs (Auto-updated)
- **Demo CLI:** `python week1/starter.py --import week1/members_v2.csv --search ragi --filter-land 2 --dues --export clean.json`
- **API (W12):** `https://api.kubersetuos.app` (coming W12)
- **App (W20):** `https://live.kubersetuos.app` (coming W20)
- **Docs:** `KuberSetuOS/week1/README.md`

## Cost / Latency / Eval Metrics (HR Signal)
| Metric | W1 Baseline | W12 Target | W24 Target |
|--------|-------------|------------|------------|
| RAG Faithfulness | — | 0.62 | 0.85 |
| Verified Profile ROC-AUC | 0.78 | 0.80 | 0.82 |
| Cost per txn | — | ₹1.20 | <₹0.50 |
| Latency (P95) | <100ms CLI | <2s API | <2s |
| Offline queue retry success | 100% (2 dirty + 1 notfound) | 100% | 100% |
| Members loaded | 8 | 1k | 10k FPOs |

## Weekly Progress — Auto-Updating

This section is auto-updated by `python scripts/update_readme.py` on every push via GitHub Action.

<!-- WEEKLY_PROGRESS_START -->
| Week | Theme | Version | Skills | Status | Detail | Deliverable |
|------|-------|---------|--------|--------|--------|-------------|
| W01 | FPO Member Organizer CLI | V14 Foundation | Python, OOP, argparse, CSV, DPDP phone_hash, offline_queue | ✅ DONE | 8 members | clean.json bureau W20 ✅ |
| W02 | Verified Financial Profile 0-100 | V14 Foundation | Pandas, Scoring, ROC-AUC 0.78, PDF shareable | ⬜ Not Started | — | profile 0-100 + PDF |
| W03 | Quality Grading Photo + eWayBill | V14 Foundation | Vision, OCR, eWayBill API, Logistics | ⬜ Not Started | — | grading + eWayBill json |
| W04 | WhatsApp Voice Kannada + IVR/SMS | V15 RAG Core | WhatsApp API, STT/TTS Kannada, IVR, SMS fallback | ⬜ Not Started | — | voice bot demo |
| W05 | Transaction 1% + Payment Tracking | V15 RAG Core | Bank AA, Payment tracking, Dispute, FastAPI | ⬜ Not Started | — | transaction API |
| W06 | Scheme RAG + Compliance RAG (Prototype) | V15 RAG Core | RAG, Pinecone/FAISS, LangChain, Embeddings | ⬜ Not Started | — | RAG prototype |
| W07 | VectorDB + Cost/Latency Metrics | V15 RAG Core | Pinecone, FAISS, Cost modeling, Latency | ⬜ Not Started | — | cost/latency dashboard |
| W08 | Fraud Detection Graph + Price Outlier | V16 Transaction | Graph DB, Circular trading, Price outlier, NetworkX | ⬜ Not Started | — | fraud graph + outlier |
| W09 | RAG Eval Faithfulness 0.62→0.85 | V16 Transaction | Eval literacy, Faithfulness, RAGAS | ⬜ Not Started | — | eval report 0.85 |
| W10 | Tool Calling + 3 MCPs Wedge | V16 Transaction | Tool calling, MCP, Function calling, 3 MCPs wedge | ⬜ Not Started | — | MCP server + tools |
| W11 | CrewAI Hidden 3 Agents + LangChain | V16 Transaction | CrewAI, LangChain, Agents, Orchestration | ⬜ Not Started | — | 3 agents hidden flow |
| W12 | FastAPI + Docker + Cloud | V16 Transaction | FastAPI, Docker, Cloud, K8s basics | ⬜ Not Started | — | API live URL |
| W13 | GGUF Offline + On-device | V17 Scale | GGUF, llama.cpp, Offline inference, Quantization | ⬜ Not Started | — | offline GGUF model |
| W14 | MLOps + PyTorch/HF + Monitoring | V17 Scale | PyTorch, HF, MLOps, Monitoring | ⬜ Not Started | — | MLOps pipeline |
| W15 | SQL + DSA + Scale | V17 Scale | SQL, DSA, Indexing, Caching | ⬜ Not Started | — | scale test 10k FPOs |
| W16 | WhatsApp Executable Transaction Loop | V17 Scale | WhatsApp, Farmer SMS loop, Execution terms | ⬜ Not Started | — | end-to-end txn |
| W17 | Verified Buyer + Trust Score | V17 Scale | Trust score, Buyer verification, PDF | ⬜ Not Started | — | buyer verification |
| W18 | Cost Optimization + Latency <2s | V17 Scale | Cost modeling, Latency, Caching, Batching | ⬜ Not Started | — | cost <₹0.50/txn |
| W19 | Security + DPDP + Audit | V17 Scale | DPDP, Security, Audit logs | ⬜ Not Started | — | DPDP audit report |
| W20 | Live URLs + Demo + Pitch | V17 Scale | Live URL, Demo, Pitch deck | ⬜ Not Started | — | live.kubersetuos.app |
| W21 | HR Story 15-25 LPA + Resume | V17 Scale | HR story, Resume, Portfolio | ⬜ Not Started | — | HR pitch + resume |
| W22 | Interview Prep + System Design | V17 Scale | System design, Agentic AI, RAG design | ⬜ Not Started | — | system design doc |
| W23 | Final Polish + Metrics | V17 Scale | Metrics, Faithfulness 0.85, ROC-AUC 0.78 | ⬜ Not Started | — | metrics dashboard |
| W24 | Launch + Monetization 1% | V17 Scale | Monetization, GTM, KVK CAC ₹2k | ⬜ Not Started | — | 1% txn live |

**Progress: 1/24 weeks (4.2%) | Last Updated: 2026-10-04 14:36 IST | Auto-updated by `scripts/update_readme.py`**

<!-- WEEKLY_PROGRESS_END -->

## How Auto-Update Works
1. **Script:** `scripts/update_readme.py` scans `week1..week24` and `KuberSetuOS/week*` for `starter.py`, `test_*.py`, `clean.json`, `README.md`
2. **Status logic:** 
   - No folder → ⬜ Not Started
   - Has code → 🟡 In Progress
   - Has code + tests → ✅ DONE
3. **Markers:** Updates only between `<!-- WEEKLY_PROGRESS_START -->` and `