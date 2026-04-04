# [ICT] V53_P2_UAT1_Postmortem-V9_20250107_01.07.2025.pptx
**Total Slides:** 174

## Slide 1
V53 UAT1 P2 Postmortem
Luxshare ICT
01-09-2025

## Slide 2
V53 UAT1 P2 build Postmortem Dashboard
Low risk
Medium risk
High risk

**Table 1:**
| Postmortem Content | V53 UAT1 Flex |
| --- | --- |
| 1 O-Chart and resource plan |  |
| 2 Configs and Build status |  |
| 3 IQC | APN: 806-50871, vendor TLG, Failure in FAI 43 OOS,A customer waived. APN: 806-53763, vendor TLG, Failure in FAI 26 OOS,A customer waived. |
| 4 Process yield of bare flex and flex Assembly |  |
| 5 OQC Issue and ORT |  |
| 6 Downstream/Customer issue review |  |
| 7 Test review |  |
| 8 Flex stackup with 5x cross-section data |  |
| 9 Cp/Cpk histogram of FAI/SPC (32pcs) | FAI225/226/229/230 has risk of low CPK<1.67,A customer waived. FAI233-1/FAI233-2 has risk of low CPK<1.67,A customer waived. |
| 10 Data collection review |  |
| 11 DFMEA, PFMEA Top 5 issue update |  |
| 12 Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality | FAI225/226/229/230 has risk of low CPK<1.67,A customer waived. FAI233-1/FAI233-2 has risk of low CPK<1.67,A customer waived. |
| 13 DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction | Same as item12 |
| 14 Flex mishandling and abuse test review |  |
| 15 NPI Soft tool and MP hard tool report |  |
| 16 Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |  |
| 17 Lesson learn from last generation and this build |  |
| 18 EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |  |
| 19 Vendor owned MP material supplier POR |  |
| 20 MP Line Qual plan (update from EVT postmortem) |  |


## Slide 3

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 4
2. Configs - Design Highlight and Comparison
P1
P2

**Table 1:**
| Items | P1 design | P2: X06P2-U1-MIYG2-SM-GEN | P2: X06P2-U1-MIYG3-SM | P2: X06P2-U1-MINA7-SA | P2: X06P2-U1-MINA6-SA | P2: X06P2-U1-MIYG2-SA-D1 | P2: X06P2-U1-MINX4-SM-D1 | P2: X06P2-U1-MIYG3-SA-D1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FPC | 4layers | 4layers,Murata | Same | Same | Same | 4layers,DOE Murata | 4layers,DOE Murata | 4layers,DOE Murata |
| LCR | CAP*22,  IND*21,  RES*7 | CAP*22,  IND*18,  RES*5 | Same | Same | Same | CAP*22,  IND*19,  RES*6 | CAP*22,  IND*19,  RES*6 | CAP*22,  IND*19,  RES*6 |
| IC | U0300:353S03304 U0301:353S03610 U0302:353S03284 U0303:353S03594 U0400:353S04043 | U0300:353S03304 (Psemi) U0301:353S03654(Psemi) U0302:353S03284 (QORVO) U0303:353S03594 (QORVO) U0400:353S03267 (QORVO) | Same | Same | Same | U0300:353S03304 (Psemi)  U0301:353S03304 (Psemi) U0302:353S03284 (QORVO) U0303:353S03594 (QORVO) U0400:353S03267 (QORVO) | Same | Same |
| Clip | Clip*13 | Clip*12(LY) | Same | Clip*12(Ennovi) | Clip*12(Ennovi) | Same | Clip*12(Ennovi) | Same |
| Conn. | APN:516S01290 | APN:516S01290 | Same | Same | Same | Same | Same | Same |
| MIC | MIC*1, 731-00333 | MIC*1, GTK 731-00333 (R-G-Q-2) | MIC*1, GTK 731-00333 (R-G-Q-3) | MIC*1, AAC 731-00337 (R-A-Q-7) | MIC*1, AAC 731-00337 (R-A-Q-6) | Same | MIC*1, IFX 731-00334 (R-X-R-4) | MIC*1, GTK 731-00333 (R-G-Q-3) |
| PSA | PSA*5 | PSA*4 | Same | Same | Same | Same | Same | Same |
| MIC film | MIC  Film*1 | MIC  Film*1 | Same | Same | Same | Same | Same | Same |
| PI flex | Strobe tail, 3 layer | Strobe tail, 3 layer (Mflex) | Same | Strobe tail, 3 layer (Avary) | Strobe tail, 3 layer (Avary) | Strobe tail, 3 layer (Avary) | Same | Strobe tail, 3 layer (Avary) |
| 2D Barcode | 7.01*4mm,half adhesive | 7*4mm,half adhesive | Same | Same | Same | Same | Same | Same |
| Diﬀerence / picture |  |  |  |  |  |  | V53 UAT1 P1 VS V53 UAT1 P2 1. Outline is changed; 2. Layout change; 3. Clip changed; 4. UAT1 bonding PAD change; 5. Strobe tail outline change;   6. Strobe tail bonding pad change; 7.PSA material/shape change  8.PSA shape change 9.PSA/clip canceled in P2 10.2D Barcode change 11.Bend area change 12.UAT1 silkscreen location change 13.Add UV glue/clip  V53 P2 UAT1 POR VS DOE 1. Layout change; |  |


## Slide 5
2. V53 UAT1 P2 build status
Remark: P2 total shipment Q’ty 4,265pcs

**Table 1:**
| Config | Description | Bareflex | Assembly | Ship to | Shipment Qty | Build Status |  | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X06P2-U1-MIYG2-SM-GEN | 632-07540-04 | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 175 | Finish all shipment |  |  |
| X06P2-U1-MIYG3-SM | 821-05494-01 | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 900 | Finish all shipment |  |  |
| X06P2-U1-MINA7-SA |  | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 900 | Finish all shipment |  |  |
| X06P2-U1-MINA6-SA |  | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 900 | Finish all shipment |  |  |
| X06P2-U1-MINX4-SM-D1 | 932-05144-04 | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 490 | Finish all shipment |  |  |
| X06P2-U1-MIYG2-SA-D1 |  | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 450 | Finish all shipment |  |  |
| X06P2-U1-MIYG3-SA-D1 |  | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 450 | Finish all shipment |  |  |


## Slide 6

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 7
3.V53 UAT1 IQC Summary and Highlight Summary

**Table 1:**
| Item | Cosmetic | Dimension | Function/Characteristic | Package |
| --- | --- | --- | --- | --- |
| Bare Flex (both PI and LCP) |  |  |  |  |
| Clip |  | 1.APN: 806-50871, vendor TLG, FAI 43 OOS,A customer waived. 2.APN: 806-53763, vendor TLG, FAI 26 OOS,A customer waived. |  |  |
| PSA |  |  |  |  |
| B2B connector |  |  |  |  |
| Chip |  |  |  |  |
| IC |  |  |  |  |
| MIC |  |  |  |  |
| Packing Tray |  |  |  |  |


## Slide 8
3.V53 UAT1 IQC Summary and Highlight Summary

**Table 1:**
| Item | APN | Vendor | Waive item | Improve Action |
| --- | --- | --- | --- | --- |
| 1 | 806-50871 | TLG | FAI 43 OOS | Short term: A customer waived in P2 Long term: Vendor proposed to change the measurement position EVT build |
| 2 | 806-53763 | TLG | FAI 26 OOS | Short term: A customer waived in P2 Long term: Vendor proposed to from 0.0065 to 0.014 EVT Build |


## Slide 9
3.V53 UAT1 IQC Summary and Highlight
Pass
Fail

**Table 1:**
| Component type | Supplier | Sampling Size | Checking items | Methodology | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- |
| Bare Flex (both PI and LCP) | MURATA(LCP) Avary (PI) Mflex (PI) | AQL 0.4 | Cosmetic | CCD | Pass |  |
|  |  | 32pcs | Dimension-FAI | OMM | Pass |  |
|  |  | 32pcs | Dimension-SPC | OMM | Pass |  |
|  |  | 3pcs | Solderability | Solder Oven | Pass |  |
|  |  | 32pcs | Ni/Au Thickness | XRF | Pass |  |
|  |  | 32pcs | Barcode readability | 2DBC grade scanner | Pass |  |
|  |  | 3pcs | WCA | WCA Fixture | Pass |  |
| Clip | ENNOVI TLG ICT | AQL 0.4 | Cosmetic | CCD | Pass |  |
|  |  | 32pcs | Dimension-FAI | OMM | ENNOVI: Pass | A customer waived |
|  |  |  |  |  | 1.APN: 806-50871, FAI 43 OOS 2.APN: 806-53763, FAI 26 OOS |  |
|  |  | 32pcs | Dimension-SPC | OMM | Pass |  |
|  |  | 32pcs | Package | Caliper/OMM | Pass |  |
|  |  | 32pcs | Peeling test z direction | Dummy board | Pass |  |
|  |  | 10pcs | Solderability | Solder Oven | Pass |  |
|  |  | 32pcs | Plating thickness | XRF | Pass |  |
| PSA | JT DX | 5pcs | Cosmetic | CCD | Pass |  |
|  |  | 32pcs | Dimension-FAI | OMM | Pass |  |
|  |  | 32pcs | Dimension-SPC | OMM | Pass |  |
|  |  | 32pcs | Thickness | Micrometer | Pass |  |
|  |  | 10pcs | Single pcs Pre-Peel test | Manual | Pass |  |
|  |  | 5pcs | Peeling Strength on both liner/carrier side | Tension meter | Pass |  |
|  |  | 5pcs | Liner Peeling Strength | Tension meter | Pass |  |


## Slide 10
3.V53 UAT1 IQC Summary and Highlight
Pass
Fail

**Table 1:**
| Component type | Supplier | Sampling Size | Checking items | Methodology | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- |
| B2B connector | MURATA | AQL 0.4 | Cosmetic | CCD | Pass |  |
|  |  | 32pcs | Dimension-FAI | OMM | Pass |  |
|  |  | 32pcs | Dimension-SPC | OMM | Pass |  |
|  |  | 32pcs | Coplanarity & warpage (before & after reflow 2 times) | OMM | Pass |  |
|  |  | 32pcs | Plating Thickness | XRF | Pass |  |
|  |  | 5pcs | Solderability | Solder oven | Pass |  |
| IC | Qorvo Psemi Infineon | AQL 0.4 | Cosmetic | CCD | Pass |  |
|  |  | 32pcs | Plating thickness | XRF | Pass |  |
|  |  | 5pcs | Solderability | Solder Oven | Pass |  |
|  |  | 32pcs | Dimension-FAI | Caliper | Pass |  |
|  |  | 32pcs | Dimension-SPC | Caliper | Pass |  |
| Chip | MURATA TDK YAGEO Samsung TAIYO | 5pcs | Cosmetic | CCD | Pass |  |
|  |  | 32pcs | Dimension-SPC | Caliper | Pass |  |
|  |  | 32pcs | Dimension-FAI | Caliper | Pass |  |
|  |  | 10pcs | Solderability | Solder oven | Pass |  |
|  |  | 32pcs | Function | LCR | Pass |  |


## Slide 11
3.V53 UAT1 IQC Summary and Highlight
Pass
Fail

**Table 1:**
| Component type | Supplier | Sampling Size | Checking items | Methodology | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- |
| MIC | GMI AAC Infineon | 5pcs | Cosmetic | CCD | Pass |  |
| Shim | LS MARIAN | 5pcs | Dimension-FAI | OMM | Pass |  |
|  |  | 32pcs | Dimension-SPC | OMM | Pass |  |
|  |  | 32pcs | Thickness | Micrometer | Pass |  |
|  |  | 10pcs | Shear off & peeling test | Tension meter | Pass |  |
| Packing Tray | KD | AQL 0.4 | Cosmetic | CCD | Pass |  |
|  |  | 5pcs | ESD | lmpedancemeter | Pass |  |
|  |  | 5pcs | Dimension | Caliper | Pass |  |


## Slide 12
3. V53 UAT1 IQC Summary and Highlight Summary
Dimension issue:
1. TLG： 806-50871
FAI 43 OOS, A customer waived.
The hole center can't be measured by the side view.
Have no influence for ICT process.
Vendor proposed to change the measurement point EVT build.
2. TLG： 806-53763
FAI 26 OOS, A customer waived.
The current 3D volume is 1.77mm³, so that calculate the mass to 0.014g (1.77mm³*7.93g/cm³/1000). 2D SPEC is 0.0065g, but actual MASS is about 0.014g.
Have no influence for ICT process.
Vendor proposed to change the specification EVT build.

## Slide 13
3.V53 UAT1 Flex Waiver List

**Table 1:**
| Item | Vendor | APN | Waiver item | Waiver Description | Analysis | Waiver approval date | Waiver approver | Build Impact |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | TLG | 806-50871 | Dimension | FAI 43 OOS | FA: One of the measurement point of FAI43 1.60mm is located at the hole center, and the hole center can't be measured by the side view, so we change the measurement point to the top side and the FAI43 is changed to 2.76mm (the data of 2.76mm is ok to meet in spec). CA: We proposed to change the FAI43 from 1.60mm to 2.76mm (the hole center is controled by the FAI39 3.07mm), and need help to waive it for P2. ——ETD:2024.12.22.  Liu Jing | 11/27 | Jackson Xu | No impact for ICT process |
| 2 | TLG | 806-53763 | Weight | FAI 26 OOS | FA: The current 3D volume is 1.77mm³, so that calculate the mass to 0.014g (1.77mm³*7.93g/cm³/1000). 2D SPEC is 0.0065g, but actual MASS is about 0.014g (as below picture shown).  CA:  We proposed to change the MASS SPEC from 0.0065±0.002 to 0.014±0.002, and need help to waive it for P2. | 11/27 | Jackson Xu | No impact for ICT process |


## Slide 14
3.V53 UAT1 Flex FAI Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | FAI | Nominal | Tol | Tol | CPK(Spec≥1.33) |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI40 | 16.880 | 0.100 | 0.100 | 8.545 | 8.044 | Pass |  |
| 2 | FAI41 | 17.630 | 0.100 | 0.100 | 5.574 | 6.128 | Pass |  |
| 3 | FAI44 | 9.610 | 0.100 | 0.100 | 6.655 | 6.480 | Pass |  |
| 4 | FAI45 | 5.580 | 0.100 | 0.100 | 3.515 | 4.010 | Pass |  |
| 5 | FAI49 | 0.500 | 0.100 | 0.100 | 4.513 | 4.288 | Pass |  |
| 6 | FAI51 | 7.490 | 0.100 | 0.100 | 7.024 | 6.774 | Pass |  |
| 7 | FAI53 | 4.910 | 0.100 | 0.100 | 5.267 | 5.625 | Pass |  |
| 8 | FAI54 | 5.030 | 0.100 | 0.100 | 2.083 | 1.981 | Pass |  |
| 9 | FAI55 | 6.740 | 0.100 | 0.100 | 6.061 | 5.638 | Pass |  |
| 10 | FAI59 | 13.580 | 0.100 | 0.100 | 4.268 | 4.051 | Pass |  |
| 11 | FAI60 | 15.950 | 0.100 | 0.100 | 8.118 | 8.701 | Pass |  |
| 12 | FAI61-1 | 17.950 | 0.100 | 0.100 | 6.234 | 6.421 | Pass |  |
| 13 | FAI61-2 | 17.950 | 0.100 | 0.100 | 7.849 | 7.140 | Pass |  |
| 14 | FAI64 | 19.360 | 0.100 | 0.100 | 6.479 | 6.825 | Pass |  |
| 15 | FAI67 | 21.200 | 0.100 | 0.100 | 6.242 | 5.902 | Pass |  |
| 16 | FAI65 | 0.250 | 0.100 | 0.100 | 3.653 | 3.330 | Pass |  |
| 17 | FAI74 | 25.090 | 0.100 | 0.100 | 3.374 | 3.956 | Pass |  |
| 18 | FAI81-1 | 9.090 | 0.100 | 0.100 | 7.445 | 6.999 | Pass |  |
| 19 | FAI81-2 | 9.090 | 0.100 | 0.100 | 6.933 | 6.469 | Pass |  |
| 20 | FAI87 | 5.020 | 0.100 | 0.100 | 4.064 | 4.440 | Pass |  |


## Slide 15
3.V53 UAT1 Flex FAI Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | FAI | Nominal | Tol | Tol | CPK(Spec≥1.33) |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 21 | FAI88 | 8.180 | 0.100 | 0.100 | 8.831 | 8.434 | Pass |  |
| 22 | FAI90 | 2.900 | 0.100 | 0.100 | 5.824 | 6.240 | Pass |  |
| 23 | FAI91 | 7.710 | 0.100 | 0.100 | 4.935 | 5.340 | Pass |  |
| 24 | FAI107 | 0.000 | 0.200 | 0.000 | 4.701 | 4.160 | Pass |  |
| 25 | FAI108 | 28.910 | 0.100 | 0.100 | 4.329 | 4.679 | Pass |  |
| 26 | FAI109 | 33.730 | 0.100 | 0.100 | 2.063 | 2.244 | Pass |  |
| 27 | FAI110 | 11.650 | 0.100 | 0.100 | 2.334 | 2.177 | Pass |  |
| 28 | FAI113 | 18.630 | 0.100 | 0.100 | 1.954 | 1.892 | Pass |  |
| 29 | FAI115 | 24.060 | 0.100 | 0.100 | 3.993 | 4.550 | Pass |  |
| 30 | FAI116 | 0.950 | 0.030 | 0.030 | 1.731 | 1.713 | Pass |  |
| 31 | FAI147 | 8.710 | 0.200 | 0.200 | 3.677 | 4.021 | Pass |  |
| 32 | FAI172 | 0.700 | 0.100 | 0.100 | 3.539 | 3.347 | Pass |  |
| 33 | FAI211 | 0.200 | 0.200 | 0.200 | 4.612 | 4.940 | Pass |  |
| 34 | FAI220 | 1.300 | 0.030 | 0.030 | 3.788 | 3.958 | Pass |  |


## Slide 16
3.V53 UAT1 Flex SPC Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | SPC | Nominal | Tol | Tol | CPK(Spec≥1.67) |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI36-SPCAJ | 18.980 | 0.100 | 0.100 | 5.821 | 5.561 | Pass |  |
| 2 | FAI37-SPCAK | 20.700 | 0.100 | 0.100 | 5.146 | 5.559 | Pass |  |
| 3 | FAI42-SPCAB | 3.480 | 0.100 | 0.100 | 6.260 | 6.105 | Pass |  |
| 4 | FAI43-SPCAM | 8.890 | 0.100 | 0.100 | 4.188 | 4.452 | Pass |  |
| 5 | FAI46-SPCAL | 4.710 | 0.100 | 0.100 | 4.797 | 4.373 | Pass |  |
| 6 | FAI52-SPCAN | 3.070 | 0.100 | 0.100 | 9.358 | 9.098 | Pass |  |
| 7 | FAI57-SPCAC | 9.090 | 0.100 | 0.100 | 5.719 | 6.489 | Pass |  |
| 8 | FAI68-SPCAI | 22.790 | 0.100 | 0.100 | 3.275 | 3.148 | Pass |  |
| 9 | FAI77-SPCAE | 13.240 | 0.100 | 0.100 | 3.963 | 4.862 | Pass |  |
| 10 | FAI78-SPCAG | 20.830 | 0.100 | 0.100 | 1.926 | 1.822 | Pass |  |
| 11 | FAI104-SPCAF | 15.440 | 0.100 | 0.100 | 4.710 | 4.367 | Pass |  |
| 12 | FAI105-SPCBE | 16.560 | 0.100 | 0.100 | 3.457 | 3.696 | Pass |  |
| 13 | FAI111-SPCAO | 30.140 | 0.100 | 0.100 | 2.584 | 2.450 | Pass |  |
| 14 | FAI112-SPCAH | 31.400 | 0.100 | 0.100 | 1.677 | 1.856 | Pass |  |
| 15 | FAI114-SPCAD | 6.730 | 0.100 | 0.100 | 5.377 | 5.681 | Pass |  |
| 16 | FAI186-SPCAP | 21.830 | 0.100 | 0.100 | 2.121 | 2.331 | Pass |  |
| 17 | FAI187-SPCAQ | 22.760 | 0.100 | 0.100 | 2.135 | 1.984 | Pass |  |
| 18 | FAI219-SPCBD | 21.420 | 0.100 | 0.100 | 3.692 | 3.890 | Pass |  |
| 19 | FAI232-SPCBH | 6.990 | 0.100 | 0.100 | 6.363 | 6.091 | Pass |  |


## Slide 17
3.V53 UAT1 Flex Stack-up Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | Thickness | Nominal | Tol | Tol | CPK(Spec≥1.67) |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI173-SPCX | 0.260 | 0.020 | 0.020 | 5.376 | 5.301 | Pass |  |
| 2 | FAI174-SPCY | 0.375 | 0.030 | 0.030 | 7.831 | 7.672 | Pass |  |
| 3 | FAI176-SPCAA | 0.200 | 0.020 | 0.020 | 4.217 | 4.474 | Pass |  |
| 4 | FAI175-SPCZ | 0.140 | 0.020 | 0.020 | 3.877 | 3.909 | Pass |  |
| 5 | FAI217-SPCBB | 0.200 | 0.020 | 0.020 | 5.892 | 5.646 | Pass |  |
| 6 | FAI218-SPCBC | 0.285 | 0.030 | 0.030 | 4.833 | 5.070 | Pass |  |


## Slide 18
3.V53 UAT1 Flex Stack-up Dimension CPK Distribution Summary

## Slide 19
3.V53 UAT1 Flex DFM Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | FAI | Nominal | Tol | Tol | CPK(Spec≥1.33) |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI1 | 26.745 | 0.050 | 0.050 | 2.963 | 2.707 | Pass |  |
| 2 | FAI2 | 24.413 | 0.050 | 0.050 | 2.430 | 2.476 | Pass |  |
| 3 | FAI3 | 23.155 | 0.050 | 0.050 | 4.317 | 3.597 | Pass |  |
| 4 | FAI4 | 1.956 | 0.050 | 0.050 | 5.968 | 6.284 | Pass |  |
| 5 | FAI5 | 15.796 | 0.050 | 0.050 | 2.176 | 2.380 | Pass |  |
| 6 | FAI6 | 11.703 | 0.050 | 0.050 | 3.875 | 3.619 | Pass |  |
| 7 | FAI7 | 12.367 | 0.050 | 0.050 | 4.229 | 4.121 | Pass |  |
| 8 | FAI8 | 1.260 | 0.075 | 0.075 | 2.004 | 2.061 | Pass |  |
| 9 | FAI9 | 2.095 | 0.075 | 0.075 | 4.397 | 4.670 | Pass |  |
| 10 | FAI10 | 10.271 | 0.050 | 0.050 | 2.394 | 2.228 | Pass |  |
| 11 | FAI11 | 12.113 | 0.050 | 0.050 | 2.278 | 2.130 | Pass |  |
| 12 | FAI12 | 16.005 | 0.050 | 0.050 | 2.404 | 2.627 | Pass |  |
| 13 | FAI13 | 13.799 | 0.050 | 0.050 | 2.076 | 1.889 | Pass |  |
| 14 | FAI14 | 14.122 | 0.050 | 0.050 | 2.025 | 1.875 | Pass |  |
| 15 | FAI15 | 3.200 | 0.050 | 0.050 | 4.703 | 5.073 | Pass |  |
| 16 | FAI16 | 1.000 | 0.050 | 0.050 | 5.037 | 5.460 | Pass |  |
| 17 | FAI19 | 2.848 | 0.050 | 0.050 | 3.271 | 3.077 | Pass |  |
| 18 | FAI20 | 6.384 | 0.050 | 0.050 | 6.108 | 5.831 | Pass |  |
| 19 | FAI23 | 20.702 | 0.050 | 0.050 | 3.747 | 3.894 | Pass |  |
| 20 | FAI24 | 3.478 | 0.050 | 0.050 | 3.034 | 3.173 | Pass |  |


## Slide 20
3.V53 UAT1 Flex DFM Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | FAI | Nominal | Tol | Tol | CPK(Spec≥1.33) |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 21 | FAI25 | 2.901 | 0.050 | 0.050 | 4.741 | 3.475 | Pass |  |
| 22 | FAI26 | 8.176 | 0.050 | 0.050 | 3.922 | 4.290 | Pass |  |
| 23 | FAI27 | 7.707 | 0.050 | 0.050 | 1.851 | 1.706 | Pass |  |
| 24 | FAI29 | 7.837 | 0.050 | 0.050 | 3.609 | 4.651 | Pass |  |
| 25 | FAI17 | 1.191 | 0.075 | 0.075 | 2.846 | 2.690 | Pass |  |
| 26 | FAI18 | 3.047 | 0.075 | 0.075 | 1.767 | 1.863 | Pass |  |
| 27 | FAI21 | 1.878 | 0.075 | 0.075 | 2.391 | 2.343 | Pass |  |
| 28 | FAI22 | 5.662 | 0.075 | 0.075 | 2.963 | 3.343 | Pass |  |
| 29 | FAI28 | 1.966 | 0.075 | 0.075 | 2.635 | 2.517 | Pass |  |
| 30 | FAI30 | 1.822 | 0.075 | 0.075 | 2.077 | 2.394 | Pass |  |
| 31 | FAI31 | 1.375 | 0.075 | 0.075 | 2.244 | 2.440 | Pass |  |
| 32 | FAI32 | 1.225 | 0.075 | 0.075 | 2.796 | 2.982 | Pass |  |


## Slide 21
3.V53 UAT1 Flex DFM Dimension CPK Distribution Summary

## Slide 22
3.V53 UAT1 DOE Flex FAI Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | FAI | Nominal | Tol | Tol | CPK(Spec≥1.33) |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI40 | 16.880 | 0.100 | 0.100 | 5.573 | 6.621 | Pass |  |
| 2 | FAI41 | 17.630 | 0.100 | 0.100 | 7.627 | 7.195 | Pass |  |
| 3 | FAI44 | 9.610 | 0.100 | 0.100 | 6.649 | 7.168 | Pass |  |
| 4 | FAI45 | 5.580 | 0.100 | 0.100 | 7.706 | 8.321 | Pass |  |
| 5 | FAI49 | 0.500 | 0.100 | 0.100 | 10.157 | 10.233 | Pass |  |
| 6 | FAI51 | 7.490 | 0.100 | 0.100 | 7.460 | 6.153 | Pass |  |
| 7 | FAI53 | 4.910 | 0.100 | 0.100 | 6.379 | 6.674 | Pass |  |
| 8 | FAI54 | 5.030 | 0.100 | 0.100 | 3.462 | 3.910 | Pass |  |
| 9 | FAI55 | 6.740 | 0.100 | 0.100 | 9.486 | 8.386 | Pass |  |
| 10 | FAI59 | 13.580 | 0.100 | 0.100 | 6.942 | 5.787 | Pass |  |
| 11 | FAI60 | 15.950 | 0.100 | 0.100 | 6.473 | 7.176 | Pass |  |
| 12 | FAI61.1 | 17.950 | 0.100 | 0.100 | 7.634 | 8.275 | Pass |  |
| 13 | FAI61.2 | 17.950 | 0.100 | 0.100 | 2.332 | 3.148 | Pass |  |
| 14 | FAI64 | 19.360 | 0.100 | 0.100 | 5.705 | 5.375 | Pass |  |
| 15 | FAI65 | 0.250 | 0.100 | 0.100 | 4.686 | 4.087 | Pass |  |
| 16 | FAI67 | 21.200 | 0.100 | 0.100 | 7.069 | 8.139 | Pass |  |
| 17 | FAI74 | 25.090 | 0.100 | 0.100 | 7.898 | 7.841 | Pass |  |
| 18 | FAI81.1 | 9.090 | 0.100 | 0.100 | 6.754 | 6.631 | Pass |  |


## Slide 23
3.V53 UAT1 DOE Flex FAI Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | FAI | Nominal | Tol | Tol | CPK(Spec≥1.33) |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 19 | FAI81.2 | 9.090 | 0.100 | 0.100 | 6.686 | 5.695 | Pass |  |
| 20 | FAI87 | 5.020 | 0.100 | 0.100 | 6.411 | 5.017 | Pass |  |
| 21 | FAI88 | 8.180 | 0.100 | 0.100 | 8.187 | 8.796 | Pass |  |
| 22 | FAI90 | 2.900 | 0.100 | 0.100 | 9.107 | 8.883 | Pass |  |
| 23 | FAI91 | 7.710 | 0.100 | 0.100 | 5.280 | 5.622 | Pass |  |
| 24 | FAI108 | 28.910 | 0.100 | 0.100 | 7.720 | 6.337 | Pass |  |
| 25 | FAI109 | 33.730 | 0.100 | 0.100 | 3.464 | 3.214 | Pass |  |
| 26 | FAI110 | 11.650 | 0.100 | 0.100 | 3.091 | 3.497 | Pass |  |
| 27 | FAI113 | 18.630 | 0.100 | 0.100 | 1.855 | 1.739 | Pass |  |
| 28 | FAI115 | 24.060 | 0.100 | 0.100 | 6.605 | 7.007 | Pass |  |
| 29 | FAI116 | 0.950 | 0.030 | 0.030 | 1.755 | 1.996 | Pass |  |
| 30 | FAI147 | 8.710 | 0.200 | 0.200 | 4.539 | 5.508 | Pass |  |
| 31 | FAI172 | 0.700 | 0.100 | 0.100 | 4.469 | 3.531 | Pass |  |
| 32 | FAI220 | 1.300 | 0.030 | 0.030 | 4.657 | 5.450 | Pass |  |
| 33 | FAI211 | 0.250 | 0.200 | 0.200 | 4.690 | 4.395 | Pass |  |
| 34 | FAI107-1 | 0.000 | 0.100 | 0.100 | 5.741 | 6.233 | Pass |  |
| 35 | FAI107-2 | 0.000 | 0.100 | 0.100 | 7.519 | 7.795 | Pass |  |


## Slide 24
3.V53 UAT1 DOE Flex SPC Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | SPC | Nominal | Tol | Tol | CPK(Spec≥1.67) |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI36SPCAJ | 18.980 | 0.100 | 0.100 | 6.879 | 6.126 | Pass |  |
| 2 | FAI37SPCAK | 20.700 | 0.100 | 0.100 | 6.007 | 7.630 | Pass |  |
| 3 | FAI42SPCAB | 3.480 | 0.100 | 0.100 | 8.131 | 7.350 | Pass |  |
| 4 | FAI43SPCAM | 8.890 | 0.100 | 0.100 | 6.561 | 6.628 | Pass |  |
| 5 | FAI46SPCAL | 4.710 | 0.100 | 0.100 | 6.076 | 6.593 | Pass |  |
| 6 | FAI52SPCAN | 3.070 | 0.100 | 0.100 | 8.944 | 7.452 | Pass |  |
| 7 | FAI57SPCAC | 9.090 | 0.100 | 0.100 | 4.768 | 5.502 | Pass |  |
| 8 | FAI68SPCAI | 22.790 | 0.100 | 0.100 | 3.481 | 4.207 | Pass |  |
| 9 | FAI77SPCAE | 13.240 | 0.100 | 0.100 | 5.258 | 6.315 | Pass |  |
| 10 | FAI78SPCAG | 20.830 | 0.100 | 0.100 | 1.798 | 1.694 | Pass |  |
| 11 | FAI104SPCAF | 15.440 | 0.100 | 0.100 | 4.242 | 4.935 | Pass |  |
| 12 | FAI105SPCBE | 16.560 | 0.100 | 0.100 | 2.522 | 2.999 | Pass |  |
| 13 | FAI111SPCAO | 30.140 | 0.100 | 0.100 | 3.774 | 3.390 | Pass |  |
| 14 | FAI112SPCAH | 31.400 | 0.100 | 0.100 | 2.425 | 3.003 | Pass |  |
| 15 | FAI114SPCAD | 6.730 | 0.100 | 0.100 | 5.887 | 6.470 | Pass |  |
| 16 | FAI186SPCAP | 21.830 | 0.100 | 0.100 | 3.672 | 3.649 | Pass |  |
| 17 | FAI187SPCAQ | 22.760 | 0.100 | 0.100 | 2.238 | 1.897 | Pass |  |
| 18 | FAI219SPCBD | 21.420 | 0.100 | 0.100 | 5.077 | 5.614 | Pass |  |
| 19 | FAI232SPCBH | 6.990 | 0.100 | 0.100 | 8.646 | 8.686 | Pass |  |


## Slide 25
3.V53 UAT1 DOE Flex Stack-up Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | Thickness | Nominal | Tol | Tol | CPK(Spec≥1.67) |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI173-SPCX | 0.260 | 0.020 | 0.020 | 4.239 | 3.616 | Pass |  |
| 2 | FAI174-SPCY | 0.375 | 0.030 | 0.030 | 4.999 | 5.630 | Pass |  |
| 3 | FAI176-SPCM | 0.200 | 0.020 | 0.020 | 3.668 | 4.618 | Pass |  |
| 4 | FAI175-SPCZ | 0.140 | 0.020 | 0.020 | 5.106 | 4.923 | Pass |  |
| 5 | FAI217-SPBB | 0.200 | 0.020 | 0.020 | 6.267 | 6.683 | Pass |  |
| 6 | FAI218-SPBC | 0.285 | 0.030 | 0.030 | 5.159 | 6.151 | Pass |  |


## Slide 26
3.V53 UAT1 DOE Flex Stack-up Dimension CPK Distribution Summary

## Slide 27
3.V53 UAT1 DOE Flex DFM Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | FAI | Nominal | Tol | Tol | CPK(Spec≥1.33) |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI1 | 26.745 | 0.050 | 0.050 | 4.984 | 4.207 | Pass |  |
| 2 | FAI2 | 24.413 | 0.050 | 0.050 | 3.531 | 2.918 | Pass |  |
| 3 | FAI3 | 23.155 | 0.050 | 0.050 | 6.160 | 6.625 | Pass |  |
| 4 | FAI4 | 1.956 | 0.050 | 0.050 | 6.975 | 6.169 | Pass |  |
| 5 | FAI5 | 15.796 | 0.050 | 0.050 | 4.107 | 3.565 | Pass |  |
| 6 | FAI6 | 11.703 | 0.050 | 0.050 | 7.304 | 7.454 | Pass |  |
| 7 | FAI7 | 12.367 | 0.050 | 0.050 | 5.827 | 5.760 | Pass |  |
| 8 | FAI8 | 1.260 | 0.075 | 0.075 | 3.399 | 2.438 | Pass |  |
| 9 | FAI9 | 2.095 | 0.075 | 0.075 | 3.088 | 3.656 | Pass |  |
| 10 | FAI10 | 10.271 | 0.050 | 0.050 | 3.386 | 2.790 | Pass |  |
| 11 | FAI11 | 12.113 | 0.050 | 0.050 | 3.252 | 4.342 | Pass |  |
| 12 | FAI12 | 16.005 | 0.050 | 0.050 | 2.956 | 3.133 | Pass |  |
| 13 | FAI13 | 13.799 | 0.050 | 0.050 | 2.753 | 2.414 | Pass |  |
| 14 | FAI14 | 14.122 | 0.050 | 0.050 | 2.092 | 1.895 | Pass |  |
| 15 | FAI15 | 3.200 | 0.050 | 0.050 | 4.181 | 4.237 | Pass |  |
| 16 | FAI16 | 1.000 | 0.050 | 0.050 | 3.336 | 3.906 | Pass |  |
| 17 | FAI19 | 2.848 | 0.050 | 0.050 | 3.790 | 3.012 | Pass |  |


## Slide 28
3.V53 UAT1 DOE Flex DFM Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | FAI | Nominal | Tol | Tol | CPK(Spec≥1.33) |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 18 | FAI20 | 6.384 | 0.050 | 0.050 | 3.858 | 4.497 | Pass |  |
| 19 | FAI23 | 20.702 | 0.050 | 0.050 | 2.811 | 2.563 | Pass |  |
| 20 | FAI24 | 3.478 | 0.050 | 0.050 | 2.772 | 3.378 | Pass |  |
| 21 | FAI25 | 2.901 | 0.050 | 0.050 | 3.204 | 2.891 | Pass |  |
| 22 | FAI26 | 8.176 | 0.050 | 0.050 | 3.932 | 3.286 | Pass |  |
| 23 | FAI27 | 7.707 | 0.050 | 0.050 | 2.705 | 1.703 | Pass |  |
| 24 | FAI29 | 7.837 | 0.050 | 0.050 | 2.624 | 3.522 | Pass |  |
| 25 | FAI17 | 1.285 | 0.075 | 0.075 | 2.478 | 1.961 | Pass |  |
| 26 | FAI18 | 3.357 | 0.075 | 0.075 | 1.687 | 1.679 | Pass |  |
| 27 | FAI21 | 1.882 | 0.075 | 0.075 | 2.727 | 1.683 | Pass |  |
| 28 | FAI22 | 5.559 | 0.075 | 0.075 | 1.703 | 1.781 | Pass |  |
| 29 | FAI28 | 1.966 | 0.075 | 0.075 | 1.973 | 1.795 | Pass |  |
| 30 | FAI30 | 1.822 | 0.075 | 0.075 | 1.717 | 1.748 | Pass |  |
| 31 | FAI31 | 1.375 | 0.075 | 0.075 | 1.928 | 1.809 | Pass |  |
| 32 | FAI32 | 1.225 | 0.075 | 0.075 | 2.346 | 1.812 | Pass |  |


## Slide 29
3.V53 UAT1 DOE Flex DFM Dimension CPK Distribution Summary

## Slide 30
3.V53 Strobe tail Flex FAI Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | FAI | Nominal | Tol | Tol | CPK(Spec≥1.33) |  |  |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Mflex | ICT | Avary |  |  |
| 1 | FAI2 | 13.640 | 0.120 | 0.120 | 4.812 | 5.174 | 2.624 | 2.449 | Pass |  |
| 2 | FAI4 | 0.190 | 0.120 | 0.120 | 2.274 | 2.103 | 2.089 | 1.904 | Pass |  |
| 3 | FAI10-1 | 0.000 | 0.400 | 0.000 | 44.478 | 46.121 | 17.625 | 19.178 | Pass |  |
| 4 | FAI10-2 | 0.000 | 0.400 | 0.000 | 47.539 | 45.755 | 17.208 | 16.946 | Pass |  |
| 5 | FAI10-3 | 0.000 | 0.400 | 0.000 | 32.764 | 34.017 | 17.515 | 17.609 | Pass |  |
| 6 | FAI10-4 | 0.000 | 0.400 | 0.000 | 71.445 | 69.905 | 16.681 | 17.549 | Pass |  |
| 7 | FAI10-5 | 0.000 | 0.400 | 0.000 | 31.783 | 29.833 | 24.299 | 22.027 | Pass |  |
| 8 | FAI10-6 | 0.000 | 0.400 | 0.000 | 46.150 | 48.985 | 19.598 | 20.957 | Pass |  |
| 9 | FAI10-7 | 0.000 | 0.400 | 0.000 | 55.595 | 57.123 | 24.415 | 22.664 | Pass |  |
| 10 | FAI10-8 | 0.000 | 0.400 | 0.000 | 35.551 | 34.865 | 16.834 | 16.250 | Pass |  |
| 11 | FAI10-9 | 0.000 | 0.400 | 0.000 | 42.099 | 45.534 | 19.325 | 20.650 | Pass |  |
| 12 | FAI11-1 | 0.600 | 0.050 | 0.050 | 6.370 | 5.989 | 7.833 | 8.346 | Pass |  |
| 13 | FAI11-2 | 0.600 | 0.050 | 0.050 | 6.403 | 6.192 | 5.005 | 4.604 | Pass |  |
| 14 | FAI11-3 | 0.600 | 0.050 | 0.050 | 7.067 | 7.622 | 7.067 | 7.752 | Pass |  |
| 15 | FAI11-4 | 0.600 | 0.050 | 0.050 | 8.045 | 7.944 | 3.554 | 3.788 | Pass |  |
| 16 | FAI11-5 | 0.600 | 0.050 | 0.050 | 6.740 | 7.316 | 4.094 | 3.801 | Pass |  |
| 17 | FAI11-6 | 0.600 | 0.050 | 0.050 | 7.124 | 6.917 | 3.430 | 3.241 | Pass |  |
| 18 | FAI11-7 | 0.600 | 0.050 | 0.050 | 6.392 | 6.893 | 3.899 | 3.682 | Pass |  |
| 19 | FAI11-8 | 0.600 | 0.050 | 0.050 | 5.691 | 6.078 | 3.624 | 3.980 | Pass |  |
| 20 | FAI11-9 | 0.600 | 0.050 | 0.050 | 6.230 | 5.853 | 3.318 | 3.034 | Pass |  |
| 21 | FAI11-10 | 0.600 | 0.050 | 0.050 | 6.105 | 5.921 | 4.694 | 5.048 | Pass |  |
| 22 | FAI12-1 | 0.720 | 0.200 | 0.200 | 9.379 | 10.537 | 11.833 | 12.781 | Pass |  |
| 23 | FAI12-2 | 0.720 | 0.200 | 0.200 | 8.633 | 7.793 | 7.332 | 6.853 | Pass |  |
| 24 | FAI17 | 4.150 | 0.200 | 0.200 | 27.005 | 25.014 | 19.676 | 21.421 | Pass |  |


## Slide 31
3.V53 Strobe tail Flex SPC Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | SPC | Nominal | Tol | Tol | CPK(Spec≥1.67) |  |  |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Mflex | ICT | Avary |  |  |
| 1 | FAI1SPCA-1 | 0.900 | 0.050 | 0.050 | 3.372 | 3.577 | 7.905 | 8.291 | Pass |  |
| 2 | FAI1SPCA-2 | 0.900 | 0.050 | 0.050 | 3.068 | 2.790 | 8.686 | 8.405 | Pass |  |
| 3 | FAI1SPCA-3 | 0.900 | 0.050 | 0.050 | 4.970 | 4.625 | 1.808 | 1.686 | Pass |  |
| 4 | FAI1SPCA-4 | 0.900 | 0.050 | 0.050 | 4.875 | 5.255 | 5.955 | 6.530 | Pass |  |
| 5 | FAI1SPCA-5 | 0.900 | 0.050 | 0.050 | 5.428 | 4.989 | 10.804 | 11.332 | Pass |  |
| 6 | FAI1SPCA-6 | 0.900 | 0.050 | 0.050 | 4.617 | 4.771 | 11.344 | 12.310 | Pass |  |
| 7 | FAI1SPCA-7 | 0.900 | 0.050 | 0.050 | 4.509 | 4.491 | 8.582 | 8.114 | Pass |  |
| 8 | FAI1SPCA-8 | 0.900 | 0.050 | 0.050 | 4.229 | 4.612 | 8.150 | 8.624 | Pass |  |
| 9 | FAI1SPCA-9 | 0.900 | 0.050 | 0.050 | 2.731 | 2.610 | 7.687 | 8.440 | Pass |  |
| 10 | FAI1SPCA-10 | 0.900 | 0.050 | 0.050 | 3.393 | 3.709 | 2.361 | 2.256 | Pass |  |
| 11 | FAI3SPCB | 5.370 | 0.200 | 0.200 | 10.141 | 9.341 | 21.132 | 22.647 | Pass |  |


## Slide 32
3.V53 Strobe tail Flex Stack-up Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | Thickness | Nominal | Tol | Tol | CPK(Spec≥1.67) |  |  |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Mflex | ICT | Avary |  |  |
| 1 | FAI8-SPCC | 0.142 | 0.020 | 0.020 | 1.916 | 1.746 | 3.340 | 3.643 | Pass |  |
| 2 | FAI7-SPCF | 0.106 | 0.020 | 0.020 | 4.027 | 4.252 | 2.865 | 2.615 | Pass |  |
| 3 | FAI9-SPCE | 0.131 | 0.020 | 0.020 | 2.715 | 2.478 | 3.295 | 3.238 | Pass |  |
| 4 | FAI6-SPCD | 0.123 | 0.020 | 0.020 | 3.096 | 3.263 | 2.485 | 2.574 | Pass |  |


## Slide 33
3.V53 Strobe tail Flex Stack-up Dimension CPK Distribution Summary

## Slide 34
3.V53 Strobe tail Flex DFM Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | FAI | Nominal | Tol | Tol | CPK(Spec≥1.33) |  |  |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  | (+) | (-) | ICT | Mflex | ICT | Avary |  |  |
| 1 | FAI1 | 4.150 | 0.050 | 0.050 | 2.981 | 2.782 | 5.129 | 4.791 | Pass |  |
| 2 | FAI2 | 1.375 | 0.075 | 0.075 | 1.973 | 2.050 | 2.350 | 2.488 | Pass |  |
| 3 | FAI3 | 1.050 | 0.075 | 0.075 | 1.881 | 2.050 | 2.022 | 2.172 | Pass |  |
| 4 | FAI4 | 12.180 | 0.050 | 0.050 | 1.983 | 1.831 | 3.401 | 3.226 | Pass |  |
| 5 | FAI5 | 6.65 | 0.050 | 0.050 | 3.152 | 3.001 | 3.152 | 3.095 | Pass |  |
| 6 | FAI6 | 16.329 | 0.050 | 0.050 | 3.556 | 3.421 | 3.556 | 3.361 | Pass |  |
| 7 | FAI7 | 135.000 | 1.000 | 1.000 | 2.345 | 2.540 | 2.593 | 2.874 | Pass |  |


## Slide 35
3.V53 UAT1 PSA FAI Dimension CPK Distribution Summary
Pass
Fail

**Table 1:**
| SN | P/N | Items | Nominal | Tol | Tol | JT |  | DX |  | Result | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | CPK(Spec≥1. 33) |  | CPK(Spec≥1. 33) |  |  |  |
|  |  |  | （mm） | （+） | （-） | JT | ICT | DX | ICT |  |  |
| 1 | 029-001H-3606 | Length | 6.24 | 0.100 | 0.100 | 2.724 | 2.085 | 1.926 | 1.969 | Pass |  |
|  |  | Width | 3.61 | 0.100 | 0.100 | 3.711 | 3.347 | 2.724 | 2.657 | Pass |  |
|  |  | Thickness | 0.25 | 0.025 | 0.025 | 4.268 | 5.734 | 3.509 | 3.317 | Pass |  |
| 2 | 029-001H-3607 | Length | 5.28 | 0.100 | 0.100 | 2.596 | 2.848 | 4.335 | 4.154 | Pass |  |
|  |  | Width | 1.22 | 0.100 | 0.100 | 5.584 | 6.692 | 3.487 | 3.528 | Pass |  |
|  |  | Thickness | 0.10 | 0.010 | 0.010 | 3.808 | 4.302 | 4.581 | 5.073 | Pass |  |
| 3 | 029-001H-3608 | Length | 9.74 | 0.100 | 0.100 | 1.908 | 2.210 | 10.275 | 9.767 | Pass |  |
|  |  | Width | 5.16 | 0.100 | 0.100 | 2.847 | 2.670 | 2.513 | 2.372 | Pass |  |
|  |  | Thickness | 0.05 | 0.005 | 0.005 | 2.894 | 2.714 | 3.454 | 2.841 | Pass |  |
| 4 | 029-001H-3609 | Length | 7.27 | 0.100 | 0.100 | 5.131 | 4.137 | 3.738 | 3.386 | Pass |  |
|  |  | Width | 7.09 | 0.100 | 0.100 | 2.833 | 2.734 | 3.264 | 2.688 | Pass |  |
|  |  | Thickness | 0.10 | 0.010 | 0.010 | 5.433 | 4.960 | 6.544 | 7.387 | Pass |  |
| 5 | 029-001H-3610 | Length | 10.02 | 0.100 | 0.100 | 1.740 | 1.705 | 16.138 | 17.633 | Pass |  |
|  |  | Width | 3.42 | 0.100 | 0.100 | 11.105 | 9.533 | 8.347 | 7.641 | Pass |  |
|  |  | Thickness | 0.05 | 0.005 | 0.005 | 2.551 | 2.075 | 2.213 | 1.592 | Pass |  |


## Slide 36
3.V53 UAT1 PSA 029-001H-3606 Peeling force Summary(TESA 4942)

## Slide 37
3.V53 UAT1 PSA 029-001H-3607 Peeling force Summary(NITTO 56110B)

## Slide 38
3.V53 UAT1 PSA 029-001H-3608 Peeling force Summary(NITTO 56105)

## Slide 39
3.V53 UAT1 PSA 029-001H-3609 Peeling force Summary(NITTO 56110B)

## Slide 40
3.V53 UAT1 PSA 029-001H-3610 Peeling force Summary (SHRETEC 5105SA)

## Slide 41

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 42
4. Assembly Process Flow Chart-UAT1&Strobe Tail
Panel
Single Piece
Traceabilty/Shopfloor station
UAT1 Flex
Strobe Tail Flex

**Table 1:**
| SMT (BOT) | Remove UV Film |
| --- | --- |
|  | Panel to Tray |
|  | Tape on metal sheet |
|  | Flex Loading |
|  | HTS Print |
|  | Add metal cover |
|  | LTS Dispensing |
|  | SPI |
|  | Pick up& Placement |
|  | Pre-AOI |
|  | HTS Reflow |
|  | Cooling |
|  | Post-AOI |
|  | SBI |
|  | Remove metal cover |
|  | VI |
|  | Flipping |


**Table 2:**
| SMT  (TOP) | Flipping AOI |
| --- | --- |
|  | HTS Print |
|  | Add metal cover |
|  | SPI |
|  | Pick up& Placement |
|  | Pre-AOI |
|  | HTS Reflow |
|  | Cooling |
|  | MIC Film P&P |
|  | X-RAY(option) |
|  | Post-AOI |
|  | Remove metal cover |
|  | VI |


**Table 3:**
| CC Glue | Add metal cover |
| --- | --- |
|  | UV Dispensing |
|  | UV AOI |
|  | UV Cure |
|  | Remove metal cover |
|  | Flipping |
|  | Add metal cover |
|  | UV Dispensing |
|  | UV AOI |
|  | UV Cure |
|  | Thermal Curing |
|  | Cooling |
|  | Remove metal cover |
| Package | Flipping |
|  | Tape remove |
|  | VI |
|  | Package scan |
|  | Tray to bonding tray |
|  | Package to box |


**Table 4:**
| Pre-SMT | Tray to bonding tray |
| --- | --- |
|  | Barcode Link |
|  | Baking |
|  | Package to box |


## Slide 43
4. Assembly Process Flow Chart-UAT1 Bonding
Panel
Single Piece
Traceabilty/Shopfloor station

**Table 1:**
| Bonding | Strobe P&P |
| --- | --- |
|  | Flux dispensing |
|  | AOI |
|  | UAT1 P&P |
|  | AOI |
|  | Add press jig |
|  | LTS Reflow |
|  | Cooling |
|  | Remove press jig |
|  | Inline X- Ray |
| PSA& 2DBC | Add PSA Support |
|  | Flipping |
|  | Remove Bonding Carrier |
|  | Add PSA Cover |
|  | PSA P&P |
|  | Press |
|  | Flipping |
|  | 2DBC&PSA P&P |
|  | Press |
|  | Link |
| Package | Carrier to Tray |
|  | VI |
|  | Scan |


**Table 2:**
| Backend | Bending |
| --- | --- |
|  | VI |
|  | MIC Film Remove |
|  | 1K test |
|  | AVI for EB |
|  | Mic film P&P |
|  | RF |
|  | ICT |
|  | AVI |
|  | Package (2DBC scan) |
|  | OQC (FR + THD + Sealing) |
|  | OQC (RF+ICT) |
|  | OQC (VI) |
|  | Package |


## Slide 44
4. Assembly Yield Trend and top5 breakdown
MP Target ：99%

## Slide 45
4. Assembly Yield Trend and top5 breakdown

**Table 1:**
| Failure Model | Quantity （Pcs） | F/R | Accumulation percentage |
| --- | --- | --- | --- |
| Clip contamination | 78 | 0.87% | 32.77% |
| Flex Dent | 42 | 0.47% | 50.42% |
| Printing solder excessive | 31 | 0.35% | 63.45% |
| Sus overlap | 23 | 0.26% | 73.11% |
| PSA dent | 16 | 0.18% | 79.83% |
| Others | 48 | 0.54% | 100.00% |


## Slide 46
4. Assembly Yield Trend and top5 breakdown

**Table 1:**
| Defect | Qty | FA | CA |
| --- | --- | --- | --- |
| PSA shift | 4 | 1. Check the press station, the equipment parameters follow SOP, no abnormality. 2. Check the press head, they are not damaged and not foreign materials sticking.  3. Check the mounting station, the equipment parameters follow SOP, no abnormal.  4. Check the nozzle, It is not damaged and not foreign materials sticking.  In summary: Not found the root cause of  PSA adhesive winkle and keep on tracking | Follow SOP define to take product Tracking next config build has no this issue. |
| Solder ball | 4 | 1. Confirm Post-AOI image that there are solder ball on flex surface 2. Confirm the Pre-AOI image, flex surface has solder paste 3. Confirm the SPI image, the product is not filled with cavity, flex surface has solder paste. In summary: half panel product, operator tear film and wipe plate lead to solder balls | Tearing the film requires two operators to work together, one to press the steel sheet to prevent the separation of the steel sheet and the carrier, and one to tear the film from the direction of the plate to the non-plate. |
| PSA foreign material | 4 | 1. Check the flex before PSA P&P, no found the foreign materials. 2. Check the PSA raw materials, no found the foreign materials.  3. Check the P&P machine, found the foreign materials on the feeder In summary: the feeder has foreign materials, it causes PSA foreign materials | At the beginning of each shift, and after changing materials, pay attention to cleaning the machine. |
| Flex foreign material | 3 | 1. Confirm AOI image, foreign body exists between tape and flex. 2. Confirm operator stick tape on electrostatic table. 3. Confirm the similar foreign material on the electrostatic table。 In  summary : The tape foreign material is attached to the flex surface after reflow. | The taping operation is performed on the cleaned PET. Automatic taping machine in EVT phase. |
| glue foreign material | 3 | 1. Confirm that there is no foreign material on the surface of flex in POST-AOI image 2. Confirm UV-AOI image, foreign material on the surface of UV glue 3. according to SMT Process flow, lock risk stations is dispensing station 4. Check and find that there are foreign material similar to filaments inside the dispensing machine In summary: internal foreign material fall during the operation of the dispensing machine, resulting in glue foreign material | Use a vacuum cleaner to clean the inside of the machine before input production. |
| Solder on SUS | 3 | 1. Confirm Post-AOI image that there are solder ball on SUS surface 2. Confirm the Pre-AOI image, SUS surface has solder paste 3. There is solder paste on the sus surface and no solder paste wipe trace of flex surface in SPI image. 4. Confirm wiping mechanism is abnormal and solder paste remains on the back of stencil. In summary : solder residue from stencil leads to solder on SUS. | Repair the wiping mechanism immediately. Check the wiping mechanism every 12H/ time. |
| Wrong polarity | 2 | 1. Confirm Post-AOI image, IC rotation offset, 2.Confirm the Pre-AOI image, IC is normal, lock  risk station between Pre-AOI and Reflow 3. Confirm with the operator that the scanning gun is abnormal, and the operator take the board to scan the code and wipe the board resulting in wrong polarity. In summary : Operator wipe  the component resulting in wrong polarity. | Device exception feedback team leader and device engineer handle the problem. Before production, check whether the position of the code scanner is abnormal. |
| PSA missing | 2 | 1. Check the PSA AOI found that PSA was missing. 2. The missing PSA product is the mantissa panel. 3. Check the mounting record, it was found that when the operator was producing the mantissa panel, cavity select error, resulting in missing PSA In summary: the operator was producing the mantissa panel, cavity select error, resulting in missing PSA | After the mantissa panel product, PE confirms the PSA mounting situation, and then continue production after there is no problem. |
| Clip foreign material | 2 | 1.Confirm Pre-AOI image , the foreign material is under the B2B component. 2.Confirm SPI image , there is not abnormal on the solder paste. 3.According to SMT process , lock risk station is P&P. 4.Confirm similar foreign material found in NPM machine. In summary : Foreign material inside NPM machine lead to B2B foreign bodies | Use a vacuum cleaner to clean the inside of the machine before input production. |


## Slide 47
4. Assembly Yield Trend and top5 breakdown

**Table 1:**
| Defect | Qty | FA | CA |
| --- | --- | --- | --- |
| Copper exposed | 2 | 1.Confirm UV-AOI image, flex is normal. 2.Confirm that  remove the cover plate does not interfere with the flex. 3.Confirm that there is no interference between the tear tape and the copper leakage position. 4.Confirm VI uses latex sleeves without risk of copper leakage in flex. In summary : SMT check no abnormal ,continue tracking. | SMT check no abnormal ,continue tracking. |
| Clip solder insufficient | 2 | 1. Confirm that the Post-AOI2 image shows no abnormal clip. 2. Confirm the Pre-AOI2 image and the clip mounting without abnormality. 3. Confirm that there is no foreign material on the surface of SPI image solder paste, and the solder volume is in spec. 4. Confirm the Flip-AOI image, pad surface is not abnormal. In summary: SMT check no abnormal, continuous tracking | Tracking 1280pcs of products, no less tin defects. |
| Glue on IC | 2 | 1. Confirm the UV-AOI image that there is glue on the IC surface. 2. According to the SMT Process, lock the risk station as the dispensing station. 3. Check the glue dispensing station and find the glue bulge in the glue cup. 4. Check that there is excess glue on the surface of the dispensing nozzle. In summary: the adhesive on the nozzle surface leads to glue on IC, | Clean the nozzle immediately with a dust-free cloth. Replace the clear glue cup immediately. |
| Solder on MIC | 2 | 1. Confirm Post-AOI image , there is solder on the surface of MIC, 2. Confirm the Pre-AOI image is normal, lock risk station between Pre-AOI and Reflow 3. Confirm with the operator that the scanning gun is abnormal, and the operator take the board to scan the code and wipe the board resulting in solder on mic. In summary : Operator wipe  board ,resulting in solder on mic. | Device exception feedback team leader and device engineer handle the problem. Before production, check whether the position of the code scanner is abnormal. |
| Floating height | 2 | 1. Confirm the Post-AOI image that there is a filamentous foreign material under the component. 2. Confirm the Pre-AOI1 image, the foreign material exists under the component. 3. Confirm the presence of foreign material in SPI image. 5. Confirm the Link-1 image, some foreign material exist under the steel sheet. In summary : The foreign material caused component float high at the loading station | Use latex gloves to loading board. The electrostatic clothes must be wrapped with your own clothes. |
| SUS contamination | 2 | 1. Confirm that Post-AOI,Pre-AOI,SPI ,link-1 images and SUS are dirty 2. According to SMT Process flow, the lock-out risk station is the loading station 3. Confirm that the finger cover of the operator  is dirty. In summary: Dirty finger covers cause SUS contamination. | Replace finger covers immediately. Quality department audit No fixed time. |
| Flex deformation | 2 | 1. Confirm that FLEX in UV-AOI image is normal.2. Ensure that there is no interference between the cover sheet and the flex, and that the tape removal method is normal3. At station VI, the product begins to move horizontally before it is completely out of Tray In summary: VI improper manipulation causes flex deformation. | After the product is completely out of the Tray, move the product horizontally. |
| Component Open | 2 | 1. Confirm Post-AOI image, chip open, 2.Confirm the Pre-AOI image，component is normal, lock risk station between Pre-AOI and Reflow 3. Confirm with the operator that the scanning gun is abnormal, and the operator take the board to scan the code and wipe the board . In summary : Operator wipe the component resulting in component open. | Device exception feedback team leader and device engineer handle the problem. Before production, check whether the position of the code scanner is abnormal. |
| Glue on SUS | 2 | 1. Confirm the UV-AOI image that there is glue on the IC surface. 2. According to the SMT Process, lock the risk station as the dispensing station. 3. Check the glue dispensing station and find the glue bulge in the glue cup. 4. Check that there is excess glue on the surface of the dispensing nozzle. In summary: the adhesive on the nozzle surface leads to glue on IC. | Clean the nozzle immediately with a dust-free cloth. Replace the clear glue cup immediately. |


## Slide 48
4. Assembly Yield Trend and top5 breakdown

**Table 1:**
| Defect | Qty | FA | CA |
| --- | --- | --- | --- |
| SUS contamination | 1 | 1. Check the press station, the equipment parameters follow SOP, no abnormality. 2. Check the press head, they are not damaged and not foreign materials sticking.  3. Check the mounting station, the equipment parameters follow SOP, no abnormal.  4. Check the nozzle, It is not damaged and not foreign materials sticking.  In summary: Not found the root cause of  PSA adhesive winkle and keep on tracking | Follow SOP define to take product Tracking next config build has no this issue. |
| BC double tape | 1 | 1. Check the PSA AOI found that PSA was BC double tape. 2. The missing PSA product is the mantissa panel. 3. Check the mounting record, it was found that when the operator was producing the mantissa panel, cavity select error, resulting in BC double tape In summary: the operator was producing the mantissa panel, cavity select error, resulting in missing PSA | After the mantissa panel product, PE confirms the PSA mounting situation, and then continue production after there is no problem. |
| PSA foreign material | 1 | 1. Check the flex before PSA P&P, no found the foreign materials. 2. Check the PSA raw materials, no found the foreign materials.  3. Check the P&P machine, found the foreign materials on the feeder In summary: the feeder has foreign materials, it causes PSA foreign materials | At the beginning of each shift, and after changing materials, pay attention to cleaning the machine. |


## Slide 49
4. Assembly Yield Trend and top5 breakdown

**Table 1:**
| Item | Defect  Description | Picture | Defect Rate % | Previous  build % | FA/Root Cause | Corrective Action | DRI  Due Date | Validation (xxF/input=defect rate%) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Clip contamination-(Process issue) |  | 0.87% (78F/8956T) | / | The solvent on the nozzle caused the clip to be contaminated during dispense glue process. | 1.Optimize the dispensing height to increase the gap between clip and nozzle from 0.05 to 0.3mm. 2.Optimize the nozzle cleaning height that can only cleaning the nozzle bottom. 3.As a lesson learn for dispense glue. | Jin 11/28 | 0.00% (0F/6376T) |
| 2 | Flex dent (Process issue) |  | 0.47% (42F/8956T) | / | Material issue: It is process issue. The machine is not set to error proof of module and program, the press heads were not pressing the correct location, lead to the flex dent. | 1. Instantly match modules and programs correctly and keep track of pressing. 2. Setting press machine system error proof. Upper and lower module laser barcode, when the first operation of the machine after changing, the visual module will scan the barcode and match the program, match OK, the machine runs normally, match NG,  the machine alarm. | Changsheng 12/05 | 0% (0F/6376T) |
| 3 | Printing solder excessive-(Raw material issue) |  | 0.35% (31F/8956T) | / | Flex scrap material leads to printing defects. | 1.Check whether there is excess material on the flex surface after panel to tray.  2.The vendor Increase laser width and improved process condition will be applied in EVT. | Xiaofeng 11/28 | 0.00% (0F/4432T) |
| 4 | Sus overlap- (Raw material issue) |  | 0.26% (23F/8956) | / | Both sides of the material tape are not sealed, resulting in clip overlap. | 1.Increase the limit wall and deepen the cavity of the product in double side of tape for clip. 2.To move the seal location from up and down sealed to close to the clip. | Xiaofeng 12/7 | 0.00% （0F/4432T） |
| 5 | PSA dent (Process issue) |  | 0.18% (16F/8,956T) | / | The MIC film remove fixture was not  fool-proof cause PSA dent. | 1.Modify fixture to fool-proof, cancel the cover head to avoid the PSA.  2.Update fixture design guideline, the structure need avoid to press PSA.  3.Cut in auto remove Mic film machine in EVT stage. | Kobe Zhang 2/7 | 0.00% (0F/6,926T) |


**Table 2:**
| Flex/Assembly | Input Qty | Output Qty | Yield | MP Yield Target QCP | Yield Gap | *Supply Chain MP target commitment to GSM | *MP Yield by ”yield calculation” |
| --- | --- | --- | --- | --- | --- | --- | --- |
| UAT1 | 8956 | 8718 | 97.34% | 97.5% | 0.16% | / | 97.5% |


## Slide 50
4. Failure FACA
UV-AOI
OK
NG
Post-AOI
Before
Clean Nozzle
Mapping
After
Simulation
Dispense nozzle
Contamination area
Start point
Gap
Dispense nozzle

**Table 1:**
| Component | CL_ANT_VERT_SP | Vendor | TLG | APN | 806-53763 | Failure process/station | VI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Issue Description | Clip contamination--Process issue  Defected rate:  0.87% (78F/8,956T )              Before:  0.00% (0F/500T )     1st Config(X06P2-U1-MIYG2-SM）                             3.75% (78F/2,080T ) 2nd Config(X06P2-U1-MIYG2-SM）                 After:  0.00% (0F/6,376T )   3rd~7th Config(X06P2-U1-MINA7-SA)                                                                                  X06P2-U1-MIYG2-SA-D1） |  |  |  |  |  |  |
| FA | VI detects clip contamination*78pcs,the defects are concentrated on 2nd config CL_ANT2_VERT_SP clips, panels and cavities are not concentrated. Check UV-AOI image, there is foreign material on the clip surface. Post-AOI images show that the clip is normal, lock the risk station is dispensing station. Check the dispensing machine found that the solvent was hanging on the nozzle after cleaning the nozzle. According to the foregoing description, it is suspected that nozzle edge solvent contamination clip during the dispensing process. Simulation: Confirm the element analysis and using the nozzle with solvent to dispense that can reproduction the defect. Conclusion: The solvent on the nozzle caused the clip to be contaminated during dispense glue process. |  |  |  |  |  |  |
| CA | 1.Optimize the dispensing height to increase the gap between clip and nozzle from 0.05mm to 0.35mm. Done 11/28 Jin 2.Optimize the nozzle cleaning height that can only cleaning the nozzle bottom. Done 11/28 Jin 3.As a lesson learn for dispensing glue. |  |  |  |  |  |  |
| Validation | Tracked 6,376pcs, the defective rate 0.00%(0F/6,376T). Done 12/20 Xiaofeng |  |  |  |  |  |  |


## Slide 51
4. Failure FACA
OK
NG

**Table 1:**
| Component | Flex | Vendor | Murata | APN | 821-05715-02 | Failure process/station | Press |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Issue  Description | Flex dent---Process issue Defected rate: 0.47%(42F/8,956T)              Before: 0.00%(0F/500T)         1st Config(X06P2-U1-MIYG2-SM)                            2.02%(42F/2,080T)     2nd Config(X06P2-U1-MIYG3-SM)                 After: 0%(0F/6,376T)             3rd ~ 7th Config (X06P2-U1-MINA7-SA~                                                                                                X06P2-U1-MIYG3-SA-D1） |  |  |  |  |  |  |
| FA | Flex dent was found at press station, defects are concentrated on 2nd config flex. The defects were found in the first panel. Check the press machine, found the upper and lower press module were not match with the program, the press heads were not pressing the correct location, lead to the flex dent. Conclusion: The machine is not set to error proof of module and program, the press heads were not pressing the correct location, lead to the flex dent. |  |  |  |  |  |  |
| CA | Short Term:  1. Instantly match modules and programs correctly and keep track of pressing. Done --DRI: PE/Changsheng 12/3 Long Term:  1. Setting press machine system error proof. Upper and lower module laser barcode, when the first operation of the machine after changing, the visual module will scan the barcode and match the program, match OK, the machine runs normally, match NG,  the machine will alarm. Done --DRI: PE/Changsheng 12/5 |  |  |  |  |  |  |
| Validation | Tracking 6,376pcs ,no found the same defect. F/R: 0% (0F/6,376T) Done –DRI: PE/Changsheng 12/17 |  |  |  |  |  |  |


## Slide 52
4. Failure FACA
SPI image
OK
Loading station
NG
Link-1 image
Un-loading station
Mapping
VI 100%

**Table 1:**
| Component | R0304&L0301 | Vendor |  | APN | 118S00267 | Failure process/station | SPI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Issue Description | Printing solder excessive—Material issue  Defected rate:  0.35% (31F/8956T)              Before:  1.40% (7F/500T )    1st Config(X06P2-U1-MIYG2-SM）                              0.87% (18F/2080T ) 2nd Config(X06P2-U1-MIYG2-SM）                              0.31% (6F/1944T )   3rd Config(X06P2-U1-MINA7-SA)                                            After:   0.00%(0F/4432T)       4th~7th Config(X06P2-U1-MINA6-SA）                                                                                  X06P2-U1-MIYG2-SA-D1） |  |  |  |  |  |  |
| FA | SPI detected Printing solder excessive*31 pcs , defects are concentrated on 1st~3rd config, panels and cavities are not concentrated. SPI image shows no foreign material on the flex surface , but the solder paste has two phenomena of leakage and bridge. Confirm the Link-1 image that there is a circular foreign material on the flex surface , lock-in risk stand in front of Link-1. Confirm that there is circular scrap material on the flex surface of in the tray at loading station. Confirm the removal UV film station, operator tear film can not carry flex residual material from slot. Confirm the scrap is the same color as flex, it's hard to find and it's not easy to fall off. Conclusion：Flex scrap material leads to printing defects. |  |  |  |  |  |  |
| CA | ICT CA：Check whether there is excess material on the flex surface after panel to tray. Done 11/28 Xiaofeng Vendor FACA: 1.Scrap sticks to substrate when UV film is removed due to narrow cutting width, then scrap is dropped out. On-going 2/8 2.Increase laser width and improved process condition will be applied in EVT. On-going 2/8 ICT Proposal：Remove the flex scrap by Murata before delivery to ICT, On-going 1/16 |  |  |  |  |  |  |
| Validation | Tracked 4432pcs, the defective rate 0.00%(0F/4432T). Done 12/20 Xiaofeng |  |  |  |  |  |  |


## Slide 53
4. Failure FACA for Murata

## Slide 54
4. Failure FACA
OK
NG
Mapping
After

**Table 1:**
| Component | CL1_SUS_STIFFENER | Vendor | ICT | APN | / | Failure process/station | Post-AOI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Issue Description | Sus overlap--Material issue Defected rate:  0.26% (23F/8956T)              Before:  0.00% (0F/500T)     1st Config(X06P2-U1-MIYG2-SM)                             0.00% (0F/2080T)   2nd Config(X06P2-U1-MIYG2-SM)                             1.18% (23F/1944T) 3rd Config(X06P2-U1-MINA7-SA)                 After :  0.00% (0F/4432T)   4th~7th Config(X06P2-U1-MINA6-SA）                                                                                       X06P2-U1-MIYG2-SA-D1） |  |  |  |  |  |  |
| FA | Post-AOI detected sus overlap*23pcs, defects are concentrated on 3rd config CL1_SUS_STIFFENER clips , panels and cavities are not concentrated. Post-AOI images show that the sus overlap and Post-AOI program alarm float height. Confirm the Pre-AOI image the sus overlap, lock-in risk station is P&P. Confirm that the identification image and mounting parameters are normal，and check it not alarm record. Confirm that the raw material is found on both sides of the material tape is not sealed that can result in sus overlap. Simulation： Two materials in the same slot can suction by nozzle that can result in sus overlap after P&P. Conclusion：Double sides of the material tape are not sealed well, will resulting in clip overlap. |  |  |  |  |  |  |
| CA | ICT CA：Sorting materials and check the materials whether is sealed well before input. Done 12/07 Xiaofeng Vendor CA： 1.Increase the limit wall and deepen the cavity of the product in double side of tape for clip. Done 12/15 2.To move the seal location from up and down sealed to close to the clip. Done 12/15 |  |  |  |  |  |  |
| Validation | Tracked 4432pcs, the defective rate 0.00%(0F/4432T). Done 12/20 Xiaofeng |  |  |  |  |  |  |


## Slide 55
AP703  029-003H-0132-3  issue
1. Failure Description
4. Failure FACA for vendor
Heat seal line location

**Table 1:**
| 2.Containment action：  1.Client products to help select ------ Ma Wenhua 2024.12.14  2.No stock in XTL factory ----- Liu Jingjing 12/14 Completed | 3.Root cause & Corrective action： FA: 1.The depth of the carrier acupoint is shallow, the periphery has rounded corners, and the product is not completely sealed after entering the acupoint; 2.the use of upper and lower two knife seal, the product in the take, transport process up and down displacement. Reasons for outflow: The inspector failed to detect the outflow. CA: 1.Increase the retaining wall at both ends of the carrier belt to deepen the acupoints of the product, so that the product is not easy to move and jump out. ---- Wei Jie/Xu Bo The next batch is completed 2.The original upper and lower blades are sealed, now move the blades to the product position ---- Wei Jie/Xu Bo finished the next batch 3.Conduct publicity and quality training for abnormal information in the factory - Liu Jingjing/Wei Jie 2024/12/15 |
| --- | --- |
|  |  |


**Table 2:**
| Issue Date | 2024/12/13 | Vendor | XTL | IPN/ Config | 029-003H-0132-3 | Rej% | N/A |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCO | 029-003H-0132-3 | Location | IQC | D/C | 20241108 |  |  |
| Detail | 12/13 Customer feedback 029-003H-0132-3 Uneven packing, DC:20241108 |  |  |  |  |  |  |


## Slide 56
4. Failure FACA
Cover head over press cause PSA dent
Cover head touch PSA
Before
After

**Table 1:**
| Component | PSA | Vendor | ICT | APN | / | Failure process/station | Mic film remove |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Issue Description | PSA dent--Process issue  Defected rate:0.18% (16F/8,956T)             Before:0.79% (16F/2,030T)                After:0% (0F/6,926T) |  |  |  |  |  |  |
| FA | The defects were found in FVI, PSA dent were in same location. Per backend process mapping, the risk station was Mic film remove.   Check Mic film remove station: when removing film in fixture, OP manual close the cover head and over press have risk cause PSA dent.  Conclusion: The MIC film remove fixture was not  fool-proof cause PSA dent. |  |  |  |  |  |  |
| CA | 1.Modify fixture to fool-proof, cancel the cover head to avoid the PSA.    Done   DRI: Peng Huang  11/30 2.Update fixture design guideline, the structure need avoid to press PSA.   Done   DRI: Peng Huang  11/30 3.Cut in auto remove Mic film machine in EVT stage.   On-going   DRI: Kobe Zhang 2025 /2/7 |  |  |  |  |  |  |
| Validation | Keep tracking product, 0F/6,926T.    Done  12/20 |  |  |  |  |  |  |


## Slide 57

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 58
5. ORT Summary
Pass
Ongoing
Fail

**Table 1:**
| Bareflex / Assembly | Test | Total Q’ty | Input date | 100C | 200C | 300C | 400C | 500C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X06P2-U1-MIYG3-SM | 1.Heat Soak（500H) | 45 | 12/11 | PASS | PASS | PASS | PASS | 1/12 |
|  | 2.Thermal Cycling（500C) | 45 | 12/11 | PASS | PASS | PASS | PASS | 1/13 |
|  | 3.Thermal Shock（200C) | 45 | 12/12 |  | PASS |  |  |  |
|  | 4.Heat Soak and Flex Bending（168H) | 20 | 12/12 | PASS |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 12/14 | PASS |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 12/14 | PASS |  |  |  |  |
| X06P2-U1-MINX4-SM-D1 | 1.Heat Soak（500H) | 45 | 12/13 | PASS | PASS | PASS | PASS | 1/14 |
|  | 2.Thermal Cycling（500C) | 45 | 12/13 | PASS | PASS | PASS | PASS | 1/15 |
|  | 3.Thermal Shock（200C) | 45 | 12/16 |  | PASS |  |  |  |
|  | 4.Heat Soak and Flex Bending（168H) | 20 | 12/16 | PASS |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 12/16 | PASS |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 12/16 | PASS |  |  |  |  |
| X06P2-U1-MIYG2-SA-D1 | 1.Heat Soak（500H) | 45 | 12/18 | PASS | PASS | PASS | 1/12 | 1/19 |
|  | 2.Thermal Cycling（500C) | 45 | 12/18 | PASS | PASS | PASS | 1/13 | 1/20 |
|  | 3.Thermal Shock（200C) | 45 | 12/22 |  | PASS |  |  |  |
|  | 4.Heat Soak and Flex Bending（168H) | 20 | 1/2 | 1/11 |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 1/2 | 1/11 |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 1/2 | 1/11 |  |  |  |  |
| X06P2-U1-MINA6-SA | 1.Heat Soak（500H) | 45 | 12/18 | PASS | PASS | PASS | 1/12 | 1/19 |
|  | 2.Thermal Cycling（500C) | 45 | 12/18 | PASS | PASS | PASS | 1/13 | 1/20 |
|  | 3.Thermal Shock（200C) | 45 | 12/22 |  | PASS |  |  |  |
|  | 4.Heat Soak and Flex Bending（168H) | 20 | 1/2 | 1/11 |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 1/2 | 1/11 |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 1/2 | 1/11 |  |  |  |  |


## Slide 59
5. ORT Summary
Pass
Ongoing
Fail

**Table 1:**
| Bareflex / Assembly | Test | Total Q’ty | Input date | 100C | 200C | 300C | 400C | 500C |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X06P2-U1-MIYG2-SM | 1.Heat Soak（500H) | 45 | 12/24 | PASS | PASS | 1/12 | 1/18 | 1/25 |
|  | 2.Thermal Cycling（500C) | 45 | 12/24 | PASS | PASS | 1/13 | 1/19 | 1/26 |
|  | 3.Thermal Shock（200C) | 45 | 12/24 |  | PASS |  |  |  |
|  | 4.Heat Soak and Flex Bending（168H) | 20 | 1/6 | 1/15 |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 1/6 | 1/15 |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 1/6 | 1/15 |  |  |  |  |
| X06P2-U1-MINA7-SA | 1.Heat Soak（500H) | 45 | 12/23 | PASS | PASS | 1/11 | 1/17 | 1/24 |
|  | 2.Thermal Cycling（500C) | 45 | 12/24 | PASS | PASS | 1/13 | 1/19 | 1/26 |
|  | 3.Thermal Shock（200C) | 45 | 12/24 |  | PASS |  |  |  |
|  | 4.Heat Soak and Flex Bending（168H) | 20 | 1/6 | 1/15 |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 1/6 | 1/15 |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 1/6 | 1/15 |  |  |  |  |
| X06P2-U1-MIYG3-SA-D1 | 1.Heat Soak（500H) | 45 | 12/26 | PASS | PASS | 1/14 | 1/20 | 1/27 |
|  | 2.Thermal Cycling（500C) | 45 | 12/25 | PASS | PASS | 1/14 | 1/20 | 1/27 |
|  | 3.Thermal Shock（200C) | 45 | 12/24 |  | PASS |  |  |  |
|  | 4.Heat Soak and Flex Bending（168H) | 20 | 1/9 | 1/18 |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 1/9 | 1/18 |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 1/9 | 1/18 |  |  |  |  |


## Slide 60

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 61

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 62
7. Test Readiness and Automation Plan

**Table 1:**
| Test item | ERS/Test Plan | Test SW Readiness | Test HW Readiness | Test Automation | Test  Correlation With FATP IQC | Remark |
| --- | --- | --- | --- | --- | --- | --- |
| Inline 1KHZ sensitivity | Y | Y | Y | EVT | NA | Introduce from EVT |
| Inline RF | Y | Y | Y | EVT | NA | Introduce from EVT |
| Inline ICT | Y | Y | Y | EVT | NA | Introduce from EVT |
| OQC  Mic Function  FR/ THD & Sealing | Y | Y | Y | NA | Y | Apple specified test supplier |
| OQC RF | Y | Y | Y | EVT | Y | Introduce from EVT |
| OQC ICT | Y | Y | Y | EVT | Y | Introduce from EVT |


## Slide 63
7. Test CPK and Highlight

**Table 1:**
| Station | Test item Q’ty | CPK<1.33 | 1.33≤CPK<2.0 | CPK≥2.0 | Comments |
| --- | --- | --- | --- | --- | --- |
| Inline 1KHZ sensitivity | 2 | 0 | 0 | 2 |  |
| Inline RF | 7,540 | 0 | 0 | 7,540 |  |
| Inline ICT | 59 | 0 | 0 | 59 |  |
| OQC  Mic Function  FR/ THD & Sealing | 30 | 0 | 0 | 30 |  |
| OQC RF | 7,540 | 0 | 0 | 7,540 |  |
| OQC  ICT | 59 | 0 | 0 | 59 |  |


## Slide 64
7. Test Coverage
SCH

**Table 1:**
| Flex | Station | Coverage | FA | CA |
| --- | --- | --- | --- | --- |
| V53 UAT1 | RF&ICT &Mic Function | 172/180=95.55% | 1.R0303,R0304, R0401,R0402 0 ohm resistor occur short does not affect its resistance. 2.B2B 18,19,20,21Pin,same function pins are in the circuit，Short does not affect their connection. | SMT SPI/AOI and visual station will focus on check this position. With the other stations’ coverage, the whole coverage is 100%. |


## Slide 65
Test Coverage RF&ICT

**Table 1:**
| V53 UAT1 RF + ICT +Mic  Function |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CAP |  |  | IND |  |  | RES |  |  | IC |  |  |  | J_ UAT1 |  |  | Clip |  |
| Component | Open | Short | Component | Open | Short | Component | Open | Short | Component | Open | Short | ESD | Component | OPEN | Short | Component | Open |
| C0600 | Y | Y | L0600 | Y | Y | R0200 | Y | Y | U0300 | Y | Y | Y | J_ UAT1.PIN1 | Y | Y | CL_JINDO_M_TUNER | Y |
| C0300 | Y | Y | L0601 | Y | Y | R0303 | Y | N | U0301 | Y | Y | Y | J_ UAT1.PIN2 | Y | Y | CL_JINDO_M_GND | Y |
| C0320 | Y | Y | L0602 | Y | Y | R0304 | Y | N | U0302 | Y | Y | Y | J_ UAT1.PIN3 | Y | Y | CL3_SUS_STIFFENER | Y |
| C0322 | Y | Y | L0603 | Y | Y | R0401 | Y | N | U0303 | Y | Y | Y | J_ UAT1.PIN4 | Y | Y | CL_ANT10_GND | Y |
| C0323 | Y | Y | L0604 | Y | Y | R0402 | Y | N | U0400 | Y | Y | Y | J_ UAT1.PIN5 | Y | Y | CL_ANT10_FEED | Y |
| C0324 | Y | Y | L0605 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN6 | Y | Y | CL_ANT2_VERT_SP | Y |
| C0309 | Y | Y | L0606 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN7 | Y | Y | CL_ANT2_SHORT | Y |
| C0321 | Y | Y | L0607 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN8 | Y | Y | CL_ANT2_FEED | Y |
| C0325 | Y | Y | L0608 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN9 | Y | Y | CL2_SUS_STIFFENER | Y |
| C0326 | Y | Y | L0305 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN10 | Y | Y | CL_JINDO_L | Y |
| C0311 | Y | Y | L0307 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN11 | Y | Y | CL_STROBE_GND_EAST | Y |
| C0306 | Y | Y | L0301 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN12 | Y | Y | CL_STROBE_GND_WEST | Y |
| C0302 | Y | Y | L0300 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN13 | Y | Y | SR_SPKR_POS | Y |
| C0400 | Y | Y | L0406 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN14 | Y | Y | SR_SPKR_NEG | Y |
| C0401 | Y | Y | L0413 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN15 | Y | Y | CL1_SUS_STIFFENER | Y |
| C0418 | Y | Y | L0411 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN16 | Y | Y |  |  |
| C0411 | Y | Y | L0416 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN17 | Y | Y |  |  |
| C0410 | Y | Y | L0303 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN18 | Y | N |  |  |
| C0403 | Y | Y |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN19 | Y | N |  |  |
| C0402 | Y | Y |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN20 | Y | N |  |  |
| C0415 | Y | Y |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN21 | Y | N |  |  |
| C0412 | Y | Y |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN22 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN23 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN24 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN25 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN26 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN27 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN28 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN29 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN30 | Y | Y |  |  |


## Slide 66

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 67

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 68
9. MCO FAI / CPK Summary

**Table 1:**
| Config | Station | Total Qty | CPK<1.33 | 1.33≤CPK<1.67 | CPK≥1.67 | CPK Raw data and chart |
| --- | --- | --- | --- | --- | --- | --- |
| X06P2-U1-MIYG2-SM-GEN | FAI | 52 | 6 | 0 | 46 | Detail follow as FAI/CPK raw data |
|  | SPC | 37 | 0 | 0 | 37 |  |
| X06P2-U1-MIYG3-SM | FAI | 52 | 6 | 0 | 46 | Detail follow as FAI/CPK raw data |
|  | SPC | 37 | 0 | 0 | 37 |  |
| X06P2-U1-MINA7-SA | FAI | 52 | 6 | 0 | 46 | Detail follow as FAI/CPK raw data |
|  | SPC | 37 | 0 | 0 | 37 |  |
| X06P2-U1-MINA6-SA | FAI | 52 | 6 | 0 | 46 | Detail follow as FAI/CPK raw data |
|  | SPC | 37 | 0 | 0 | 37 |  |
| X06P2-U1-MIYG2-SA-D1 | FAI | 52 | 6 | 0 | 46 | Detail follow as FAI/CPK raw data |
|  | SPC | 37 | 0 | 0 | 37 |  |
| X06P2-U1-MINX4-SM-D1 | FAI | 52 | 6 | 0 | 46 | Detail follow as FAI/CPK raw data |
|  | SPC | 37 | 0 | 0 | 37 |  |
| X06P2-U1-MIYG3-SA-D1 | FAI | 52 | 6 | 0 | 46 | Detail follow as FAI/CPK raw data |
|  | SPC | 37 | 0 | 0 | 37 |  |


## Slide 69
9. Low CPK(CPK<1.67) FACA
Long term
FAI225/226/229/230 with proposal spec:±0.10mm,CPK>1.67
P2 data collection for reference
Current design
FAI225 CPK=0.984<1.67,FAI226 CPK=0.772<1.67
FAI229 CPK=0.954<1.67,FAI230 CPK=0.915<1.67

**Table 1:**
| MCO# | 056-21672-16 | Gerber# | POR:821-05715-02/DOE:921-05897-01 |
| --- | --- | --- | --- |
| Issue Description | FAI225/226/229/230 low CPK<1.67. |  |  |
| FA | Clip location dimensions is low CPK based on tolerance ±0.05mm. |  |  |
| CA/Suggestion | Short term: PD waive the FAI225/226/229/230 dimensions CPK<1.67 for P2. Long term: Suggest to release the FAI225/226/229/230 dimensions tolerance from ± 0.05mm to ±0.10mm in EVT. |  |  |
| Validation | Proposal for EVT |  |  |


## Slide 70
9. Low CPK(CPK<1.67) FACA
Long term
FAI233-1/233-2 with proposal spec:±0.20mm,CPK>1.67
P2 data collection for reference
Current design
FAI233-1 CPK=0.967<1.67
FAI233-2 CPK=0.948<1.67
D83 kenai MCO for reference
D83 kenai bonding data collection for reference, with tolerance ±0.20mm,CPK>1.67

**Table 1:**
| MCO# | 056-21672-16 | Gerber# | POR:821-05715-02/DOE:921-05897-01 |
| --- | --- | --- | --- |
| Issue Description | FAI233-1/FAI233-2 low CPK<1.67. |  |  |
| FA | Bonding dimensions is low CPK based on tolerance ±0.10mm. |  |  |
| CA/Suggestion | Short term: PD waive the FAI233-1/233-2 dimensions CPK<1.67 for P2. Long term: Suggest to release the FAI233-1/233-2 dimensions tolerance  from  0.10mm to ±0.20mm in EVT. |  |  |
| Validation | Proposal for EVT |  |  |


## Slide 71

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 72
10. Data Collection summary

**Table 1:**
| Items | Component | Criteria | 5x Test sample pictures | Result | Note |
| --- | --- | --- | --- | --- | --- |
| X-ray | B2B | Solder void<20% | Details as below | Pass |  |
|  | Clip | Solder void<35% | Details as below | Pass |  |
|  | BGA | Solder void<20% | Details as below | Pass |  |
|  | MIC | Solder void<25% | Details as below | Pass |  |
|  | Bending area | Trace no crack | Details as below | Pass |  |
| Cross section | B2B | 1. IMC thickness check2. solder thickness check | Details as below | Pass |  |
|  | Clip | 1. IMC thickness check2. solder thickness check | Details as below | Pass |  |
|  | BGA | 1. IMC thickness check2. solder thickness check | Details as below | Pass |  |
|  | MIC | 1. IMC thickness check2. solder thickness check | Details as below | Pass |  |
|  | Bending area | Trace no crack | Details as below | Pass |  |


## Slide 73
10. Data Collection summary

**Table 1:**
| Items | Component | Criteria | 5x Test sample pictures | Result | Note |
| --- | --- | --- | --- | --- | --- |
| Peeling test | Clip | Peeling force >5 N  No solder crack | Details as below | Pass |  |
|  | Bonding | Peeling force >5 N  No solder crack | Details as below | Pass |  |
|  | B2B | Peeling force >5 N  No solder crack | Details as below | Pass |  |
|  | BGA | No spec，for data collection | Details as below | Pass |  |
|  | MIC | Peeling force >5 N  No solder crack | Details as below | Pass |  |
| Pull test | Clip | Pull force >5 N  No solder crack | Details as below | Pass |  |
|  | Bonding | Pull force >5 N  No solder crack | Details as below | Pass |  |
|  | B2B | Pull force >5 N  No solder crack | Details as below | Pass |  |
|  | MIC | Pull force >5 N  No solder crack | Details as below | Pass |  |
| Shear test | B2B | Shear force >5 N  No solder crack | Details as below | Pass |  |
|  | BGA | Shear force >5 N  No solder crack | Details as below | Pass |  |


## Slide 74
Void: 0.17%
Void:0.5%
Void:0.24%
Void: 0.84%
Void: 2.27%
Void: 0.06%
Void: 0.12%
Void: 0.02%
Void:0.72%
Void:2.97%
Void:0.99%
Void:1.74%
Void:1.27%
Void:0.27%
Void:0.70%
Void: 0.42%
Void: 0.36%
Void: 0.14%
Void: 0.81%
Void:0.35%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | J-UAT1 | Solder void<20% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |


## Slide 75
Void: 0.86%
Void:0.18%
Void:1.19%
Void: 0.30%
Void: 0.13%
Void: 1.91%
Void: 0.92%
Void: 0.39%
Void:4.00%
Void:1.19%
Void:0.79%
Void:0.15%
Void:0.59%
Void:0.68%
Void:0.29%
Void: 0.03%
Void: 0.86%
Void: 1.67%
Void:0.77%
Void: 0.54%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | J-UAT1 | Solder void<20% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |


## Slide 76
Void: 1.52%
Void: 0.78%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | J-UAT1 | Solder void<20% |  |  |  |  |  | Pass |  |


## Slide 77
Void: 0.46%
Void:0.15%
Void: 0.11%
Void: 0.40%
Void: 1.45%
Void: 0.63%
Void:0.11%
Void:7.25%
Void:0.22%
Void:0.04%
Void:0.07%
Void:0.04%
Void:1.95%
Void:1.58%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | U0400 | Solder void<20% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  | U0301 |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |


## Slide 78
Void: 0.69%
Void:0.13%
Void: 0.27%
Void: 0.21%
Void: 0.37%
Void: 0.30%
Void:0.09%
Void:0.28%
Void:0.13%
Void:0.26%
Void:0.63%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | U0303 | Solder void<20% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |


## Slide 79
Void: 2.18%
Void:0.32%
Void: 2.86%
Void: 0.43%
Void: 1.46%
Void: 0.39%
Void:1.37%
Void:0.40%
Void: 0.14%
Void: 0.11%
Void: 0.10%
Void: 0.20%
Void: 0.03%
Void: 0.26%
Void: 0.12%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | U0302 | Solder void<20% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
| X-ray | U0300 |  |  |  |  |  |  | Pass |  |


## Slide 80
Void: 13.47%
Void: 14.08%
Void: 15.26%
Void: 12.71%
Void: 13.73%
Void: 14.71%
Void: 6.98%
Void: 7.04%
Void: 14.67%
Void: 7.80%
Void: 9.44%
Void: 9.10%
Void: 7.72%
Void: 6.96%
Void: 8.37%
Void: 7.19%
Void: 3.96%
Void: 6.75%
Void: 7.17%
Void: 4.50%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | SP-SPKR-POS | Solder void<35% |  |  |  |  |  | Pass |  |
|  | SP-SPKR-NEG |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  | CL-STROBE-GND-WEST |  |  |  |  |  |  | Pass |  |
|  | CL-ANT10-FEED |  |  |  |  |  |  | Pass |  |


## Slide 81
Void: 14.08%
Void: 10.35%
Void: 17.43%
Void: 10.59%
Void: 8.30%
Void: 9.10%
Void: 12.46%
Void: 10.63%
Void: 12.07%
Void: 9.62%
Void: 2.79%
Void: 4.10%
Void: 3.43%
Void: 3.77%
Void: 1.69%
Void: 4.05%
Void: 7.62%
Void: 6.85%
Void: 5.53%
Void: 7.07%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | CL-ANT10-GND | Solder void<35% |  |  |  |  |  | Pass |  |
|  | CL1-SUS-STIFFENER |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  | CL-ANT2-SHORT |  |  |  |  |  |  | Pass |  |
|  | CL-ANT2-VERT-SP |  |  |  |  |  |  | Pass |  |


## Slide 82
Void: 14.70%
Void: 3.87%
Void: 18.90%
Void: 17.28%
Void: 18.45%
Void: 14.83%
Void: 5.25%
Void: 2.61%
Void: 4.96%
Void: 4.31%
Void: 7.33%
Void: 10.36%
Void: 7.26%
Void: 19.09%
Void: 11.91%
Void: 8.15%
Void: 7.97%
Void: 8.25%
Void: 10.48%
Void: 13.30%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | CL-JINDO-L | Solder void<35% |  |  |  |  |  | Pass |  |
|  | CL2-SUS-STIFFENER |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  | CL-JINDO-M-GND |  |  |  |  |  |  | Pass |  |
|  | CL-JINDO-M-TUNER |  |  |  |  |  |  | Pass |  |


## Slide 83
Void: 7.93%
Void: 16.05%
Void: 2.61%
Void: 14.46%
Void: 8.44%
Void: 10.50%
Void: 11.36%
Void: 17.25%
Void: 14.94%
Void: 16.65%
Void: 12.13%
Void: 6.21%
Void: 4.26%
Void: 6.28%
Void: 2.23%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | CL3-SUS-STIFFENER | Solder void<35% |  |  |  |  |  | Pass |  |
|  | CL-STROBE-GND-EAST |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  | CL-ANT2-FEED |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Pass |  |


## Slide 84
Void: 0.72%
Void:0.84%
Void: 0.13%
Void: 1.94%
Void: 0.14%
Void: 0.36%
Void:1.71%
Void: 0.93%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | MIC | Solder void<20% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |


## Slide 85
Void: 8.07%
Void: 8.95%
Void: 7.46%
Void: 14.22%
Void: 3.63%
Void: 14.51%
Void: 13.43%
Void: 14.28%
Void: 4.55%
Void:9.76%
Void: 11.82%
Void: 4.06%
Void: 8.03%
Void: 9.69%
Void: 10.61%
Void: 8.98%
Void: 13.52%
Void: 2.11%
Void: 4.24%
Void: 6.22%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | Bonding | Solder void<35% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |


## Slide 86
Void: 19.79%
Void: 11.39%
Void: 23.92%
Void: 22.56%
Void: 21.90%
Void: 19.69%
Void: 24.11%
Void: 18.70%
Void: 19.95%
Void: 17.00%
Void: 13.80%
Void: 16.31%
Void: 23.44%
Void: 11.98%
Void: 23.61%
Void: 22.87%
Void: 21.03%
Void: 21.52%
Void: 13.92%
Void: 15.92%
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | Bonding | Solder void<35% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |


## Slide 87
Bending 1# & 12#
Bending 1# & 12#
Bending 1# & 12#
Bending 1# & 12#
Bending 1# & 12#
Bending 4# & 5#
Bending 4# & 5#
Bending 4# &5#
Bending 4# & 5#
Bending 4# & 5#
Bending 6# & 7#
Bending 6# & 7#
Bending 6# & 7#
Bending 6# & 7#
Bending 6# & 7#
10. Data Collection

**Table 1:**
| Items | Component | Criteria | location | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | Bending | Trace no crack in bending area |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |  | Pass |  |


## Slide 88
Bending 8# & 9#
Bending 8# & 9#
Bending 8# & 9#
Bending 8# & 9#
Bending 8# & 9#
Bending 10# & 11
Bending 10# & 11
Bending 10# & 11
Bending 10# & 11
Bending 10# & 11
Bending (1) &(2)
Bending (1) &(2)
Bending (1) &(2)
Bending (1) &(2)
Bending (1) &(2)
10. Data Collection

**Table 1:**
| Items | Component | Criteria | location | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X-ray | Bending | Trace no crack in bending area |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |  | Pass |  |


## Slide 89
G1
G2
P5
P6
P2
P3
P7
P1
P4
Solder Thickness :39.16µm
Solder Thickness :45.22µm
Solder Thickness :17.28µm
Solder Thickness :20.51µm
Solder Thickness :17.76µm
Solder Thickness :14.02µm
IMC Thickness :1.42~2.75µm
IMC Thickness :1.61~2.60µm
IMC Thickness :1.66~2.6µm
IMC Thickness :1.42	~2.37µm
IMC Thickness :1.56~2.6µm
IMC Thickness :1.66~3.08µm
Solder Thickness :10.75µm
IMC Thickness :1.28 ~2.32µm
Solder Thickness :11.98µm
IMC Thickness :1.42~2.23µm
Solder Thickness :19.18µm
IMC Thickness :1.89~2.94µm
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 90
P8
P9
P14
P15
P11
P12
G3
P10
P13
Solder Thickness :14.3µm
Solder Thickness :13.54µm
Solder Thickness :21.07µm
Solder Thickness :18.99µm
Solder Thickness :12.69µm
Solder Thickness :14.87µm
IMC Thickness :1.37~2.98µm
IMC Thickness :1.18~2.79µm
IMC Thickness :1.42~2.70µm
IMC Thickness :1.42~2.23µm
IMC Thickness :1.23~2.13µm
IMC Thickness :1.42~2.70µm
Solder Thickness :34.81µm
IMC Thickness :1.42~2.42µm
Solder Thickness :11.79µm
IMC Thickness :1.7~2.846µm
Solder Thickness :13.83µm
IMC Thickness :1.23~2.13µm
G1
P15
G2
P1
G4
G3
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 91
G4
G5
G7
G8
G6
Solder Thickness :21.07µm
Solder Thickness :45.56µm
Solder Thickness :29.13µm
Solder Thickness :37.27µm
IMC Thickness :1.52~3.84µm
IMC Thickness :1.66~3.79µm
IMC Thickness :1.68~3.36µm
IMC Thickness :1.66	~3.79µm
Solder Thickness :18.99µm
IMC Thickness :1.37~3.22µm
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |


## Slide 92
G9
G10
P20
P21
P17
P18
P22
P16
P19
Solder Thickness :46.98µm
Solder Thickness :55.55µm
Solder Thickness :33.39µm
Solder Thickness :34.14µm
Solder Thickness :32.58µm
Solder Thickness :26.85µm
IMC Thickness :1.61~3.46µm
IMC Thickness :1.89~3.40µm
IMC Thickness :1.61~2.89µm
IMC Thickness :1.80	~3.13µm
IMC Thickness :1.42~3.36µm
IMC Thickness :1.47~2.6µm
Solder Thickness :28.98µm
IMC Thickness :1.52~3.13µm
Solder Thickness :39.92µm
IMC Thickness :1.52~2.94µm
Solder Thickness :32.63µm
IMC Thickness :1.37~3.41µm
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 93
P23
P24
P29
P30
P26
P27
G11
P25
P28
Solder Thickness :29.69µm
Solder Thickness :28.51µm
Solder Thickness :22.26µm
Solder Thickness :26.33µm
Solder Thickness :23.82µm
Solder Thickness :24.96µm
IMC Thickness :1.52~2.70µm
IMC Thickness :1.66~3.13	µm
IMC Thickness :1.94~2.84µm
IMC Thickness :1.85~3.22µm
IMC Thickness :1.37~2.70µm
IMC Thickness :1.33~2.65µm
Solder Thickness :46.98µm
IMC Thickness :1.47 ~3.13µm
Solder Thickness :23.63µm
IMC Thickness :1.52~3.63µm
Solder Thickness :28.51µm
IMC Thickness :1.75~3.17µm
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 94
G12
G13
Solder Thickness :34.71µm
Solder Thickness :46.72µm
IMC Thickness :1.42~3.36µm
IMC Thickness :1.61~3.51µm
G13
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 95
G1
G9
P1
P16
G2
G10
Solder Thickness :47.26µm
Solder Thickness :59.43µm
Solder Thickness :52.56µm
Solder Thickness :53.15µm
Solder Thickness :35.23µm
Solder Thickness :26.28µm
IMC Thickness :1.47~2.89µm
IMC Thickness :1.62~3.31µm
IMC Thickness :1.56~3.56µm
IMC Thickness :1.41	~3.41µm
IMC Thickness :1.28~3.55µm
IMC Thickness :1.23~3.17µm
G1
P16
P1
G9
G2
G10
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 96
P3
P18
P7
P22
P5
Solder Thickness :22.64µm
Solder Thickness :25.90µm
Solder Thickness :31.29µm
Solder Thickness :25.96µm
Solder Thickness :19.91µm
IMC Thickness :1.33~2.65µm
IMC Thickness :1.52~3.27µm
IMC Thickness :1.28~3.79µm
IMC Thickness :1.33~3.46µm
IMC Thickness :1.42~3.46µm
P20
Solder Thickness :29.13µm
IMC Thickness :1.47~3.88µm
P3
P18
P5
P20
P7
P22
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 97
P9
P24
P13
P28
P11
Solder Thickness :27.13µm
Solder Thickness :26.98µm
Solder Thickness :20.13µm
IMC Thickness :1.66~3.69µm
IMC Thickness :1.85~3.61µm
IMC Thickness :1.43~2.78	µm
P20
Solder Thickness :15.06µm
IMC Thickness :1.66~3.46µm
P11
P26
P13
P28
P9
P24
Solder Thickness :23.29µm
Solder Thickness :21.68µm
IMC Thickness :1.85~3.36µm
IMC Thickness :1.75~3.65µm
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 98
P15
P30
G4
G12
G3
Solder Thickness :30.69µm
Solder Thickness :19.73µm
Solder Thickness :37.70µm
Solder Thickness :42.53µm
Solder Thickness :44.66µm
IMC Thickness :1.70~3.85µm
IMC Thickness :1.90~2.73µm
IMC Thickness :2.14~3.65µm
IMC Thickness :1.28~3.65µm
IMC Thickness :1.52~3.69µm
G11
Solder Thickness :40.09µm
IMC Thickness :1.46~2.97µm
G3
G11
G4
G12
P15
P30
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 99
G8
Solder Thickness :53.75µm
IMC Thickness :1.18~3.79µm
G8
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |


## Slide 100
Solder Thickness : 15.25µm
IMC Thickness :1.33~3.60µm
Solder Thickness : 17.81µm
IMC Thickness :1.56~3.27µm
Solder Thickness :32.82µm
IMC Thickness :1.56~3.27µm
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | CL_JINDO_L | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | PAD_GND_NORTH_TOP | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | PAD_GND_NORTH_BTTM | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |


## Slide 101
Solder Thickness : 15.39µm
IMC Thickness :1.42~3.55µm
Solder Thickness : 10.89µm
IMC Thickness :1.33~3.22µm
Solder Thickness :18.28µm
IMC Thickness :1.47~3.13µm
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | CL_ANT2_FEED | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | CL_ANT2_SHORT | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | CL_ANT_VERT_SP | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |


## Slide 102
Solder Thickness : 16.91µm
IMC Thickness :1.23~3.55µm
Solder Thickness : 29.98µm
IMC Thickness :1.18~3.55µm
Solder Thickness :17.05µm
IMC Thickness :1.28~3.55µm
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | CL_ANT10_FEED | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | CL_ANT10_GND | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | CL_STROBE_GND_WEST | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |


## Slide 103
Solder Thickness : 24.39µm
IMC Thickness :1.70~3.03µm
Solder Thickness : 29.27µm
IMC Thickness :1.23~3.79µm
Solder Thickness :26.21µm
IMC Thickness :2.09~3.26µm
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | SUS_Stiffener_TOP | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | CL_STROBE_GND_EAST | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | SP_SPKR_POS | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |


## Slide 104
Solder Thickness : 20.56µm
IMC Thickness :1.61~2.53µm
Solder Thickness : 16.81µm
IMC Thickness :1.42~3.74µm
Solder Thickness : 17.47µm
IMC Thickness :1.42~3.31µm
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | SP_SPKR_NEG | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | CL_JINDO_M_GND | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | CL_JINDO_M_TUNER | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |


## Slide 105
Solder Thickness : 31.02um
IMC Thickness :1.47~1.94µm
Solder Thickness : 36.65µm
IMC Thickness :2.27~3.6µm
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | L0406 | 1.Solder thickness(spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 106
P1
P4
P2
P3
IMC Thickness :1.28~1.89µm
IMC Thickness :1.37~2.27µm
IMC Thickness :1.28~2.94µm
IMC Thickness :1.33~3.08µm
P5
IMC Thickness :1.33~2.27µm
P1
P2
P4
P5
P3
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | U0300 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 107
P1
P2
P3
IMC Thickness :1.33～2.51µm
IMC Thickness :1.28~2.6µm
IMC Thickness :1.28~2.37µm
P6
P4
P5
IMC Thickness :1.32～2.39µm
IMC Thickness :1.22~2.85µm
IMC Thickness :1.22~1.95µm
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | U0301 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 108
P1
P2
P3
IMC Thickness :2.04～3.79µm
IMC Thickness :1.33~3.46µm
IMC Thickness :1.61~3.03µm
P6
P4
P5
IMC Thickness :1.85～2.68µm
IMC Thickness :2.23~2.79µm
IMC Thickness :1.85~3.79µm
P4
P2
P9
P7
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | U0302 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 109
P7
P8
P9
IMC Thickness :1.80～3.02µm
IMC Thickness :1.85~3.26µm
IMC Thickness :1.566~3.80µm
P10
IMC Thickness :1.61~3.56µm
P4
P2
P9
P7
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | U0302 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |


## Slide 110
P1
P2
P3
IMC Thickness :1.28～3.42µm
IMC Thickness :1.37~2.98µm
IMC Thickness :1.18~3.36µm
P4
P6
IMC Thickness :1.28~3.27µm
IMC Thickness :1.95~3.51µm
P1
P2
P3
P4
P6
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | U0303 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 111
P5
P7
P8
IMC Thickness :2.09～3.56µm
IMC Thickness :1.95~3.8µm
IMC Thickness :1.7~3.56µm
P11
P9
P10
IMC Thickness :1.61～3.41µm
IMC Thickness :1.56~3.80µm
IMC Thickness :1.95~3.07µm
P5
P7
P11
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | U0303 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 112
P1
P2
P3
IMC Thickness :1.22～3.65µm
IMC Thickness :1.75~3.12µm
IMC Thickness :1.27~3.36µm
P6
P4
P5
IMC Thickness :1.18～3.60µm
IMC Thickness :1.32~2.78µm
IMC Thickness :1.56~3.46µm
P4
P8
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | U0400 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 113
P7
P8
IMC Thickness :1.52～3.60µm
IMC Thickness :1.33~3.08µm
P8
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | U0400 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |


## Slide 114
Solder Thickness :35.66µm
IMC Thickness :1.23~2.04µm
Solder Thickness :40.39µm
IMC Thickness :1.23~2.18µm
Solder Thickness :41.39µm
IMC Thickness :1.23~3.03µm
P1
P3
P2
P1
P4
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | U0601 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 115
Solder Thickness :40.06µm
IMC Thickness :1.18~2.32µm
Solder Thickness :29.03µm
IMC Thickness :1.47~2.75µm
Solder Thickness :37.55µm
IMC Thickness :1.28~3.79µm
P4
P6
P5
P5
P8
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | U0601 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 116
Solder Thickness :38.78µm
IMC Thickness :1.18~2.23µm
Solder Thickness :38.83µm
IMC Thickness :1.7~2.32µm
P7
P8
P5
P8
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | U0601 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 117
PP0522
Solder Thickness :33.34µm
IMC Thickness :1.23~3.03µm
PP0521
Solder Thickness :35µm
IMC Thickness :1.23~2.98µm
PP0520
Solder Thickness :40.25µm
IMC Thickness :1.23~2.37µm
PP0522
PP0521
PP0520
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 118
PP0519
Solder Thickness :34.9µm
IMC Thickness :1.18~3.13µm
PP0515
Solder Thickness :38.83µm
IMC Thickness :1.42~2.84µm
PP0512
Solder Thickness :38.82µm
IMC Thickness :1.54~2.54µm
PP0519
PP0515
PP0512
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 119
PP0518
Solder Thickness :38.55µm
IMC Thickness :1.28~2.23µm
PP0509
Solder Thickness :41.34µm
IMC Thickness :1.28~2.7µm
PP0506
Solder Thickness :40.49µm
IMC Thickness :1.33~2.70µm
PP0509
PP0506
PP0518
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 120
PP0503
Solder Thickness :44.75µm
IMC Thickness :1.33~2.42µm
PP0523
Solder Thickness :35.00µm
IMC Thickness :1.33~2.70µm
PP0523
PP0503
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 121
PP0519
Solder Thickness :29.12µm
IMC Thickness :1.33~2.70µm
PP0517
Solder Thickness :37.6µm
IMC Thickness :1.37~2.42µm
PP0516
Solder Thickness :33.95µm
IMC Thickness :1.37~2.70µm
PP0519
PP0517
PP0516
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 122
PP0511
Solder Thickness :35.75µm
IMC Thickness :1.28~2.18µm
PP0508
Solder Thickness :32.06µm
IMC Thickness :1.47~2.42µm
PP0505
Solder Thickness :35.85µm
IMC Thickness :1.33~2.94µm
PP0511
PP0508
PP0505
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 123
PP0502
Solder Thickness :39.4µm
IMC Thickness :1.42~2.37µm
PP0523
Solder Thickness :37.08µm
IMC Thickness :1.28~2.84µm
PP0502
PP0523
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 124
PP0519
Solder Thickness :39.16µm
IMC Thickness :1.18~2.75µm
PP0514
Solder Thickness :38.69µm
IMC Thickness :1.47~2.94µm
PP0510
Solder Thickness :35.99µm
IMC Thickness :1.8~3.27µm
PP0519
PP0514
PP0510
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 125
PP0513
Solder Thickness :36.99µm
IMC Thickness :1.28~2.84µm
PP0507
Solder Thickness :34.71µm
IMC Thickness :1.42~2.65µm
PP0504
Solder Thickness :32.63µm
IMC Thickness :1.47~3.74µm
PP0513
PP0507
PP0504
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 126
PP0501
Solder Thickness :44.09µm
IMC Thickness :1.33~2.75µm
PP0523
Solder Thickness :35.23µm
IMC Thickness :1.23~3.08µm
PP0501
PP0523
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 127
PP0526
Solder Thickness :35.66µm
IMC Thickness :1.18~2.18µm
PP0525
Solder Thickness :32.91µm
IMC Thickness :1.33~2.46µm
PP0524
Solder Thickness :32.58µm
IMC Thickness :1.23~2.18µm
PP0526
PP0525
PP0524
10. Data Collection

**Table 1:**
| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |


## Slide 128
Bending 1# & 12#
Bending 1# & 12#
Bending 4# & 5#
Bending 4# & 5#
Bending 6# &7#
Bending 6# &7#
Bending 8# &9#
Bending 8# &9#
Bending 10# &11#
Bending 10# &11#
Bending (1)&(2)
Bending (1)&(2)
10. Data Collection

**Table 1:**
| Items | Component | Criteria | location | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cross section | Bending | Trace no crack in bending area |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |  | Pass |  |


## Slide 129
9.00N
9.81N
9.17N
8.77N
11.05N
6.60N
6.48N
7.70N
7.60N
5.98N
7.34N
6.53N
6.56N
6.80N
7.21N
8.96N
10.08N
9.81N
9.89N
10.43N
10. Data Collection

**Table 1:**
| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peeling test | CL_STROBE_GND_WEST_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT10_GND_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT10_FEED_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT2_VERT_SP-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |


## Slide 130
10.26N
10.14N
11.43N
8.75N
10.39N
9.48N
10.41N
9.31N
8.99N
9.89N
9.08N
9.85N
8.58N
7.30N
8.88N
5.15N
5.18N
5.69N
5.63N
5.63N
10. Data Collection

**Table 1:**
| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peeling test | CL_ANT2_SHORT_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT2_FEED_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_STROBE_GND_EAST_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_JINDO_L_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |


## Slide 131
8.86N
10.72N
10.62N
9.12N
10.07N
6.86N
5.48N
5.96N
5.99N
5.28N
7.49N
7.30N
6.17N
6.07N
6.76N
14.17N
14.26N
14.40N
13.45N
11.71N
10. Data Collection

**Table 1:**
| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peeling test | CL_JINDO_M_TUNER_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ JINDO_M_GND_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | Bonding - Z(PI) | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | Bonding - Z(LCP) | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |


## Slide 132
24.78N
21.15N
25.83N
25.96N
23.22N
9.94N
11.49N
9.49N
11.21N
10.69N
10. Data Collection

**Table 1:**
| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peeling test | MIC_U0600_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | JUAT1-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |


## Slide 133
9.94 N
11.49 N
9.49 N
11.21 N
10.69 N
13.96 N
15.89 N
13.43 N
17.51N
15.91 N
10. Data Collection for MIC Glue & No Glue Peeling

**Table 1:**
| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Peeling test | MIC_Z axis (No glue) | 1. Force >4N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Peeling test | MIC_Z axis (UV glue) | 1. Force >4N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |


## Slide 134
10. Data Collection for MIC Glue & No Glue Peeling

## Slide 135
56.57N
54.71N
53.34N
60.03N
57.72N
52.49N
50.35N
56.64N
58.20N
54.34N
75.4N
76.30N
76.88N
77.13N
64.86N
13.60N
11.13N
14.66N
14.50N
15.39N
10. Data Collection

**Table 1:**
| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pull test | CL_STROBE_GND_WEST_Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT10_GND_Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT10_FEED_X | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT2_VERT_SP-X | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |


## Slide 136
21.88N
22.85N
20.04N
22.51N
18.16N
87.09N
84.66N
86.67N
86.90N
84.96N
33.40N
28.70N
32.17N
35.35N
26.63N
63.56N
63.81N
57.15N
67.97N
61.39N
10. Data Collection

**Table 1:**
| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pull test | CL_ANT2_SHORT_Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT2_FEED_Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_STROBE_GND_EAST_X | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_JINDO_L_Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |


## Slide 137
75.89N
80.48N
74.16N
73.29N
72.26N
63.29N
71.17N
72.30N
69.27N
68.59N
59.98N
61.18N
65.23N
58.74N
60.38N
46.30N
45.53N
48.69N
47.19N
47.62N
10. Data Collection

**Table 1:**
| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pull test | CL_JINDO_M_TUNER_X | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ JINDO_M_GND_Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | Bonding - Y(PI) | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | Bonding - Y（LCP) | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |


## Slide 138
115.68N
119.20N
109.21N
99.27N
113.84N
57.04N
53.32N
51.12N
56.63N
57.40N
10. Data Collection

**Table 1:**
| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Pull test | MIC -X | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | JUAT1-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |


## Slide 139
112.28 N
118.5N
125.58 N
126.42 N
127.13 N
5.96N
6.53 N
6.76 N
5.25 N
6.04 N
7.59N
8.00N
5.59N
7.57N
7.39N
8.08N
7.00N
9.76N
8.64 N
10.54N
10. Data Collection

**Table 1:**
| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shear test | JUAT1-Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0300-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0301-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0302-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |


## Slide 140
12.31 N
13.60N
11.59N
10.70 N
12.05N
8.57 N
8.62 N
8.55 N
8.78 N
7.82 N
6.53N
6.96N
5.71N
6.45N
6.25N
6.21N
5.57 N
8.11N
7.27 N
7.06N
10. Data Collection

**Table 1:**
| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shear test | BGA U0303-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0400-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0300-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0301-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |


## Slide 141
8.70 N
6.92N
9.11 N
9.60 N
7.35 N
13.50 N
14.29 N
13.09 N
12.66N
13.52 N
8.60N
9.17N
11.19N
9.70N
9.00N
10. Data Collection

**Table 1:**
| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Shear test | BGA U0302-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0303-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0400-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |


## Slide 142

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 143
11. Assembly DFMEA top5

**Table 1:**
| Process | Failure Mode | Failure Eﬀects | Sev | Occ | Det | RPN | Current Design | Improved Design | Action Results |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  | Sev | Occ | Det | RPN |
| SMT | FAI225/226/229/230 has risk of low CPK | Affect FATP assembly | 7 | 4 | 6 | 168 | 0.05 tolerance for stiffener hole to flex hole | 1.Build and monitor, collect  data(SUS_STIFFENER_BOTTOM/TOP); 2. Control flex pad to flex hole tolerance. 3. Control stiffener outer and inner ring tolerance. 4.DFM propose to release stiffener location tolerance to 0.10 in EVT Result :  FAI225=0.984               FAI226=0.772               FAI229=0.954               FAI230=0.915 | 7 | 4 | 6 | 168 |
| Bonding | FAI233 has risk of low CPK | Affect FATP assembly | 7 | 4 | 6 | 168 | 0.1 tolerance for bonding process. | 1.Build and monitor, collect data;  2.Control incoming flex outline 0.05;  3.Optimize bonding fixture limitation. 4.DFM propose to release FAI233 dimension tolerance to 0.20 in EVT Result :  FAI233-1=0.967               FAI233-2=0.948 | 7 | 4 | 6 | 168 |
| SMT | Z direction peeling force is lower than the SPEC.( 5N Min) | Fall off in transfer process and assembly process in FATP. | 7 | 3 | 6 | 126 | Clip peeling start point is at the bottom layer. | 1.Build and monitor, collect  data(CL_JINDO_M_TUNER); 2.Add glue for force improvement if needed. Result :  Peeling force Z:(range:5.14-6.86N,mean:5.82N) | 7 | 2 | 6 | 84 |
| SMT | FAI10/11/2/4 has risk of low CPK | Affect FATP assembly | 7 | 3 | 6 | 126 | Tight tolerance | 1.Build and monitor, collect  data; 2.Control dimension in IQC and OQC;  Result :  CPK>1.67 | 7 | 2 | 6 | 84 |
| SMT | Reverse | Damage flex | 7 | 3 | 6 | 126 | Stiffener two sides is difficult to distinguish. | 1.Build and monitor, collect  data(SUS_STIFFENER_TOP/Bottom); 2.Carrier tab for 100% VI; 3.DFM propose to change clip plating spec in EVT, recognized clip flipped by color difference. Result : F/R=0F/8,956T | 7 | 2 | 6 | 84 |


## Slide 144
11. Assembly PFMEA top5

**Table 1:**
| Process | Failure Mode | Failure Effects | Sev | Occ | Det | RPN | Current process control | Improved control | Action results |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  | Sev | Occ | Det | RPN |
| UAT1 | Bonding coverage issue | Function issue | 6 | 5 | 5 | 150 | 1.Stencil opening follow cpp.2.SPI Inspection in spec.3.Bonding fixture and jig pressure in spec.4.Dispense flux parameter and Inspection in spec. | 1.Optimize stencil aperture.2. Jig pressure DOE.3.Build and monitor, data collection. 4.Result: F/R=0F/8956T | 6 | 4 | 5 | 120 |
| UAT1 | L0406 dispense issue | Cosmetic NG | 6 | 5 | 5 | 150 | 1.Dispense Parameter and UV volume follow CPP. 2.Optimize dispense DOE for it.3.Control the component shift issue. | 1optimize UV dispense parameter and path.2.Build and monitor, data collection. 3.Result: F/R=0F/8956T | 6 | 4 | 5 | 120 |
| UAT1 | PI flex warpage issue | Cosmetic NG | 6 | 5 | 4 | 120 | 1.Manual loading and unloading follow SOP.2.Use cover to press the flex in process.3.VI Handling follow SOP. | 1.process mapping data collection by every station.2.Define in SOP VI handling  can not touch it.3.Build and monitor, data collection. 4.Result: F/R=0F/8956T | 6 | 4 | 4 | 96 |
| UAT1 | Bonding area flux residual issue | Cosmetic NG | 5 | 4 | 4 | 80 | 1.Dispensing flux parameter and Inspection in spec.2.fixture design for flux residual.3.Reflow profile set up in spec. | 1.Optimize Bonding carrier design.2.Dispensing flux volume check.3.Build and monitor, data collection. 4.Result: F/R=0F/8956T | 5 | 3 | 4 | 60 |
| UAT1 | Clip deformation issue | Affect FATP assembly | 5 | 4 | 4 | 80 | 1.Op operation follow SOP production;2.Tray and carrier add avoid for clip; | 1.Build and monitor, collect data.2.IQC control.3.Fixture and package add avoid. 4.Result: F/R=0F/8956T | 5 | 3 | 4 | 60 |


## Slide 145

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 146
12. OK2FAB”build and collect data + Reject” item Follow up

**Table 1:**
| Item | Issue detail | Category | Apple DFM feed back | Build follow up result | Status / Next step |
| --- | --- | --- | --- | --- | --- |
| 1 | FAI225/226/229/230 has risk of low CPK<1.67. | Design | Build and monitor | Result :FAI225=0.984               FAI226=0.772               FAI229=0.954               FAI230=0.915 | Update clip location dimension tolerance, then it can meet CPK in EVT. |
| 2 | FAI233 has risk of low CPK<1.67. | Design | Build and monitor | Result :FAI233-1=0.967               FAI233-2=0.948 | Update bonding dimension tolerance, then it can meet CPK in EVT. |
| 3 | Clip CL_JINDO_M_TUNER has risk of low peeling force in Z-axis direction. | Design | Build and monitor | Result :  Peeling force Z:(range:5.14-6.86N,mean:5.82N) | Close |
| 4 | FAI223/224 has risk of low CPK<1.67. | Design | Build and monitor | Result : FAI223=6.803                FAI224=5.198 | Close |
| 5 | SMT solder clip has risk of reversal. | Design | Build and monitor | Result : F/R=0F/8,956T | Close |
| 6 | The restricted height of glue has low CPK risk base on Spec: Max:0.30mm(FAI260). | Design | Build and monitor | Result :FAI260-1=2.505               FAI260-2=4.473 | Close |
| 7 | FAI248 pull force has risk of low CPK<1.67. | Design | Build and monitor | Result :  FAI248=2.170(CL_STROBE_GND_WEST)  FAI248=6.673(CL_ANT10_GND)  FAI248=4.727(CL_ANT10_FEED)  FAI248=1.822(CL_ANT2_VERT_SP)  FAI248=2.167(CL_ANT2_SHORT)  FAI248=1.910(CL_ANT2_FEED)  FAI248=2.198(CL_STROBE_GND_EAST)  FAI248=2.707(CL_JINDO_L)  FAI248=6.697(CL_JINDO_M_TUNER)  FAI248=2.118(CL_ JINDO_M_GND) | Close |


## Slide 147

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 148
13. DFM on MCO, CPP, QCP design, automation, Quality, Eﬃciency, Cost reduction
P2 data collection for reference
Current design
FAI225 CPK=0.984<1.67,FAI226 CPK=0.772<1.67
FAI229 CPK=0.954<1.67,FAI230 CPK=0.915<1.67
Long term
FAI225/226/229/230 with proposal spec:±0.10mm,CPK>1.67

**Table 1:**
| MCO# | 056-21672-16 | Gerber# | POR:821-05715-02/DOE:921-05897-01 |
| --- | --- | --- | --- |
| Issue Description | FAI225/226/229/230 low CPK<1.67. |  |  |
| FA | Clip location dimensions is low CPK based on tolerance ±0.05mm. |  |  |
| CA/ Suggestion | Short term: PD waive the FAI225/226/229/230 dimensions CPK<1.67 for P2. Long term: Suggest to release the FAI225/226/229/230 dimensions tolerance from ± 0.05mm to ±0.10mm in EVT. |  |  |
| Validation | Proposal for EVT |  |  |


**Table 2:**
| Item | Category | Issue decription | Suggestions | Status |
| --- | --- | --- | --- | --- |
| 1 | Design | FAI225/226/229/230 has risk of low CPK<1.67. | Short term: PD waive the FAI225/226/229/230 dimensions CPK<1.67 for P2. Long term: Suggest to release the FAI225/226/229/230 dimensions tolerance from ± 0.05mm to ±0.10mm in EVT. |  |


## Slide 149
P2 data collection for reference
FAI233-1 CPK=0.967<1.67
FAI233-2 CPK=0.948<1.67
Current design
Long term
FAI233-1/233-2 with proposal spec:±0.20mm,CPK>1.67
D83 kenai MCO for reference
D83 kenai bonding data collection for reference, with tolerance ±0.20mm,CPK>1.67
13. DFM on MCO, CPP, QCP design, automation, Quality, Eﬃciency, Cost reduction

**Table 1:**
| MCO# | 056-21672-16 | Gerber# |  | POR:821-05715-02/DOE:921-05897-01 |
| --- | --- | --- | --- | --- |
| Issue Description | FAI233-1/FAI233-2 low CPK<1.67 |  |  |  |
| FA | Bonding dimensions is low CPK based on tolerance ±0.10mm. |  |  |  |
| CA/ Suggestion | Short term: PD waive the FAI233-1/233-2 dimensions CPK<1.67 for P2. Long term: Suggest to release the FAI233-1/233-2 dimensions tolerance  from  0.10mm to ±0.20mm in EVT. |  |  |  |
| Validation | Proposal for EVT |  |  |  |


**Table 2:**
| Item | Category | Issue decription | Suggestions | Status |
| --- | --- | --- | --- | --- |
| 2 | Design | FAI233-1/FAI233-2 has risk of low CPK<1.67. | Short term: PD waive the FAI233-1/233-2 dimensions CPK<1.67 for P2. Long term: Suggest to release the FAI233-1/233-2 dimensions tolerance  from  0.10mm to ±0.20mm in EVT. |  |


## Slide 150

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 151
Test instruction
Twisting location
Mishandling by engineer
Bending location
Pressing location
14.Mis-handling and Abuse Test Review – Test to fail

**Table 1:**
| Test condition | Location | Sample size |
| --- | --- | --- |
| Bending | 1 | 10x |
|  | 2 | 10x |
|  | 3 | 10x |
|  | 4 | 10X |
|  | 5 | 10x |
|  | 6 | 10x |
|  | 7 | 10x |
|  | 8 | 10x |
|  | 9 | 10x |
| Pressing | 10 | 10x |
|  | 11 | 10x |
|  | 12 | 10x |
|  | 13 | 10x |
|  | 14 | 10x |
|  | 15 | 10x |
|  | 16 | 10x |
|  | 17 | 10x |
|  | 18 | 10x |
| Twisting | 19 | 10x |
|  | 20 | 10x |
|  | 21 | 10x |
|  | 22 | 10x |
|  | 23 | 10x |
|  | 24 | 10x |
|  | 25 | 10x |
|  | 26 | 10x |


## Slide 152
Bending 45° one cycle
Bending 90° one cycle
Test method SOP
14.Mis-handling and Abuse Test Review – Test to fail

## Slide 153
Twisting 45° one cycle
Test method SOP
Twisting 90° one cycle
14.Mis-handling and Abuse Test Review – Test to fail

## Slide 154
Pressing one cycle
Step 2:
Pressing
Step 3:
Hold flex
Step 1:
Hold flex
Test method SOP
14.Mis-handling and Abuse Test Review – Test to fail

## Slide 155
Bending location
14.Mis-handling and Abuse Test Review – Test to fail

**Table 1:**
| Test instruction |  |  | Test items |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Location | Test condition |  | Sample Q'ty | Condition | Cosmetic inspection | Full function each time | X-ray inspection when fail | Cross section Validation |
| 1 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
| 2 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 46 cycles NG (2pcs) 47 cycles NG (3pcs) | 46 cycles NG (2pcs) 47 cycles NG (3pcs) | NG | NA |
| 3 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 38 cycles NG (1pcs) 40 cycles NG (4pcs) | 38 cycles NG (1pcs) 40 cycles NG (4pcs) | NG | NA |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 17 cycles NG (2pcs) 18 cycles NG (3pcs) | 17 cycles NG (2pcs) 18 cycles NG (3pcs) | NG | NA |
| 4 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 37 cycles NG (1pcs) 38 cycles NG (4pcs) | 37 cycles NG (1pcs) 38 cycles NG (4pcs) | NG | NA |
| 5 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
| 6 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
| 7 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |


## Slide 156
Bending location
Pressing location
14.Mis-handling and Abuse Test Review – Test to fail

**Table 1:**
| Test instruction |  |  | Test items |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Location | Test condition |  | Sample Q'ty | Condition | Cosmetic inspection | Full function each time | X-ray inspection when fail | Cross section Validation |
| 8 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 28 cycles NG (2pcs)29 cycles NG (3pcs) | 28 cycles NG (2pcs)29 cycles NG (3pcs) | NG | NA |
| 9 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 23 cycles NG (2pcs)24 cycles NG (3pcs) | 23 cycles NG (2pcs)24 cycles NG (3pcs) | NG | NA |
| 10 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 11 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 12 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 13 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 14 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 15 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 16 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 17 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 18 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |


## Slide 157
Twisting location
14.Mis-handling and Abuse Test Review – Test to fail

**Table 1:**
| Test instruction |  | Test items |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Location | Test condition | Sample Q'ty | Condition | Cosmetic inspection | Full function each time | X-ray inspection when fail | Cross section Validation |


**Table 2:**
| 19 | Twisting | 45° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 90° | 10pcs | 10 times | 2 cycles NG(4pcs) 3 cycles NG(6pcs) | 2 cycles NG(4pcs) 3 cycles NG(6pcs) | NG | NA |
| 20 | Twisting | 45° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | 90° | 10pcs | 10 times | 2 cycles NG(3pcs) 3 cycles NG(7pcs) | 2 cycles NG(3pcs) 3 cycles NG(7pcs) | NG | NA |
| 21 | Twisting | 45° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | 90° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 22 | Twisting | 45° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | 90° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 23 | Twisting | 45° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | 90° | 10pcs | 10 times | 7 cycles NG(4pcs) 8 cycles NG(6pcs) | 7 cycles NG(4pcs) 8 cycles NG(6pcs) | NG | NA |
| 24 | Twisting | 45° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | 90° | 10pcs | 10 times | 8 cycles NG(5pcs) 9 cycles NG(5pcs) | 8 cycles NG(5pcs) 9 cycles NG(5pcs) | NG | NA |
| 25 | Twisting | 45° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | 90° | 10pcs | 10 times | 2 cycles NG(5pcs) 3 cycles NG(5pcs) | 2 cycles NG(5pcs) 3 cycles NG(5pcs) | NG | NA |
| 26 | Twisting | 45° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | 90° | 10pcs | 10 times | 4 cycles NG(6pcs) 5 cycles NG(4pcs) | 4 cycles NG(6pcs) 5 cycles NG(4pcs) | NG | NA |


## Slide 158
Bending location
Failure mode
14.Mis-handling and Abuse Test Review – Test to fail

**Table 1:**
| Item | Location 3 | Location 2 | Location 3 | Location 4 | Location 8 | Location 9 |
| --- | --- | --- | --- | --- | --- | --- |
|  | Bending 45° | Bending 90° | Bending 90° | Bending 90° | Bending 90° | Bending 90’° |
| Cosmetic |  |  |  |  |  |  |
| X-ray |  |  |  |  |  |  |


## Slide 159
Bending 45° one cycle
Bending 90° one cycle
Bending location
14.Mis-handling and Abuse Test Review – Test to fail

**Table 1:**
| Item | Location 9 (No glue) | Location 9 (UV glue) |
| --- | --- | --- |
|  | Bending 90’° | Bending 90° |
| Cosmetic |  |  |
| X-ray |  |  |


**Table 2:**
| Test instruction |  |  | Test items |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Location | Test condition |  | Sample Q'ty | Condition | Cosmetic inspection | Full function each time | X-ray inspection when fail | Cross section Validation |
| 9 (No glue) | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 23 cycles NG (2pcs)24 cycles NG (3pcs) | 23 cycles NG (2pcs)24 cycles NG (3pcs) | NG | NA |
| 9 (With UV glue) | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |


## Slide 160
Twisting location
Failure mode
14.Mis-handling and Abuse Test Review – Test to fail

**Table 1:**
| Item | Location 19 | Location 20 | Location 23 | Location 24 | Location 25 | Location 26 |
| --- | --- | --- | --- | --- | --- | --- |
|  | Twisting 90° | Twisting 90° | Twisting 90° | Twisting 90° | Twisting 90° | Twisting 90° |
| Cosmetic |  |  |  |  |  |  |
| X-ray |  |  |  |  |  |  |


## Slide 161
Twisting location
9
Bending location
14.Mis-handling and Abuse Test Review – Test to fail

**Table 1:**
| Design Weakness FACA |  |  |  |  |
| --- | --- | --- | --- | --- |
| Location | Test  Failure FA | Improve plan | DRI | Due date |
| 9 | Location 9 failed at 90 degree bending less than 23 cycles. FA: (1) Per ICT process review, there are no risk to cause over bending 90°, low risk. (2) FATP need bending 180 degree and assemble, there are risk cause mic location crack. | 1.Optimize handling SOP for FATP 2.Do DOE add UV Gule in mic location，then 90 degree bending can more than 50cycles. | PQM/Jacs Huang,  PE/Peng Huang. PD/Carr Cui | 12/18 Done |
| 19&20&25 | Location 19&20&25 failed at 90 degree twisting less than 3  cycles. FA: (1) Flex thickness of location 19&20&25 are 0.28mm with 4 layers copper. (2) The torque of twisting is smaller. Per ICT process review, there are no risk to cause over twisting 90°, low risk. | Optimize handling SOP for FATP | PQM/Jacs Huang,  PE/Peng Huang. | 12/18 Done |


## Slide 162

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 163
15. NPI / MP Tooling status – From Bareflex to Assembly

**Table 1:**
| Station |  | Tooling | NPI soft tool | MP hard tool | FACA if not meet MP hard tool |
| --- | --- | --- | --- | --- | --- |
| Assembly | SMT | Carrier |  | V |  |
| Assembly | Glue | Carrier |  | V |  |
| Assembly | Bonding | Carrier |  | V |  |
| Assembly | PSA | Carrier |  | V |  |
| Assembly | Press | Fixture | V |  | Semi-auto |
| Assembly | Bending | Fixture | V |  | Semi-auto |
| Assembly | Test | ICT test | V |  | Semi-auto |
| Assembly | Test | RF test | V |  | Semi-auto |


## Slide 164

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 165

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 166
FA:
The bonding force between the MIC pad and the flex pad is smaller than FATP assembly mishandling force, resulting in cracking of the MIC solder pad in FATP inline.
V53 UAT1| Lesson learn from build(What can make the next build better)
Issue description:
The MIC solder pad cracking in FATP inline.
POR design
DOE design
Lesson learn:
Adding UV glue on the MIC edge can improve the bonding force between MIC pad and flex pad, reduce MIC solder pad cracking risk in FATP inline.
MIC edge without UV glue
MIC edge to add UV glue
MIC edge to add UV glue
FATP did not respond to the MIC solder pad cracking issue.
MIC edge with UV glue
MIC solder pad cracking
V53 UAT1
V54 UAT1
Box plots for reference

**Table 1:**
| Project | V53 UAT1 |  | V54 UAT1 |  |
| --- | --- | --- | --- | --- |
| Spec | ≥5.0N |  | ≥5.0N |  |
| UV glue (Y/N) | N | Y | N | Y |
| 1 | 9.34 | 13.96 | 9.55 | 22.78 |
| 2 | 11.49 | 15.89 | 9.92 | 22.35 |
| 3 | 9.49 | 13.43 | 10.53 | 22.46 |
| 4 | 11.21 | 17.51 | 9.66 | 19.66 |
| 5 | 10.69 | 15.91 | 8.44 | 24.56 |
| Min | 9.49 | 13.43 | 8.44 | 19.66 |
| Max | 11.49 | 17.51 | 10.53 | 24.56 |
| Average | 10.56 | 15.34 | 9.62 | 22.36 |
| Remark | V5X UAT1(without UV glue VS with UV glue):MIC edge add UV glue can increase the bonding force between MIC pad and flex pad |  |  |  |


## Slide 167
FA:
1.Clip structure is symmetric.
2.The contact side color is the same as the solder side.
V53 UAT1| Lesson learn from build(What can make the next build better)
Issue description:
AOI cannot identify clip contact side and solder side after flipping the clip, the contact side(burr side) has damage the flex risk.
Lesson learn:
Clip structure is symmetrical, AOI can not identify the contact side and solder side, by modifying the contact side and solder side color is different, so that AOI can realize recognition, to prevent contact side(burr side) damage flex.
Current design
Proposal design
Conclusion:
Clip solder side is changed from Ni to Sn, AOI can identify whether the clip solder side is turned over, prevent the contact side(burr side) from facing the flex pad and damaging the flex.
Contact side: Ni
Clip solder view for reference
AOI identifies resultsfor  for reference
Solder side: Ni
Contact side: Ni
Solder side: Sn
Contact side: Ni
Solder side: Sn
Contact side: Ni
Solder side: Ni
V5x UAT1
/Duran
V5x UAT2
The clip contact side up is pass, the clip solder side up is fail, and the AOI identification results are consistent with the actual sample side

**Table 1:**
| No. | 81 | 82 | 83 | 84 | 85 |
| --- | --- | --- | --- | --- | --- |
| PIC. |  |  |  |  |  |
| Result | PASS | PASS | PASS | PASS | PASS |
| No. | 91 | 92 | 93 | 94 | 95 |
| PIC. |  |  |  |  |  |
| Result | FAIL | FAIL | PASS | PASS | FAIL |


## Slide 168

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness (update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 169
18. V53 UAT1-Flex EVT automation readiness

**Table 1:**
| Project | NO. | Stage | Equipment | Q’ty | Equipment | Fixture |
| --- | --- | --- | --- | --- | --- | --- |
| V53 UAT1 | 1 | Pre-SMT | Singulator | 1 | 2/7 | 2/7 |
|  | 2 | Pre-SMT | Kapton auto placement | 1 | 2/7 | 2/7 |
|  | 3 | Pre-SMT | Auto loading | 1 | 2/7 | 2/7 |
|  | 4 | SMT | Add metal cover | 4 | 2/7 | 2/7 |
|  | 5 | SMT | Remove metal cover | 4 | 2/7 | 2/7 |
|  | 6 | SMT | Flipping | 4 | 2/7 | 2/7 |
|  | 7 | SMT | MIC Film P&P | 1 | 2/7 | 2/7 |
|  | 8 | SMT | Tape remove | 1 | 2/7 | 2/7 |
|  | 9 | SMT | SMT NG Part Pick up | 1 | 2/7 | 2/7 |
|  | 10 | SMT | Tray to bonding tray | 1 | 2/7 | 2/7 |


## Slide 170
18. V53 Strobe Tail EVT automation readiness

**Table 1:**
| Project | NO. | Stage | Equipment | Q’ty | Equipment | Fixture |
| --- | --- | --- | --- | --- | --- | --- |
| V53 Strobe | 1 | Pre-SMT | Tray to bonding tray | 1 | 2/7 | 2/7 |


## Slide 171
18. V53 UAT1 EVT automation readiness

**Table 1:**
| Project | NO. | Stage | Equipment | Q’ty | Equipment | Fixture |
| --- | --- | --- | --- | --- | --- | --- |
| V53 UAT1 Bonding | 1 | Bonding | Bonding flex loading | 1 | 2/3 | 2/7 |
|  | 2 | Bonding | Add press jig | 1 | 2/3 | 2/7 |
|  | 3 | Bonding | Remove press jig | 1 | 2/3 | 2/7 |
|  | 4 | Bonding | Add PSA support | 1 | 2/3 | 2/7 |
|  | 5 | Bonding | Flipping | 2 | 2/3 | 2/7 |
|  | 6 | Bonding | Remove bonding carrier & Add PSA cover | 1 | 2/3 | 2/7 |
|  | 7 | Bonding | Press | 2 | 2/3 | 2/7 |
|  | 8 | Bonding | Carrier to tray | 1 | 2/3 | 2/7 |
|  | 9 | BE | Auto bending | 1 | 2/3 | 2/7 |
|  | 10 | BE | Auto 1k test | 1 | 2/3 | 2/7 |
|  | 11 | BE | Auto RF/ICT test | 1 | 2/3 | 2/7 |
|  | 12 | BE | Transfer tray | 2 | 2/3 | 2/7 |
|  | 13 | BE | AVI | 1 | 2/3 | 2/7 |
|  | 14 | BE | Auto OQC RF/ICT test | 1 | 2/3 | 2/7 |
|  | 15 | Package | Auto scanner | 1 | 2/3 | 2/7 |


## Slide 172

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |


## Slide 173
Black: Customer control
Blue: ICT owned
19. Vendor owned MP key part supplier POR Plan

**Table 1:**
| Category | Component | P1 POR |  | P2 POR |  | P2 DOE |  | Remark |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Vendor | Type/APN | Vendor | Type/APN | Vendor | Type/APN |  |
| SMT | Flex | Murata | 821-05715-01 | Murata | 821-05715-02 | Murata | 921-05897-01 |  |
| SMT | Resistance | TDK | 107S00297*1 | TDK | 107S00297*1 | TDK | 107S00297*1 |  |
|  |  | YAGEO | 118S00267*6 | YAGEO | 118S00267*4 | YAGEO | 118S00267*5 |  |
| SMT | Inductor | TDK | 152S00401 | Murata | 152S00470,152S2036,152S00565, 152S00052, 152S00021, 152S02096, 152S2055, 152S00026, 152S00134, 152S01707*4, 152S01708*5 | Murata | 152S00470,152S2036,152S00565, 152S00052*2, 152S00021, 152S02096, 152S2055, 152S00026, 152S00134, 152S01707*4, 152S01708*5 |  |
|  |  | Murata | 152S00470,152S2036,152S00565, 152S00021*2,152S00153,152S02096, 152S00143*2,152S00026,152S00134, 152S01707*4,152S01708*5 |  |  |  |  |  |
| SMT | Capacitor | Murata | 138S00008*4,131S0278,131S00017*5, 131S00700,131S00646*3,131S0338, 131S00547*2,131S00698*3,131S0562 | Murata | 138S00008*4, 131S0337, 131S00017*5, 131S00863*4, 131S00883, 131S0731, 131S0351*2, 131S0559, 131S0561, 131S00264 | Murata | 138S00008*4, 131S0337, 131S00017*5, 131S00863*4, 131S00883, 131S0731, 131S0351*2, 131S0559, 131S0561, 131S00264 |  |
|  |  | TAIYO | 138S0692 | TAIYO | 138S0692 | TAIYO | 138S0692 |  |
| SMT | IC | Qorvo | 353S03284, 353S03594 | Qorvo | 353S03284, 353S03594, 353S03267 | Qorvo | 353S03284, 353S03594, 353S03267 |  |
|  |  | PSEMI | 353S04043, 353S03304 |  |  |  |  |  |
|  |  | Infineon | 353S03610 | PSEMI | 353S03654, 353S03304 |  | 353S03304*2 |  |
| SMT | B2B | Murata | 516S01290 | Murata | 516S01290 | Murata | 516S01290 |  |
| SMT | Clip | ENNOVI/LY | 806-50867,806-50868,806-50869, 806-50870,806-50871,806-50873, 806-51162,806-51201,806-51346, 806-51391,870-23917,870-23918*2 | ENNOVI/LY | 806-53698, 806-50869, 806-53763, 806-53387, 806-50871, 806-53366, 806-51162, 806-51391, 806-53371,  806-53367, 870-23918*2 | ENNOVI/LY | 806-53698, 806-50869, 806-53763, 806-53387, 806-50871, 806-53366, 806-51162, 806-51391, 806-53371,  806-53367, 870-23918*2 |  |
| SMT | PI flex | Mflex Avary | 821-05769-01 | Mflex Avary | 821-05769-02 | Mflex Avary | 821-05769-02 |  |
| SMT | MIC | GTK IFX AAC | 731-00333(R-G-P-8) 731-00333(R-G-P-9) 731-00334(R-X-R-2) 731-00337(R-A-P-8) | GTK AAC | 731-00333(R-G-Q-2) 731-00333(R-G-Q-3) 731-00337(R-A-Q-7) 731-00337(R-A-Q-6) | GTK IFX | 731-00333(R-G-Q-2) 731-00333(R-G-Q-3) 731-00334(R-X-R-4) |  |
| SMT | MIC film | JT/DX | / | JT/DX | / | JT/DX | / |  |
| SMT | PSA | JT/DX | / | JT/DX | / | JT/DX | / |  |


## Slide 174

**Table 1:**
| Item | Agenda |
| --- | --- |
| 0 | Round Table Introduction and Agenda |
| 1 | O-Chart and resource plan |
| 2 | Configs and Build status |
| 3 | IQC |
| 4 | Process yield of bare flex and flex Assembly |
| 5 | OQC Issue and ORT |
| 6 | Downstream/Customer issue review |
| 7 | Test review |
| 8 | Flex stackup with 5x cross-section data |
| 9 | Cp/Cpk histogram of FAI/SPC (32pcs) |
| 10 | Data collection review |
| 11 | DFMEA, PFMEA Top 5 issue update |
| 12 | Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |
| 13 | DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |
| 14 | Flex mishandling and abuse test review |
| 15 | NPI Soft tool and MP hard tool report |
| 16 | Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |
| 17 | Lesson learn from last generation and this build |
| 18 | EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |
| 19 | Vendor owned MP material supplier POR |
| 20 | MP Line Qual plan (update from EVT postmortem) |

