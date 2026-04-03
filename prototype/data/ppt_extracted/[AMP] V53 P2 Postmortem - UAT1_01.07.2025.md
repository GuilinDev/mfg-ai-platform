# [AMP] V53 P2 Postmortem - UAT1_01.07.2025


## Slide 1: V53 P2 Postmortem - UAT1
V53 P2 Postmortem - UAT1
Amphenol
01-07-2025

## Slide 2
PM Contents Overall
Low
High
Mid

| No. | PM Contents | V53 UAT1 |
|---|---|---|
| 1 | O-Chart and Resource |  |
| 2 | Config and Build Status |  |
| 3 | IQC | APD waived Clips OOS for 806-50871/806-53763 |
| 4 | Process, Yield and FACA |  |
| 5 | OQC and ORT | On going, so far low risk, all items will be done by 1/19/2025 |
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
| V53 UAT1 | 632-07540 | LCP | POR | AMP | FXGL | Completed |  | 4,900x shipped to FATP |
| V53 UAT1 | 932-05144 | LCP | DOE | AMP | FXGL | Completed |  | 1,950x shipped to FATP |


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
| Outline |  |  | N/A | N/A |  |
| Layout |  |  | N/A | N/A |  |


## Slide 7
V53 | Design Comparison | UAT1

| Difference | Build Stage |  |  |  |  |
|---|---|---|---|---|---|
|  | P1 | P2 | EVT | CRB | Comparison P1 vs. P2 |
| CL_STROBE_GND_WEST | 806-50867 | 806-53366 | N/A | N/A |  |
| CL_ANT2_FEED | 806-50868 | 806-53387 | N/A | N/A |  |


## Slide 8
V53 | Design Comparison | UAT1

| Difference | Build Stage |  |  |  |  |
|---|---|---|---|---|---|
|  | P1 | P2 | EVT | CRB | Comparison P1 vs. P2 |
| CL_ANT2_SHORT | 806-50869 | 806-50869 | N/A | N/A | P2 same as P1 |
| CL_ANT_VERT_SP | 806-50870 | 806-53763 | N/A | N/A |  |
| CL_ANT10_FEED | 806-50871 | 806-50871 | N/A | N/A | P2 same as P1 |


## Slide 9
V53 | Design Comparison | UAT1

| Difference | Build Stage |  |  |  |  |
|---|---|---|---|---|---|
|  | P1 | P2 | EVT | CRB | Comparison P1 vs. P2 |
| CL_STROBE_GND_EAST | 806-50873 | 806-53367 | N/A | N/A |  |
| CL_JINDO_L | 806-51162 | 806-51162 | N/A | N/A |  |
| CL_JINDO_M_GND | 806-51201 | 806-53698 | N/A | N/A |  |


## Slide 10
V53 | Design Comparison | UAT1

| Difference | Build Stage |  |  |  |  |
|---|---|---|---|---|---|
|  | P1 | P2 | EVT | CRB | Comparison P1 vs. P2 |
| CL_ANT10_GND | 806-51346 | 806-53371 | N/A | N/A |  |
| CL_JINDO_M_TUNER | 806-51391 | 806-51391 | N/A | N/A |  |
| PAD_GND_NORTH_BTTM | 870-23917 | Removed | N/A | N/A | P2 remove PAD_GND NORTH_BTTM |


## Slide 11
V53 | Design Comparison | UAT1

| Difference | Build Stage |  |  |  |  |
|---|---|---|---|---|---|
|  | P1 | P2 | EVT | CRB | Comparison P1 vs. P2 |
| SUS-1 |  | Removed | N/A | N/A | P2 remove SUS-1 |
| SUS-2 |  |  | N/A | N/A | P2 same as P1 |
| Stiffener | / |  | N/A | N/A | P2 add Stiffener both in TOP/BOTTOM side |


## Slide 12
V53 | Design Comparison | UAT1

| Difference | Build Stage |  |  |  |  |
|---|---|---|---|---|---|
|  | P1 | P2 | EVT | CRB | Comparison P1 vs. P2 |
| PSA-1 |  | Removed | N/A | N/A | P2 remove PSA-1 |
| PSA-2 |  |  | N/A | N/A | P2 same as P1 |
| PSA-3 |  |  | N/A | N/A |  |


## Slide 13
V53 | Design Comparison | UAT1

| Difference | Build Stage |  |  |  |  |
|---|---|---|---|---|---|
|  | P1 | P2 | EVT | CRB | Comparison P1 vs. P2 |
| PSA-4 | Stackup:  PSA, 0.10mm PET Spacer, 0.10mm PSA, 0.05mm Liner, 0.036mm | Stackup:  PSA, 0.14mm Liner, 0.036mm | N/A | N/A | 1. Stackup change: P1:PSA+Spacer+PSA+Liner P2:PSA+Liner 2. Size change: |
| PSA-5 | CPSA,3M 9701H-100, 0.1mm | PSA, Nitto denko 56110B(NSS), 0.1 mm | N/A | N/A | 1. Adhesive type change: P1:CPSA,3M 9701H-100, 0.1mm P2:PSA, Nitto denko 56110B(NSS), 0.1 mm 2. Size change |
| MIC film |  |  | N/A | N/A |  |


## Slide 14
V53 | Design Comparison | UAT1

| Difference | Build Stage |  |  |  |  |
|---|---|---|---|---|---|
|  | P1 | P2 | EVT | CRB | Comparison P1 vs. P2 |
| Barcode |  |  | N/A | N/A |  |
| Silkscreen |  |  | N/A | N/A |  |
| Bonding pad | UAT1         Strobe | UAT1         Strobe | N/A | N/A | P1:UAT1 Bonding pads bigger than Strobe  P2:UAT1 Bonding pads smaller than Strobe |


## Slide 15
V53 | Design Comparison | UAT1

| Difference | Build Stage |  |  |  |  |
|---|---|---|---|---|---|
|  | P1 | P2 | EVT | CRB | Comparison P1 vs. P2 |
| Glue on Clip |  |  | N/A | N/A | Add UV glue on Clip pad |
| N/A | N/A | N/A | N/A | N/A | N/A |
| N/A | N/A | N/A | N/A | N/A | N/A |


## Slide 16
V53 | Design Comparison | UAT1

| Difference | Build Stage |  |  |  |  |
|---|---|---|---|---|---|
|  | P1 | P2 | EVT | CRB | Comparison P1 vs. P2 |
| Bending |  |  | N/A | N/A | P2 bending line change. Refer to MCO for details. |
| Bending |  |  | N/A | N/A | P2 bending line change. Refer to MCO for details. |
| Strobe outline |  |  | N/A | N/A |  |


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
3. Dashboard | V53 UAT1 Dashboard

| Project |  | Flex | UAT1 | Remark |
|---|---|---|---|---|
|  |  | Program | V53 |  |
| SPOR |  | Back-End Supplier | AMP |  |
| Status |  |  | Yellow |  |
| Trend |  |  |  |  |
| Back-End/SMT |  | P2 |  |  |
|  |  | Latest Yield | 97.10% |  |
|  |  | Latest SMT Yield | 99.82% |  |
|  |  | Latest Bonding Yield | 97.59% |  |
|  |  | Latest BE Yield | 99.68% |  |
|  |  | MP Yield Target | 96.5% |  |
|  |  | Build Yield Target | 88.0% |  |
|  |  | Supply Plan Yield | 98.0% |  |
| Project  Criteria | QE | DRI | Mark.Di |  |
|  |  | Flex IQC | Yellow | LY Clip 806-50871/806-53763dimension OOS Waived by PD  No impact on flex assembly，keep pushing vendor fix issue and improvement. |
|  |  | Flex OQC | Green |  |
|  |  | FATP/MI Walkthrough |  |  |
|  |  | Traceability | Green |  |
|  |  | GR&R | Green |  |
|  |  | Tester Correlation | Green |  |
|  |  | ERS Compliance | Green |  |
|  |  | MCO Compliance | Green |  |
|  |  | AMREP |  |  |
|  |  | Source Inspection |  |  |
|  |  | Cross-Team Meeting (Flex&MI) |  |  |
|  |  | MSOP | Green |  |
|  |  | Inspection Criteria | Green |  |
|  |  | FATP and MI DPPM targets |  |  |
|  |  | Quality (QCP) | Green |  |
|  |  | OK2Ship | Yellow | FAI225/FAI226/FAI229/FAI230/FAI233 all in SPEC； but CPK<1.67 Deviation was waived in OK2B report and refer to DFM slides. |
|  |  | Flex ORT | Yellow | so far no  risk , final check point 1/19 |
|  |  | FATP/MI IQC | Green |  |
|  |  | FATP/MI Process | Green |  |
|  |  | Sys./Mod. REL |  |  |

Pass or finished
Fail
Waived or on-going
NA

## Slide 19

| Component type | Supplier | APN | Chekcing items | Sampling size | Methology | Result |
|---|---|---|---|---|---|---|
| Clip | Ennvoi | 806-50869 806-50871 806-51162 806-51391 806-53366 806-53367 806-53371 806-53387 806-53698 806-53763 870-23918 | Cosmetic | AQL 0.4, per Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Reel | OMM | Pass |
|  |  |  | Package | 32pcs/package D/C | OMM | Pass |
|  |  |  | Plating thickness | 32pcs/Reel | XRF | Pass |
|  |  |  | Solder-ability | 10pcs/Lot | Dipping | Pass |
|  |  |  | Peeling test | 32pcs/package D/C | Dummy board | Pass |
| Clip | Ennvoi LY LV | 806-50869 806-50871 806-51162 806-51391 806-53366 806-53367 806-53371 806-53387 806-53698 806-53763 870-23918 | Cosmetic | AQL 0.4, per Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Reel | OMM | 806-50871:FAI 43 OOS；806-53763:FAI 26 OOS；APD waiver. No impact on flex assembly，keep pushing vendor fix issue and improvement. |
|  |  |  | Package | 32pcs/package D/C | OMM | Pass |
|  |  |  | Plating thickness | 32pcs/Reel | XRF | Pass |
|  |  |  | Solder-ability | 10pcs/Lot | Dipping | Pass |
|  |  |  | Peeling test | 32pcs/package D/C | Dummy board | Pass |
| Clip | LV | SAA PN： C-H365-12-L14-44 C-H367-12-L02-44 | Cosmetic | AQL 0.4, per Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Reel | OMM | Pass |
|  |  |  | Package | 32pcs/package D/C | OMM | Pass |
|  |  |  | Plating thickness | 32pcs/Reel | XRF | Pass |
|  |  |  | Solder-ability | 10pcs/Lot | Dipping | Pass |

3. IQC Summary and Highlight | V53 UAT1
Pass
Fail
Waived

## Slide 20
AP waiver
Clip dimension NG waiver - LY
3. IQC Summary and Highlight | V53 UAT1

| Item | Flex project | Build Phase | Vendor | APN | Waived Qty | Wavier Item | Wavier Description | Analysis | Wavier Approval Date | Wavier Approver | Layout |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | V53 | P2 | LY | 806-50871 | P2 | Dimension | FAI 43 OOS | FA:  One of the measurement point of FAI43 1.60mm is located at the hole center, and the hole center can't be measured by the side view, so we change the measurement point to the top side and the FAI43 is changed to 2.76mm (the data of 2.76mm is ok to meet in spec). CA: We proposed to change the FAI43 from 1.60mm to 2.76mm (the hole center is controlled by the FAI39 3.07mm), and need help to waive it for P2. —-ETD：1/22 | 11/26 | Jackson Xu |  |
| 2 | V53 | P2 | LY | 806-53763 | P2 | Dimension | FAI 26 OOS | FA:  The current 3D volume is 1.77mm³, so that calculate the mass to 0.014g (1.77mm³*7.93g/cm³/1000). 2D SPEC is 0.0065g, but actual MASS is about 0.014g.  CA:  We proposed to change the MASS SPEC from 0.0065±0.002 to 0.014±0.002, and need help to waive it for P2. —-ETD：1/20 | 11/26 | Jackson Xu |  |


## Slide 21

| Component type | Supplier | APN | Chekcing items | Sampling size | Methology | Result |
|---|---|---|---|---|---|---|
| LCP Bare Flex | muRata | 821-05715-02 921-05897-01 | Cosmetic | AQL 0.4/incoming lot | CCD | Pass |
|  |  |  | Dimension | 32pcs/incoming lot | OMM | Pass |
|  |  |  | Barcode read-ability | 32pcs/incoming lot | SR-2000 | Pass |
|  |  |  | Solder-ability | 3pcs/incoming lot | Dipping | Pass |
|  |  |  | Plating thickness | 32pcs/incoming lot | XRF | Pass |
| PI Bare Flex | Mflex | 821-05769-02 | Cosmetic | AQL 0.4/incoming lot | CCD | Pass |
|  |  |  | Dimension | 32pcs/incoming lot | OMM | Pass |
|  |  |  | Barcode read-ability | 32pcs/incoming lot | SR-2000 | Pass |
|  |  |  | Solder-ability | 3pcs/incoming lot | Dipping | Pass |
|  |  |  | Plating thickness | 32pcs/incoming lot | XRF | Pass |
| PI Bare Flex | Avary | 821-05769-02 | Cosmetic | AQL 0.4/incoming lot | CCD | Pass |
|  |  |  | Dimension | 32pcs/incoming lot | OMM | Pass |
|  |  |  | Barcode read-ability | 32pcs/incoming lot | SR-2000 | Pass |
|  |  |  | Solder-ability | 3pcs/incoming lot | Dipping | Pass |
|  |  |  | Plating thickness | 32pcs/incoming lot | XRF | Pass |
| Connector | muRata | 516S01290 | Cosmetic | AQL 0.4/Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Reel | OMM | Pass |
|  |  |  | Coplanarity & warpage | 32pcs/incoming lot | OMM | Pass |
|  |  |  | Plating thickness | 32pcs/incoming lot | XRF | Pass |
|  |  |  | Solder-ability | 5pcs/incoming lot | Dipping | Pass |
| MIC | IFX | 731-00334 | Cosmetic | AQL 0.4/Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Per dimension | OMM | Pass |
|  |  |  | Solder-ability | 5pcs/per vendor | Dipping | Pass |
|  |  |  | Plating thickness | 32pcs/per vendor | XRF | Pass |
| MIC | GTK | 731-00337 | Cosmetic | AQL 0.4/Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Per dimension | OMM | Pass |
|  |  |  | Solder-ability | 5pcs/per vendor | Dipping | Pass |
|  |  |  | Plating thickness | 32pcs/per vendor | XRF | Pass |

3. IQC Summary and Highlight | V53 UAT1
Pass
Fail
Waived

## Slide 22

| Component type | Supplier | APN | Chekcing items | Sampling size | Methology | Result |
|---|---|---|---|---|---|---|
| MIC | IFX | 731-00334 | Cosmetic | AQL 0.4/Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Per dimension | OMM | Pass |
|  |  |  | Solder-ability | 5pcs/per vendor | Dipping | Pass |
|  |  |  | Plating thickness | 32pcs/per vendor | XRF | Pass |
| IC | Qorvo | 353S03267 353S03284 353S03594 | Cosmetic | AQL 0.4/Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Reel | OMM | Pass |
| IC | Psemi | 353S03304 353S03654 | Cosmetic | AQL 0.4/Reel | CCD | Pass |
|  |  |  | Dimension | 32pcs/Reel | OMM | Pass |
| PSA | HB SGN | No APN | Cosmetic | 5pcs/incoming lot | CCD | Pass |
|  |  |  | Dimension | 32pcs/incoming lot | OMM | Pass |
|  |  |  | Thickness | 32pcs/incoming lot | OMM | Pass |
|  |  |  | Single pcs pre-peel test | 10pcs/incoming lot | Manual | Pass |
|  |  |  | Peeling strength | 5pcs/adhesive lot | Pull tester | Pass |
|  |  |  | Composition | 3pcs/die cut lot | FTIR | Pass |

3. IQC Summary and Highlight | V53 UAT1
Pass
Fail
Waived

## Slide 23
V53 UAT1 LCP bare flex all outline dimension CPK can meet target 1.33.
3. IQC Summary and Highlight | V53 UAT1

| V53 UAT1 LCP bare flex outline dimension CPK |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| Bare flex | Dimension |  | POR |  | Dimension |  | DOE |  |
|  |  |  | AMP | muRata |  |  | AMP | muRata |
| muRata | FAI1 | 26.745±0.05 | 2.07 | 2.71 | FAI1 | 26.745±0.05 | 3.88 | 4.21 |
|  | FAI2 | 24.413±0.05 | 2.20 | 2.48 | FAI2 | 24.413±0.05 | 2.63 | 2.92 |
|  | FAI3 | 23.155±0.05 | 2.97 | 3.60 | FAI3 | 23.155±0.05 | 4.86 | 6.62 |
|  | FAI4 | 1.956±0.05 | 6.82 | 6.28 | FAI4 | 1.956±0.05 | 6.19 | 6.17 |
|  | FAI5 | 15.796±0.05 | 2.23 | 2.38 | FAI5 | 15.796±0.05 | 2.11 | 3.56 |
|  | FAI6 | 11.703±0.05 | 3.79 | 3.62 | FAI6 | 11.703±0.05 | 5.61 | 7.45 |
|  | FAI7 | 12.367±0.05 | 4.44 | 4.12 | FAI7 | 12.367±0.05 | 4.75 | 5.76 |
|  | FAI8 | 1.260±0.075 | 1.89 | 2.06 | FAI8 | 1.260±0.075 | 3.04 | 2.44 |
|  | FAI9 | 2.095±0.075 | 3.96 | 4.67 | FAI9 | 2.095±0.075 | 2.40 | 3.66 |
|  | FAI10 | 10.271±0.05 | 1.88 | 2.23 | FAI10 | 10.271±0.05 | 2.17 | 2.79 |
|  | FAI11 | 12.113±0.05 | 2.70 | 2.13 | FAI11 | 12.113±0.05 | 2.85 | 4.34 |
|  | FAI12 | 16.005±0.05 | 3.16 | 2.63 | FAI12 | 16.005±0.05 | 2.22 | 3.13 |
|  | FAI13 | 13.799±0.05 | 1.93 | 1.89 | FAI13 | 13.799±0.05 | 1.88 | 2.41 |
|  | FAI14 | 14.122±0.05 | 2.07 | 1.88 | FAI14 | 14.122±0.05 | 1.70 | 1.89 |
|  | FAI15 | 3.200±0.05 | 3.40 | 5.07 | FAI15 | 3.200±0.05 | 3.67 | 4.24 |
|  | FAI16 | 1.000±0.05 | 5.19 | 5.46 | FAI16 | 1.000±0.05 | 4.01 | 3.91 |
|  | FAI17 | 1.191±0.075 | 2.13 | 2.69 | FAI17 | 1.191±0.075 | 2.58 | 1.96 |
|  | FAI18 | 3.047±0.075 | 1.71 | 1.86 | FAI18 | 3.047±0.075 | 1.74 | 1.68 |
|  | FAI19 | 2.848±0.05 | 3.09 | 3.08 | FAI19 | 2.848±0.05 | 3.94 | 3.01 |
|  | FAI20 | 6.384±0.05 | 4.29 | 5.83 | FAI20 | 6.384±0.05 | 4.24 | 4.50 |
|  | FAI21 | 1.878±0.075 | 2.01 | 2.34 | FAI21 | 1.878±0.075 | 1.76 | 1.68 |
|  | FAI22 | 5.662±0.075 | 2.31 | 3.34 | FAI22 | 5.662±0.075 | 2.29 | 1.78 |
|  | FAI23 | 20.702±0.05 | 3.99 | 3.89 | FAI23 | 20.702±0.05 | 2.71 | 2.56 |
|  | FAI24 | 17.224±0.05 | 2.79 | 3.17 | FAI24 | 17.224±0.05 | 2.73 | 3.38 |
|  | FAI25 | 2.901±0.05 | 3.80 | 3.48 | FAI25 | 2.901±0.05 | 2.63 | 2.89 |
|  | FAI26 | 8.176±0.05 | 3.42 | 4.29 | FAI26 | 8.176±0.05 | 3.52 | 3.29 |
|  | FAI27 | 7.707±0.05 | 2.09 | 1.71 | FAI27 | 7.707±0.05 | 2.09 | 1.70 |
|  | FAI28 | 1.966±0.075 | 2.67 | 2.52 | FAI28 | 1.966±0.075 | 2.21 | 1.79 |
|  | FAI29 | 7.837±0.05 | 4.11 | 4.65 | FAI29 | 7.837±0.05 | 3.42 | 3.52 |
|  | FAI30 | 1.822±0.075 | 1.88 | 2.39 | FAI30 | 1.822±0.075 | 1.71 | 1.75 |
|  | FAI31 | 1.375±0.05 | 1.84 | 2.44 | FAI31 | 1.375±0.05 | 1.73 | 1.81 |
|  | FAI32 | 1.225±0.05 | 2.11 | 2.98 | FAI32 | 1.225±0.05 | 2.23 | 1.81 |


## Slide 24
V53 UAT1 Strobe Tail all outline dimension CPK can meet target 1.33.
3. IQC Summary and Highlight | V53 UAT1

| V53 UAT1 Strobe Tail outline dimension CPK |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Bare flex | Dimension |  | POR |  | POR |  |
|  |  |  | AMP | Mflex | AMP | Avary |
| Mflex Avary | FAI01 | 4.150±0.05 | 4.59 | 5.37 | 5.67 | 6.35 |
|  | FAI02 | 1.375±0.05 | 2.73 | 2.27 | 1.95 | 2.42 |
|  | FAI03 | 1.050±0.075 | 2.24 | 1.80 | 3.60 | 3.49 |
|  | FAI04 | 12.181±0.05 | 1.46 | 1.39 | 2.20 | 3.28 |
|  | FAI05 | 6.647±0.05 | 2.41 | 2.06 | 1.75 | 2.35 |
|  | FAI06 | 16.329±0.05 | 2.56 | 2.12 | 3.23 | 2.70 |
|  | FAI07 | 135°±1° | 2.07 | 1.93 | 2.92 | 2.87 |
|  | FAI08 | 5.370±0.05 | 5.10 | 5.85 | 4.55 | 6.40 |


## Slide 25
3. IQC Summary and Highlight | V53 UAT1 PSA adhesive Data Collection
Total PSA*5 from 2 die cut vendors
PSA2/PSA3/PSA4/PSA5/PSA7 liner peeling force all in spec

## Slide 26
3. IQC Summary and Highlight | V53 UAT1 PSA liner Data Collection
Total PSA*5 from 2 die cut vendors
PSA2/PSA3/PSA4/PSA5/PSA7 adhesive peeling force all in spec

## Slide 27
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

## Slide 28
UV Glue
(TOP)
1st reflow
(BOT)
Pre-SMT
(BOT)
2nd reflow
(TOP)
Clean booth
4. Flex Yield Trend and Top Issues Breakdown | V53 UAT1 Flow Chart

## Slide 29
Bonding
Backend
Clean booth
Pre-SMT
Strobe flex
4. Flex Yield Trend and Top Issues Breakdown | V53 UAT1 Flow Chart

## Slide 30
4. Flex Yield Trend and Top Issues Breakdown | V53 UAT1/Bonding

## Slide 31
4. Flex Yield Trend and Top Issues Breakdown | V53 UAT1 BE

## Slide 32
4. Flex Yield Trend and Top Issues Breakdown | V53 UAT1 Overall

## Slide 33
4. Flex Yield Trend and Overall Breakdown - V53 UAT1
Others Details breakdown

| Config | Failure mode | Quantity | FR | Accu FR | Remark |
|---|---|---|---|---|---|
| X06P2-U1-MAYG2-SA-GEN X06P2-U1-MANG3-SM X06P2-U1-MAYA6-SA X06P2-U1-MAYA7-SM X06P2-U1-MAYX4-SM X06P2-U1-MANG3-SM-D1 X06P2-U1-MANA7-SA-D1 X06P2-U1-MANX4-SM-D1 | SPI -B Solder OOS | 9 | 0.11% | 85.42% | solder Print issue |
| X06P2-U1-MAYA6-SA-D1 | SPI-T Solder OOS | 2 | 0.02% | 85.83% | solder Print issue |
| X06P2-U1-MAYA7-SM X06P2-U1-MAYX4-SM | OQC X-ray low coverage | 3 | 0.04% | 87.08% | UAT1 P&P issue |
| X06P2-U1-MANG3-SM | X-ray low coverage | 1 | 0.01% | 87.50% | UAT1 P&P issue |
| X06P2-U1-MAYX4-SM X06P2-U1-MAYA6-SA-D1 X06P2-U1-MANG3-SM-D1 | Post AOI-T clip shift | 3 | 0.04% | 88.75% | P&P issue |
| X06P2-U1-MANG3-SM X06P2-U1-MAYA7-SM | Post AOI-B clip shift | 2 | 0.02% | 89.58% | Loading FPC issue |
| X06P2-U1-MAYG2-SA-GEN | Clip deformation | 4 | 0.05% | 91.25% | Handling issue |
| X06P2-U1-MAYG2-SA-GEN | inline sensitivity NTF | 2 | 0.02% | 92.08% | NTF |
| X06P2-U1-MAYA6-SA | Inline sensitivity True fail | 1 | 0.01% | 92.50% | Raw material issue |
| X06P2-U1-MANG3-SM X06P2-U1-MAYA7-SM X06P2-U1-MANG3-SM-D1 X06P2-U1-MANA7-SA-D1 | inline VSWR NTF | 6 | 0.07% | 95.00% | Handling issue |
| X06P2-U1-MAYG2-SA-GEN X06P2-U1-MANG3-SM X06P2-U1-MAYA6-SA | OQC MIC NTF | 5 | 0.06% | 97.08% | NTF |
| X06P2-U1-MAYG2-SA-GEN X06P2-U1-MAYA6-SA | OQC VSWR NTF | 3 | 0.04% | 98.33% | NTF |
| X06P2-U1-MANG3-SM X06P2-U1-MAYA6-SA X06P2-U1-MAYA7-SM X06P2-U1-MAYX4-SM | OQC ICT NTF | 4 | 0.05% | 100.00% | NTF |


## Slide 34
4. Flex Yield Trend and Top Issues Breakdown - V53 UAT1- by Config

## Slide 35: 4. Failure FACA | V53 UAT1-SMT

| Component | FPC | Vendor | AMP | APN | 632-07540 | Failure process / station | SMT VI |
|---|---|---|---|---|---|---|---|
| Issue Description | Bonding solder ball FR:  129F/8,300T=1.55%  FR for Config: |  |  |  |  |  |  |
| FA | Root cause: Strobe LPI thickness issue. Normal LPI thickness (19+/-5um) 1.Check the SPI, SBI, Bonding AOI, Bonding Jig, no abnormal. 2:Check the failure sample. The solder ball was concentrated around pad 26 2.Cross-section analysis; Pic-1 2.1. Strobe (Avary) LPI thickness <14 μm. lower than the normal thickness 2.2. Avary P1 LPI Thickness= 16~18 μm, MFLEX P2 LPI thickness = 14~20um.  No solder ballIssue. Failure mode analysis: The thickness of LPI is too thin and cause the solder ball issue.  When comparing the solder coverage data of the Mflex config, it was found that even the solder mask thickness meet 19+/-5um, the coverage of some pads is still above 100%.  The current solder jetting parameter is 4Dots. The coverage:85%~110%(solder mask thickness:28~32um) Pic-2 DOE validation optimized solder jetting from 4 Dots to 3 Dots and collected coverage data: 67% to 85%. Pic-3 Marginal pass. Simulation calculation, it is found that the current bonding pad size has a critical value.  4-dots solder jetting, coverage: 75%-128% (risk for solder ball); Pic-4 3-dots solder jetting, coverage: 56%-96%   (risk for low coverage); Pic-5 according to simulation calculation.  with 3Dots solder jetting parameters, optimize pad 26 size from  LCP flex: 0.2*2.32 (PI: 0.3*2.42) to LCP flex: 0.2*2.1 (PI: 0.3*2.2).  It can meet coverage in 75% to 95%; Pic-6 |  |  |  |  |  |  |

4. Failure FACA | V53 UAT1-SMT

| No. | Config | F/R | No. | Config | F/R |
|---|---|---|---|---|---|
| 1 | X06P2-U1-MAYG2-SA | 42F/1,020T=4.1% | 6 | X06P2-U1-MAYA6-SA-D1 | 25F/700T=3.6% |
| 2 | X06P2-U1-MANG3-SM | 0F/1,020T=0% | 7 | X06P2-U1-MANG3-SM-D1 | 0F/700T=0% |
| 3 | X06P2-U1-MAYA6-SA | 39F/1,020T=3.8% | 8 | X06P2-U1-MANA7-SA-D1 | 23F/700T=3.3% |
| 4 | X06P2-U1-MAYA7-SM | 0F/1,020T=0% | 9 | X06P2-U1-MANX4-SM-D1 | 0F/700T=0% |
| 5 | X06P2-U1-MAYX4-SM | 0F/1,020T=0% | 10 | X06P2-U1-MANG2-SM-D1-AB1 | 0F/400T=0% |

Schematic diagram of cross section

## Slide 36: 4. Failure FACA | V53 UAT1-SMT

| Component | FPC | Vendor | AMP | APN | 632-07540 | Failure process / station | SMT VI |
|---|---|---|---|---|---|---|---|
| Issue Description | Bonding solder ball FR:  129F/8,300T=1.55% FR for Config: |  |  |  |  |  |  |
| CA | Improve action: 1. Continue to work with DFM/SQE/Flex vendor to control LPI thickness within 19+/-5um. Currently Flex vendor feedback can provide improve sample in EVT build.Pic-1.Pic-2 2. Change solder dispensing parameter from 4dots to 3dots. And proposal to optimized pad 26 size from LCP flex: 0.2*2.32 (PI: 0.3*2.42) to LCP flex: 0.2*2.1 (PI: 0.3*2.2). |  |  |  |  |  |  |
| Validation | Keep monitor at EVT build. DRI: Xianhui Chen. CP: 2/28 |  |  |  |  |  |  |

4. Failure FACA | V53 UAT1-SMT

| No. | Config | F/R | No. | Config | F/R |
|---|---|---|---|---|---|
| 1 | X06P2-U1-MAYG2-SA | 42F/1,020T=4.1% | 6 | X06P2-U1-MAYA6-SA-D1 | 25F/700T=3.6% |
| 2 | X06P2-U1-MANG3-SM | 0F/1,020T=0% | 7 | X06P2-U1-MANG3-SM-D1 | 0F/700T=0% |
| 3 | X06P2-U1-MAYA6-SA | 39F/1,020T=3.8% | 8 | X06P2-U1-MANA7-SA-D1 | 23F/700T=3.3% |
| 4 | X06P2-U1-MAYA7-SM | 0F/1,020T=0% | 9 | X06P2-U1-MANX4-SM-D1 | 0F/700T=0% |
| 5 | X06P2-U1-MAYX4-SM | 0F/1,020T=0% | 10 | X06P2-U1-MANG2-SM-D1-AB1 | 0F/400T=0% |


## Slide 37: 4. Failure FACA | V53 UAT1-SMT

| Component | FPC | Vendor | AMP | APN | 632-07540 | Failure process / station | SMT VI |
|---|---|---|---|---|---|---|---|
| Issue Description | Bonding solder ball FR:  129F/8,300T=1.55%  (tracking: 0F/3,140T=0%) FR for Config: |  |  |  |  |  |  |
| FA | Root cause: Strobe Ink issue 1.Check the distribution of failure samples, The failure samples are concentrated in 12 panels, The solder balls are distributed at pad 26. Pic1&Pic2 2. Check the SPI Data, no abnormal.Pic3 3.Check the SBI Data, no abnormal.Pic4 5.Check the Bonding Strobe Flex AOI, no abnormal.Pic5 6.Check the Bonding UAT1 AOI, no abnormal.Pic6 7.Check the elasticity data of the Bonding JIG, no abnormal.Pic7 8.The solder paste stability test: The amplitude of the solder paste at a single point is 32%, no abnormal.Pic8 |  |  |  |  |  |  |

4. Failure FACA | V53 UAT1-SMT

| No. | Config | F/R | No. | Config | F/R |
|---|---|---|---|---|---|
| 1 | X06P2-U1-MAYG2-SA | 42F/1,020T=4.1% | 6 | X06P2-U1-MAYA6-SA-D1 | 25F/700T=3.6% |
| 2 | X06P2-U1-MANG3-SM | 0F/1,020T=0% | 7 | X06P2-U1-MANG3-SM-D1 | 0F/700T=0% |
| 3 | X06P2-U1-MAYA6-SA | 39F/1,020T=3.8% | 8 | X06P2-U1-MANA7-SA-D1 | 23F/700T=3.3% |
| 4 | X06P2-U1-MAYA7-SM | 0F/1,020T=0% | 9 | X06P2-U1-MANX4-SM-D1 | 0F/700T=0% |
| 5 | X06P2-U1-MAYX4-SM | 0F/1,020T=0% | 10 | X06P2-U1-MANG2-SM-D1-AB1 | 0F/400T=0% |


## Slide 38
Bonding process
The solder paste of bonding pad was finished solder bump at UAT1 process
For bonding process, The size of the solder joint is closely related to the thickness of the solder mask. Thicker solder mask will result in low coverage.
The thinner solder mask will cause excess solder paste to be squeezed out, caused solder ball issue.
OK parts
solder ball sample
Low coverage sample

## Slide 39

| Pad 26 | Solder paste volume | Metal composition volume |
|---|---|---|
| average | 0.0317285 | 0.01586425 |
| max | 0.036512842 | 0.018256421 |
| min | 0.027125215 | 0.013562607 |

Bonding issue analysis and simulation

## Slide 40: 4. Failure FACA | V53 UAT1-SMT

| Component | FPC | Vendor | AMP | APN | 632-07540 | Failure process / station | SMT VI |
|---|---|---|---|---|---|---|---|
| Issue Description | UV Glue on CL-ANT-VERT-SP FR: 67F/8,300T=0.81%  (tracking: 0F/7,280T=0%) FR for Config: |  |  |  |  |  |  |
| FA | Root cause: Process issue.UV glue remains on the side of the dispensing nozzle during nozzle cleaning. the side wall of the nozzle was in contact with the clip during UV glue dispensing 1. Check the defective product under violet light to confirm that the clip is UV glue. 2. Check the Dispensing Height distance: The safe distance for dispensing is 0.63 mm, this is no risk.  Pic5 3. Check the Nozzle: UV glue was found on the nozzle side.  Pic6 4. Check the dispensing nozzle clean: When cleaning the nozzle, there is a risk of UV glue sticking to the side of the nozzle. Pic7 5. Check the glue path: The distance from both the starting position and the ending position of dispensing UV glue to the CLIP is 0.85mm;  When the distance between the nozzle and the CLIP is 0.75mm, the nozzle side will make contact with the CLIP.  Pic8-9 |  |  |  |  |  |  |
| CA | Short term: 1.Optimize the dispensing coordinates. Move the dispensing coordinates 0.25 mm to the left and  increase the distance from the CLIP to 1.1mm. Pic 10 2.Tracking 7,280pcs FR:0F/7,280T=0%  Long term: Add the issue to Lesson Learned, The distance from the dispensing coordinates to the CLIP   should be greater than 1.0 mm. |  |  |  |  |  |  |
| Validation | FR: 0F/7,280T=0.0% |  |  |  |  |  |  |

4. Failure FACA | V53 UAT1-SMT
3.87mm

| No. | Config | F/R | No. | Config | F/R |
|---|---|---|---|---|---|
| 1 | X06P2-U1-MAYG2-SA | 67F/1,020T=6.6% | 6 | X06P2-U1-MAYA6-SA-D1 | 0F/700T=0% |
| 2 | X06P2-U1-MANG3-SM | 0F/1,020T=0% | 7 | X06P2-U1-MANG3-SM-D1 | 0F/700T=0% |
| 3 | X06P2-U1-MAYA6-SA | 0F/1,020T=0% | 8 | X06P2-U1-MANA7-SA-D1 | 0F/700T=0% |
| 4 | X06P2-U1-MAYA7-SM | 0F/1,020T=0% | 9 | X06P2-U1-MANX4-SM-D1 | 0F/700T=0% |
| 5 | X06P2-U1-MAYX4-SM | 0F/1,020T=0% | 10 | X06P2-U1-MANG2-SM-D1-AB1 | 0F/400T=0% |


## Slide 41: 4. Failure FACA | V53 UAT1-SMT

| Component | FPC | Vendor | AMP | APN | 632-07540 | Failure process / station | SMT VI |
|---|---|---|---|---|---|---|---|
| Issue Description | UV Glue on CL-ANT-VERT-SP FR: 67F/8,300T=0.81%  (tracking: 0F/7,280T=0%) FR for Config: |  |  |  |  |  |  |
| FA | Root cause: Process issue 1.Check the distribution of failure samples, The failure samples are concentrated in 3 panels.  Pic1 2. Check the defective product under violet light to confirm that the clip is UV glue.Pic2 3. Check dispensing parameters, dispensing height of 2.5mm, The running height is 4.0mm.Pic3 4. Check the CLIP Spec drawing, The Clip height is 3.84mm, Including the thickness of the solder paste, the height of the CLIP is 3.88 mm.Pic4 5. Measuring raw material data of clip: the measured value of CLIP is 3.87-3.91mm.Pic5 |  |  |  |  |  |  |

4. Failure FACA | V53 UAT1-SMT

| No. | Config | F/R | No. | Config | F/R |
|---|---|---|---|---|---|
| 1 | X06P2-U1-MAYG2-SA | 67F/1,020T=6.6% | 6 | X06P2-U1-MAYA6-SA-D1 | 0F/700T=0% |
| 2 | X06P2-U1-MANG3-SM | 0F/1,020T=0% | 7 | X06P2-U1-MANG3-SM-D1 | 0F/700T=0% |
| 3 | X06P2-U1-MAYA6-SA | 0F/1,020T=0% | 8 | X06P2-U1-MANA7-SA-D1 | 0F/700T=0% |
| 4 | X06P2-U1-MAYA7-SM | 0F/1,020T=0% | 9 | X06P2-U1-MANX4-SM-D1 | 0F/700T=0% |
| 5 | X06P2-U1-MAYX4-SM | 0F/1,020T=0% | 10 | X06P2-U1-MANG2-SM-D1-AB1 | 0F/400T=0% |


## Slide 42: 4. Failure FACA | V53 UAT1- Test

| Component | V53 UAT1 | Vendor | AMP | APN | 632-07540 | Failure process / station | Inline Sensitivity Station |
|---|---|---|---|---|---|---|---|
| Issue Description | Inline Sensitivity failure Fail Item: Sensitivity_N and Sensitivity_L Config：X06P2-U1-MAYA6-SA Rate：1F/979T=0.1% |  |  |  |  |  |  |
| FA | Root cause: MIC raw material issue, has contamination on inner EB film. 1. Checked the appearance of the product and MIC welding, and no abnormal is found.(Pic1) 2. Returned NG MIC to AAC for analysis, AAC results are shown below:    a) Cosmetic and 3D X-ray did not find any abnormal.    b) EB flatness check with flex : Pass    c) Retest MIC function without flex: fail    d) After remove EB, cosmetic check found contamination on EB inside.(Pic2)    e) Retest function without EB, result shown fail.    f) After de-cap lid, contamination stuck between membrane and back plate that caused MIC function fail. EDX result shown the contamination were related to environment. (Pic3) 3.AAC OQC retest plot is also added，which is aligned with AMP inline；both fail.(Pic4)   The reason for the pass of AAC original data is that the position of particle has changed during the process, which is the analysis provided by AAC. |  |  |  |  |  |  |

Pic4
4. Failure FACA | V53 UAT1- Test

## Slide 43: 4. Failure FACA | V53 UAT1- Test

| Component | V53 UAT1 | Vendor | AMP | APN | 632-07540 | Failure process / station | Inline Sensitivity Station |
|---|---|---|---|---|---|---|---|
| Issue Description | Inline Sensitivity failure Fail Item: Sensitivity_N and Sensitivity_L Config：X06P2-U1-MAYA6-SA Rate：1F/979T=0.1% |  |  |  |  |  |  |
| CA | Actions from AAC:    1. Keep regularly check all equipment cleaning and avoid Friction of equipment air tubes, wires.    2. Add clean frequency for MEMS suction nozzle from 1 time/shift to 1 time/lot.     3. Installation of ionizing nozzles on MEMS Die Bond machine. |  |  |  |  |  |  |
| Validation | Keep tracking in future build |  |  |  |  |  |  |

4. Failure FACA | V53 UAT1- Test

## Slide 44
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

## Slide 45
5. ORT | V53 UAT1

| Project | Config | Test | Cycle/Hour | Total Qty | Begin date | Due date | Status |
|---|---|---|---|---|---|---|---|
| V53 UAT1 | X06P2-U1-MAYG2-SA-GEN | Thermal cycling | 500 cycles | 45 | 12/10 | 1/8 | 400 cycles Pass, Next CP: 1/8 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 12/6 | 1/3 | Pass |
|  |  | Thermal shock | 200 cycles | 45 | 12/10 | 12/18 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 12/8 | 12/13 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 12/8 | 12/13 | Pass |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 12/17 | 12/22 | Pass |
|  | X06P2-U1-MANG3-SM | Thermal cycling | 500 cycles | 45 | 12/10 | 1/8 | 400 cycles Pass, Next CP: 1/8 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 12/6 | 1/3 | Pass |
|  |  | Thermal shock | 200 cycles | 45 | 12/10 | 12/18 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 12/8 | 12/13 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 12/8 | 12/13 | Pass |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 12/17 | 12/22 | Pass |


## Slide 46
5. ORT | V53 UAT1

| Project | Config | Test | Cycle/Hour | Total Qty | Begin date | Due date | Status |
|---|---|---|---|---|---|---|---|
| V53 UAT1 | X06P2-U1-MAYA6-SA | Thermal cycling | 500 cycles | 45 | 12/13 | 1/9 | 400 cycles Pass, Next CP: 1/9 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 12/9 | 1/8 | 400 cycles Pass, Next CP: 1/8 |
|  |  | Thermal shock | 200 cycles | 45 | 12/10 | 12/18 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 12/9 | 12/14 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 12/16 | 12/21 | Pass |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 12/17 | 12/22 | Pass |
|  | X06P2-U1-MAYA7-SM | Thermal cycling | 500 cycles | 45 | 12/13 | 1/9 | 400 cycles Pass, Next CP: 1/9 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 12/9 | 1/8 | 400 cycles Pass, Next CP: 1/8 |
|  |  | Thermal shock | 200 cycles | 45 | 12/10 | 12/18 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 12/9 | 12/14 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 12/16 | 12/21 | Pass |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 12/17 | 12/22 | Pass |


## Slide 47
5. ORT | V53 UAT1

| Project | Config | Test | Cycle/Hour | Total Qty | Begin date | Due date | Status |
|---|---|---|---|---|---|---|---|
| V53 UAT1 | X06P2-U1-MAYX4-SM | Thermal cycling | 500 cycles | 45 | 12/20 | 1/19 | 300 cycles Pass, Next CP: 1/19 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 12/17 | 1/14 | 400 cycles Pass, Next CP: 1/14 |
|  |  | Thermal shock | 200 cycles | 45 | 12/17 | 12/27 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 12/16 | 12/21 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 12/23 | 12/28 | Pass |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 12/27 | 1/1 | Pass |
|  | X06P2-U1-MAYA6-SA-D1 | Thermal cycling | 500 cycles | 45 | 12/20 | 1/19 | 300 cycles Pass, Next CP: 1/19 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 12/17 | 1/14 | 400 cycles Pass, Next CP: 1/14 |
|  |  | Thermal shock | 200 cycles | 45 | 12/17 | 12/27 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 12/16 | 12/21 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 12/23 | 12/28 | Pass |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 12/27 | 1/1 | Pass |


## Slide 48
5. ORT | V53 UAT1

| Project | Config | Test | Cycle/Hour | Total Qty | Begin date | Due date | Status |
|---|---|---|---|---|---|---|---|
| V53 UAT1 | X06P2-U1-MANG3-SM-D1 | Thermal cycling | 500 cycles | 45 | 12/20 | 1/19 | 200 cycles Pass, Next CP: 1/19 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 12/17 | 1/14 | 400 cycles Pass, Next CP: 1/14 |
|  |  | Thermal shock | 200 cycles | 45 | 12/17 | 12/27 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 12/16 | 12/21 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 12/23 | 12/28 | Pass |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 12/27 | 1/1 | Pass |
|  | X06P2-U1-MANA7-SA-D1 | Thermal cycling | 500 cycles | 45 | 12/22 | 1/19 | 200 cycles Pass, Next CP: 1/19 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 12/19 | 1/15 | 400 cycles Pass, Next CP: 1/15 |
|  |  | Thermal shock | 200 cycles | 45 | 12/25 | 1/3 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 12/19 | 12/24 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 12/30 | 1/3 | Pass |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 12/27 | 1/1 | Pass |


## Slide 49
5. ORT | V53 UAT1

| Project | Config | Test | Cycle/Hour | Total Qty | Begin date | Due date | Status |
|---|---|---|---|---|---|---|---|
| V53 UAT1 | X06P2-U1-MANX4-SM-D1 | Thermal cycling | 500 cycles | 45 | 12/20 | 1/19 | 200 cycles Pass, Next CP: 1/19 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 12/17 | 1/14 | 400 cycles Pass, Next CP: 1/14 |
|  |  | Thermal shock | 200 cycles | 45 | 12/17 | 12/27 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 12/16 | 12/21 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 12/23 | 12/28 | Pass |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 12/27 | 1/1 | Pass |
|  | X06P2-U1-MANG2-SM-D1-AB1 | Thermal cycling | 500 cycles | 45 | 12/22 | 1/19 | 200 cycles Pass, Next CP: 1/19 |
|  |  | Heat soak and recovery | 500 hrs | 45 | 12/19 | 1/15 | 400 cycles Pass, Next CP: 1/15 |
|  |  | Thermal shock | 200 cycles | 45 | 12/25 | 1/3 | Pass |
|  |  | Flex bending test | 25 cycles | 20 | 12/19 | 12/24 | Pass |
|  |  | Thermal Cycling and Flex Bending | 100 cycles+50 cycles | 20 | 12/30 | 1/3 | Pass |
|  |  | Heat Soak and Flex Bending | 168 hrs+50 cycles | 20 | 12/27 | 1/1 | Pass |

Remark
ORT test covered all configs, all items will be finished by 2025/01/19.

## Slide 50
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

## Slide 51

| Process/Station | Failure Description | Failure Rate | Root Cause | Corrective Action | DRI/ Due Date | Validation (Defect Rate%) |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

6. FATP/MI IQC, in-Line, ORT MIL and FACA | V53 UAT1
So far no feedback

## Slide 52
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

## Slide 53
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


## Slide 54

| Flex | Station | Coverage |
|---|---|---|
| V53 UAT1 | RF+ICT | 97.27% |

7. Function Test Coverage V53 UAT1
Yes
No

## Slide 55
Covered
Uncovered
7. Function Test Coverage | V53 UAT1

| Failure mode :Open |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B2B | Pin name | Test coverage | Pin name | Test coverage | Clip | Clip name | Test coverage | PAD |  | PAD name | Test coverage | Component | Component Name | Test coverage | Component Name | Test coverage | Component Name | Test coverage |
| JUAT1 | Pin1 | Y | Pin22 | Y | Clip | CL_ANT10_GND | Y | Strobe_Pad |  | PIN1 | Y | Components | R0401 | Y | U0303 | Y | MIC L0603 | Y |
|  | Pin2 | Y | Pin23 | Y |  | CL_ATN10_FEED | Y |  |  | PIN2 | Y |  | C0412 | Y | C0311 | Y | MIC C0600 | Y |
|  | Pin3 | Y | Pin24 | Y |  | CL_ANT2_Vert_SP | Y |  |  | PIN3 | Y |  | L0416 | Y | C0326 | Y | MIC L0600 | Y |
|  | Pin4 | Y | Pin25 | Y |  | CL_ANT2_short | Y |  |  | PIN4 | Y |  | C0415 | Y | L0301 | Y | MIC L0604 | Y |
|  | Pin5 | Y | Pin26 | Y |  | CL_ANT2_FEED | Y |  |  | PIN5 | Y |  | L0411 | Y | C0305 | Y | MIC L0607 | Y |
|  | Pin6 | Y | Pin27 | Y |  | PAD_GND_NORTH | Y |  |  | PIN6 | Y |  | U0400 | Y | C0309 | Y | MIC L0608 | Y |
|  | Pin7 | Y | Pin28 | Y |  | CL_JINDO_L | Y |  |  | PIN7 | Y |  | C0403 | Y | C0321 | Y | MIC L0605 | Y |
|  | Pin8 | Y | Pin29 | Y |  | CL_JINDO_M_TUNER | Y |  |  | PIN8 | Y |  | C0402 | Y | U0301 | Y | MIC L0606 | Y |
|  | Pin9 | Y | Pin30 | Y |  | CL_ANT2_GND | Y |  |  | PIN9 | Y |  | C0410 | Y | C0300 | Y | MIC U0601 | Y |
|  | Pin10 | Y | B2B STL | Y |  | CL_Strobe_GND | Y |  |  | PIN10 | Y |  | C0411 | Y | R0402 | Y |  |  |
|  | Pin11 | Y |  |  |  | CL_JINDO_M_GND | Y |  |  |  |  |  | L0413 | Y | L0310 | Y |  |  |
|  | Pin12 | Y |  |  |  | SUS Stiffener | Y |  |  |  |  |  | L0406 | Y | L0305 | Y |  |  |
|  | Pin13 | Y |  |  |  | SP_SPKR_POS | Y |  |  |  |  |  | R0200 | Y | L0307 | Y |  |  |
|  | Pin14 | Y |  |  |  | SP_SPKR_NEG | Y |  |  |  |  |  | C0418 | Y | C0322 | Y |  |  |
|  | Pin15 | Y |  |  |  |  |  |  |  |  |  |  | C0401 | Y | U0302 | Y |  |  |
|  | Pin16 | Y |  |  |  |  |  |  |  |  |  |  | C0400 | Y | R0303 | Y |  |  |
|  | Pin17 | Y |  |  |  |  |  |  |  |  |  |  | R0304 | Y | U0300 | Y |  |  |
|  | Pin18 | Y |  |  |  |  |  |  |  |  |  |  | C0302 | Y | C0324 | Y |  |  |
|  | Pin19 | Y |  |  |  |  |  |  |  |  |  |  | L0303 | Y | C0323 | Y |  |  |
|  | Pin20 | Y |  |  |  |  |  |  |  |  |  |  | C0327 | Y | MIC L0602 | Y |  |  |
|  | Pin21 | Y |  |  |  |  |  |  |  |  |  |  | C0306 | Y | MIC L0601 | Y |  |  |
| Failure mode :Short |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Description |  |  | Test coverage |  | Description |  |  |  | Test coverage |  |  | Description |  |  | Component Name |  | Test coverage |  |
| B2B adjacent GND pin short |  |  | N |  | B2B and bonding signal pads short to other adjacent pads |  |  |  | Y |  |  | Short two poles of 0ohm component |  |  | R0303 |  | N |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | R0304 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | R0401 |  |  |  |
| Bonding adjacent GND pads short |  |  | N |  |  |  |  |  |  |  |  |  |  |  | R0402 |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |


## Slide 56
Covered
Uncovered
7. Function Test Coverage | V53 UAT1 Mic

| Item | Failure mode | Sensitivity test | Summary |
|---|---|---|---|
| #1 | No tin on Mic signal pads | Y | Y |
| #2 | Short between signal and other pads | Y | Y |


## Slide 57
Covered
Uncovered
7. Function Test Coverage | | V53 UAT1 Mic

| Failure mode | Sensitivity test | Summary |
|---|---|---|
| Shatter EB membrane   (manually break) | N | N |

EB membrane has a dustproof effect, and damage does not affect sensitivity testing .

## Slide 58
7. Function Test Coverage | V53 UAT1 Mic

| Failure mode | Sensitivity test | Summary |
|---|---|---|
| Mic shielding case void(≥φ0.06mm) | N | N |

Covered
Uncovered

## Slide 59
Covered
Uncovered

| Failure mode | Sensitivity test | Summary |
|---|---|---|
| No tin on Mic signal pads | Y | Y |

7. Function Test Coverage | | V53 UAT1 Mic

## Slide 60
Covered
Uncovered

| Failure mode | Sensitivity test | Summary |
|---|---|---|
| Short between signal and other pads | Y | Y |

7. Function Test Coverage | | V53 UAT1 Mic

## Slide 61

| Station | Test item Q’ty | CPK<1.33 | 1.33<=CPK<1.67 | 1.67<=CPK<2.0 | CPK>=2.0 | Comments |
|---|---|---|---|---|---|---|
| V53 UAT1 | 5,030 | 0 | 0 | 0 | 5,030 | All CPK value are above 2.0 ,which means the spec we are using is a good balance between  limit and data. |

7. Function test CPK V53 UAT1
>2.00
<1.33
1.33~2.00

## Slide 62
7. Test Yield, Retest Rate

| Station | V53 UAT1 |  |  |
|---|---|---|---|
|  | Mic | RF | ICT |
| Input Q’ty | 8,081 | 8,078 | 8,072 |
| First Pass Yield  Target 97% | 99.12% | 98.89% | 99.24% |
| Final Yield | 99.96% | 99.93% | 100.00% |
| Retest Rate  Target 3% | 0.84% | 1.04% | 0.76% |

OK
NG

## Slide 63
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

## Slide 64
V53 | MCO CPK Summary | UAT1

| Flex | Project | Station | Total Qty | CPK<1.33 | 1.33<=CPK<1.67 | CPK>=1.67 |
|---|---|---|---|---|---|---|
| V53 UAT1 | Flex | FAI | 58 | 5 | 0 | 53 |
|  |  | SPC | 28 | 0 | 0 | 28 |

FAI225, Clip SMT dimension, refer to DFM.
FAI226, Clip SMT dimension, refer to DFM.
FAI229, Clip SMT dimension, refer to DFM.
FAI230, Clip SMT dimension, refer to DFM.
FAI233, Bonding dimension, refer to DFM.

## Slide 65
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

## Slide 66

| Flex | Test Item |  | Result | Remark |
|---|---|---|---|---|
| V53 UAT1 | X-ray | Clip | Pass | Max void is 12.29%. meet spec<35% |
|  |  | B2B | Pass | No void |
|  |  | IC | Pass | No void |
|  |  | Mic | Pass | Max void is 11.33%, meet spec<25% |
|  |  | Bonding | Pass | Max void is 26.51%, meet spec<35% |
|  |  | Bending | Pass | No micro crack. |
|  | Peeling Force | Clip | Pass | Min 5.33, meet spec >5N |
|  |  | B2B | Pass | Min 20.47N, meet spec >5N |
|  |  | Mic | Pass | Min 9.75, meet spec >4N |
|  |  | IC | Pass | Min 0.57N for data collection. |
|  |  | Bonding | Pass | Min 9.02, meet spec >5N |
|  | Shearing Force | Clip | Pass | Min 12.54N, meet spec  >5N. |
|  |  | Mic | Pass | Min 56.03N, meet spec  >4N. |
|  |  | IC | Pass | Min 6.42N for data collection. |
|  |  | Bonding | Pass | Min 36.47N, meet spec  >5N. |
|  | X-section | Clip | Pass | IMC: 1.16um-3.37um, meet spec (1-4um), soldring OK. |
|  |  | B2B | Pass | IMC: 1.05um-3.05um. meet spec (1-4um), soldring OK. |
|  |  | Mic | Pass | IMC: 1.58um-2.42um. meet spec (1-4um), soldring OK. |
|  |  | IC | Pass | IMC: 1.26um-2.95um. meet spec (1-4um), soldring OK. |
|  |  | Bonding | Pass | IMC: 1.16um-2.21um. meet spec (1-4um), soldring OK. |
|  |  | Bending | Pass | No micro crack. |

10. Data Collection Summary | V53 UAT1

## Slide 67
10. Data Collection Summary | V53 UAT1 - Clip Peeling Force Summary
No obvious difference between configs and vendors.

## Slide 68
10. Data Collection Summary | V53 UAT1 - Clip Peeling Force Summary
No obvious difference between configs and vendors.

## Slide 69
10. Data Collection Summary | V53 UAT1 - Mic/B2B/Bonding Peeling Force Summary
Mic/B2B/Boding peeling force no obvious difference between configs and vendors.
(6) CL0205
ANT39 GND

## Slide 70
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

## Slide 71: 11. Assembly PFMEA  Top 5 | UAT1  
11. Assembly PFMEA  Top 5 | UAT1

| Process | Failure Mode | Failure Effects | Sev | Occ | Det | RPN | Current Design | Improved Design | Action Results |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | Sev | Occ | Det | RPN |
| Top Process | Clip Pollution Flux | Function Fail | 8 | 6 | 6 | 288 | Process: When the SUS is reflow twice, the Flux will remain on the carrier, and there is a risk of SUS contamination   Detection: - 100% inspection by VI | Process: Optimize the carrier, and the carrier is designed to avoid SUS；SUS do not contact with the carrier to reduce the risk.  Detection: -100% VI using CCD | 8 | 3 | 6 | 144 |
| Dispensing UV Glue | CLIP Over glue | Cosmetic fail | 7 | 6 | 5 | 210 | Process: The height of CL-ANT-VERT-SP is 3.84mm. The dispensing path is incorrect, and there is a risk of glue hanging  Detection: - 100% inspection by VI | Process: Optimize the parameters of the dispensing path. The running height of the nozzle is required to be at least 1mm higher than that of the CLI Detection: - 100% inspection by VI | 7 | 3 | 5 | 105 |
| Tape remove | Clip deformation | Cosmetic fail | 7 | 6 | 6 | 252 | Process: The remove tape cover is not tightly pressed on FPC. FPC will tilt upward during manual remove tape , which will cause the FPC deformation  Detection: -100% inspection by VI. | Process: 1.Optimize Mylar position to reserve support position for carrier 2.Use automation for tape removing station in EVT build.  Detection: -100% inspection by VI. | 7 | 3 | 6 | 126 |
| Bonding | Bonding solder open、low coverage | Function Fail | 8 | 6 | 6 | 288 | Process: Strobe plate thickness 0.15mm, the risk of deformation is very large; Bonding has the risk of solder open and low coverage  Detection: -100% inspection by X-ray. | Process: Optimize the carrier design and increase the precision limit around the Strobe.  Detection: -100% inspection by X-ray. | 8 | 3 | 6 | 144 |
| Testing | Clip deformation | Cosmetic fail | 6 | 5 | 8 | 240 | Process: Testing station manual loading& unloading step has the risk to cause clip deformation when misplacement.    Detection: -100% VI using CCD | Process: 1.Optimize the SOP, high light the risk to OP,    define a reasonable motion for flex picking&    placing. 2.Implement auto loading& unloading process to    avoid manual risk in EVT build.  Detection: -100% VI using CCD | 6 | 3 | 8 | 144 |


## Slide 72
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

## Slide 73
13. Flex Mishandling and Abuse Test Review – Test location instruction& Suggestion | V53 UAT1
Bend & Twist test location
Suggestion
Pressure test location
Total 7 locations, no abnormal
Total 11 locations, no abnormal.

## Slide 74

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 1 (Bending area) | Engineer | 45° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (10times) | 1 | 7 | 7 | 7 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 8 | 8 | 8 | N/A |
|  |  |  | 4 | 8 | 8 | 8 | N/A |
|  |  |  | 5 | 9 | 9 | 9 | N/A |
|  |  | 45° (test to fail or 50 times max.) | 1 | 30 | 30 | 30 | N/A |
|  |  |  | 2 | 35 | 35 | 35 | N/A |
|  |  |  | 3 | 30 | 30 | 30 | N/A |
|  |  |  | 4 | 30 | 30 | 30 | N/A |
|  |  |  | 5 | 35 | 35 | 35 | N/A |
|  |  | 90° (test to fail or 50 times max.) | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 7 | 7 | 7 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
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

## Slide 75

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 2 (Bending area) | Engineer | 45° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (10times) | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
|  |  |  | 4 | 7 | 7 | 7 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |
|  |  | 45° (test to fail or 50 times max.) | 1 | 35 | 35 | 35 | N/A |
|  |  |  | 2 | 30 | 30 | 30 | N/A |
|  |  |  | 3 | 35 | 35 | 35 | N/A |
|  |  |  | 4 | 30 | 30 | 30 | N/A |
|  |  |  | 5 | 30 | 30 | 30 | N/A |
|  |  | 90° (test to fail or 50 times max.) | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
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

## Slide 76

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 3 (Bending area) | Engineer | 45° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (10times) | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 7 | 7 | 7 | N/A |
|  |  |  | 3 | 8 | 8 | 8 | N/A |
|  |  |  | 4 | 8 | 8 | 8 | N/A |
|  |  |  | 5 | 6 | 6 | 6 | N/A |
|  |  | 45° (test to fail or 50 times max.) | 1 | 25 | 25 | 25 | N/A |
|  |  |  | 2 | 25 | 25 | 25 | N/A |
|  |  |  | 3 | 25 | 25 | 25 | N/A |
|  |  |  | 4 | 30 | 30 | 30 | N/A |
|  |  |  | 5 | 25 | 25 | 25 | N/A |
|  |  | 90° (test to fail or 50 times max.) | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 7 | 7 | 7 | N/A |
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

## Slide 77

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 4 (Bending area) | Engineer | 45° (10times) | 1 | OK | OK | OK | N/A |
|  |  |  | 2 | OK | OK | OK | N/A |
|  |  |  | 3 | OK | OK | OK | N/A |
|  |  |  | 4 | OK | OK | OK | N/A |
|  |  |  | 5 | OK | OK | OK | N/A |
|  |  | 90° (10times) | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
|  |  |  | 4 | 8 | 8 | 8 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |
|  |  | 45° (test to fail or 50 times max.) | 1 | 35 | 35 | 35 | N/A |
|  |  |  | 2 | 35 | 35 | 35 | N/A |
|  |  |  | 3 | 30 | 30 | 30 | N/A |
|  |  |  | 4 | 30 | 30 | 30 | N/A |
|  |  |  | 5 | 30 | 30 | 30 | N/A |
|  |  | 90° (test to fail or 50 times max.) | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
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

## Slide 78

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
|  |  |  | 3 | 30 | 30 | 30 | N/A |
|  |  |  | 4 | 30 | 30 | 30 | N/A |
|  |  |  | 5 | 35 | 35 | 35 | N/A |
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

## Slide 79

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

## Slide 80

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

## Slide 81
13. Flex Mishandling and Abuse Test Review - Twist Test | V53 UAT1

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 1 | Engineer | 45° | 1 | 7 | 7 | 7 | N/A |
|  |  |  | 2 | 7 | 7 | 7 | N/A |
|  |  |  | 3 | 6 | 6 | 6 | N/A |
|  |  |  | 4 | 8 | 8 | 8 | N/A |
|  |  |  | 5 | 6 | 6 | 6 | N/A |
| Location 2 |  |  | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 7 | 7 | 7 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
|  |  |  | 4 | 8 | 8 | 8 | N/A |
|  |  |  | 5 | 6 | 6 | 6 | N/A |
| Location 3 |  |  | 1 | 7 | 7 | 7 | N/A |
|  |  |  | 2 | 6 | 6 | 6 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
|  |  |  | 4 | 8 | 8 | 8 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |
| Location 4 |  |  | 1 | 7 | 7 | 7 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
|  |  |  | 4 | 6 | 6 | 6 | N/A |
|  |  |  | 5 | 7 | 7 | 7 | N/A |

Location1
Location2
Location3
Location4
Twist test location
Defects

## Slide 82

| Location | Test Condition |  | Sample | Cosmetic | X-ray | Function Test | Proposal |
|---|---|---|---|---|---|---|---|
| Location 5 | Engineer | 45° | 1 | 7 | 7 | 7 | N/A |
|  |  |  | 2 | 7 | 7 | 7 | N/A |
|  |  |  | 3 | 6 | 6 | 6 | N/A |
|  |  |  | 4 | 8 | 8 | 8 | N/A |
|  |  |  | 5 | 6 | 6 | 6 | N/A |
| Location 6 |  |  | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
|  |  |  | 4 | 7 | 7 | 7 | N/A |
|  |  |  | 5 | 8 | 8 | 8 | N/A |
| Location 7 |  |  | 1 | 8 | 8 | 8 | N/A |
|  |  |  | 2 | 8 | 8 | 8 | N/A |
|  |  |  | 3 | 7 | 7 | 7 | N/A |
|  |  |  | 4 | 7 | 7 | 7 | N/A |
|  |  |  | 5 | 8 | 8 | 8 | N/A |

Location5
Location6
Location7
Twist test location
Defects
13. Flex Mishandling and Abuse Test Review - Twist Test | V53 UAT1

## Slide 83

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

## Slide 84

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

## Slide 85

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

## Slide 86

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

## Slide 87

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

## Slide 88

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

## Slide 89

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
Location 7
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1

## Slide 90

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

## Slide 91

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
Location 9
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1

## Slide 92

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
Location 10
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1

## Slide 93

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
Location11(Bonding area)
Defects
High pressure(10 times)
Location 11
13. Flex Mishandling and Abuse Test Review – Pressure Test | V53 UAT1

## Slide 94
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

## Slide 95
V53 | Open DFM_P2 | UAT1

| Item | Flex | Drawing | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|---|
| 1 | V53 UAT1 | MCO 056-21672-16 | FAI low CPK | FAI 225 / 226 CPK < 1.67 due to tightened tolerance ±0.05mm. | Release tolerance from ±0.05 to ±0.10mm. | Open for EVT |
| 2 | V53 UAT1 | MCO 056-21672-16 | FAI low CPK | FAI 229 / 230 CPK < 1.67 due to tightened tolerance ±0.05mm. | Release tolerance from ±0.05 to ±0.10mm. | Open for EVT |
| 3 | V53 UAT1 | MCO 056-21672-16 | FAI low CPK | FAI 233 CPK < 1.67 due to tightened tolerance ±0.10mm. | Release tolerance from ±0.10 to ±0.20mm. | Open for EVT |
| 4 | V53 UAT1 | MCO 056-21672-16 | Clip Encap | CL_ANT10_FEED Clip Peeling force increased only 1N by adding Encap glue. Still similar as P1 and still has risk of peel off. | Option-1: Enlarge Clip pad from 1.78 to 2.78mm (Remove Encap glue).  Option-2: Change Clip pad design to make Clip arm on top layer. | Open for EVT |
| 5 | V53 UAT1 | MCO 056-21672-16 | Clip Encap | CL_ANT_VERT_SP Clip  Peeling force increased only 1N by adding Encap glue around Clip pad. Risk of peel off again. | Option-1: Enlarge Clip pad from 1.59 to 2.59mm (Remove Encap glue).  Option-2: Change Clip pad design to make Clip arm on top layer. | Open for EVT |
| 6 | V53 UAT1 | MCO 056-21672-16 | SUS Plating | SUS Stiffener has Ni plated on both contact side and solder side.  Risk of CAN NOT identify it if solder side face up. | Change SUS Stiffener solder side plating from “Ni” to “Sn over Ni”. (Same as V54 UAT1) | Open for EVT |
| 7 | V53 UAT1 | MCO 056-21672-16 | PSA cost down | Current PSA has lower utilization rate of raw material in diecut process. Raw material utilization rate could be increased 50.0% when change PSA liner as proposed. | Change PSA liner tab position to upper side. | Open for EVT |
| 8 | V53 UAT1 | MCO 056-21672-16 | Solder ball | Solder ball issue in bonding area due to LPI thickness and Pad size. FR: 129F/8,300T=1.55%. (Focused on configs with Avary strobe flex) | Reduce UAT1 Pad length from 2.32 to 2.10mm. Reduce Strobe Pad length from 2.42 to 2.20mm. | Open for EVT |


## Slide 96
V53 | Open DFM_P2 | UAT1

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 1 | V53 UAT1 | MCO 056-21672-16 | FAI 225 / 226 CPK < 1.67 due to tightened tolerance ±0.05mm. | Release tolerance from ±0.05 to ±0.10mm. | Open for EVT |
|  |  |  |  |  |  |

Issue:
FAI 225 / 226 CPK < 1.67 due to tightened tolerance ±0.05mm.
Proposal:
Release tolerance from ±0.05 to ±0.10mm.
MCO 056-21672-16
PD waived for P2.
CPK < 1.67 with current ±0.05mm.
CPK > 1.67 with proposed ±0.10mm.

## Slide 97
V53 | Open DFM_P2 | UAT1

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 2 | V53 UAT1 | MCO 056-21672-16 | FAI 229 / 230 CPK < 1.67 due to tightened tolerance ±0.05mm. | Release tolerance from ±0.05 to ±0.10mm. | Open for EVT |
|  |  |  |  |  |  |

Issue:
FAI 229 / 230 CPK < 1.67 due to tightened tolerance ±0.05mm.
Proposal:
Release tolerance from ±0.05 to ±0.10mm.
MCO 056-21672-16
PD waived for P2.
CPK < 1.67 with current ±0.05mm.
CPK > 1.67 with proposed ±0.10mm.

## Slide 98
V53 | Open DFM_P2 | UAT1

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 3 | V53 UAT1 | MCO 056-21672-16 | FAI 233 CPK < 1.67 due to tightened tolerance ±0.10mm. | Release tolerance from ±0.10 to ±0.20mm. | Open for EVT |
|  |  |  |  |  |  |

Issue:
FAI 233 CPK < 1.67 due to tightened tolerance ±0.10mm.
Proposal:
Release tolerance from ±0.10 to ±0.20mm.
MCO 056-21672-16
D47 UAT2 for reference
Bonding tolerance ±0.20mm
PD waived for P2.
CPK < 1.67 with current ±0.10mm.
CPK > 1.67 with proposed ±0.20mm.
V54 UAT1 for reference
Bonding tolerance ±0.20mm

| FAI233 CPK by config |  |  |  |  |  |
|---|---|---|---|---|---|
| Tolerance | 1 | 2 | 3 | 4 | 5 |
| ±0.10 | 1.092 | 1.030 | 1.061 | 1.080 | 0.947 |
| ±0.15 | 1.670 | 1.556 | 1.657 | 1.636 | 1.494 |
| ±0.20 | 2.248 | 2.082 | 2.253 | 2.193 | 2.041 |

More data collection:

## Slide 99

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 4 | V53 UAT1 | MCO 056-21672-16 | CL_ANT10_FEED Clip Peeling force increased only 1N by adding Encap glue. Still similar as P1 and still has risk of peel off. | Option-1: Enlarge Clip pad from 1.78 to 2.78mm (Remove Encap glue).  Option-2: Change Clip pad design to make Clip arm on top layer. | Open for EVT |
|  |  |  |  |  |  |

V53 | Open DFM_P2 | UAT1
Issue:
CL_ANT10_FEED Clip Peeling force increased only 1N by adding Encap glue. Still similar as P1 and still has risk of peel off.
Proposal:
Option-1: Enlarge Clip pad from 1.78 to 2.78mm. (Remove Encap glue, also cost down)
Option-2: Change Clip pad design to make Clip arm on top layer.

|  | Peeling force / N |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Config | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Min | Max | Ave | Difference |
| P1 W/O Encap | 6.07 | 5.88 | 5.82 | 5.29 | 6.03 | 5.59 | 5.50 | 5.67 | 5.74 | 5.99 | 5.29 | 6.07 | 5.76 | - |
| P2 W/O Encap | 5.92 | 6.29 | 5.95 | 5.92 | 5.74 | 5.91 | 5.95 | 5.40 | 5.96 | 5.89 | 5.40 | 6.29 | 5.89 | Same as P1 |
| P2 W/    Encap | 6.94 | 6.41 | 7.37 | 6.84 | 7.05 | 7.53 | 7.44 | 6.18 | 7.35 | 6.41 | 6.18 | 7.53 | 6.95 | 1.06N ↑ |

Encap increased only 1N Peeling force.
Risk of  Clip peel off again.
CL_ANT10_FEED Clip
W/ Encap glue
W/O Encap glue
Peeling force 1N ↑ with Encap around Clip pad.
2.65

## Slide 100
V53 | Open DFM_P2 | UAT1

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 5 | V53 UAT1 | MCO 056-21672-16 | CL_ANT_VERT_SP Clip  Peeling force increased only 1N by adding Encap glue around Clip pad. Risk of peel off again. | Option-1: Enlarge Clip pad from 1.59 to 2.59mm (Remove Encap glue).  Option-2: Change Clip pad design to make Clip arm on top layer. | Open for EVT |
|  |  |  |  |  |  |

Issue:
CL_ANT_VERT_SP Clip Peeling force increased only 1N by adding Encap glue around Clip pad. Risk of peel off again.
Proposal:
Option-1: Enlarge Clip pad from 1.59 to 2.59mm. (Remove Encap glue, also cost down)
Option-2: Change Clip pad design to make Clip arm on top layer.

|  | Peeling force / N |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Config | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Min | Max | Ave | Difference |
| P1 W/O Encap | 6.64 | 6.14 | 5.33 | 5.82 | 5.22 | 7.80 | 6.95 | 5.45 | 7.56 | 5.45 | 5.22 | 7.80 | 6.24 | - |
| P2 W/O Encap | 7.68 | 9.91 | 9.58 | 10.02 | 9.66 | 8.44 | 9.28 | 8.50 | 8.44 | 10.23 | 7.68 | 10.23 | 9.17 | 2.93N ↑ |
| P2 W/    Encap | 11.58 | 11.55 | 11.09 | 10.64 | 9.00 | 11.18 | 10.00 | 8.81 | 11.71 | 10.17 | 8.81 | 11.71 | 10.57 | 1.40N ↑ |

Encap increased only 1N Peeling force.
Risk of  Clip peel off again.
CL_ANT_VERT_SP Clip
W/ Encap glue
W/O Encap glue
Peeling force 1N ↑ with Encap around Clip pad.

## Slide 101
V53 | Open DFM_P2 | UAT1

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 6 | V53 UAT1 | MCO 056-21672-16 | SUS Stiffener has Ni plated on both contact side and solder side.  Risk of CAN NOT identify it if solder side face up. | Change SUS Stiffener solder side plating from “Ni” to “Sn over Ni”. (Same as V54 UAT1) | Open for EVT |
|  |  |  |  |  |  |

Issue:
SUS Stiffener has Ni plated on both contact side and solder side. Risk of CAN NOT identify it if solder side face up.
Proposal:
Change SUS Stiffener solder side plating from Ni to Sn over Ni. (same as V54 UAT1)
SUS Stiffener

| Plating | Contact side: Ni / Solder side: Ni |  | Contact side: Ni / Solder side: Sn over Ni |  |
|---|---|---|---|---|
| DOE | POR Contact side face up | DOE Solder side face up | POR Contact side face up | DOE Solder side face up |
| Identified Picture (Pre-AOI) |  |  |  |  |
| DOE result | Can NOT identify if solder side face up. |  | Can identify if solder side face up. |  |

Solder side
Contact side
Contact side
Solder side

## Slide 102
V53 | Open DFM_P2 | UAT1

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 7 | V53 UAT1 | MCO 056-21672-16 | Current PSA has lower utilization rate of raw material in diecut process. Raw material utilization rate could be increased 50.0% when change PSA liner as proposed. | Change PSA liner tab position to upper side. | Open for EVT |
|  |  |  |  |  |  |

Issue:
Current PSA has lower utilization rate of raw material in diecut process.
Raw material utilization rate could be increased 50.0% when change PSA liner as proposed.
Proposal:
Change PSA liner tab position to upper side.
PSA Layout on carrier (2 rows)
PSA Layout on carrier (4 rows)
Raw material utilization rate 50.0% ↑
Current PSA liner
Proposed PSA liner

## Slide 103
V53 | Open DFM_P2 | UAT1

| Item | Flex | Category | Issue description | Suggestions | Status |
|---|---|---|---|---|---|
| 8 | V53 UAT1 | MCO 056-21672-16 | Solder ball issue in bonding area due to LPI thickness and Pad size. FR: 129F/8,300T=1.55%. (Focused on configs with Avary strobe flex) | Reduce UAT1 Pad length from 2.32 to 2.10mm. Reduce Strobe Pad length from 2.42 to 2.20mm. | Open for EVT |
|  |  |  |  |  |  |

Issue:
Solder ball issue in bonding area. FR: 129F/8,300T=1.55%.
Proposal:
Reduce UAT1 Pad length from 2.32 to 2.10mm.
Reduce Strobe Pad length from 2.42 to 2.20mm.
Failure focused on P2 Avary Flex:
LPI thickness < general spec 19±5um.
Failure also focused on narrow GND pad.

| Solder | Total LPI thickness / um | 28(14+14) | 32(16+16) | 38(19+19) | 42(21+21) | 48(24+24) |
|---|---|---|---|---|---|---|
| 4 dots | Solder volume / mm² | 0.021312 | 0.021312 | 0.021312 | 0.021312 | 0.021312 |
|  | Bonding volume / mm² | 0.01666 | 0.01904 | 0.02261 | 0.02499 | 0.02856 |
|  | Coverage | 127.92% | 111.93% | 94.26% | 85.28% | 74.62% |
| 3 dots | Solder volume / mm² | 0.015984 | 0.015984 | 0.015984 | 0.015984 | 0.015984 |
|  | Bonding volume / mm² | 0.01666 | 0.01904 | 0.02261 | 0.02499 | 0.02856 |
|  | Coverage | 95.94% | 83.95% | 70.69% | 63.96% | 55.97% |

Jetting 4 dots solder, when LPI thickness to be lower limit 14um,
risk of coverage > 100%, cause solder ball issue.
Jetting 3 dots solder, when LPI thickness to be upper limit 24um, risk of low solder coverage.

| Solder | UAT1  Pad size | Strobe Pad size | Total  LPI thickness | 28(14+14) | 32(16+16) | 38(19+19) | 42(21+21) | 48(24+24) |
|---|---|---|---|---|---|---|---|---|
| 3 dots | 0.20 * 2.32 | 0.30 * 2.42 | Bonding volume | 0.01666 | 0.01904 | 0.02261 | 0.02499 | 0.02856 |
|  |  |  | Coverage | 95.94% | 83.95% | 70.69% | 63.96% | 55.97% |
|  | 0.20 * 2.20 | 0.30 * 2.30 | Bonding volume | 0.01582 | 0.01808 | 0.02147 | 0.02373 | 0.02712 |
|  |  |  | Coverage | 101.04% | 88.41% | 74.45% | 67.36% | 58.94% |
|  | 0.20 * 2.10 | 0.30 * 2.20 | Bonding volume | 0.01512 | 0.01728 | 0.02052 | 0.02268 | 0.02592 |
|  |  |  | Coverage | 105.71% | 92.50% | 77.89% | 70.48% | 61.67% |
|  | 0.20 * 2.00 | 0.30 * 2.10 | Bonding volume | 0.01442 | 0.01648 | 0.01957 | 0.02163 | 0.02472 |
|  |  |  | Coverage | 110.85% | 96.99% | 81.68% | 73.90% | 64.66% |

Simulated calculation, suggest reduce pad size to: UAT1 0.20 * 2.10 & Strobe 0.30 * 2.20mm.
UAT1
0.20 * 2.32 → 0.20 * 2.10
Strobe
0.30 * 2.42 → 0.30 * 2.20