# [AMP] V53 P1 Postmortem - UAT1_09.18.2024


## Slide 1: V53 P1 Postmortem - UAT1
V53 P1 Postmortem - UAT1
Amphenol
09-18-2024

## Slide 2
PM Contents Overall
Low
High
Mid

| No. | PM Contents | V53 UAT1 |
|---|---|---|
| 1 | O-Chart and Resource |  |
| 2 | Config and Build Status |  |
| 3 | IQC | Avary FAI5 low CPK issue waived by AP |
| 4 | Process, Yield and FACA |  |
| 5 | OQC and ORT | On-going，due date 10/16，so far low  risk |
| 6 | Customer Issue |  |
| 7 | Test Review |  |
| 8 | Stack up |  |
| 9 | CPK of FAI/SPC |  |
| 10 | Data Collection Review |  |
| 11 | PFMEA |  |
| 12 | DFM “build and collect data” |  |
| 13 | Mis-handling |  |
| 14 | DFMs |  |
| 15 | Soft/Hard tool |  |
| 16 | MP layout |  |
| 17 | Lesson Learnt |  |
| 18 | MP Readiness |  |
| 19 | SPOR |  |
| 20 | MP LQ Plan |  |


## Slide 3: 2. Build status
2. Build status
Complete
On-Track
At Risk - Non Blocking/TBD
At Risk - Blocking

| Flex Name | Ass’y APN | BF Material | Config | Assembly | Ship to | Build Status |  | Remark |
|---|---|---|---|---|---|---|---|---|
| V53 UAT1 | 632-07540 | LCP | POR | AMP | FXGL | Completed |  | 2,300x shipped to FATP |
| V53 UAT1 | 932-04977 | LCP | DOE | AMP | FXGL | Completed |  | 1,000x shipped to FATP |


## Slide 4
Postmortem Review Items:
A. Resource (NPI and  MP)
1) O-chart and resource plan
Team list from x-function team, provide CA if any gap per apple resource plan for both NPI and MP.
B. Build review (Design, Process and Quality)
2) Configs and build status
3) IQC
IQC yield and issue FACA, MIL review. CPK is needed for dimensional, parametric data. IQC should do check for all material such as FCCL, coverlay, stiffener, SUS and TSA/PSA, and SMT parts.
4) Process yield of bare flex and flex Assembly
Bare flex, Flex assembly process flow chart,  design/process/quality summary, yield tread chart, Update MP yield projection based on “yield calculator” tool.
5) OQC Issue and ORT
Bare flex and Assembly ORT review.
6) Downstream/Customer issue review
FATP/MI IQC / online /ORT issue MIL review,
7) Test review
Test fixture, ERS, correlation, funnel spec, test coverage+mitigation plan, test data distribution + Cpk, and any recommendation on testing. Test automation + MP plan.
8) Flex stackup with 5x cross-section data table, FACA if CPK not meeting 1.67
9) Cp/Cpk histogram of FAI/SPC (32pcs).
Need FACA for Cpk<1.33 or distribution abnormal; Improvement plan and control plan needed for both FAI/SPC Cpk over 1.33 but less than 1.67
10) Data collection review
Follow “Apple Flex DFM NPI Data Collection Requirement”,  “Component Peel Test Procedure for FPCA “, “Component Shear Test Procedure for FPCA”.  Data analysis and FACA are needed for failures and findings
11) DFMEA/PFMEA Top5 issue update
12) Follow up of DFM “build and collect data” items when OK2Fab. Plus monitoring and reject item, which impact quality
13) Flex mishandling and abuse test review
Follow “Flex mishandling and abuse test guideline”, and test to failure to catch design weakness. *Not MCO defined bending line
C.  Readiness (NPI and MP)
14) DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction
For bare flex, pls. provide detailed self-assessment per Apple product CPP or generic CPP and Quality control list,  provide actions how to meet requests if there is gap.
Sufficient data and validation are needed for design change and recommendation.
15) NPI Soft tool and MP hard tool report
MP hard tool refers to MP intended hard tool, any tool not for final MP is not MP hard tool. MP intended hard tool is a must from EVT.
16) Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT)
17) Lesson learn from last generation and this build (what can make next build and MP better for design, process and build management)
18) MP readiness (update from P2 postmortem), MP readiness + Automation/traceability scores (update from EVT postmortem)
19) Vendor owned MP material supplier POR (Plan Of Record), including FCCL, coverlay, PSA&TSA, DIE Cut suppliers, SUS. Also need tracking list of these material used in each build (Proto,EVT, Carrier, DVT,PVT, Rampup).
20) MP line qual plan including, define DRI and team list

## Slide 5
V53 | Product Introduction | UAT1

| Project | Flat | Fold |
|---|---|---|
| V53 UAT1 |  |  |


## Slide 6
V53 | Design Comparison | UAT1

| Difference | Build Stage |  |  |  |  |
|---|---|---|---|---|---|
|  | P1 | P2 | EVT | CRB | Comparison P1 vs. P2 |
| N/A | N/A | N/A | N/A | N/A | N/A |
| N/A | N/A | N/A | N/A | N/A | N/A |


## Slide 7
V53 | Design Comparison | UAT1

| Difference | Flex |  |  |  |  |  |
|---|---|---|---|---|---|---|
|  | D93 | V53 | Comparison D93 vs. V53 |  |  |  |
| SMT |  |  | No. | Flex | D93 | V53 |
|  |  |  | 1 | Flex Outline | 41.37 * 14.29 mm | 22.89 * 43.76 mm |
|  |  |  | 2 | Flex Stackup | 4 layers | 4 layers |
|  |  |  | 3 | Bonding | UAT1 + Honeycrisp | UAT1 + Strobe |
|  |  |  | 4 | Barcode | Bot side | Top side |
|  |  |  | 5 | Component | 0402 | 0805 |
|  |  |  | 6 | CPSA | N/A | 1 pcs |
|  |  |  | 7 | PSA/Mic film | 1 pcs | 5 pcs |
|  |  |  | 8 | Clip | 10 pcs | 15 pcs |
|  |  |  | 9 | B2B | 516S00528, 22Pin | 516S01290, 30Pin |
| Bending |  |  | D93: Bending * 2 V53: Bending * 5 |  |  |  |


## Slide 8
V53 | Config Comparison | UAT1

| BM Config | POR | DOE | Difference |
|---|---|---|---|
| Gerber | 821-05715-01 | 921-05695-01 |  |
| Component |  |  | POR: 0805 Component * 1 DOE: 0402 Component * 4 |


| Flex | BM Config | Stackup | MCO | MCO Rev | Gerber | Gerber Rev | BOM | BOM Rev | SCH | SCH Rev | EEEEEEE |
|---|---|---|---|---|---|---|---|---|---|---|---|
| V53 UAT1 | POR | 4 layers | 056-20573 | 37 | 821-05715 | 01 | 632-07540 | 02 | 051-11437 | 2.0.0 | 0000TPV |
|  | DOE | 4 layers | 056-20573 | 37 | 921-05695 | 01 | 932-04977 | - | 951-24641 | 1.0.0 | - |


## Slide 9
Postmortem Review Items:
A. Resource (NPI and  MP)
1) O-chart and resource plan
Team list from x-function team, provide CA if any gap per apple resource plan for both NPI and MP.
B. Build review (Design, Process and Quality)
2) Configs and build status
3) IQC
IQC yield and issue FACA, MIL review. CPK is needed for dimensional, parametric data. IQC should do check for all material such as FCCL, coverlay, stiffener, SUS and TSA/PSA, and SMT parts.
4) Process yield of bare flex and flex Assembly
Bare flex, Flex assembly process flow chart,  design/process/quality summary, yield tread chart, Update MP yield projection based on “yield calculator” tool.
5) OQC Issue and ORT
Bare flex and Assembly ORT review.
6) Downstream/Customer issue review
FATP/MI IQC / online /ORT issue MIL review,
7) Test review
Test fixture, ERS, correlation, funnel spec, test coverage+mitigation plan, test data distribution + Cpk, and any recommendation on testing. Test automation + MP plan.
8) Flex stackup with 5x cross-section data table, FACA if CPK not meeting 1.67
9) Cp/Cpk histogram of FAI/SPC (32pcs).
Need FACA for Cpk<1.33 or distribution abnormal; Improvement plan and control plan needed for both FAI/SPC Cpk over 1.33 but less than 1.67
10) Data collection review
Follow “Apple Flex DFM NPI Data Collection Requirement”,  “Component Peel Test Procedure for FPCA “, “Component Shear Test Procedure for FPCA”.  Data analysis and FACA are needed for failures and findings
11) DFMEA/PFMEA Top5 issue update
12) Follow up of DFM “build and collect data” items when OK2Fab. Plus monitoring and reject item, which impact quality
13) Flex mishandling and abuse test review
Follow “Flex mishandling and abuse test guideline”, and test to failure to catch design weakness. *Not MCO defined bending line
C.  Readiness (NPI and MP)
14) DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction
For bare flex, pls. provide detailed self-assessment per Apple product CPP or generic CPP and Quality control list,  provide actions how to meet requests if there is gap.
Sufficient data and validation are needed for design change and recommendation.
15) NPI Soft tool and MP hard tool report
MP hard tool refers to MP intended hard tool, any tool not for final MP is not MP hard tool. MP intended hard tool is a must from EVT.
16) Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT)
17) Lesson learn from last generation and this build (what can make next build and MP better for design, process and build management)
18) MP readiness (update from P2 postmortem), MP readiness + Automation/traceability scores (update from EVT postmortem)
19) Vendor owned MP material supplier POR (Plan Of Record), including FCCL, coverlay, PSA&TSA, DIE Cut suppliers, SUS. Also need tracking list of these material used in each build (Proto,EVT, Carrier, DVT,PVT, Rampup).
20) MP line qual plan including, define DRI and team list

## Slide 10
3. Dashboard | V53 UAT1 Dashboard

| Project |  | Flex | UAT1 | Remark |
|---|---|---|---|---|
|  |  | Program | V53 |  |
| SPOR |  | Back-End Supplier | AMP |  |
| Status |  |  | Yellow |  |
| Trend |  |  |  |  |
| Back-End/SMT |  | P1 |  |  |
|  |  | Latest Yield | 95.65% |  |
|  |  | Latest SMT Yield | 97.1% |  |
|  |  | Latest BE Yield | 98.99% |  |
|  |  | MP Yield Target | 96.5% |  |
|  |  | Build Yield Target | 85.0% |  |
|  |  | Supply Plan Yield | 99.0% |  |
| Project  Criteria | QE | DRI | Mark.Di |  |
|  |  | Flex IQC | Yellow | Avary PI flex FAI5 low CPK issue waived by AP. |
|  |  | Flex OQC | Green |  |
|  |  | FATP/MI Walkthrough | N/A |  |
|  |  | Traceability | Green |  |
|  |  | GR&R | Green |  |
|  |  | Tester Correlation | Green |  |
|  |  | ERS Compliance | Green |  |
|  |  | MCO Compliance | Green |  |
|  |  | AMREP | N/A |  |
|  |  | Source Inspection | N/A |  |
|  |  | Cross-Team Meeting (Flex&MI) | N/A |  |
|  |  | MSOP | Green |  |
|  |  | Inspection Criteria | Green |  |
|  |  | FATP and MI DPPM targets | N/A |  |
|  |  | Quality (QCP) | Green |  |
|  |  | OK2Ship | Green |  |
|  |  | Flex ORT | Yellow | On-going，due date 10/16，so far low  risk ， |
|  |  | FATP/MI IQC | Green |  |
|  |  | FATP/MI Process | Green |  |
|  |  | Sys./Mod. REL | N/A |  |

Pass or finished
Fail
Waived or on-going
NA
Yield cut-off date: 2024/09/10

## Slide 11

| Component type | Supplier | APN | Chekcing items | Sampling size | Methology | Result |
|---|---|---|---|---|---|---|
| LCP Bare Flex | muRata | 821-05715-01 921-05695-01 | Cosmetic | AQL 0.4/incoming lot | CCD | Pass |
|  |  |  | Dimension | 32pcs/incoming lot | OMM | Pass |
|  |  |  | Barcode read-ability | 32pcs/incoming lot | SR-2000 | Pass |
|  |  |  | Solder-ability | 3pcs/incoming lot | Dipping | Pass |
|  |  |  | Plating thickness | 32pcs/incoming lot | XRF | Pass |
| PI Bare Flex | Mflex Avary | 821-05769-01 | Cosmetic | AQL 0.4/incoming lot | CCD | Pass |
|  |  |  | Dimension | 32pcs/incoming lot | OMM | Avary FAI5 low CPK issue waived by AP. |
|  |  |  | Barcode read-ability | 32pcs/incoming lot | SR-2000 | Pass |
|  |  |  | Solder-ability | 3pcs/incoming lot | Dipping | Pass |
|  |  |  | Plating thickness | 32pcs/incoming lot | XRF | Pass |
| Connector | muRata | 516S01290 | Cosmetic | AQL 0.4/Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Reel | OMM | Pass |
|  |  |  | Coplanarity & warpage | 32pcs/incoming lot | OMM | Pass |
|  |  |  | Plating thickness | 32pcs/incoming lot | XRF | Pass |
|  |  |  | Solder-ability | 5pcs/incoming lot | Dipping | Pass |
| MIC | IFX GTK AAC | 731-00334 731-00337 731-00333 | Cosmetic | AQL 0.4/Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Per dimension | OMM | Pass |
|  |  |  | Solder-ability | 5pcs/per vendor | Dipping | Pass |
|  |  |  | Plating thickness | 32pcs/per vendor | XRF | Pass |
| IC | Qorvo Psemi Infineon | 353S03284 353S03304 353S03594 353S03610 353S04043 | Cosmetic | AQL 0.4/Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Reel | OMM | Pass |
| PSA | HB Dycut | No APN | Cosmetic | 5pcs/incoming lot | CCD | Pass |
|  |  |  | Dimension | 32pcs/incoming lot | OMM | Pass |
|  |  |  | Thickness | 32pcs/incoming lot | OMM | Pass |
|  |  |  | Single pcs pre-peel test | 10pcs/incoming lot | Manual | Pass |
|  |  |  | Peeling strength | 5pcs/adhesive lot | Pull tester | Pass |
| Clip | Ennvoi LY | 806-50867  806-50868 806-50869 806-50870 806-50871 806-50873 806-51162 806-51201 806-51346 806-51391 870-23917 870-23918 | Cosmetic | AQL 0.4, per Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Reel | OMM | Pass |
|  |  |  | Package | 32pcs/package D/C | OMM | Pass |
|  |  |  | Plating thickness | 32pcs/Reel | XRF | Pass |
|  |  |  | Solder-ability | 10pcs/Lot | Dipping | Pass |
|  |  |  | Peeling test | 32pcs/package D/C | Dummy board | Pass |

3. IQC Summary and Highlight | V53 UAT1
Pass
Fail
Waived

## Slide 12
AP waiver-Avary
3. IQC Summary and Highlight | V53 UAT1

| X5106 Strobe Tail | P1 | Avary | 821-05769-01 | 056-20744-17 | NA | All | Dimension | FAI5 low CPK. | FA: FAI 5-1 is less than 1/4 arc，FAI 5-2 is less than 1/8 arc(Measurement equipment capability≥1/4 arc)，Inaccurate point capture leads to unstable measurement. CA: 1. Waived for this build. 2. Suggest remove FAI 5, or change the two dimensions as reference. Next build. |
|---|---|---|---|---|---|---|---|---|---|


## Slide 13
V53 UAT1 LCP bare flex all outline dimension CPK can meet target 1.33.
3. IQC Summary and Highlight | V53 UAT1

| V53 UAT1 LCP bare flex outline dimension CPK |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Bare flex | Dimension |  | POR |  | DOE |  |
|  |  |  | AMP | muRata | AMP | muRata |
| muRata | FAI01 | 32.445±0.05 | 2.28 | 3.12 | 1.95 | 1.88 |
|  | FAI02 | 24.413±0.05 | 2.19 | 2.30 | 1.93 | 1.71 |
|  | FAI03 | 23.155±0.05 | 4.30 | 3.22 | 2.74 | 2.13 |
|  | FAI04 | 1.956±0.05 | 4.02 | 4.20 | 3.93 | 4.13 |
|  | FAI05 | 13.371±0.05 | 2.10 | 2.66 | 2.13 | 1.85 |
|  | FAI06 | 11.319±0.05 | 10.16 | 11.07 | 3.09 | 4.59 |
|  | FAI07 | 12.305±0.05 | 10.78 | 11.30 | 9.68 | 10.91 |
|  | FAI08 | 1.260±0.075 | 3.32 | 3.09 | 2.22 | 2.70 |
|  | FAI09 | 2.095±0.075 | 2.12 | 2.93 | 3.02 | 2.38 |
|  | FAI10 | 10.209±0.05 | 2.13 | 3.01 | 1.75 | 1.79 |
|  | FAI11 | 12.037±0.05 | 4.26 | 6.45 | 4.57 | 6.27 |
|  | FAI12 | 15.928±0.05 | 4.74 | 6.71 | 3.63 | 5.66 |
|  | FAI13 | 13.415±0.05 | 2.07 | 3.35 | 2.52 | 2.64 |
|  | FAI14 | 8.716±0.05 | 2.87 | 2.23 | 1.94 | 2.07 |
|  | FAI15 | 7.716±0.05 | 2.24 | 1.77 | 2.13 | 1.81 |
|  | FAI16 | 2.200±0.05 | 17.12 | 23.46 | 11.35 | 14.56 |
|  | FAI17 | 6.384±0.05 | 10.38 | 10.79 | 5.13 | 7.08 |
|  | FAI18 | 2.669±0.075 | 2.03 | 1.79 | 2.07 | 2.82 |
|  | FAI19 | 4.210±0.075 | 2.05 | 1.84 | 1.83 | 1.74 |
|  | FAI20 | 2.420±0.05 | 11.49 | 13.71 | 4.62 | 6.62 |
|  | FAI21 | 4.752±0.05 | 2.98 | 2.75 | 2.05 | 2.10 |
|  | FAI22 | 5.868±0.05 | 2.45 | 3.82 | 3.72 | 2.22 |
|  | FAI23 | 2.243±0.075 | 2.02 | 1.85 | 2.59 | 4.28 |
|  | FAI24 | 5.346±0.075 | 2.13 | 1.75 | 2.01 | 1.72 |
|  | FAI25 | 20.702±0.05 | 2.67 | 4.21 | 2.45 | 2.69 |
|  | FAI26 | 3.478±0.05 | 3.75 | 4.22 | 2.13 | 3.72 |
|  | FAI27 | 2.901±0.05 | 4.00 | 4.56 | 2.41 | 3.46 |
|  | FAI28 | 8.176±0.05 | 3.60 | 5.86 | 2.73 | 3.09 |
|  | FAI29 | 5.020±0.05 | 2.07 | 3.33 | 2.66 | 2.59 |
|  | FAI30 | 7.707±0.05 | 2.35 | 3.17 | 1.98 | 2.58 |
|  | FAI31 | 1.966±0.075 | 1.91 | 2.21 | 1.80 | 2.27 |
|  | FAI32 | 1.822±0.075 | 1.93 | 1.96 | 3.92 | 3.50 |
|  | FAI33 | 1.350±0.075 | 1.93 | 2.20 | 2.11 | 3.67 |
|  | FAI34 | 1.225±0.075 | 2.11 | 1.87 | 1.83 | 2.02 |
|  | FAI35 | 5.406±0.05 | 5.48 | 7.13 | 7.96 | 9.18 |


## Slide 14
V53 UAT1 Strobe Tail all outline dimension CPK can meet target 1.33.
3. IQC Summary and Highlight | V53 UAT1

| V53 UAT1 Strobe Tail outline dimension CPK |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Bare flex | Dimension |  | POR |  | POR |  |
|  |  |  | AMP | Mflex | AMP | Avary |
| Mflex Avary | FAI01 | 4.100±0.05 | 10.06 | 13.69 | 4.88 | 5.63 |
|  | FAI02 | 1.350±0.075 | 2.93 | 2.29 | 3.08 | 3.38 |
|  | FAI03 | 1.025±0.075 | 2.11 | 2.69 | 2.09 | 2.00 |
|  | FAI04 | 12.045±0.05 | 1.50 | 1.57 | 1.50 | 1.43 |
|  | FAI05 | 135°±1° | 2.02 | 3.13 | 1.55 | 1.39 |


## Slide 15
3. IQC Summary and Highlight | V53 UAT1 PSA adhesive Data Collection
Total PSA*6 from 2 die cut vendors
PSA1/PSA2/PSA3/PSA4/PSA5/PSA7 adhesive peeling force all in spec

## Slide 16
3. IQC Summary and Highlight | V53 UAT1 PSA liner Data Collection
Total PSA*6 from 2 die cut vendors
PSA1/PSA2/PSA3/PSA4/PSA5/PSA7 liner peeling force all in spec

## Slide 17
Postmortem Review Items:
A. Resource (NPI and  MP)
1) O-chart and resource plan
Team list from x-function team, provide CA if any gap per apple resource plan for both NPI and MP.
B. Build review (Design, Process and Quality)
2) Configs and build status
3) IQC
IQC yield and issue FACA, MIL review. CPK is needed for dimensional, parametric data. IQC should do check for all material such as FCCL, coverlay, stiffener, SUS and TSA/PSA, and SMT parts.
4) Process yield of bare flex and flex Assembly
Bare flex, Flex assembly process flow chart,  design/process/quality summary, yield tread chart, Update MP yield projection based on “yield calculator” tool.
5) OQC Issue and ORT
Bare flex and Assembly ORT review.
6) Downstream/Customer issue review
FATP/MI IQC / online /ORT issue MIL review,
7) Test review
Test fixture, ERS, correlation, funnel spec, test coverage+mitigation plan, test data distribution + Cpk, and any recommendation on testing. Test automation + MP plan.
8) Flex stackup with 5x cross-section data table, FACA if CPK not meeting 1.67
9) Cp/Cpk histogram of FAI/SPC (32pcs).
Need FACA for Cpk<1.33 or distribution abnormal; Improvement plan and control plan needed for both FAI/SPC Cpk over 1.33 but less than 1.67
10) Data collection review
Follow “Apple Flex DFM NPI Data Collection Requirement”,  “Component Peel Test Procedure for FPCA “, “Component Shear Test Procedure for FPCA”.  Data analysis and FACA are needed for failures and findings
11) DFMEA/PFMEA Top5 issue update
12) Follow up of DFM “build and collect data” items when OK2Fab. Plus monitoring and reject item, which impact quality
13) Flex mishandling and abuse test review
Follow “Flex mishandling and abuse test guideline”, and test to failure to catch design weakness. *Not MCO defined bending line
C.  Readiness (NPI and MP)
14) DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction
For bare flex, pls. provide detailed self-assessment per Apple product CPP or generic CPP and Quality control list,  provide actions how to meet requests if there is gap.
Sufficient data and validation are needed for design change and recommendation.
15) NPI Soft tool and MP hard tool report
MP hard tool refers to MP intended hard tool, any tool not for final MP is not MP hard tool. MP intended hard tool is a must from EVT.
16) Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT)
17) Lesson learn from last generation and this build (what can make next build and MP better for design, process and build management)
18) MP readiness (update from P2 postmortem), MP readiness + Automation/traceability scores (update from EVT postmortem)
19) Vendor owned MP material supplier POR (Plan Of Record), including FCCL, coverlay, PSA&TSA, DIE Cut suppliers, SUS. Also need tracking list of these material used in each build (Proto,EVT, Carrier, DVT,PVT, Rampup).
20) MP line qual plan including, define DRI and team list

## Slide 18
4. Flex Yield Trend and Top Issues Breakdown | V53 UAT1 Flow Chart
UAT1 flex
Clean booth

## Slide 19
4. Flex Yield Trend and Top Issues Breakdown | V53 UAT1 Flow Chart

## Slide 20
4. Flex Yield Trend and Top Issues Breakdown | V53 UAT1/Strobe SMT

## Slide 21
4. Flex Yield Trend and Top Issues Breakdown | V53 UAT1&Strobe Bonding&BE

## Slide 22
4. Flex Yield Trend and Top Issues Breakdown | V53 UAT1&Strobe Overall

## Slide 23
4. Flex Yield Trend and Overall Breakdown - V53 UAT1
Others Details breakdown

| Config | Failure mode | Quantity | FR | Accu FR | Remark |
|---|---|---|---|---|---|
| X06P1-U1-MANG9-SA X06P1-U1-MANG8-SM-D1 | inline VSWR NTF | 9 | 0.14% | 84.67% | Tester issue |
| X06P1-U1-MANG8-SA X06P1-U1-MAYA8-SM X06P1-U1-MAYX2-SM-D1 | Solder OOS | 8 | 0.12% | 87.46% | Solder print issue |
| X06P1-U1-MANG8-SA X06P1-U1-MANG9-SA-D1 | Clip shift | 7 | 0.11% | 89.90% | PnP issue |
| X06P1-U1-MANG9-SA X06P1-U1-MANG9-SA-D1 X06P1-U1-MAYA8-SM-D1 | Solder Under Volume | 5 | 0.08% | 91.64% | Solder print issue |
| X06P1-U1-MANG8-SA X06P1-U1-MANG9-SA | Components missing | 5 | 0.08% | 93.38% | PnP issue |
| X06P1-U1-MAYX2-SM X06P1-U1-MAYA8-SM-D1 | OQC Mic NTF | 5 | 0.08% | 95.12% | Tester issue |
| X06P1-U1-MANG8-SA | MIC shift | 4 | 0.06% | 96.52% | Handling issue |
| X06P1-U1-MANG9-SA X06P1-U1-MAYX2-SM-D1 | inline ICT NTF | 4 | 0.06% | 97.91% | Tester issue |
| X06P1-U1-MANG8-SA | Strobe SPI OOS | 2 | 0.03% | 98.61% | Solder print issue |
| X06P1-U1-MAYA8-SM | FPC Cosmetic fail | 2 | 0.03% | 99.30% | Handling issue |
| X06P1-U1-MAYX2-SM | Chip shift | 1 | 0.02% | 99.65% | Solder print issue |
| X06P1-U1-MAYA8-SM-D1 | Inline Mic NTF | 1 | 0.02% | 100.00% | Tester issue |


## Slide 24
4. Flex Yield Trend and Top Issues Breakdown - V53 UAT1- by Config

## Slide 25: 5. Failure FACA | V53 UAT1-SMT

| Component | FPC | Vendor | AMP | APN | 632-07540 | Failure process / station | X-ray |
|---|---|---|---|---|---|---|---|
| Issue Description | U0601 solder open FR: 132F/6,549T=2.02%  FR for Config: |  |  |  |  |  |  |
| FA | Root cause: handling issue.When handling the exception, the personnel handled it improperly. The metal cover moves towards the MIC, causing the solder to open 1.Check the distribution of failure sample, The failure sample are concentrated in 2 panels. Pic1 2.Check the Pre-AOI: no abnormal.Pic2 3.Check the Post-AOI: Metal cover is found to move.Pic3 4.Check production records: found the pre-AOI had barcode scan fail record. The time from Pre-AOI to the reflow was 8 minutes.Pic4 5.Check CCTV: 2024/8/30 19:03, An operator is handling an exception. Pic5 Fail Mode: When handling the exception, the personnel handled it improperly. The metal cover moves towards the MIC, causing the solder to open. Pic6 |  |  |  |  |  |  |
| CA | improved action 1.MES personnel corrected the scanner and fixed the position。Pic1 2.Tracking 2,959pcs FR:0F/2,959T=0% |  |  |  |  |  |  |
| Validation | FR: 0F/2,959T=0.0% |  |  |  |  |  |  |

5. Failure FACA | V53 UAT1-SMT

|  | Config | Defect rate |  | Config | Defect rate |
|---|---|---|---|---|---|
| 1 | X06P1-U1-MANG8-SA | 0F/1,100T=0% | 5 | X06P1-U1-MAYX2-SM-D1 | 0F/800T=0% |
| 2 | X06P1-U1-MANG9-SM | 0F/1,028T=0% | 6 | X06P1-U1-MANG8-SM-D1 | 0F/800T=0% |
| 3 | X06P1-U1-MAYA8-SM | 0F/900T=0% | 7 | X06P1-U1-MANX2-SA-D1 | 0F/559T=0% |
| 4 | X06P1-U1-MAYX2-SM | 132F/900T=14.6% | 8 | X06P1-U1-MAYA8-SM-D1 | 0F/800T=0% |


## Slide 26: 5. Failure FACA | V53 UAT1-SMT

| Component | FPC | Vendor | AMP | APN | 632-07540 | Failure process / station | SMT VI |
|---|---|---|---|---|---|---|---|
| Issue Description | PAD_GND_NORTH_BOTTOM Pollution Flux FR: 45F/6,549T=0.69%   FR for Config: |  |  |  |  |  |  |
| FA | Root cause: Carrier design issue 1. 20pcs for process mapping. No defect found for after 1st reflow, 4pcs defects found after the 2nd reflow. Pic1 2. Check the TOP Carrier: Residual Flux was found on the carrier.Pic2 3. During the detection of the second reflow, Flux residue was found on the surface of SUS-2, and simultaneously Flux residue was also detected on the surface of the carrier on the TOP side. Pic3 |  |  |  |  |  |  |
| CA | improved action: 1. The avoidance width of the carrier is increased from 1.0mm to 2.6mm. Pic3 2. After optimizing the carrier, the average volume of SPI for SUS - 1 printing is 80%~125%. No abnormal. Pic4 3. Tracking 4,759pcs FR:0F/4,759T=0% |  |  |  |  |  |  |
| Validation | FR:0F/4,759T=0% |  |  |  |  |  |  |

5. Failure FACA | V53 UAT1-SMT
OK

|  | Config | Defect rate |  | Config | Defect rate |
|---|---|---|---|---|---|
| 1 | X06P1-U1-MANG8-SA | 0F/1,100T=0% | 5 | X06P1-U1-MAYX2-SM-D1 | 0F/800T=0% |
| 2 | X06P1-U1-MANG9-SM | 45F/1,028T=4,38% | 6 | X06P1-U1-MANG8-SM-D1 | 0F/800T=0% |
| 3 | X06P1-U1-MAYA8-SM | 0F/900T=0% | 7 | X06P1-U1-MANX2-SA-D1 | 0F/559T=0% |
| 4 | X06P1-U1-MAYX2-SM | 0F/900T=0% | 8 | X06P1-U1-MAYA8-SM-D1 | 0F/800T=0% |


## Slide 27: 5. Failure FACA | V53 UAT1-SMT

| Component | FPC | Vendor | AMP | APN | 632-07540 | Failure process / station | SMT VI |
|---|---|---|---|---|---|---|---|
| Issue Description | PAD_GND_NORTH_BOTTOM Pollution Flux FR: 45F/6,549T=0.69%   FR for Config: |  |  |  |  |  |  |
| FA | Root cause: Carrier design issue 1.Check the distribution of failure sample，The failure sample are concentrated in 6 panels. Pic1 2.Check the Dispensing: With UV magnetic cover design, PAD has occlusion, no risk。Pic2 3.Check the BOT Post-AOI：PAD_GND_NORTH_BOTTOM is not abnormal, VI check 500pcs, no abnormal。Pic3 4.Check Reflow profile：no abnormal.Pic4 |  |  |  |  |  |  |

5. Failure FACA | V53 UAT1-SMT

|  | Config | Defect rate |  | Config | Defect rate |
|---|---|---|---|---|---|
| 1 | X06P1-U1-MANG8-SA | 0F/1,100T=0% | 5 | X06P1-U1-MAYX2-SM-D1 | 0F/800T=0% |
| 2 | X06P1-U1-MANG9-SM | 45F/1,028T=4,38% | 6 | X06P1-U1-MANG8-SM-D1 | 0F/800T=0% |
| 3 | X06P1-U1-MAYA8-SM | 0F/900T=0% | 7 | X06P1-U1-MANX2-SA-D1 | 0F/559T=0% |
| 4 | X06P1-U1-MAYX2-SM | 0F/900T=0% | 8 | X06P1-U1-MAYA8-SM-D1 | 0F/800T=0% |


## Slide 28: 5. Failure FACA | V53 UAT1-SMT

| Component | FPC | Vendor | AMP | APN | 632-07540 | Failure process / station | X-RAY |
|---|---|---|---|---|---|---|---|
| Issue Description | Bonding solder open FR: 11F/6,549T=0.17%   FR for Config: |  |  |  |  |  |  |
| FA | Root cause: Bonding carrier design issue 1.Check the Bonding AOI-1, no abnormal. Bonding AOI-2 found Strobe offset. 2.Process Mapping:Pic4 2.1.The Carrier is transmitted normally in the track, Strobe offset was found when stopping. pic5 2.2.Check the Carrier design:The limit height of the Carrier is only 0.35mm, The strobe thickness is 0.15mm, There is a risk of the FPC offset.Pic6 2.3.Check the Strobe warpage data: Strobe warpage values ranged from 0.22 to 0.53mm,(SPC<0.7mm).Pic7   Fail mode: When strobe warpage is greater than 0.35mm, Strobe is at risk of exceeding carrier, Strobe shift causes Bonding solder open. Pic8 |  |  |  |  |  |  |
| CA | Improved action 1.Modify the Bonding carrier, the limit height is optimized from 0.35mm to 1.9mm. Pic1 2.Tracking 5,787pcs FR:0F/5,787T=0% |  |  |  |  |  |  |
| Validation | FR: 0F/5,787T=0.0% |  |  |  |  |  |  |

5. Failure FACA | V53 UAT1-SMT

|  | Config | Defect rate |  | Config | Defect rate |
|---|---|---|---|---|---|
| 1 | X06P1-U1-MANG8-SA | 11F/1,100T=1% | 5 | X06P1-U1-MAYX2-SM-D1 | 0F/800T=0% |
| 2 | X06P1-U1-MANG9-SM | 0F/1,028T=0% | 6 | X06P1-U1-MANG8-SM-D1 | 0F/800T=0% |
| 3 | X06P1-U1-MAYA8-SM | 0F/900T=0% | 7 | X06P1-U1-MANX2-SA-D1 | 0F/559T=0% |
| 4 | X06P1-U1-MAYX2-SM | 0F/900T=0% | 8 | X06P1-U1-MAYA8-SM-D1 | 0F/800T=0% |


## Slide 29: 5. Failure FACA | V53 UAT1-SMT

| Component | FPC | Vendor | AMP | APN | 632-07540 | Failure process / station | X-RAY |
|---|---|---|---|---|---|---|---|
| Issue Description | Bonding solder open FR: 11F/7,600T=0.15%   FR for Config: |  |  |  |  |  |  |
| FA | Root cause: Bonding carrier design issue 1.Check the distribution of failure sample，The failure sample are concentrated in 2 panels. Pic1 2.Check the Bonding AOI-1:no abnormal.Pic2 3.Check the Bonding AOI-2,Strobe offset found, AOI alarm, personnel Rpass.Pic3 |  |  |  |  |  |  |

5. Failure FACA | V53 UAT1-SMT

|  | Config | Defect rate |  | Config | Defect rate |
|---|---|---|---|---|---|
| 1 | X06P1-U1-MANG8-SA | 11F/1,100T=1% | 5 | X06P1-U1-MAYX2-SM-D1 | 0F/800T=0% |
| 2 | X06P1-U1-MANG9-SM | 0F/1,028T=0% | 6 | X06P1-U1-MANG8-SM-D1 | 0F/800T=0% |
| 3 | X06P1-U1-MAYA8-SM | 0F/900T=0% | 7 | X06P1-U1-MANX2-SA-D1 | 0F/559T=0% |
| 4 | X06P1-U1-MAYX2-SM | 0F/900T=0% | 8 | X06P1-U1-MAYA8-SM-D1 | 0F/800T=0% |


## Slide 30
Postmortem Review Items:
A. Resource (NPI and  MP)
1) O-chart and resource plan
Team list from x-function team, provide CA if any gap per apple resource plan for both NPI and MP.
B. Build review (Design, Process and Quality)
2) Configs and build status
3) IQC
IQC yield and issue FACA, MIL review. CPK is needed for dimensional, parametric data. IQC should do check for all material such as FCCL, coverlay, stiffener, SUS and TSA/PSA, and SMT parts.
4) Process yield of bare flex and flex Assembly
Bare flex, Flex assembly process flow chart,  design/process/quality summary, yield tread chart, Update MP yield projection based on “yield calculator” tool.
5) OQC Issue and ORT
Bare flex and Assembly ORT review.
6) Downstream/Customer issue review
FATP/MI IQC / online /ORT issue MIL review,
7) Test review
Test fixture, ERS, correlation, funnel spec, test coverage+mitigation plan, test data distribution + Cpk, and any recommendation on testing. Test automation + MP plan.
8) Flex stackup with 5x cross-section data table, FACA if CPK not meeting 1.67
9) Cp/Cpk histogram of FAI/SPC (32pcs).
Need FACA for Cpk<1.33 or distribution abnormal; Improvement plan and control plan needed for both FAI/SPC Cpk over 1.33 but less than 1.67
10) Data collection review
Follow “Apple Flex DFM NPI Data Collection Requirement”,  “Component Peel Test Procedure for FPCA “, “Component Shear Test Procedure for FPCA”.  Data analysis and FACA are needed for failures and findings
11) DFMEA/PFMEA Top5 issue update
12) Follow up of DFM “build and collect data” items when OK2Fab. Plus monitoring and reject item, which impact quality
13) Flex mishandling and abuse test review
Follow “Flex mishandling and abuse test guideline”, and test to failure to catch design weakness. *Not MCO defined bending line
C.  Readiness (NPI and MP)
14) DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction
For bare flex, pls. provide detailed self-assessment per Apple product CPP or generic CPP and Quality control list,  provide actions how to meet requests if there is gap.
Sufficient data and validation are needed for design change and recommendation.
15) NPI Soft tool and MP hard tool report
MP hard tool refers to MP intended hard tool, any tool not for final MP is not MP hard tool. MP intended hard tool is a must from EVT.
16) Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT)
17) Lesson learn from last generation and this build (what can make next build and MP better for design, process and build management)
18) MP readiness (update from P2 postmortem), MP readiness + Automation/traceability scores (update from EVT postmortem)
19) Vendor owned MP material supplier POR (Plan Of Record), including FCCL, coverlay, PSA&TSA, DIE Cut suppliers, SUS. Also need tracking list of these material used in each build (Proto,EVT, Carrier, DVT,PVT, Rampup).
20) MP line qual plan including, define DRI and team list

## Slide 31
5. ORT | V53 UAT1
Remark
ORT test covered all configs, all items will be finished on 2024/10/9

| Project | Config | Test | Cycle/Hour | Total Qty | Begin date | Due date | Status |
|---|---|---|---|---|---|---|---|
| V53 UAT1 | X06P1-U1-MANG8-SA | Thermal cycling | 500 cycles | 45 | 9/6 | 10/4 | 300cycles ongoing, CP: 9/23 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 9/4 | 10/3 | 300cycles ongoing, CP: 9/22 |
|  |  | Thermal shock | 200 cycles | 45 | 9/7 | 9/17 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 9/5 | 9/10 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 9/14 | 9/19 | Test ongoing, CP: 9/19 |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 9/13 | 9/18 | Pass |
|  | X06P1-U1-MANG9-SM | Thermal cycling | 500 cycles | 45 | 9/10 | 10/9 | 200cycles ongoing, CP: 9/20 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 9/5 | 10/3 | 300cycles ongoing, CP: 9/22 |
|  |  | Thermal shock | 200 cycles | 45 | 9/7 | 9/17 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 9/5 | 9/10 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 9/14 | 9/19 | Pass |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 9/13 | 9/18 | Pass |


## Slide 32
5. ORT | V53 UAT1

| Project | Config | Test | Cycle/Hour | Total Qty | Begin date | Due date | Status |
|---|---|---|---|---|---|---|---|
| V53 UAT1 | X06P1-U1-MAYA8-SM | Thermal cycling | 500 cycles | 45 | 9/5 | 10/4 | 300cycles ongoing, CP: 9/23 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 9/4 | 10/4 | 300cycles ongoing, CP: 9/22 |
|  |  | Thermal shock | 200 cycles | 45 | 9/7 | 9/17 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 9/5 | 9/10 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 9/14 | 9/19 | Test ongoing, CP: 9/19 |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 9/13 | 9/18 | Pass |
|  | X06P1-U1-MAYX2-SM-D1 | Thermal cycling | 500 cycles | 45 | 9/11 | 10/9 | 200cycles ongoing, CP: 9/20 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 9/8 | 10/9 | 200cycles ongoing, CP: 9/19 |
|  |  | Thermal shock | 200 cycles | 45 | 9/12 | 9/20 | Test ongoing, CP: 9/20 |
|  |  | Flex bending test | 25 cycles | 20 | 9/9 | 9/14 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 9/14 | 9/19 | Test ongoing, CP: 9/19 |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 9/26 | 10/1 | Test ongoing, CP: 10/1 |

Remark
ORT test covered all configs, all items will be finished on 2024/10/9

## Slide 33
5. ORT | V53 UAT1
Remark
ORT test covered all configs, all items will be finished before 2024/10/16.

| Project | Config | Test | Cycle/Hour | Total Qty | Begin date | Due date | Status |
|---|---|---|---|---|---|---|---|
| V53 UAT1 | X06P1-U1-MANG8-SM-D1 | Thermal cycling | 500 cycles | 45 | 9/13 | 10/14 | 200cycles ongoing, CP: 9/26 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 9/11 | 10/9 | 200cycles ongoing, CP: 9/22 |
|  |  | Thermal shock | 200 cycles | 45 | 9/12 | 9/20 | Test ongoing, CP: 9/20 |
|  |  | Flex bending test | 25 cycles | 20 | 9/12 | 9/17 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 9/23 | 9/28 | Test ongoing, CP: 9/28 |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 9/26 | 10/1 | Test ongoing, CP: 10/1 |
|  | X06P1-U1-MANX2-SA-D1 | Thermal cycling | 500 cycles | 45 | 9/14 | 10/15 | Test ongoing, CP: 9/20 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 9/15 | 10/10 | Ongoing |
|  |  | Thermal shock | 200 cycles | 45 | 9/15 | 9/21 | Ongoing |
|  |  | Flex bending test | 25 cycles | 20 | 9/16 | 9/22 | Ongoing |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 9/24 | 9/29 | Ongoing |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 9/27 | 10/2 | Ongoing |


## Slide 34
5. ORT | V53 UAT1
Remark
ORT test covered all configs, all items will be finished before 2024/10/16.

| Project | Config | Test | Cycle/Hour | Total Qty | Begin date | Due date | Status |
|---|---|---|---|---|---|---|---|
| V53 UAT1 | X06P1-U1-MANG8-SM-D1 | Thermal cycling | 500 cycles | 45 | 9/14 | 10/15 | Test ongoing, CP: 9/20 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 9/15 | 10/10 | Ongoing |
|  |  | Thermal shock | 200 cycles | 45 | 9/15 | 9/21 | Ongoing |
|  |  | Flex bending test | 25 cycles | 20 | 9/16 | 9/22 | Ongoing |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 9/24 | 9/29 | Ongoing |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 9/27 | 10/2 | Ongoing |
|  | X06P1-U1-MANX2-SA-D1 | Thermal cycling | 500 cycles | 45 | 9/11 | 10/9 | 200cycles ongoing, CP: 9/21 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 9/8 | 10/9 | 200cycles ongoing, CP: 9/20 |
|  |  | Thermal shock | 200 cycles | 45 | 9/12 | 9/20 | Test ongoing, CP: 9/20 |
|  |  | Flex bending test | 25 cycles | 20 | 9/9 | 9/14 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 9/14 | 9/19 | Ongoing |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 9/26 | 10/1 | Ongoing |


## Slide 35
Postmortem Review Items:
A. Resource (NPI and  MP)
1) O-chart and resource plan
Team list from x-function team, provide CA if any gap per apple resource plan for both NPI and MP.
B. Build review (Design, Process and Quality)
2) Configs and build status
3) IQC
IQC yield and issue FACA, MIL review. CPK is needed for dimensional, parametric data. IQC should do check for all material such as FCCL, coverlay, stiffener, SUS and TSA/PSA, and SMT parts.
4) Process yield of bare flex and flex Assembly
Bare flex, Flex assembly process flow chart,  design/process/quality summary, yield tread chart, Update MP yield projection based on “yield calculator” tool.
5) OQC Issue and ORT
Bare flex and Assembly ORT review.
6) Downstream/Customer issue review
FATP/MI IQC / online /ORT issue MIL review,
7) Test review
Test fixture, ERS, correlation, funnel spec, test coverage+mitigation plan, test data distribution + Cpk, and any recommendation on testing. Test automation + MP plan.
8) Flex stackup with 5x cross-section data table, FACA if CPK not meeting 1.67
9) Cp/Cpk histogram of FAI/SPC (32pcs).
Need FACA for Cpk<1.33 or distribution abnormal; Improvement plan and control plan needed for both FAI/SPC Cpk over 1.33 but less than 1.67
10) Data collection review
Follow “Apple Flex DFM NPI Data Collection Requirement”,  “Component Peel Test Procedure for FPCA “, “Component Shear Test Procedure for FPCA”.  Data analysis and FACA are needed for failures and findings
11) DFMEA/PFMEA Top5 issue update
12) Follow up of DFM “build and collect data” items when OK2Fab. Plus monitoring and reject item, which impact quality
13) Flex mishandling and abuse test review
Follow “Flex mishandling and abuse test guideline”, and test to failure to catch design weakness. *Not MCO defined bending line
C.  Readiness (NPI and MP)
14) DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction
For bare flex, pls. provide detailed self-assessment per Apple product CPP or generic CPP and Quality control list,  provide actions how to meet requests if there is gap.
Sufficient data and validation are needed for design change and recommendation.
15) NPI Soft tool and MP hard tool report
MP hard tool refers to MP intended hard tool, any tool not for final MP is not MP hard tool. MP intended hard tool is a must from EVT.
16) Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT)
17) Lesson learn from last generation and this build (what can make next build and MP better for design, process and build management)
18) MP readiness (update from EVT postmortem), MP readiness + Automation/traceability scores (update from EVT postmortem)
19) Vendor owned MP material supplier POR (Plan Of Record), including FCCL, coverlay, PSA&TSA, DIE Cut suppliers, SUS. Also need tracking list of these material used in each build (Proto,EVT, Carrier, DVT,PVT, Rampup).
20) MP line qual plan including, define DRI and team list

## Slide 36

| Process/Station | Failure Description | Failure Rate | Root Cause | Corrective Action | DRI/ Due Date | Validation (Defect Rate%) |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

6. FATP/MI IQC, in-Line, ORT MIL and FACA | V53 UAT1
So far no feedback

## Slide 37
Postmortem Review Items:
A. Resource (NPI and MP)
1) O-chart and resource plan
Team list from x-function team, provide CA if any gap per apple resource plan for both NPI and MP.
B. Build review (Design, Process and Quality)
2) Configs and build status
3) IQC
IQC yield and issue FACA, MIL review. CPK is needed for dimensional, parametric data. IQC should do check for all material such as FCCL, coverlay, stiffener, SUS and TSA/PSA, and SMT parts.
4) Process yield of bare flex and flex Assembly
Bare flex, Flex assembly process flow chart,  design/process/quality summary, yield tread chart, Update MP yield projection based on “yield calculator” tool.
5) OQC Issue and ORT
Bare flex and Assembly ORT review.
6) Downstream/Customer issue review
FATP/MI IQC / online /ORT issue MIL review,
7) Test review
Test fixture, ERS, correlation, funnel spec, test coverage+mitigation plan, test data distribution + Cpk, and any recommendation on testing. Test automation + MP plan.
8) Flex stackup with 5x cross-section data table, FACA if CPK not meeting 1.67
9) Cp/Cpk histogram of FAI/SPC (32pcs).
Need FACA for Cpk<1.33 or distribution abnormal; Improvement plan and control plan needed for both FAI/SPC Cpk over 1.33 but less than 1.67
10) Data collection review
Follow “Apple Flex DFM NPI Data Collection Requirement”,  “Component Peel Test Procedure for FPCA “, “Component Shear Test Procedure for FPCA”.  Data analysis and FACA are needed for failures and findings
11) DFMEA/PFMEA Top5 issue update
12) Follow up of DFM “build and collect data” items when OK2Fab. Plus monitoring and reject item, which impact quality
13) Flex mishandling and abuse test review
Follow “Flex mishandling and abuse test guideline”, and test to failure to catch design weakness. *Not MCO defined bending line
C.  Readiness (NPI and MP)
14) DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction
For bare flex, pls. provide detailed self-assessment per Apple product CPP or generic CPP and Quality control list,  provide actions how to meet requests if there is gap.
Sufficient data and validation are needed for design change and recommendation.
15) NPI Soft tool and MP hard tool report
MP hard tool refers to MP intended hard tool, any tool not for final MP is not MP hard tool. MP intended hard tool is a must from EVT.
16) Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT)
17) Lesson learn from last generation and this build (what can make next build and MP better for design, process and build management)
18) MP readiness (update from P2 postmortem), MP readiness + Automation/traceability scores (update from EVT postmortem)
19) Vendor owned MP material supplier POR (Plan Of Record), including FCCL, coverlay, PSA&TSA, DIE Cut suppliers, SUS. Also need tracking list of these material used in each build (Proto,EVT, Carrier, DVT,PVT, Rampup).
20) MP line qual plan including, define DRI and team list

## Slide 38
Ready
Not ready
Ongoing
7. Tester readiness V53 UAT1

| Project | Flex | Test Items | Station | Test ERS/Plan | Test SW Readiness | Fixture HW Readiness | Test Qualification | Remark |
|---|---|---|---|---|---|---|---|---|
| V53 | UAT1 | Mic | Inline | Y | Y | Y | Y |  |
|  |  | RF+ICT |  | Y | Y | Y | Y |  |
|  |  | Mic | OQC | Y | Y | Y | Y |  |
|  |  | RF+ICT |  | Y | Y | Y | Y |  |


## Slide 39

| Flex | Station | Coverage |
|---|---|---|
| V53 UAT1 | RF+ICT | 97.37% |

7. Function Test Coverage V53 UAT1
Yes
No

## Slide 40
Covered
Uncovered
7. Function Test Coverage | V53 UAT1

| Failure mode :Open |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B2B | Pin name | Test coverage | Pin name | Test coverage | Clip | Clip name | Test coverage | PAD |  | PAD name | Test coverage | Component | Component Name | Test coverage | Component Name | Test coverage | Component Name | Test coverage |
| JUAT1 | Pin1 | Y | Pin22 | Y | Clip | CL_ANT10_GND | Y | Strobe_Pad |  | PIN1 | Y | Components | R0401 | Y | L0300 | Y | R0402 | Y |
|  | Pin2 | Y | Pin23 | Y |  | CL_ATN10_FEED | Y |  |  | PIN2 | Y |  | C0412 | Y | L0303 | Y | U0300 | Y |
|  | Pin3 | Y | Pin24 | Y |  | CL_ANT2_Vert_SP | Y |  |  | PIN3 | Y |  | L0416 | Y | C0306 | Y | U0302 | Y |
|  | Pin4 | Y | Pin25 | Y |  | CL_ANT2_short | Y |  |  | PIN4 | Y |  | C0409 | Y | C0309 | Y | L0602 | Y |
|  | Pin5 | Y | Pin26 | Y |  | CL_ANT2_FEED | Y |  |  | PIN5 | Y |  | C0403 | Y | C0301 | Y | L0601 | Y |
|  | Pin6 | Y | Pin27 | Y |  | PAD_GND_NORTH | Y |  |  | PIN6 | Y |  | R0400 | Y | C0319 | Y | L0603 | Y |
|  | Pin7 | Y | Pin28 | Y |  | CL_JINDO_L | Y |  |  | PIN7 | Y |  | U0400 | Y | C0311 | Y | L0607 | Y |
|  | Pin8 | Y | Pin29 | Y |  | CL_JINDO_M_TUNER | Y |  |  | PIN8 | Y |  | C0411 | Y | C0321 | Y | L0604 | Y |
|  | Pin9 | Y | Pin30 | Y |  | CL_ANT2_GND | Y |  |  | PIN9 | Y |  | L0413 | Y | C0325 | Y | L0600 | Y |
|  | Pin10 | Y | B2B STL | Y |  | CL_Strobe_GND | Y |  |  | PIN10 | Y |  | C0410 | Y | U0301 | Y | L0605 | Y |
|  | Pin11 | Y |  |  |  | CL_JINDO_M_GND | Y |  |  |  |  |  | L0409 | Y | C0300 | Y | L0608 | Y |
|  | Pin12 | Y |  |  |  | SUS Stiffener | Y |  |  |  |  |  | L0411 | Y | C0320 | Y | C0600 | Y |
|  | Pin13 | Y |  |  |  | SP_SPKR_POS | Y |  |  |  |  |  | C0402 | Y | L0305 | Y | L0609 | Y |
|  | Pin14 | Y |  |  |  | SP_SPKR_NEG | Y |  |  |  |  |  | L0406 | Y | L0307 | Y |  |  |
|  | Pin15 | Y |  |  |  |  |  |  |  |  |  |  | C0401 | Y | L0308 | Y |  |  |
|  | Pin16 | Y |  |  |  |  |  |  |  |  |  |  | C0418 | Y | L0309 | Y |  |  |
|  | Pin17 | Y |  |  |  |  |  |  |  |  |  |  | R0200 | Y | C0322 | Y |  |  |
|  | Pin18 | Y |  |  |  |  |  |  |  |  |  |  | C0302 | Y | C0324 | Y |  |  |
|  | Pin19 | Y |  |  |  |  |  |  |  |  |  |  | R0304 | Y | R0303 | Y |  |  |
|  | Pin20 | Y |  |  |  |  |  |  |  |  |  |  | U0303 | Y | R0302 | Y |  |  |
|  | Pin21 | Y |  |  |  |  |  |  |  |  |  |  | C0400 | Y | C0303 | Y |  |  |
| Failure mode :Short |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Description |  |  | Test coverage |  | Description |  |  |  | Test coverage |  |  | Description |  |  | Component Name |  | Test coverage |  |
| B2B adjacent GND pin short |  |  | N |  | B2B and bonding signal pads short to other adjacent pads |  |  |  | Y |  |  | Short two poles of 0ohm component |  |  | R0302 |  | N |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | R0303 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | R0304 |  |  |  |
| Bonding adjacent GND pads short |  |  | N |  |  |  |  |  |  |  |  |  |  |  | R0400 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | R0401 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | R0402 |  |  |  |


## Slide 41
Covered
Uncovered
7. Function Test Coverage | V53 UAT1 Mic

| Item | Failure mode | Sensitivity test | Summary |
|---|---|---|---|
| #1 | No tin on Mic signal pads | Y | Y |
| #2 | Short between adjacent pads | Y | Y |


## Slide 42
Covered
Uncovered
7. Function Test Coverage | V53 UAT1 Mic

| Failure mode | Sensitivity test | Summary |
|---|---|---|
| Shatter EB membrane   (manually break) | N | N |

EB membrane has a dustproof effect, and damage does not affect sensitivity testing .

## Slide 43
7. Function Test Coverage | V53 UAT1 Mic

| Failure mode | Sensitivity test | Summary |
|---|---|---|
| Mic shielding case void(≥φ0.06mm) | N | N |

Covered
Uncovered

## Slide 44
Covered
Uncovered

| Failure mode | Sensitivity test | Summary |
|---|---|---|
| No tin on Mic signal pads | Y | Y |

7. Function Test Coverage | V53 UAT1 Mic

## Slide 45
Covered
Uncovered

| Failure mode | Sensitivity test | Summary |
|---|---|---|
| Short between adjacent pads | Y | Y |

7. Function Test Coverage | V53 UAT1 Mic

## Slide 46

| Station | Test item Qty | CPK<1.33 | 1.33<=CPK<1.67 | 1.67<=CPK<2.0 | CPK>=2.0 | Comments |
|---|---|---|---|---|---|---|
| V53 UAT1 | 5226 | 0 | 0 | 0 | 5226 | All CPK value are above 2.0 ,which means the spec we are using is a good balance between  limit and data. |

7. Function test CPK V53 UAT1
>2.00
<1.33
1.33~2.00

## Slide 47
7. Test Yield, Retest Rate

| Station | V53 UAT1 |  |  |
|---|---|---|---|
|  | MIC | RF | ICT |
| Input Q’ty | 6329 | 6328 | 6323 |
| First Pass Yield  Target 97% | 99.46% | 98.59% | 98.15% |
| Final Yield | 99.98% | 99.92% | 99.91% |
| Retest Rate  Target 3% | 0.52% | 1.33% | 1.76% |

OK
NG

## Slide 48: 7. Failure FACA | V53 UAT1

| Component | V53 UAT1 | Vendor | AMP | APN | 632-07540 | Failure process / station | OQC VSWR |
|---|---|---|---|---|---|---|---|
| Issue Description | RF Test NTF issue  FR=28F/6328T=0.44% Config:06P1-U1-MANG8-SA=8F/1100T=0.72% Config:X06P1-U1-MANG9-SA=5F/990T=0.5% Config:X06P1-U1-MAYA8-SM=3F/900T=0.33% Config:X06P1-U1-MAYX2-SM=4F/900T=0.44% Config:X06P1-U1-MANG8-SM-D1=5F/700T=0.71% Config:X06P1-U1-MAYX2-SM-D1=2F/700T=0.29% Config:X06P1-U1-MANG9-SA-D1=1F/559T=0.18% Config:X06P1-U1-MAYA8-SM-D1=0F/700T=0% Fail item:ANT2 |  |  |  |  |  |  |
| FA | -FACA retest confirmed NTF(Not Ture fail)，these failures came from OQC tester misjudgment. -Failure item related analyze shows the root cause is: due to software bug ， the related plastic block did not move to press onto the clip， which leads to insufficient contacting issue. |  |  |  |  |  |  |
| CA | -Upgraded test software on 9/9 |  |  |  |  |  |  |
| Validation | Verify 500x pcs sample, 0 defected was found |  |  |  |  |  |  |

7. Failure FACA | V53 UAT1
original
improved
Update test software to make sure the block pressing onto clip during testing
The block which is supposed to move to right side and press onto the clip during testing

## Slide 49: 7. Failure FACA | V53 UAT1

| Component | V53 UAT1 | Vendor | AMP | APN | 632-07540 | Failure process / station | OQC ICT |
|---|---|---|---|---|---|---|---|
| Issue Description | ICT Test NTF issue Defected rate:0.26%（16F/6328T) Config:06P1-U1-MANG8-SA=7F/1100T=0.63% Config:X06P1-U1-MANG9-SA=4F/990T=0.44% Config:X06P1-U1-MAYA8-SM=3F/900T=0.33% Config:X06P1-U1-MAYX2-SM=2F/900T=0.22% Config:X06P1-U1-MANG8-SM-D1=0F/700T=0% Config:X06P1-U1-MAYX2-SM-D1=2F/700T=0.29% Config:X06P1-U1-MANG9-SA-D1=0F/559T=0% Config:X06P1-U1-MAYA8-SM-D1=0F/700T=0% Fail item: S_U0200.X:J_UAT1.X; |  |  |  |  |  |  |
| FA | -FACA retest confirmed failures are all NTF（ Not Ture Fail），these failures were from OQC tester misjudgment. -Failure item related analyze shows the root cause is unstable contacting at DUT pad shown below. |  |  |  |  |  |  |
| CA | -Adding extra test pins on OQC tester , deployed on 9/2 |  |  |  |  |  |  |
| Validation | Verify 500x pcs sample, 0 defected was found |  |  |  |  |  |  |

7. Failure FACA | V53 UAT1
contacting pins
Add more contact thinner pins for better contacting stability
Using thinner  contact pins
Diameter0.8mm
Diameter0.22mm

## Slide 50
Postmortem Review Items:
A. Resource (NPI and MP)
1) O-chart and resource plan
Team list from x-function team, provide CA if any gap per apple resource plan for both NPI and MP.
B. Build review (Design, Process and Quality)
2) Configs and build status
3) IQC
IQC yield and issue FACA, MIL review. CPK is needed for dimensional, parametric data. IQC should do check for all material such as FCCL, coverlay, stiffener, SUS and TSA/PSA, and SMT parts.
4) Process yield of bare flex and flex Assembly
Bare flex, Flex assembly process flow chart,  design/process/quality summary, yield tread chart, Update MP yield projection based on “yield calculator” tool.
5) OQC Issue and ORT
Bare flex and Assembly ORT review.
6) Downstream/Customer issue review
FATP/MI IQC / online /ORT issue MIL review,
7) Test review
Test fixture, ERS, correlation, funnel spec, test coverage+mitigation plan, test data distribution + Cpk, and any recommendation on testing. Test automation + MP plan.
8) Flex stackup with 5x cross-section data table, FACA if CPK not meeting 1.67
9) Cp/Cpk histogram of FAI/SPC (32pcs).
Need FACA for Cpk<1.33 or distribution abnormal; Improvement plan and control plan needed for both FAI/SPC Cpk over 1.33 but less than 1.67
10) Data collection review
Follow “Apple Flex DFM NPI Data Collection Requirement”,  “Component Peel Test Procedure for FPCA “, “Component Shear Test Procedure for FPCA”.  Data analysis and FACA are needed for failures and findings
11) DFMEA/PFMEA Top5 issue update
12) Follow up of DFM “build and collect data” items when OK2Fab. Plus monitoring and reject item, which impact quality
13) Flex mishandling and abuse test review
Follow “Flex mishandling and abuse test guideline”, and test to failure to catch design weakness. *Not MCO defined bending line
C.  Readiness (NPI and MP)
14) DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction
For bare flex, pls. provide detailed self-assessment per Apple product CPP or generic CPP and Quality control list,  provide actions how to meet requests if there is gap.
Sufficient data and validation are needed for design change and recommendation.
15) NPI Soft tool and MP hard tool report
MP hard tool refers to MP intended hard tool, any tool not for final MP is not MP hard tool. MP intended hard tool is a must from EVT.
16) Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT)
17) Lesson learn from last generation and this build (what can make next build and MP better for design, process and build management)
18) MP readiness (update from P2 postmortem), MP readiness + Automation/traceability scores (update from EVT postmortem)
19) Vendor owned MP material supplier POR (Plan Of Record), including FCCL, coverlay, PSA&TSA, DIE Cut suppliers, SUS. Also need tracking list of these material used in each build (Proto,EVT, Carrier, DVT,PVT, Rampup).
20) MP line qual plan including, define DRI and team list

## Slide 51
V53 | MCO CPK Summary | UAT1

| Project | Flex | Station | Total Qty | CPK<1.33 | 1.33<=CPK<1.67 | CPK>=1.67 |
|---|---|---|---|---|---|---|
| V53 UAT1 | UAT1 Flex | FAI | 39 | 4 | 2 | 33 |
|  |  | SPC | 29 | 0 | 0 | 29 |

Encap dimension FAI148 CPK < 1.33, refer to DFM.
Encap dimension FAI150 CPK < 1.33, refer to DFM.
Encap dimension FAI152 CPK < 1.33, refer to DFM.
Encap dimension FAI154 CPK < 1.33, refer to DFM.
Encap dimension FAI151 CPK < 1.67, refer to DFM.
Encap dimension FAI153 CPK < 1.67, refer to DFM.

## Slide 52
Postmortem Review Items:
A. Resource (NPI and  MP)
1) O-chart and resource plan
Team list from x-function team, provide CA if any gap per apple resource plan for both NPI and MP.
B. Build review (Design, Process and Quality)
2) Configs and build status
3) IQC
IQC yield and issue FACA, MIL review. CPK is needed for dimensional, parametric data. IQC should do check for all material such as FCCL, coverlay, stiffener, SUS and TSA/PSA, and SMT parts.
4) Process yield of bare flex and flex Assembly
Bare flex, Flex assembly process flow chart,  design/process/quality summary, yield tread chart, Update MP yield projection based on “yield calculator” tool.
5) OQC Issue and ORT
Bare flex and Assembly ORT review.
6) Downstream/Customer issue review
FATP/MI IQC / online /ORT issue MIL review,
7) Test review
Test fixture, ERS, correlation, funnel spec, test coverage+mitigation plan, test data distribution + Cpk, and any recommendation on testing. Test automation + MP plan.
8) Flex stackup with 5x cross-section data table, FACA if CPK not meeting 1.67
9) Cp/Cpk histogram of FAI/SPC (32pcs).
Need FACA for Cpk<1.33 or distribution abnormal; Improvement plan and control plan needed for both FAI/SPC Cpk over 1.33 but less than 1.67
10) Data collection review
Follow “Apple Flex DFM NPI Data Collection Requirement”,  “Component Peel Test Procedure for FPCA “, “Component Shear Test Procedure for FPCA”.  Data analysis and FACA are needed for failures and findings
11) DFMEA/PFMEA Top5 issue update
12) Follow up of DFM “build and collect data” items when OK2Fab. Plus monitoring and reject item, which impact quality
13) Flex mishandling and abuse test review
Follow “Flex mishandling and abuse test guideline”, and test to failure to catch design weakness. *Not MCO defined bending line
C.  Readiness (NPI and MP)
14) DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction
For bare flex, pls. provide detailed self-assessment per Apple product CPP or generic CPP and Quality control list,  provide actions how to meet requests if there is gap.
Sufficient data and validation are needed for design change and recommendation.
15) NPI Soft tool and MP hard tool report
MP hard tool refers to MP intended hard tool, any tool not for final MP is not MP hard tool. MP intended hard tool is a must from EVT.
16) Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT)
17) Lesson learn from last generation and this build (what can make next build and MP better for design, process and build management)
18) MP readiness (update from P2 postmortem), MP readiness + Automation/traceability scores (update from EVT postmortem)
19) Vendor owned MP material supplier POR (Plan Of Record), including FCCL, coverlay, PSA&TSA, DIE Cut suppliers, SUS. Also need tracking list of these material used in each build (Proto,EVT, Carrier, DVT,PVT, Rampup).
20) MP line qual plan including, define DRI and team list

## Slide 53

| Flex | Test Item |  | Result | Remark |
|---|---|---|---|---|
| V53 UAT1 | X-ray | Clip | Pass | Max void is 14.1%. meet spec<35% |
|  |  | B2B | Pass | Max void is 1.18%, meet spec<25% |
|  |  | IC | Pass | No void |
|  |  | Mic | Pass | Max void is 4.64%, meet spec<25% |
|  |  | Bonding | Pass | Max void is 26.70%, meet spec<35% |
|  |  | Bending | Pass | No micro crack. |
|  | Peeling Force | Clip | Waiver | Min 4.11, CL_JINDO_M_TUNER peeling<5N waived by DFM. |
|  |  | B2B | Pass | Min 23.14N, meet spec>5N |
|  |  | Mic | Pass | Min 9.65, meet spec>4N |
|  |  | IC | Pass | Min 0.62N for data collection. |
|  |  | Bonding | Pass | Min 5.22, meet spec>5N |
|  | Shearing Force | Clip | Pass | Min 7.70N, meet spec>5N. |
|  |  | Mic | Pass | Min 54.43N, meet spec>4N. |
|  |  | IC | Pass | Min 5.93N for data collection. |
|  |  | Bonding | Pass | Min 37.47N, meet spec>5N. |
|  | X-section | Clip | Pass | IMC: 1.26um-2.63um, meet spec (1-4um), soldring OK. |
|  |  | B2B | Pass | IMC: 1.05um-2.42um. meet spec (1-4um), soldring OK. |
|  |  | MIc | Pass | IMC: 1.58um-2.42um. meet spec (1-4um), soldring OK. |
|  |  | IC | Pass | IMC: 1.54um-3.65um. meet spec (1-4um), soldring OK. |
|  |  | Bonding | Pass | IMC: 1.16um-2.53um. meet spec (1-4um), soldring OK. |
|  |  | Bending | Pass | No micro crack. |

Remark
All data have been posted in Box
10. Data Collection Summary | V53 UAT1

## Slide 54
10. Data Collection Summary | V53 UAT1 - Clip Peeling Force Summary
No obvious difference between configs and vendors.
CL_JINDO_M_TUNER (806-51391) Peeling force < 5N waived by DFM ,others clips peeling force can meet target.

## Slide 55
10. Data Collection Summary | V53 UAT1 - Mic/B2B/Bonding Peeling Force Summary
Mic/B2B/Boding peeling force no obvious difference between configs and vendors.
(6) CL0205
ANT39 GND
B2B

## Slide 56
Postmortem Review Items:
A. Resource (NPI and  MP)
1) O-chart and resource plan
Team list from x-function team, provide CA if any gap per apple resource plan for both NPI and MP.
B. Build review (Design, Process and Quality)
2) Configs and build status
3) IQC
IQC yield and issue FACA, MIL review. CPK is needed for dimensional, parametric data. IQC should do check for all material such as FCCL, coverlay, stiffener, SUS and TSA/PSA, and SMT parts.
4) Process yield of bare flex and flex Assembly
Bare flex, Flex assembly process flow chart,  design/process/quality summary, yield tread chart, Update MP yield projection based on “yield calculator” tool.
5) OQC Issue and ORT
Bare flex and Assembly ORT review.
6) Downstream/Customer issue review
FATP/MI IQC / online /ORT issue MIL review,
7) Test review
Test fixture, ERS, correlation, funnel spec, test coverage+mitigation plan, test data distribution + Cpk, and any recommendation on testing. Test automation + MP plan.
8) Flex stackup with 5x cross-section data table, FACA if CPK not meeting 1.67
9) Cp/Cpk histogram of FAI/SPC (32pcs).
Need FACA for Cpk<1.33 or distribution abnormal; Improvement plan and control plan needed for both FAI/SPC Cpk over 1.33 but less than 1.67
10) Data collection review
Follow “Apple Flex DFM NPI Data Collection Requirement”,  “Component Peel Test Procedure for FPCA “, “Component Shear Test Procedure for FPCA”.  Data analysis and FACA are needed for failures and findings
11) DFMEA/PFMEA Top5 issue update
12) Follow up of DFM “build and collect data” items when OK2Fab. Plus monitoring and reject item, which impact quality
13) Flex mishandling and abuse test review
Follow “Flex mishandling and abuse test guideline”, and test to failure to catch design weakness. *Not MCO defined bending line
C.  Readiness (NPI and MP)
14) DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction
For bare flex, pls. provide detailed self-assessment per Apple product CPP or generic CPP and Quality control list,  provide actions how to meet requests if there is gap.
Sufficient data and validation are needed for design change and recommendation.
15) NPI Soft tool and MP hard tool report
MP hard tool refers to MP intended hard tool, any tool not for final MP is not MP hard tool. MP intended hard tool is a must from EVT.
16) Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT)
17) Lesson learn from last generation and this build (what can make next build and MP better for design, process and build management)
18) MP readiness (update from P2 postmortem), MP readiness + Automation/traceability scores (update from EVT postmortem)
19) Vendor owned MP material supplier POR (Plan Of Record), including FCCL, coverlay, PSA&TSA, DIE Cut suppliers, SUS. Also need tracking list of these material used in each build (Proto,EVT, Carrier, DVT,PVT, Rampup).
20) MP line qual plan including, define DRI and team list

## Slide 57: 11. Assembly PFMEA  Top 5 | UAT1  

| Process | Failure Mode | Failure Effects | Sev | Occ | Det | RPN | Current Design | Improved Design | Action Results |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | Sev | Occ | Det | RPN |
| Dispensing UV Glue | U0402 Less glue | Cosmetic fail | 7 | 6 | 6 | 252 | Process: There is a Clip above the IC, the dispensing path is avoided, and there is a risk of less glue Detection: -100% VI using CCD | Process: 1. The dispensing path was optimized and the best path was selected according to the DOE results Detection: -100% VI using CCD | 7 | 2 | 6 | 84 |
| Dispensing UV Glue | CL-ANT2-SHORT hanging glue | Cosmetic fail | 7 | 6 | 6 | 252 | Process: The height of Clip is 3.25mm, and the height of dispensing is 2.5mm, so there is a risk of hanging glue in operation. Detection: -100% VI using CCD | Process: 1.The dispensing path was optimized, and the height was increased to 4.5mm after dispensing Detection: -100% VI using CCD | 7 | 2 | 6 | 84 |
| Tape remove | Clip deformation | Cosmetic fail | 6 | 5 | 6 | 180 | Process: The remove tape cover is not tightly pressed on FPC. FPC will tilt upward during manual remove tape , which will cause the clip deformation  Detection: -100% VI using CCD | Process: 1.Optimize the fixture, Add a fixed block on the remove tape cover to hold down the FPC. 2.Use automation for tape removing station in EVT build.  Detection: -100% VI using CCD | 6 | 3 | 6 | 108 |
| PSA pressing | Clip deformation | Cosmetic fail | 6 | 5 | 6 | 180 | Process: Manual press PSA may touch and deform clip.       Detection: -100% VI using CCD | Process: 1. Optimize the SOP, high light the risk to OP,     add self-inspection motion to decrease the     risk. 2. Use auto PSA pressing machine    for EVT build to avoid manual risk.   Detection: -100% VI using CCD | 6 | 3 | 6 | 108 |
| Bending | Bending line shift | Cosmetic fail | 6 | 5 | 8 | 240 | Process: Flex has the risk to be inclined in the holder cavity when OP carelessly loads.     Detection: -100% VI using CCD | Process: 1. Optimize the SOP, highlight the risk to OP,     add self-inspection motion to decrease the     risk. 2. Use auto loading& unloading bending machine    for EVT build to avoid manual risk.   Detection: -100% VI using CCD | 6 | 3 | 8 | 144 |
| Bending | Clip deformation | Cosmetic fail | 6 | 5 | 8 | 240 | Process: Bending station manual loading& unloading step has the risk to touch and deform the clip   Detection: -100% VI using CCD. | Process: 1.Optimize the handling SOP, define a reasonable      position and motion for tweezers picking&    placing. 2.Implement auto loading& unloading process to    avoid manual risk in EVT build. Detection: -100% VI using CCD. | 6 | 3 | 8 | 144 |

11. Assembly PFMEA  Top 5 | UAT1

## Slide 58
Postmortem Review Items:
A. Resource (NPI and  MP)
1) O-chart and resource plan
Team list from x-function team, provide CA if any gap per apple resource plan for both NPI and MP.
B. Build review (Design, Process and Quality)
2) Configs and build status
3) IQC
IQC yield and issue FACA, MIL review. CPK is needed for dimensional, parametric data. IQC should do check for all material such as FCCL, coverlay, stiffener, SUS and TSA/PSA, and SMT parts.
4) Process yield of bare flex and flex Assembly
Bare flex, Flex assembly process flow chart,  design/process/quality summary, yield tread chart, Update MP yield projection based on “yield calculator” tool.
5) OQC Issue and ORT
Bare flex and Assembly ORT review.
6) Downstream/Customer issue review
FATP/MI IQC / online /ORT issue MIL review,
7) Test review
Test fixture, ERS, correlation, funnel spec, test coverage+mitigation plan, test data distribution + Cpk, and any recommendation on testing. Test automation + MP plan.
8) Flex stackup with 5x cross-section data table, FACA if CPK not meeting 1.67
9) Cp/Cpk histogram of FAI/SPC (32pcs).
Need FACA for Cpk<1.33 or distribution abnormal; Improvement plan and control plan needed for both FAI/SPC Cpk over 1.33 but less than 1.67
10) Data collection review
Follow “Apple Flex DFM NPI Data Collection Requirement”,  “Component Peel Test Procedure for FPCA “, “Component Shear Test Procedure for FPCA”.  Data analysis and FACA are needed for failures and findings
11) DFMEA/PFMEA Top5 issue update
12) Follow up of DFM “build and collect data” items when OK2Fab. Plus monitoring and reject item, which impact quality
13) Flex mishandling and abuse test review
Follow “Flex mishandling and abuse test guideline”, and test to failure to catch design weakness. *Not MCO defined bending line
C.  Readiness (NPI and MP)
14) DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction
For bare flex, pls. provide detailed self-assessment per Apple product CPP or generic CPP and Quality control list,  provide actions how to meet requests if there is gap.
Sufficient data and validation are needed for design change and recommendation.
15) NPI Soft tool and MP hard tool report
MP hard tool refers to MP intended hard tool, any tool not for final MP is not MP hard tool. MP intended hard tool is a must from EVT.
16) Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT)
17) Lesson learn from last generation and this build (what can make next build and MP better for design, process and build management)
18) MP readiness (update from P2 postmortem), MP readiness + Automation/traceability scores (update from EVT postmortem)
19) Vendor owned MP material supplier POR (Plan Of Record), including FCCL, coverlay, PSA&TSA, DIE Cut suppliers, SUS. Also need tracking list of these material used in each build (Proto,EVT, Carrier, DVT,PVT, Rampup).
20) MP line qual plan including, define DRI and team list

## Slide 59
13. Flex Mishandling and Abuse Test Review – Test location instruction& Suggestion | V53 UAT1
Bend & Twist test location
Suggestion
Pressure test location
Total 7 locations, no abnormal
Total 12 locations, no abnormal.

## Slide 60

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 1 (Bending area) | Engineer | 45° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (10times) | 1 | 7 | 7 | 7 | N/A |
|  |  |  | 2 | 7 | 7 | 7 | N/A |
|  |  |  | 3 | 9 | 9 | 9 | N/A |
|  |  |  | 4 | 8 | 8 | 8 | N/A |
|  |  |  | 5 | 9 | 9 | 9 | N/A |
|  |  | 45° (test to fail or 50 times max.) | 1 | 30 | 30 | 30 | N/A |
|  |  |  | 2 | 30 | 30 | 30 | N/A |
|  |  |  | 3 | 35 | 35 | 35 | N/A |
|  |  |  | 4 | 30 | 30 | 30 | N/A |
|  |  |  | 5 | 35 | 35 | 35 | N/A |
|  |  | 90° (test to fail or 50 times max.) | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 9 | 9 | 9 | N/A |
|  |  |  | 3 | 9 | 9 | 9 | N/A |
|  |  |  | 4 | 8 | 8 | 8 | N/A |
|  |  |  | 5 | 9 | 9 | 9 | N/A |

45°(10 times)
Bend instruction
45°
90°
Defects
90°(10 times)
13. Flex Mishandling and Abuse Test Review – Mishandling Test | V53 UAT1
45°(test to fail or 50 times)
90°(test to fail or 50 times)
Location 1
1

## Slide 61

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 2 (Bending area) | Engineer | 45° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (10times) | 1 | 9 | 9 | 9 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 8 | 8 | 8 | N/A |
|  |  |  | 4 | 7 | 7 | 7 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |
|  |  | 45° (test to fail or 50 times max.) | 1 | 35 | 35 | 35 | N/A |
|  |  |  | 2 | 30 | 30 | 30 | N/A |
|  |  |  | 3 | 30 | 30 | 30 | N/A |
|  |  |  | 4 | 30 | 30 | 30 | N/A |
|  |  |  | 5 | 30 | 30 | 30 | N/A |
|  |  | 90° (test to fail or 50 times max.) | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 9 | 9 | 9 | N/A |
|  |  |  | 3 | 9 | 9 | 9 | N/A |
|  |  |  | 4 | 7 | 7 | 7 | N/A |
|  |  |  | 5 | 6 | 6 | 6 | N/A |

45°(10 times)
Bend instruction
Location 2
45°
90°
Defects
90°(10 times)
45°(test to fail or 50 times)
90°(test to fail or 50 times)
2
13. Flex Mishandling and Abuse Test Review – Mishandling Test | V53 UAT1

## Slide 62

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 3 (Bending area) | Engineer | 45° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (10times) | 1 | 9 | 9 | 9 | N/A |
|  |  |  | 2 | 7 | 7 | 7 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
|  |  |  | 4 | 8 | 8 | 8 | N/A |
|  |  |  | 5 | 6 | 6 | 6 | N/A |
|  |  | 45° (test to fail or 50 times max.) | 1 | 25 | 25 | 25 | N/A |
|  |  |  | 2 | 30 | 30 | 30 | N/A |
|  |  |  | 3 | 25 | 25 | 25 | N/A |
|  |  |  | 4 | 30 | 30 | 30 | N/A |
|  |  |  | 5 | 25 | 25 | 25 | N/A |
|  |  | 90° (test to fail or 50 times max.) | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 8 | 8 | 8 | N/A |
|  |  |  | 4 | 7 | 7 | 7 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |

45°(10 times)
Bend instruction
Location 3
45°
90°
Defects
90°(10 times)
45°(test to fail or 50 times)
90°(test to fail or 50 times)
3
13. Flex Mishandling and Abuse Test Review – Mishandling Test | V53 UAT1

## Slide 63

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 4 (Bending area) | Engineer | 45° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (10times) | 1 | 9 | 9 | 9 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 9 | 9 | 9 | N/A |
|  |  |  | 4 | 7 | 7 | 7 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |
|  |  | 45° (test to fail or 50 times max.) | 1 | 35 | 35 | 35 | N/A |
|  |  |  | 2 | 30 | 30 | 30 | N/A |
|  |  |  | 3 | 30 | 30 | 30 | N/A |
|  |  |  | 4 | 35 | 35 | 35 | N/A |
|  |  |  | 5 | 30 | 30 | 30 | N/A |
|  |  | 90° (test to fail or 50 times max.) | 1 | 9 | 9 | 9 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 6 | 6 | 6 | N/A |
|  |  |  | 4 | 9 | 9 | 9 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |

45°(10 times)
Bend instruction
Location 4
45°
90°
Defects
90°(10 times)
45°(test to fail or 50 times)
90°(test to fail or 50 times)
4
13. Flex Mishandling and Abuse Test Review – Mishandling Test | V53 UAT1

## Slide 64

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 5 (Bending area) | Engineer | 45° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 45° (test to fail or 50 times max.) | 1 | 35 | 35 | 35 | N/A |
|  |  |  | 2 | 35 | 35 | 35 | N/A |
|  |  |  | 3 | 35 | 35 | 35 | N/A |
|  |  |  | 4 | 30 | 30 | 30 | N/A |
|  |  |  | 5 | 30 | 30 | 30 | N/A |
|  |  | 90° (test to fail or 50 times max.) | 1 | 10 | 10 | 10 | N/A |
|  |  |  | 2 | 15 | 15 | 15 | N/A |
|  |  |  | 3 | 15 | 15 | 15 | N/A |
|  |  |  | 4 | 10 | 10 | 10 | N/A |
|  |  |  | 5 | 15 | 15 | 15 | N/A |

45°(10 times)
Bend instruction
Location 5
45°
90°
Defects
90°(10 times)
45°(test to fail or 50 times)
90°(test to fail or 50 times)
5
13. Flex Mishandling and Abuse Test Review – Mishandling Test | V53 UAT1

## Slide 65

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 6 (Bending area) | Engineer | 45° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 45° (test to fail or 50 times max.) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (test to fail or 50 times max.) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |

45°(10 times)
Bend instruction
Location 6
45°
90°
Defects
90°(10 times)
45°(test to fail or 50 times)
90°(test to fail or 50 times)
6
13. Flex Mishandling and Abuse Test Review – Mishandling Test | V53 UAT1

## Slide 66

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 7 (Bending area) | Engineer | 45° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 45° (test to fail or 50 times max.) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (test to fail or 50 times max.) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |

45°(10 times)
Bend instruction
Location 7
45°
90°
Defects
90°(10 times)
45°(test to fail or 50 times)
90°(test to fail or 50 times)
7
13. Flex Mishandling and Abuse Test Review – Mishandling Test | V53 UAT1

## Slide 67
13. Flex Mishandling and Abuse Test Review - Twist Test | V53 UAT1

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 1 | Engineer | 45︒ | 1 | 6 | 6 | 6 | N/A |
|  |  |  | 2 | 7 | 7 | 7 | N/A |
|  |  |  | 3 | 8 | 8 | 8 | N/A |
|  |  |  | 4 | 6 | 6 | 6 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |
| Location 2 |  |  | 1 | 6 | 6 | 6 | N/A |
|  |  |  | 2 | 7 | 7 | 7 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
|  |  |  | 4 | 6 | 6 | 6 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |
| Location 3 |  |  | 1 | 7 | 7 | 7 | N/A |
|  |  |  | 2 | 7 | 7 | 7 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
|  |  |  | 4 | 6 | 6 | 6 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |
| Location 4 |  |  | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 6 | 6 | 6 | N/A |
|  |  |  | 3 | 8 | 8 | 8 | N/A |
|  |  |  | 4 | 7 | 7 | 7 | N/A |
|  |  |  | 5 | 6 | 6 | 6 | N/A |

Location1
Location2
Location3
Location4
Twist test location
Defects

## Slide 68

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 5 | Engineer | 45︒ | 1 | 6 | 6 | 6 | N/A |
|  |  |  | 2 | 7 | 7 | 7 | N/A |
|  |  |  | 3 | 8 | 8 | 8 | N/A |
|  |  |  | 4 | 6 | 6 | 6 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |
| Location 6 |  |  | 1 | 7 | 7 | 7 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
|  |  |  | 4 | 6 | 6 | 6 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |
| Location 7 |  |  | 1 | 7 | 7 | 7 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
|  |  |  | 4 | 5 | 5 | 5 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |

Location5
Location6
Location7
Twist test location
Defects
13. Flex Mishandling and Abuse Test Review - Twist Test | V53 UAT1

## Slide 69

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 1 | Engineer | Normal pressure  (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |
|  |  | High pressure (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |

Normal pressure(10 times)
Pressure test instruction
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1
Location1(Mic area)
Defects
High pressure(10 times)

## Slide 70

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 2 | Engineer | Normal pressure  (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |
|  |  | High pressure (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |

Normal pressure(10 times)
Pressure test instruction
Location2（coating area）
Defects
High pressure(10 times)
Location 2
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1

## Slide 71

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 3 | Engineer | Normal pressure  (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |
|  |  | High pressure (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |

Normal pressure(10 times)
Pressure test instruction
Location3(PSA area)
Defects
High pressure(10 times)
No defects, result is OK
Location 3
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1

## Slide 72

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 4 | Engineer | Normal pressure  (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |
|  |  | High pressure (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |

Normal pressure(10 times)
Pressure test instruction
Location4(B2B area)
Defects
High pressure(10 times)
Location 4
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1

## Slide 73

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 5 | Engineer | Normal pressure  (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |
|  |  | High pressure (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |

Normal pressure(10 times)
Pressure test instruction
Location5(Coating area)
Defects
High pressure(10 times)
Location 5
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1

## Slide 74

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 6 | Engineer | Normal pressure  (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |
|  |  | High pressure (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |

Normal pressure(10 times)
Pressure test instruction
Location6(Coating area)
Defects
High pressure(10 times)
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1

## Slide 75

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 7 | Engineer | Normal pressure  (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |
|  |  | High pressure (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |

Normal pressure(10 times)
Pressure test instruction
Location7(PSA area)
Defects
High pressure(10 times)
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1
Location 7

## Slide 76

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 8 | Engineer | Normal pressure  (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |
|  |  | High pressure (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |

Normal pressure(10 times)
Pressure test instruction
Location8(Coating area)
Defects
High pressure(10 times)
Location 8
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1

## Slide 77

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 9 | Engineer | Normal pressure  (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |
|  |  | High pressure (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |

Normal pressure(10 times)
Pressure test instruction
Location9(PSA area)
Defects
High pressure(10 times)
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1
Location 9

## Slide 78

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 10 | Engineer | Normal pressure  (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |
|  |  | High pressure (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |

Normal pressure(10 times)
Pressure test instruction
Location10(Coating area)
Defects
High pressure(10 times)
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1
Location 10

## Slide 79

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 11 | Engineer | Normal pressure  (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |
|  |  | High pressure (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |

Normal pressure(10 times)
Pressure test instruction
Location11(PSA area)
Defects
High pressure(10 times)
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1
Location 11

## Slide 80

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 12 | Engineer | Normal pressure  (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |
|  |  | High pressure (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  |  | 6 | OK | OK | OK | N/A |
|  |  |  | 7 | OK | OK | OK | N/A |
|  |  |  | 8 | OK | OK | OK | N/A |
|  |  |  | 9 | OK | OK | OK | N/A |
|  |  |  | 10 | OK | OK | OK | N/A |

Normal pressure(10 times)
Pressure test instruction
Location12(Bonding area)
Defects
High pressure(10 times)
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1
Location 12

## Slide 81
Postmortem Review Items:
A. Resource (NPI and  MP)
1) O-chart and resource plan
Team list from x-function team, provide CA if any gap per apple resource plan for both NPI and MP.
B. Build review (Design, Process and Quality)
2) Configs and build status
3) IQC
IQC yield and issue FACA, MIL review. CPK is needed for dimensional, parametric data. IQC should do check for all material such as FCCL, coverlay, stiffener, SUS and TSA/PSA, and SMT parts.
4) Process yield of bare flex and flex Assembly
Bare flex, Flex assembly process flow chart,  design/process/quality summary, yield tread chart, Update MP yield projection based on “yield calculator” tool.
5) OQC Issue and ORT
Bare flex and Assembly ORT review.
6) Downstream/Customer issue review
FATP/MI IQC / online /ORT issue MIL review,
7) Test review
Test fixture, ERS, correlation, funnel spec, test coverage+mitigation plan, test data distribution + Cpk, and any recommendation on testing. Test automation + MP plan.
8) Flex stackup with 5x cross-section data table, FACA if CPK not meeting 1.67
9) Cp/Cpk histogram of FAI/SPC (32pcs).
Need FACA for Cpk<1.33 or distribution abnormal; Improvement plan and control plan needed for both FAI/SPC Cpk over 1.33 but less than 1.67
10) Data collection review
Follow “Apple Flex DFM NPI Data Collection Requirement”,  “Component Peel Test Procedure for FPCA “, “Component Shear Test Procedure for FPCA”.  Data analysis and FACA are needed for failures and findings
11) DFMEA/PFMEA Top5 issue update
12) Follow up of DFM “build and collect data” items when OK2Fab. Plus monitoring and reject item, which impact quality
13) Flex mishandling and abuse test review
Follow “Flex mishandling and abuse test guideline”, and test to failure to catch design weakness. *Not MCO defined bending line
C.  Readiness (NPI and MP)
14) DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction
For bare flex, pls. provide detailed self-assessment per Apple product CPP or generic CPP and Quality control list,  provide actions how to meet requests if there is gap.
Sufficient data and validation are needed for design change and recommendation.
15) NPI Soft tool and MP hard tool report
MP hard tool refers to MP intended hard tool, any tool not for final MP is not MP hard tool. MP intended hard tool is a must from EVT.
16) Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT)
17) Lesson learn from last generation and this build (what can make next build and MP better for design, process and build management)
18) MP readiness (update from P2 postmortem), MP readiness + Automation/traceability scores (update from EVT postmortem)
19) Vendor owned MP material supplier POR (Plan Of Record), including FCCL, coverlay, PSA&TSA, DIE Cut suppliers, SUS. Also need tracking list of these material used in each build (Proto,EVT, Carrier, DVT,PVT, Rampup).
20) MP line qual plan including, define DRI and team list

## Slide 82
V53 | Open DFM_P1 | UAT1

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 1 | V53 UAT1 | MCO 056-20573-37 | FAI148 / 150 / 151 / 152 / 153 / 154 Encap dimensions CPK < 1.67 due to default tolerance ±0.20mm. | Change Encap dimension control from ±0.20 to Max / Min limit. | Open for P2 |
| 2 | V53 UAT1 | MCO 056-20573-37 | Encap to bending line is only 0.42mm against Guideline 0.50mm when Encap overflow to upper limit 4.83+0.20mm. Risk of Encap damage. | Enlarge Encap from 4.83 to 4.95mm and controlled by “Max 4.95”. (0.55mm for Encap overflow and 0.50mm for Bending) | Open for P2 |
| 3 | V53 UAT1 | MCO 056-20573-37 | CL_JINDO_M_Tuner Clip Peeling force < 5N. Risk of Clip peel off in FATP REL test. | Change Clip pad design to make Clip arm on top layer. | Open for P2 |
| 4 | V53 UAT1 | Gerber 821-05715-01 821-05769-01 | Strobe flex need extra SMT line due to current pad design.  If exchange UAT1 / Strobe pad size, we could save strobe pre-bump line. | Exchange pad size of UAT1 and Strobe Flex. | Open for P2 |


## Slide 83
V53 | Open DFM_P1 | UAT1

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 1 | V53 UAT1 | MCO 056-20573-37 | FAI148 / 150 / 151 / 152 / 153 / 154 Encap dimensions CPK < 1.67 due to default tolerance ±0.20mm. | Change Encap dimension control from ±0.20 to Max / Min limit. | Open for P2 |
|  |  |  |  |  |  |

Issue:
Encap dimensions CPK < 1.67 due to default tolerance ±0.20mm.
Proposal:
Change Encap dimension control from tolerance limit to Max / Min limit.
MCO 056-20573-37
D37 UAT1 for reference
Encap control by Max / Min limit.
PD waived FAI263 for P1.
CPK < 1.67
Current tolerance ±0.20mm

| Dimension | Current | Proposed |
|---|---|---|
| FAI 148 | 17.25 ±0.20 | Min 17.25 |
| FAI 150 | -0.78 ±0.20 | Max -0.78 |
| FAI 151 | 23.09 ±0.20 | Min 23.09 |
| FAI 152 | 26.50 ±0.20 | Max 26.50 |
| FAI 153 | 28.24 ±0.20 | Min 28.24 |
| FAI 154 | 31.84 ±0.20 | Max 31.84 |


## Slide 84
V53 | Open DFM_P1 | UAT1

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 2 | V53 UAT1 | MCO 056-20573-37 | Encap to bending line is only 0.42mm against Guideline 0.50mm when Encap overflow to upper limit 4.83+0.20mm. Risk of Encap damage. | Enlarge Encap from 4.83 to 4.95mm and controlled by “Max 4.95”. (0.55mm for Encap overflow and 0.50mm for Bending) | Open for P2 |
|  |  |  |  |  |  |

Issue:
Encap is close to bending line when Encap overflow to upper limit. Risk of Encap damage.
Proposal:
Enlarge Encap from 4.83 to 4.95mm and controlled by “Max 4.95”.
(0.55mm for Encap overflow and 0.50mm for Bending)
MCO 056-20573-37
When Encap overflow to upper limit
Encap to Bending line is 0.42mm.
Risk of Encap damage by bending tool.
Bending Guideline: 0.50mm gap is needed for bending
P1 data CPK > 1.67
Proposed Max 4.95

## Slide 85
V53 | Open DFM_P1 | UAT1

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 3 | V53 UAT1 | MCO 056-20573-37 | CL_JINDO_M_Tuner Clip Peeling force < 5N. Risk of Clip peel off in FATP REL test. | Change Clip pad design to make Clip arm on top layer. | Open for P2 |
|  |  |  |  |  |  |

Issue:
CL_JINDO_M_Tuner Clip Peeling force < 5N. Risk of Clip peel off in FATP REL test.
Proposal:
Change Clip pad design to make Clip arm on top layer.
CL_JINDO_M_Tuner Clip

| Peeling force / N |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | Min | Max | Ave |
| 5.88 | 4.72 | 5.20 | 6.07 | 4.91 | 4.72 | 6.07 | 5.35 |
| 5.33 | 4.83 | 5.55 | 5.25 | 5.72 |  |  |  |

Peeling force < 5N.
Failure mode: Flex pad peel off, OK.
Clip arm on top layer

| Peeling force / N |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| DOE | 1 | 2 | 3 | 4 | 5 | Ave | Improve |
| POR | 5.88 | 4.72 | 5.20 | 6.07 | 4.91 | 5.35 | - |
|  | 5.33 | 4.83 | 5.55 | 5.25 | 5.72 |  |  |
| DOE | 8.91 | 8.61 | 10.03 | 7.91 | 9.14 | 8.92 | 3.57 ↑ |

DOE:  Turn over POR Clip to make clip arm on top layer.

## Slide 86
V53 | Open DFM_P1 | UAT1

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 4 | V53 UAT1 | Gerber 821-05715-01 821-05769-01 | Strobe flex need extra SMT line due to current pad design.  If exchange UAT1 / Strobe pad size, we could save strobe pre-bump line. | Exchange pad size of UAT1 and Strobe Flex. | Open for P2 |
|  |  |  |  |  |  |

Issue:
Strobe flex need extra SMT line due to current pad design.
If exchange UAT1 / Strobe pad, we could save strobe pre-bump line.
Proposal:
Exchange pad size of UAT1 and Strobe Flex.
Pad design
Save pre-bump line
Big pad on UAT1 flex
Small pad on UAT1 flex

## Slide 87: Thanks!
Thanks!