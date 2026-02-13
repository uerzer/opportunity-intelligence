# Context Restoration Playbook

**Purpose**: Eliminate "Groundhog Day" resets - restore full project context from GitHub if memory is lost.

**Last Updated**: 2026-02-12 22:51 WET

---

## Quick Start: 3-Minute Context Recovery

If you wake up with no memory of the opportunity scanner project:

1. **Read this file first** - You're reading it now ✓
2. **Clone the key documents** (order matters):
   - `PROGRESS_TRACKING.md` - Master status document
   - Each scanner's Python file to understand capabilities
3. **Review latest commit messages** - Shows what was worked on recently
4. **Check trigger status** - Are automated backups running?

---

## Full Context: What This Project Is

### The Goal
Build a $100K/month revenue stream within 12-18 months after previous failures (crypto, FBA, blogging).

### The Solution
6 automated scanners that monitor different revenue opportunities in real-time, with AI-driven scoring to prioritize the best path forward.

### The Decision
After comprehensive research, **AI Automation Agency targeting HVAC companies** scored 79.75/100 - the clear winner for fastest path to $100K/month.

---

## The 6 Scanners (What They Do)

### 1. Crypto Arbitrage Monitor
**File**: `crypto_arbitrage_monitor.py`
**Score**: 45/100 (supplemental only)
**Purpose**: Track DEX/CEX spreads, MEV opportunities, cross-chain arbitrage
**Reality**: Needs $500K+ capital for $100K/month. With $10K capital → $1K-3K/month realistic max.
**Status**: Built but deprioritized. Use for supplemental income only.

### 2. AI Agency Lead Generator ⭐ PRIMARY PATH
**File**: `ai_agency_lead_generator.py`
**Score**: 79.75/100 (HIGHEST)
**Purpose**: Find and qualify leads in 7 high-value niches (HVAC, dental, roofing, tree removal, med spas, plumbing, auto repair)
**Why It Won**: 
- Proven pricing: $1.5K-7K/month per client
- Clear pain points: Missed calls = lost revenue
- 12-18 month path to $100K MRR with 15-20 clients
- Low competition in boring industries
**Next Action**: Start with HVAC (highest pain + budget combo)

### 3. Viral Trend Detector
**File**: `viral_trend_detector.py`
**Score**: 59/100 (portfolio play)
**Purpose**: Monitor Product Hunt, Hacker News, Reddit for early viral signals
**Research**: 
- Product Hunt: 4-6 week prep = 2.5x better results
- Reddit: 27 best marketing subreddits mapped
- Early detection window: 4-6 weeks before saturation
**Use Case**: Build quick tools that ride viral waves, or use as agency lead magnet

### 4. Enterprise Pricing Intelligence
**File**: `enterprise_pricing_tracker.py`
**Score**: 62.5/100 (long game)
**Purpose**: Track RFPs, SOC 2 requirements, $50K-150K/month deals
**Reality**: 
- Average enterprise AI spending: $85,521/month
- 6-12 month sales cycles
- SOC 2 required (~$50K investment)
**Strategy**: Long-term play after agency proves out. Use agency revenue to fund enterprise transition.

### 5. Micro-SaaS Validation Framework
**File**: `micro_saas_validation_framework.py`
**Score**: 72.25/100 (solid middle path)
**Purpose**: Validate product ideas in 2-4 weeks before building
**Key Insight**: 42% of startups fail due to "no market need" - validation prevents waste
**7 Boring Goldmines**: Manufacturing compliance, florist inventory, cemetery management, dry cleaner routing, parking lot maintenance, vending machines, porta-potty logistics
**Strategy**: Run in parallel with agency for diversification

### 6. Unified Opportunity Scorer
**File**: `unified_opportunity_scorer.py`
**Purpose**: Master dashboard that ranks all opportunities
**Algorithm**: Revenue Potential (35%) + Speed to First $ (25%) + Probability (20%) + Scalability (15%) + Capital Efficiency (5%)
**Output**: Clear rankings that led to AI Agency decision

---

## The $100K/Month Roadmap (If Context Lost)

### Phase 1: Foundation (Months 1-3)
- **Action**: Launch AI agency targeting HVAC
- **Goal**: Land 2-3 clients at $1.5K-3K/month
- **Revenue**: $4.5K-9K MRR
- **Focus**: Delivery excellence + case studies

### Phase 2: Scale (Months 4-6)
- **Action**: Add 2-5 more clients via referrals
- **Goal**: Systematize delivery, hire VA
- **Revenue**: $10K-20K MRR
- **Focus**: Process documentation + hiring

### Phase 3: Growth (Months 7-12)
- **Action**: Reach 10-15 clients at $3K-5K/month
- **Goal**: Hire delivery specialist + SDR
- **Revenue**: $30K-50K MRR
- **Focus**: Team building + multi-niche expansion

### Phase 4: Optimization (Months 13-18)
- **Action**: 15-20 clients at $5K-7K/month average
- **Goal**: Full systematization, documented playbooks
- **Revenue**: $100K MRR
- **Focus**: Exit options + enterprise transition

---

## GitHub Backup Structure

**Repository**: https://github.com/uerzer/opportunity-intelligence

### File Organization
```
opportunity-intelligence/
├── README.md (comprehensive project overview)
├── STATUS.md (daily backup status)
├── docs/
│   ├── PROGRESS_TRACKING.md (master status document)
│   └── CONTEXT_RESTORATION_GUIDE.md (this file)
├── crypto_arbitrage_monitor.py
├── ai_agency_lead_generator.py
├── viral_trend_detector.py
├── enterprise_pricing_tracker.py
├── micro_saas_validation_framework.py
└── unified_opportunity_scorer.py
```

---

## Automated Backup Schedule

### Hourly Backups
- **What**: Scanner execution outputs and logs
- **Why**: Capture real-time opportunity detection
- **Trigger**: @trigger:hourly-scanner-backup
- **Schedule**: Runs every hour at :00

### Daily Backups
- **What**: Progress tracking and context guides
- **Why**: Preserve strategic thinking and decision rationale
- **Trigger**: @trigger:daily-github-backup-opportunity-intelligence
- **Schedule**: Runs daily at midnight UTC

---

## Manual Restoration Steps

### Step 1: Clone the Repository
```bash
git clone https://github.com/uerzer/opportunity-intelligence.git
cd opportunity-intelligence
```

### Step 2: Read Core Documents (in order)
1. `docs/CONTEXT_RESTORATION_GUIDE.md` (this file)
2. `docs/PROGRESS_TRACKING.md` (master status)
3. `README.md` (project overview)
4. `STATUS.md` (latest backup status)

### Step 3: Review Scanner Files
- All 6 Python scanners are in root directory
- Each scanner is a standalone executable with comprehensive comments
- Review the unified scorer for current rankings

### Step 4: Check Commit History
```bash
# See what was worked on recently
git log --oneline -20

# See specific file changes
git log -p docs/PROGRESS_TRACKING.md
```

---

## Decision Rationale (Why AI Agency Won)

### Scoring Breakdown
**AI Agency: 79.75/100**
- Revenue Potential: 90/100 (clear path to $100K/month)
- Speed to First $: 85/100 (30-60 days to first client)
- Probability: 75/100 (proven model, clear pain points)
- Scalability: 70/100 (hire to scale, eventually productize)
- Capital Efficiency: 90/100 (minimal upfront investment)

**Why It Beat Others:**
- Crypto: Too capital intensive ($500K+ needed)
- Enterprise: Too slow (18-24 months to first deal)
- Micro-SaaS: Higher risk (42% failure rate)
- Viral Trends: Unpredictable timing (opportunistic only)

**Why HVAC Specifically:**
- Highest pain point intensity (missed calls = lost revenue)
- Strong budget availability ($1.5K-7K/month sustainable)
- Low technical sophistication (easier to demonstrate value)
- Seasonal demand spikes (automation crucial)
- Clear ROI measurement (calls answered, appointments booked)

---

## Next Actions (If Starting Fresh)

### Immediate (Today)
1. ✅ Read this restoration guide
2. ✅ Review PROGRESS_TRACKING.md for current status
3. ✅ Check GitHub to confirm all 6 scanners are backed up
4. ✅ Verify automated backup triggers are running

### This Week (If Launching Agency)
1. Build HVAC lead gen demo (sample bot flow)
2. Create case study template
3. Scrape 100 HVAC prospects (Google Maps, directories)
4. Write email sequence (5-7 emails for cold outreach)

### Week 2-4 (If Launching Agency)
1. Send 25 emails/day (175/week total)
2. Book 2-3 calls/week
3. Close 1-2 pilot clients at $1.5K-3K/month
4. Begin delivery on first project

---

## Success Metrics (How to Track Progress)

### Monthly KPIs
- **MRR**: Target $100K by month 18
- **Client count**: 15-20 active clients
- **Churn rate**: <5% monthly
- **Average contract value**: $5K-7K/month

### Leading Indicators (Weekly)
- **Outreach**: 25 emails/day = 125/week
- **Calls booked**: 2-3/week minimum
- **Close rate**: 20-30% (realistic B2B)
- **Referral rate**: 30-40% of new clients from referrals

---

## Common Scenarios & Solutions

### Scenario 1: "I don't remember the project at all"
1. Read this file top to bottom
2. Read PROGRESS_TRACKING.md
3. Review latest GitHub commits
4. Check trigger status

### Scenario 2: "Which scanner should I focus on?"
- **Primary**: AI Agency (79.75/100 score)
- **Secondary**: Micro-SaaS (72.25/100)
- **Monitor**: Viral trends + Enterprise (opportunistic)
- **Ignore**: Crypto (supplemental income only)

### Scenario 3: "How do I start the AI agency?"
- Week 1: Build demo, scrape 100 HVAC prospects
- Week 2-4: 25 emails/day, book 2-3 calls/week
- Goal: 1-2 pilot clients at $1.5K-3K/month

### Scenario 4: "What if the agency path fails?"
- Backup: Pivot to micro-SaaS full-time
- Validation: 2-4 weeks per idea, minimal investment
- Fallback: Use viral trend detector for quick flip income

---

## Recovery Checklist

Use this checklist if context is completely lost:

- [ ] Clone GitHub repository
- [ ] Read CONTEXT_RESTORATION_GUIDE.md (this file)
- [ ] Read PROGRESS_TRACKING.md
- [ ] Review README.md
- [ ] Check STATUS.md for latest backup
- [ ] Review latest 20 commit messages
- [ ] Verify trigger status (hourly + daily backups)
- [ ] Understand primary recommendation (AI Agency)
- [ ] Understand why it won (79.75/100 score)
- [ ] Review $100K/month roadmap
- [ ] Identify next action based on current phase

**After completing checklist**: You should have full context restored and know exactly what to work on next.

---

## Contact & Support

**Repository**: https://github.com/uerzer/opportunity-intelligence
**Owner**: uerzer (GitHub account)
**Email**: phobik2000+ai@gmail.com
**Timezone**: Europe/Lisbon (WET)

---

**Remember**: This file exists to prevent "Groundhog Day" resets. If you're reading this with no memory, you've successfully recovered the context. Now take action based on PROGRESS_TRACKING.md current status.