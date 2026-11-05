# REFERENCE INVENTORY & SOURCE REPOSITORY AUDIT
## ERP Knowledge Hub — Enterprise Resource Planning & Supply Chain Management

---

## 1. Executive Summary & Audit Scope

This document establishes the official reference inventory for the **ERP Knowledge Hub**. In strict accordance with Project Directive Section 1 & Section 3, all files in the `references/` directory are treated as **strictly read-only artifacts**. No source files have been altered, renamed, moved, or deleted.

The source repository contains one primary university textbook and five case study artifacts (four PDF case studies and one high-resolution supplementary image artifact) utilized in the course **"Enterprise Resource Planning (ERP) Applied to Logistics & Supply Chain Management"** at the **School of International Business and Marketing — University of Economics Ho Chi Minh City (UEH)**.

---

## 2. Source Files Inventory Table

| # | File Name | Format | Size (Bytes) | Source Path | Primary Role & Domain |
|---|---|---|---|---|---|
| **REF-01** | `ERP transportation  inventory Textbook for Students.pdf` | PDF (Digital slides) | 3,616,914 | `references/` | Primary Academic Coursebook (Weeks 1–6): ERP Foundations, Mathematical LP Transportation, Variations, Inventory Modeling (EOQ, EPQ), Solver & QM. |
| **REF-02** | `Case 1 – A CASE STUDY THE TEXAGO CORP. SITE SELECTION PROBLEM.pdf` | PDF (Document) | 247,721 | `references/Case studies/` | Case Study 1: Multi-echelon petroleum network, crude oil routing, plant location, finished product distribution. |
| **REF-03** | `Bổ sung dữ liệu cho case study 1 - TEXAGO.jpg` | JPEG Image | 31,136 | `references/Case studies/` | Critical supplementary data table: Finished product freight matrix & distribution center demand units for Texago Corp. |
| **REF-04** | `Case 2.1 – ASSIGNING PLANTS TO PRODUCTS (BETTER PRODUCTS COMPANY).pdf` | PDF (Document) | 194,377 | `references/Case studies/` | Case Study 2: Production allocation, capacity balancing, product splitting vs. zero-splitting assignment constraint. |
| **REF-05** | `Case 3 - The Atlantic coast tire corp (ACT) problem.pdf` | PDF (Document) | 282,701 | `references/Case studies/` | Case Study 3: Wholesaler distribution inventory control, cost trade-offs, holding vs. ordering vs. stockout costs. |
| **REF-06** | `Case 4 - SOCA - gradual replenishment.pdf` | PDF (Document) | 203,067 | `references/Case studies/` | Case Study 4: Manufacturing batch sizing, Economic Production Quantity (EPQ), non-instantaneous replenishment dynamics. |

---

## 3. Detailed Source Breakdown & Technical Characteristics

### 3.1 REF-01: Primary Academic Textbook
- **Filename**: `ERP transportation  inventory Textbook for Students.pdf` *(Note: Contains double space in original filename; preserved intact).*
- **Title**: *Enterprise Resource Planning (ERP) Applied to Logistics & Supply Chain Management (2 Credits)*
- **Issuing Institution**: University of Economics Ho Chi Minh City (UEH) — School of International Business and Marketing.
- **Author**: Y Hoang.
- **Publication Year**: 2020 (Internal circulation).
- **Physical Extent**: 149 slides / pages.
- **Creator / Producer**: Microsoft® PowerPoint® for Office 365.
- **Structure**:
  - Pages 1–8: Course Introduction, Syllabus, Learning Objectives, Grading Matrix, Weekly Schedule (Weeks 1–6).
  - Pages 9–47: **Week 1** — Introduction to ERP & Software Applications in Transportation (SCM definitions, business modules, LP Transportation formulation, P&T Co. case, Excel Solver, QM for Windows).
  - Pages 48–58: **Week 2** — Variations of Transportation Problems Part 1 (Supply $\neq$ Demand: Metro Water District; Prohibited Combinations: Energetic Company).
  - Pages 59–70: **Week 3** — Variations of Transportation Problems Part 2 (Unstable Demand Ranges: Middletown School District; Profit Maximization: Nifty Company; Assignment Problems, Hungarian & Simplex Methods; Transportation Glossary).
  - Pages 71–97: **Week 4** — Software Applications in Inventory Management (Inventory definitions, 4 cost components, Basic EOQ model derivation, Atlantic Coast Tire Corp. baseline model, Excel Solver non-linear formulation).
  - Pages 98–142: **Week 5** — Variations of EOQ Model in Inventory Management (Variant 1: EOQ with Planned Shortages / Backorders; Variant 2: EOQ with Quantity Discounts; Variant 3: EOQ with Gradual Replenishment / EPQ; Solver & QM workflows).
  - Pages 143–148: Inventory Management Glossary.
  - Page 149: Week 6 — Wrap-up & Project Presentation.

### 3.2 REF-02 & REF-03: Case Study 1 & Supplementary Image
- **REF-02 Title**: *Case 1 – A Case Study: The Texago Corp. Site Selection Problem*
- **Extent**: 3 pages.
- **Context**: Texago Corporation operates 3 domestic oil fields (Texas, California, Alaska) and imports Middle East crude. It operates 3 refineries (New Orleans, Charleston, Seattle) and seeks to select 1 new refinery site among 3 candidates (Los Angeles, Galveston, St. Louis) to satisfy 4 regional distribution centers (Pittsburgh, Atlanta, Kansas City, San Francisco).
- **REF-03 Audit**: `Bổ sung dữ liệu cho case study 1 - TEXAGO.jpg` (Resolution: 587 $\times$ 315 px).
  - **Critical Role**: Table 2.8.2 in REF-02 was mislabeled as "Cost Data for shipping crude oil to a Texago Refinery 2" and lacked the required customer demand units. The JPG artifact supplies the definitive matrix titled:
    `Cost per Unit Shipped to Distribution Center (Millions of Dollars)` with the essential bottom row:
    - Pittsburgh: 100 million barrels
    - Atlanta: 80 million barrels
    - Kansas City: 80 million barrels
    - San Francisco: 100 million barrels
    - Total Demand: 360 million barrels (exactly balancing total refinery capacity of 360 million barrels: New Orleans 100 + Charleston 60 + Seattle 80 + New Site 120 = 360).

### 3.3 REF-04: Case Study 2
- **Title**: *Case 2.1 & Case 2.2 – Assigning Plants to Products (Better Products Company)*
- **Extent**: 2 pages.
- **Context**: Better Products Company has 3 manufacturing plants with excess capacity (75, 75, 45 units/day = 195 units/day total) and 4 new products with projected daily sales (20, 30, 30, 40 units/day = 120 units/day total).
  - **Part 2.1 (Product Splitting Permitted)**: Balanced via dummy product (demand = 75 units/day at zero cost). Plant 2 is prohibited from manufacturing Product 3 (enforced via high penalty cost $M$).
  - **Part 2.2 (Product Splitting Prohibited)**: Formulated as a zero-one binary assignment problem where plants 1 & 2 have capacity to produce up to 2 products, plant 3 can produce 1 product, and each product must be allocated to exactly one plant to eliminate split-setup and coordination overhead.

### 3.4 REF-05: Case Study 3
- **Title**: *Case Study: The Atlantic Coast Tire Corp. (ACT) Problem*
- **Extent**: 3 pages.
- **Context**: ACT is the eastern seaboard wholesaler of Eversafe tires supplying 1,500 retail dealers. Focuses on tire size 185/70 R13.
- **Parameters**: Monthly sales = 500 tires ($D = 6,000$ tires/year); purchase cost $c = \$20$/tire; order administrative & labor setup $K = \$90 + \$25 = \$115$/order; capital opportunity cost = 15% + storage/handling/insurance = 6% $\rightarrow h = 21\% \times \$20 = \$4.20$/tire/year; shortage penalty $p = \$7.50$/tire short/year.
- **Role in Platform**: Serves as the continuous thread for Week 4 (Basic EOQ) and Week 5 (Planned Shortages and Quantity Discounts).

### 3.5 REF-06: Case Study 4
- **Title**: *Case Study: The SOCA (Gradual Replenishment)*
- **Extent**: 2 pages.
- **Context**: SOCA is a consumer electronics manufacturer assembling television sets requiring 1,000 internal speakers per day ($d = 1,000$). Speaker production line operates at $p = 3,000$ units/day when active.
- **Parameters**: 250 operational days/year ($D = 250,000$ units/year); unit production cost $c = \$12$; setup cost $K = \$12,000$/run; holding cost $h = \$3.60$/unit/year.
- **Role in Platform**: Benchmark case study for Economic Production Quantity (EPQ), gradual inventory build-up, and production cycle optimization.

---

## 4. Traceability & Academic Integrity Rules

1. **Direct Provenance**: Every formula, parameter, decision variable, and cost coefficient presented in the Knowledge Base, Practice Exams, Flashcards, and Case Studies is directly cross-referenced to these source files.
2. **Editorial Transparency**: Any supplementary Business Analyst insights, enterprise ERP mappings (e.g., SAP S/4HANA, Oracle SCM), or modern operational workflows added to enrich student learning are explicitly labeled as *[BA Perspective & ERP Industry Practice]* to differentiate them from UEH primary course slides.
3. **Immutability Assurance**: The hash, byte size, and path of all reference files have been indexed and will remain untouched across all development cycles.
