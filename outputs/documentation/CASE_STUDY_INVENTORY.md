# CASE STUDY INVENTORY & DETAILED ARCHITECTURAL AUDIT
## Comprehensive Analysis of Core Case Studies & Datasets

---

## 1. Case Study Overview Matrix

| Case ID | Official Case Title | File Name & Format | Page Count | Industry / Domain | Core Mathematical & ERP Optimization Models |
|---|---|---|---|---|---|
| **CASE-01** | The Texago Corp. Site Selection Problem | `Case 1 – A CASE STUDY THE TEXAGO CORP. ...pdf` + `Bổ sung dữ liệu...jpg` | 3 pages + 1 JPG | Petroleum & Petrochemical Refining / Energy SCM | Two-echelon linear programming transportation model, facility location selection, crude oil supply chain logistics. |
| **CASE-02** | Assigning Plants to Products (Better Products Company) | `Case 2.1 – ASSIGNING PLANTS TO PRODUCTS ...pdf` | 2 pages | Consumer Goods Manufacturing / Industrial Production | Unbalanced transportation model with dummy demand, prohibited routing ($M$-method), zero-one binary integer assignment model. |
| **CASE-03** | The Atlantic Coast Tire Corp. (ACT) Problem | `Case 3 - The Atlantic coast tire corp (ACT) problem.pdf` | 3 pages | Automotive Aftermarket & Wholesale Tire Distribution | Scientific inventory management, cost trade-off analysis, Basic EOQ, EOQ with Planned Shortages (Backorders), EOQ with Quantity Discounts. |
| **CASE-04** | The SOCA Problem (Gradual Replenishment) | `Case 4 - SOCA - gradual replenishment.pdf` | 2 pages | Consumer Electronics & Television Manufacturing | Economic Production Quantity (EPQ), gradual replenishment, finite production rates, manufacturing batch lot sizing. |

---

## 2. In-Depth Case Analysis & Parameter Inventory

### 2.1 CASE-01: The Texago Corp. Site Selection Problem

#### A. Business Context & Strategic Setting
The Texago Corporation is a major, fully integrated petroleum corporation headquartered in the United States. It extracts crude oil from company-owned domestic oil fields and supplements its petroleum balance through imports from Middle East oil terminals. An extensive logistics pipeline, tanker, and rail distribution network connects crude sources to regional refineries, and subsequently transports refined consumer products (gasoline, diesel, lubricants) to regional wholesale distribution centers.

Due to growing domestic market share, Texago's executive leadership has authorized a capital expansion program: construct one additional high-capacity refinery (processing 120 million barrels of crude annually) and increase imports of Middle East crude oil. The core strategic decision facing executive leadership is **selecting the optimal geographic location for the new refinery** among three candidate sites:
1. Near Los Angeles, California
2. Near Galveston, Texas
3. Near St. Louis, Missouri

#### B. Stakeholders & Organizational Roles
- **Chief Supply Chain Officer (CSCO) & VP of Logistics**: Responsible for freight contracts, pipeline allocations, and overall network distribution costs.
- **VP of Refining & Operations**: Responsible for plant capacity utilization and annual operating budgets.
- **Corporate Controller & Chief Financial Officer (CFO)**: Responsible for minimizing total annual variable operating and distribution expenditure.
- **Regional Distribution Center Managers**: Responsible for product availability and meeting regional customer fuel demands.

#### C. Facility Locations & Operational Capacities

**Table 1: Existing & Expanded Crude Oil Supply Capacities**
| Source Field / Terminal | Annual Crude Capacity (Million Barrels) | Notes |
|---|---|---|
| **Texas Oil Fields** | 80 | Domestic field extraction |
| **California Oil Fields** | 60 | Domestic field extraction |
| **Alaska Oil Fields** | 100 | Tanker shipping from North Slope |
| **Middle East Imports** | 120 | Variable import quantity to balance network ($360 - 240 = 120$) |
| **Total Crude Available** | **360** | Matches total refinery capacity exactly |

**Table 2: Refinery Capacities**
| Refinery | Annual Crude Requirement (Million Barrels) | Status |
|---|---|---|
| **New Orleans, Louisiana** | 100 | Existing refinery |
| **Charleston, South Carolina** | 60 | Existing refinery |
| **Seattle, Washington** | 80 | Existing refinery |
| **New Refinery Site (Candidate)** | 120 | One of: Los Angeles, Galveston, or St. Louis |
| **Total Refinery Capacity** | **360** | Must operate at 100% rated capacity |

**Table 3: Regional Distribution Centers & Annual Product Requirements**
*(Source: Cross-verified with `Bổ sung dữ liệu cho case study 1 - TEXAGO.jpg`)*
| Distribution Center | Location | Annual Required Finished Product (Million Barrels) |
|---|---|---|
| **Pittsburgh** | Pennsylvania | 100 |
| **Atlanta** | Georgia | 80 |
| **Kansas City** | Missouri | 80 |
| **San Francisco** | California | 100 |
| **Total Finished Demand** | | **360** |

#### D. Transportation & Operating Cost Datasets

**Table 4: Unit Freight Costs for Shipping Crude Oil to Refineries ($ Millions per Million Barrels)**
| Crude Source \ Refinery | New Orleans | Charleston | Seattle | Los Angeles (Cand.) | Galveston (Cand.) | St. Louis (Cand.) |
|---|---|---|---|---|---|---|
| **Texas** | \$2 | \$4 | \$5 | \$3 | \$1 | \$1 |
| **California** | \$5 | \$5 | \$3 | \$1 | \$3 | \$4 |
| **Alaska** | \$5 | \$7 | \$3 | \$4 | \$5 | \$7 |
| **Middle East** | \$2 | \$3 | \$5 | \$4 | \$3 | \$4 |

**Table 5: Unit Freight Costs for Shipping Finished Products to Distribution Centers ($ Millions per Million Barrels)**
*(As audited from `Bổ sung dữ liệu cho case study 1 - TEXAGO.jpg`)*
| Refinery \ Distribution Center | Pittsburgh | Atlanta | Kansas City | San Francisco |
|---|---|---|---|---|
| **New Orleans** | \$6.5 | \$5.5 | \$6.0 | \$8.0 |
| **Charleston** | \$7.0 | \$5.0 | \$4.0 | \$7.0 |
| **Seattle** | \$7.0 | \$8.0 | \$4.0 | \$3.0 |
| **Los Angeles (Candidate)** | \$8.0 | \$6.0 | \$3.0 | \$2.0 |
| **Galveston (Candidate)** | \$5.0 | \$4.0 | \$3.0 | \$6.0 |
| **St. Louis (Candidate)** | \$4.0 | \$3.0 | \$1.0 | \$5.0 |
| **Units Needed** | **100** | **80** | **80** | **100** |

**Table 6: Annual Refinery Operating Costs by Candidate Location**
| Candidate Site | Annual Fixed Operating Cost ($ Millions) | Key Strategic Advantages |
|---|---|---|
| **Los Angeles, CA** | \$620 | Adjacent to CA fields; direct tanker access from Alaska; close to SF distribution center. |
| **Galveston, TX** | \$570 | Adjacent to Texas fields; direct deepwater Gulf port for Middle East tankers; close to corporate HQ. |
| **St. Louis, MO** | \$530 | Lowest operating cost; centrally located for midwestern/eastern distribution; Mississippi barge access. |

#### E. Analytical Requirements & Mathematical Decision Model
The problem requires formulating and evaluating three distinct scenarios (one for each candidate site $k \in \{\text{LA}, \text{Galveston}, \text{St. Louis}\}$). For each scenario, two independent LP transportation models must be solved:
1. **Crude Transportation Model**: 4 Sources $\times$ 4 Refineries ($3 \text{ existing} + 1 \text{ candidate}$).
2. **Finished Product Transportation Model**: 4 Refineries $\times$ 4 Distribution Centers.
3. **Total Variable Cost Calculation**:
   $$\text{Total Cost}_k = \text{Crude Shipping Cost}_k + \text{Finished Shipping Cost}_k + \text{Annual Operating Cost}_k$$
4. **Site Recommendation**: Select candidate site $k^*$ that minimizes total annual variable system expenditure.

---

### 2.2 CASE-02: Assigning Plants to Products (Better Products Company)

#### A. Business Context & Strategic Setting
Better Products Company is a diversified manufacturing enterprise preparing to launch four new consumer products (Product 1, 2, 3, 4). The company possesses three operational manufacturing plants currently operating with excess production capacity. The products require comparable manufacturing equipment and processing times per unit, enabling capacity to be measured in homogeneous units per day.

#### B. Case 2.1: Product Splitting Permitted (Unbalanced Transportation Formulation)
- **Plant Capacities (Supply)**:
  - Plant 1: 75 units/day
  - Plant 2: 75 units/day
  - Plant 3: 45 units/day
  - **Total Available Capacity**: 195 units/day
- **Product Demand**:
  - Product 1: 20 units/day
  - Product 2: 30 units/day
  - Product 3: 30 units/day
  - Product 4: 40 units/day
  - **Total Required Production**: 120 units/day
- **Supply-Demand Imbalance**: Supply (195) > Demand (120) by **75 units/day**.
  - Add **Dummy Product (Unused Capacity)** with demand = 75 units/day and unit cost = \$0.
- **Infeasible / Prohibited Route**: Plant 2 cannot produce Product 3.
  - Handled via penalty cost $M$ (e.g., \$999,999) or setting variable bound $x_{23} = 0$.
- **Unit Variable Cost Matrix ($/unit)**:
  | Plant \ Product | 1 | 2 | 3 | 4 | Dummy | Available Capacity |
  |---|---|---|---|---|---|---|
  | **Plant 1** | \$41 | \$27 | \$28 | \$24 | \$0 | 75 |
  | **Plant 2** | \$40 | \$29 | Prohibited ($M$) | \$23 | \$0 | 75 |
  | **Plant 3** | \$37 | \$30 | \$27 | \$21 | \$0 | 45 |
  | **Required** | **20** | **30** | **30** | **40** | **75** | **195** |

#### C. Case 2.2: Product Splitting Prohibited (Binary Integer Assignment Formulation)
- **Business Rationale**: Management recognizes that splitting the production of a single product across multiple plants introduces severe hidden overhead: redundant machine tooling setups, duplicated quality inspections, split freight shipments, and complex administrative tracking.
- **Decision Restriction**: Each product must be assigned to **exactly one plant**.
- **Plant Assignment Capacities**:
  - Plant 1: capacity for up to 2 products.
  - Plant 2: capacity for up to 1 product.
  - Plant 3: capacity for up to 1 product.
  - Total assignments = $2 + 1 + 1 = 4$ products.
- **Daily Operating & Tooling Cost Matrix ($/day)**:
  | Plant \ Product | 1 | 2 | 3 | 4 | Max Allowed Products |
  |---|---|---|---|---|---|
  | **Plant 1** | \$820 | \$810 | \$840 | \$960 | 2 |
  | **Plant 2** | \$800 | \$870 | Prohibited ($M$) | \$920 | 1 |
  | **Plant 3** | \$740 | \$900 | \$810 | \$840 | 1 |
  | **Required** | **1** | **1** | **1** | **1** | **4** |
- **Mathematical Structure**: Binary 0–1 Integer Programming ($x_{ij} \in \{0, 1\}$) or converted to standard assignment tableau by splitting Plant 1 into two identical sub-plants (Plant 1A and Plant 1B).

---

### 2.3 CASE-03: The Atlantic Coast Tire Corp. (ACT) Problem

#### A. Business Context & Strategic Setting
Atlantic Coast Tire Corporation (ACT) is the premier regional wholesale distributor of Eversafe brand automobile tires across the eastern seaboard of the United States. ACT maintains a central distribution warehouse serving 1,500 independent retail tire dealerships and automotive service centers. The warehouse stocks a dozen tire specifications, focusing analytically on high-volume model **185/70 R13**.

Shipments are made continually to retail dealers. Replenishment orders are sent via electronic EDI/fax to Eversafe's manufacturing plant, with an average transit and handling lead time of **9 working days**.

#### B. Inventory Baseline & Cost Breakdown
- **Demand Rate ($D$)**: 500 tires/month = **6,000 tires/year** (regular, constant demand).
- **Unit Purchase Price ($c$)**: **\$20.00** per tire.
- **Order Setup Cost ($K$)**:
  - Labor: 6 hours $\times \$15.00$/hour = \$90.00.
  - Overhead (supervision, facilities, paperwork): \$25.00.
  - Total setup cost $K = \$90.00 + \$25.00 = \mathbf{\$115.00}$ per order.
- **Holding Cost Rate ($I$ & $h$)**:
  - Opportunity cost of capital: 15% per annum.
  - Physical warehouse leasing, property insurance, security, and inventory valuation taxes: 6% per annum.
  - Total annual holding rate: $I = 15\% + 6\% = 21\%$ per annum.
  - Unit annual holding cost: $h = 0.21 \times \$20.00 = \mathbf{\$4.20}$ per tire per year.
- **Shortage Penalty Cost ($p$)**:
  - Customers will wait a reasonable period (backorders), but ACT incurs customer dissatisfaction, discounts to placate delayed buyers, deferred cash flow, and manual expediting labor.
  - Unit shortage cost: $p = \mathbf{\$7.50}$ per tire short per year.

#### C. Decision Modeling & Variations Explored
1. **Current Heuristic Policy**: $Q = 1,000$ tires ordered every 2 months.
   - Average inventory = 500 tires.
   - Annual Setup Cost = $\$115 \times \frac{6,000}{1,000} = \$690$.
   - Annual Holding Cost = $\$4.20 \times 500 = \$2,100$.
   - Current $TVC = \mathbf{\$2,790}$.
2. **Basic EOQ Model**:
   - $Q^* = \sqrt{\frac{2 \times 115 \times 6000}{4.20}} \approx 573.2 \implies \mathbf{573 \text{ tires}}$.
   - $TVC^* = \mathbf{\$2,407.48}$ (13.7% savings).
3. **Planned Shortages Model**:
   - $Q^* \approx 716$ tires, Max Shortage $S^* \approx 257$ tires, Max Inventory = 459 tires.
   - $TVC^* = \mathbf{\$1,927.56}$ (30.9% savings vs. current heuristic).
4. **Quantity Discounts Model**:
   - Tier 1 (0–749): \$20.00 $\rightarrow TC = \$122,407.48$
   - Tier 2 (750–1,999): \$19.80 $\rightarrow TC(750) = \mathbf{\$121,279.25}$ (Optimal)
   - Tier 3 ($\ge 2,000$): \$19.60 $\rightarrow TC(2,000) = \$122,061.00$

---

### 2.4 CASE-04: The SOCA Problem (Gradual Replenishment)

#### A. Business Context & Strategic Setting
SOCA is a leading consumer television and home entertainment manufacturing company. To ensure acoustic quality and component availability, SOCA operates an internal specialized speaker fabrication department that feeds its final television assembly line.

#### B. Operational & Cost Parameters
- **Assembly Consumption Rate ($d$)**: **1,000 speakers per day**.
- **Internal Production Rate ($p$)**: **3,000 speakers per day** when active.
- **Operating Schedule**: 250 working days per year.
- **Annual Demand ($D$)**: $1,000 \times 250 = \mathbf{250,000 \text{ speakers per year}}$.
- **Unit Production Cost ($c$)**: **\$12.00** per speaker ($c \times D = \$3,000,000$ fixed baseline).
- **Setup Cost ($K$)**: **\$12,000.00** per production setup run.
- **Holding Cost ($h$)**: **\$3.60** per speaker in inventory per year.

#### C. Mechanics of Gradual Replenishment
Because $p = 3,000 > d = 1,000$, speakers are produced three times faster than they are consumed. Production runs operate during only $\frac{d}{p} = \frac{1}{3}$ of the working calendar. During production, inventory accumulates at net rate $p - d = 2,000$ units/day.

- **Current Policy ($Q = 30,000$ speakers)**:
  - Production duration: $t_p = \frac{30,000}{3,000} = 10$ working days.
  - Depletion duration: $t_d = \frac{20,000}{1,000} = 20$ working days.
  - Total cycle length: $T = 10 + 20 = 30$ working days.
  - Maximum inventory: $M = 30,000 - (10 \times 1,000) = \mathbf{20,000 \text{ speakers}}$.
  - Average inventory: $\frac{20,000}{2} = \mathbf{10,000 \text{ speakers}}$.
  - Annual Setup Cost: $\$12,000 \times \frac{250,000}{30,000} = \mathbf{\$100,000}$.
  - Annual Holding Cost: $\$3.60 \times 10,000 = \mathbf{\$36,000}$.
  - Current $TVC = \mathbf{\$136,000}$.

- **Optimal EPQ Policy**:
  - Lot size:
    $$Q^* = \sqrt{\frac{2 \times 12,000 \times 250,000}{3.60 \times \left(1 - \frac{1,000}{3,000}\right)}} = \sqrt{\frac{6,000,000,000}{2.40}} = \mathbf{50,000 \text{ speakers}}$$
  - Production run time: $t_p^* = \frac{50,000}{3,000} = 16.67$ working days.
  - Cycle length: $T^* = \frac{50,000}{1,000} = 50$ working days (5 cycles per year).
  - Maximum inventory: $M^* = 50,000 \times \frac{2}{3} = \mathbf{33,333.33 \text{ speakers}}$.
  - Average inventory: $\mathbf{16,666.67 \text{ speakers}}$.
  - Annual Setup Cost: $\$12,000 \times 5 = \mathbf{\$60,000}$.
  - Annual Holding Cost: $\$3.60 \times 16,666.67 = \mathbf{\$60,000}$.
  - Optimal $TVC^* = \$60,000 + \$60,000 = \mathbf{\$120,000}$.
  - **Annual Cost Reduction**: $\mathbf{\$16,000 \text{ per year}}$ (11.8% savings).

---

## 3. Supplementary Data Artifact Integration Audit: `Bổ sung dữ liệu cho case study 1 - TEXAGO.jpg`

- **Visual Properties**: Grayscale high-contrast image (587 $\times$ 315 px), containing a clean typeset table.
- **Discrepancy in Original PDF**:
  In `Case 1 – A CASE STUDY THE TEXAGO CORP. SITE SELECTION PROBLEM.pdf`, Table 2.8.2 on Page 2 was titled:
  *“Table 2.8.2 – Cost Data for shipping crude oil to a Texago Refinery 2”*
  This was an erroneous heading, as the columns were Pittsburgh, Atlanta, Kansas City, and San Francisco (which are Distribution Centers, not Refineries!). Furthermore, the PDF table failed to print the required annual finished product units needed by these distribution centers.
- **Resolution via Supplementary Image**:
  The JPG artifact provides the corrected title:
  *“Cost per Unit Shipped to Distribution Center (Millions of Dollars)”*
  and supplies the definitive demand figures:
  $$\text{Pittsburgh: 100} \quad \text{Atlanta: 80} \quad \text{Kansas City: 80} \quad \text{San Francisco: 100} \quad (\Sigma = 360)$$
  This provides mathematical closure to the Texago optimization model, ensuring total supply ($360$) equals total demand ($360$).
