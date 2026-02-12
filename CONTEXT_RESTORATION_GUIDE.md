# Context Restoration Guide
**Emergency Recovery Playbook for Opportunity Intelligence System**

## Quick Recovery (5 minutes)

If you lose context or need to restore from scratch, follow these steps:

### 1. Access GitHub Repository
```
Repository: https://github.com/uerzer/opportunity-intelligence
Branch: main
Folder: /scanners/
```

### 2. Core System Files (All 6 Scanners)
All scanner files are backed up hourly to GitHub:

1. **crypto_arbitrage_monitor.py** (12.7KB)
   - DEX/CEX spreads, MEV opportunities, cross-chain arbitrage
   - Reality check: Needs $500K+ for $100K/month target
   
2. **ai_agency_lead_generator.py** (25.3KB) ⭐ PRIMARY PATH
   - HVAC, dental, roofing, tree removal, med spas
   - Score: 79.75/100 (highest)
   - Target: 15-20 clients at $5K-7K/month = $100K MRR in 12-18 months
   
3. **viral_trend_detector.py** (21.4KB)
   - Product Hunt, Hacker News, Reddit early signals
   - Score: 59/100 (portfolio play or lead magnet)
   
4. **enterprise_pricing_tracker.py** (22.8KB)
   - RFPs, SOC 2, $50K-150K/month enterprise deals
   - Score: 62.5/100 (long game, 18-24 months)
   
5. **micro_saas_validation_framework.py** (23.3KB)
   - Boring industries, pain extraction, 2-4 week validation
   - Score: 72.25/100 (solid middle path)
   
6. **unified_opportunity_scorer.py** (25.6KB)
   - Ranks all opportunities by revenue potential + speed
   - Primary recommendation: AI Automation Agency

### 3. Key Decisions & Context

**Your Profile:**
- Entrepreneur/Developer/Hacker
- Solo founder, previous losses (crypto, FBA, blogging)
- Goal: $100K/month revenue
- Preference: Execute directly, no micromanagement

**The Chosen Path: AI Automation Agency**
Based on unified scoring, this is your optimal route:

**Months 1-3:** Launch AI Agency
- Target: HVAC industry (highest pain + budget)
- Tactic: 100 prospects → 25 emails/day → 10 calls → 2-3 clients
- Revenue: $4.5K-9K MRR

**Months 4-6:** Scale to $10K-20K MRR
- Add 2-5 clients via referrals
- Systematize delivery, hire VA

**Months 7-12:** Hit $30K-50K MRR
- 10-15 total clients at $3K-5K/month
- Hire delivery specialist + SDR

**Months 13-18:** Reach $100K MRR
- 15-20 clients at $5K-7K/month average
- Full systematization
- Consider productizing into SaaS

### 4. Active Automations

**Hourly Backup Trigger:**
- Name: @trigger:hourly-scanner-backup
- Schedule: Every hour (0 */1 * * *)
- Action: Auto-commits scanner outputs and logs to GitHub

**Status Tracking:**
- Project status: @file:notes/github_backup_project_status.md
- This recovery guide: @file:docs/CONTEXT_RESTORATION_GUIDE.md

### 5. Technical Setup

**GitHub Accounts:**
- uerzer (apn_1KhplQb, apn_Dphv0KB)

**Available Agents:**
- @agent:github-agent - Repository operations
- @agent:nebula-memory-reader - Memory context (requires NEBULA_API_KEY)
- @agent:memory-context-loader - Automatic context loading

**Nebula Email:**
- pho@nebula.me (for verification codes, external service signups)

### 6. Recovery Commands

If starting fresh conversation:

```
1. Check latest scanner files:
   @file:scripts/opportunity-scanners/unified_opportunity_scorer.py

2. Review project status:
   @file:notes/github_backup_project_status.md

3. Access GitHub backup:
   https://github.com/uerzer/opportunity-intelligence

4. Load this guide:
   @file:docs/CONTEXT_RESTORATION_GUIDE.md
```

### 7. Research Sources & Key Insights

**Market Validation Data:**
- 42% of startups fail due to "no market need" (CB Insights)
- Top micro-SaaS: $5K-50K MRR, 70-90% margins
- Enterprise AI spending average: $85,521/month
- SOC 2 required for enterprise, 6-12 month sales cycles

**AI Agency Economics:**
- HVAC pain points: Lead gen, booking automation, review management
- Average deal size: $1.5K-7K/month
- Client acquisition: 100 prospects → 2-3 clients
- Top 7 niches documented in ai_agency_lead_generator.py

**Viral Trend Intelligence:**
- Product Hunt: 4-6 week prep = 2.5x better results
- 27 best Reddit marketing subreddits mapped
- Hacker News scoring algorithm decoded

### 8. File Locations

**Scanners (GitHub + Local):**
- GitHub: uerzer/opportunity-intelligence/scanners/
- Local: scripts/opportunity-scanners/

**Documentation:**
- Recovery Guide: docs/CONTEXT_RESTORATION_GUIDE.md
- Project Status: notes/github_backup_project_status.md

**Triggers:**
- Hourly backup: @trigger:hourly-scanner-backup
- Auto context load: @trigger:auto-load-context-on-new-conversations

---

## Emergency Contact
If all else fails, GitHub is the single source of truth:
**https://github.com/uerzer/opportunity-intelligence**

Last backup: Automated hourly (check commit history for latest)

---
**Document Created:** 2026-02-12 22:49 WET  
**Auto-Updated:** Via hourly GitHub backup trigger