# [ICT] V53_P1_UAT1_Postmortem-V7_20240924_09.24.2024


## Slide 1: D23&V53 P1 Postmortem 
D23&V53 P1 Postmortem
Luxshare ICT
09-24-2024

## Slide 2
0. Meeting Agenda

| China Date:9/24 | CPTO Date:9/23 |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| China Time | CPTO Time | L/T | Content | Vendor Site | CPTO DFM DRI | I/R DFM DRI | I/R PQM DRI |
| 8:35~8:40 AM | 17:35~17:40 | 5 Mins | Team introduction | ICT KS | / | / | / |
| 8:40~9:05 AM | 17:40~18:05 | 25 Mins | V53 UAT1 Flex Review |  | Erfan Mohammadi | Mark Di | Mark Di |
| 9:05~9:30  AM | 18:05~18:30 | 25 Mins | V53 UAT2 Flex Review |  |  |  |  |
| 9:30~9:50 AM | 18:30~18:50 | 20 Mins | V53 Duran Flex Review |  |  |  |  |
| 9:50~10:15 AM | 18:50~19:15 | 25 Mins | D23 LAT1 Flex Review |  | Tamir Alquran | Liang Xu | Hansen Dai |
| 10:15~10:40 AM | 19:15~19:40 | 25 Mins | D23 LAT2 Flex Review |  | Tamir Alquran | Liang Xu | Hansen Dai |
| 10:40~11:05 AM | 19:40~20:05 | 25 Mins | D23 UAT1 Flex Review |  |  |  |  |
| 11:05~11:30 AM | 20:05~20:30 | 25 Mins | D23 UAT2 Flex Review |  |  |  |  |
| 11:30~11:40 AM | 20:30~20:40 | 10 Mins | Break time |  | / | / | / |
| 11:40~11:50 AM | 20:40~20:50 | 10 Mins | Close meeting |  | / | / | / |


## Slide 3

| Item | Agenda |
|---|---|
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


## Slide 4
0. Round table team introduction

| Department | Name | Title | Role | Contact |
|---|---|---|---|---|
| VP | Hanson Qian | VP | Overall | +86 185 1215 7889 Hanson.Qian@luxshare-ict.com |
| EPM | Judy Du | EPM Director | Overall | +86 182 6165 4167 judy@luxshare-ict.com |
|  | Winey Wang | EPM Manager | Overall | +86 151 5153 5501 Winey.wang@luxshare-ict.com |
|  | Zoe Zeng | EPM | Overall | +86 180 68074550 Zoe.zeng@luxshare-ict.com |
|  | Andrea Wang | EPM | D23 LAT1/LAT2/UAT1/UAT2 | +86 134 0513 2087 Andrea.wang@luxshare-ict.com |
|  | Rainie Bai | EPM | V53 Duran/UAT1/UAT2 | +86 188 7118 0984  Rainie.Bai@luxshare-ict.com |
| PD | Lucky Zhang | PD director | Overall | +86 150 5026 2518 Lucky.zhang@luxshare-ict.com |
| PD | James Cui | PD Manager | Overall | +86 159 5016 5664 James.Cui@luxshare-ict.com |
|  | Alan Zhu | PD Leader | D23/V53 Antenna Flex | +86 153 5846 0383 Alan.Zhu@luxshare-ict.com |
|  | Jianpan Xu | PD | D23 LAT1/LAT2/UAT1/UAT2 | +86 199 0703 3194 Jianpan.Xu@luxshare-ict.com |
|  | Carr Cui | PD | V53 Duran/UAT1/UAT2 | +86 185 1289 9436 Carr.Cui@luxshare-ict.com |
| Quality | Trench Li | Quality Manager | Overall | +86 186 6216 2818 Trench.Li@luxshare-ict.com |
|  | Qihui Cao | Quality Leader | D23/V53 Antenna Flex | +86 152 6240 2381 Qihui.Cao&luxshare-ict.com |
|  | Yaru Li | PQM | D23 LAT1/LAT2/UAT1/UAT2 | +86 136 2503 6253 Yaru.Li2@luxshare-ict.com |
|  | Yanmei Lu | PQM | V53 Duran/UAT1/UAT2 | +86 157 0510 7735 Yanmei.Lu@luxshare-ict.com |
|  | Kovu | SQE | D23/V53 Antenna Flex | + 86 158 5033 6437 Kovu.Gao@luxshare-ict.com |


## Slide 5
0. Round table team introduction

| Department | Name | Title | Role | Contact |
|---|---|---|---|---|
| DFM & SMT-PE | Daniel Zhang | DFM & PE Manager | Overall | +86 137 7313 9750 Daniel.zhang@luxshare-ict.com |
|  | Qaa Wang | DFM & PE Leader | D23&V53 Antenna Flex | +86 182 6161 6769 Qaa.Wang@luxshare-ict.com |
|  | Trees Yan | PE | D23 LAT1/LAT2/UAT1/UAT2 | +86 159 6253 1827 Trees.Yan@luxshare-ict.com |
|  | Jarvan Wang | DFM | D23 LAT1/LAT2/UAT1/UAT2 | +86 134 5179 3890 Jarvan.Wang@luxshare-ict.com |
|  | Zhilei Yan | PE | V53 Duran/UAT1/UAT2 | +86 159 2142 1514 Zhilei.Yan@luxshare-ict.com |
|  | Mingyang Wang | DFM | V53 Duran/UAT1/UAT2 | +86 151 1832 4193 Mingyang.Wang2@luxshare-ict.com |
| BE-PE | Aden Xu | BE-PE Manager | Overall | +86 158 0092 9551 Aden.Xu@luxshare-ict.com |
|  | Puck Zhang | BE-PE Leader | D23&V53 Antenna Flex | +86 182 6022 8177 Puck.Zhang@luxshare-ict.com |
| BE-PE | Guangjun Lin | BE PE | D23 LAT1/LAT2/UAT1/UAT2 | +86 180 7160 2057 Guangjun.Lin@luxshare-ict.com |
|  | Hpeng Huang | BE PE | V53 Duran/UAT1/UAT2 | +86 175 0161 9188 Hpeng.Huang@luxshare-ict.com |
| TE | Lang Cheng | TE Manager | Overall | +86 186 2171 1749 Lang.chen@lushare-ict.com |
|  | Kobe Zhang | TE Leader | D23&V53 Antenna Flex | +86 137 3266 5812 Kobe.Zhang@luxshare-ict.com |
|  | CK Huang | TE | D23 LAT1/LAT2/UAT1/UAT2 | +86 139 1553 7871 ck.huang@luxshare-ict.com |
|  | Yazhou Ding | TE | V53 Duran/UAT1/UAT2 | +86 175 0142 5525 Yazhou.Ding@luxshare-ict.com |


## Slide 6

| Item | Agenda |
|---|---|
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


## Slide 7
1. Site Management | ICT Flex Management System

## Slide 8

| Dept | Project HC Target | Project HC Actual | HC Gap | HC Hiring plan |
|---|---|---|---|---|
| EPM | 5 | 5 | 0 | NA |
| TPM/PMC/CSR | 12 | 12 | 0 | NA |
| PD/EE | 15 | 15 | 0 | NA |
| PQM | 5 | 5 | 0 | NA |
| SMT DFM/PE | 30 | 30 | 0 | NA |
| SMT QE | 8 | 8 | 0 | NA |
| Backend PE | 8 | 8 | 0 | NA |
| Testing | 8 | 8 | 0 | NA |
| AE | 4 | 4 | 0 | NA |
| IQC | 15 | 15 | 0 | NA |
| IPQC/OQC | 25 | 25 | 0 | NA |
| CQE | 4 | 4 | 0 | NA |
| Lab and Measurement | 56 | 56 | 0 | NA |
| Total |  | 195 | 0 | NA |

1. V53&D23 Antenna Flex | NPI Engineering Resource Plan

## Slide 9
D2 - 24,000㎡
D5
D23/V53 | Space/Layout---D5-1F
D5 Building
3rd Floor for D23V53 NPI
1st Floor for D23V53 NPI

## Slide 10
D23/V53 | NPI workshop Space/Layout---D5-1F

| D23V53  NPI  Production Line Resource |  |  |
|---|---|---|
| SMT  Line | V53 Duran/V53 Strobe /D23 UAT1 | Dedicated 1×for V53 Duran/V53 Strobe /D23 UAT1 share line |
|  | D23 LAT2 | Dedicated 1×for  D23 LAT2 share line |
|  | V53 UAT1 /D23 UAT2- Bonding | Dedicated 1×for  V53 UAT1 / D23 UAT2 Bonding share line |
|  | V53 UAT2/D23 UAT2 | Dedicated 1×for  V53 UAT2/D23 UAT2 share line |

SMT: 5 Lines

## Slide 11
SMT: 2 Lines

| D23V53  NPI  Production Line Resource |  |  |
|---|---|---|
| Backend Line | Duran | Dedicated 1×for V53 |
|  | UAT1 | Dedicated 1×for D23 |
|  |  | Dedicated 1×for V53 |
|  | UAT2 | Dedicated 1×for D23 |
|  |  | Dedicated 1×for V53 |
|  | LAT1 | Dedicated 1×for D23 |
|  | LAT2 | Dedicated 1×for D23 |


| D23V53  NPI  Production Line Resource |  |  |
|---|---|---|
| SMT Line | V53 UAT1 | Dedicated 1×for V53 UAT1 share line |
|  | D23 LAT1 | Dedicated 1×for D23 LAT1 share line |

BE： 8 Lines
D23/V53 | NPI workshop Space/Layout---D5-3F

## Slide 12

| Project | Line | Flex | P1 line Q'ty | Line | Floor |
|---|---|---|---|---|---|
| D23V53 | SMT | V53 Duran/V53 Strobe /D23 UAT1 | 1 line | Share  line | D5-1F |
|  |  | D23 LAT2 | 1 line | Share  line |  |
|  |  | V53 UAT1 Bonding/D23 UAT2 Bonding | 1 line | Share  line |  |
|  |  | V53 UAT2/D23 UAT2 | 1 line | Share  line |  |
|  |  | V53 UAT1 | 1 line | Share  line | D5 3F |
|  |  | D23 LAT1 | 1 line | Share  line |  |

D23/V53 P1 readiness review (line design plan for SMT)
Note: Total 6 lines for D23V53 Phone flex  P1 SMT

## Slide 13
Note: Total 7 short lines for D23V53 Phone flex P1 Backend

| Project | Line | Flex | P1 Bending line Q'ty (manual) | P1 1K Test line Q'ty (manual) | P1 RF/ICTTest line Q'ty(manual) | Floor |
|---|---|---|---|---|---|---|
| D23V53 | Backend | V53 Duran | 1 | NA | 1 | D5 3F |
|  |  | D23 UAT1 | 1 | NA | 1 |  |
|  |  | V53 UAT1 | 1 | 1 | 1 |  |
|  |  | D23 UAT2 | 1 | NA | 1 |  |
|  |  | V53 UAT2 | 1 | NA | 1 |  |
|  |  | D23 LAT1 | 1 | NA | 1 |  |
|  |  | D23 LAT2 | 1 | NA | 1 |  |

D23/V53 P1 readiness review (line design plan for Backend)

## Slide 14
V53 Duran/UAT1/UAT2 & D23 LAT1/LAT2/UAT1/UAT2 P1 build Postmortem Dashboard
Low risk
Medium risk
High risk

| Postmortem Content | D53 UAT1 Flex | D53 UAT2 Flex | V53 Duran Flex | D23 LAT1 Flex | D23 LAT2 | D23 UAT1 | D23 UAT2 |
|---|---|---|---|---|---|---|---|
| 1 O-Chart and resource plan |  |  |  |  |  |  |  |
| 2 Configs and Build status |  |  |  |  |  |  |  |
| 3 IQC |  |  |  |  |  |  |  |
| 4 Process yield of bare flex and flex Assembly |  |  |  |  |  |  |  |
| 5 OQC Issue and ORT |  |  |  |  |  |  |  |
| 6 Downstream/Customer issue review |  |  |  |  |  |  |  |
| 7 Test review |  |  |  |  |  |  |  |
| 8 Flex stackup with 5x cross-section data |  |  |  |  |  |  |  |
| 9 Cp/Cpk histogram of FAI/SPC (32pcs) |  |  |  |  |  |  |  |
| 10 Data collection review |  |  |  |  |  |  |  |
| 11 DFMEA, PFMEA Top 5 issue update |  |  |  |  |  |  |  |
| 12 Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality |  |  |  |  |  |  |  |
| 13 DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction |  |  |  |  |  |  |  |
| 14 Flex mishandling and abuse test review |  |  |  |  |  |  |  |
| 15 NPI Soft tool and MP hard tool report |  |  |  |  |  |  |  |
| 16 Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |  |  |  |  |  |  |  |
| 17 Lesson learn from last generation and this build |  |  |  |  |  |  |  |
| 18 EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |  |  |  |  |  |  |  |
| 19 Vendor owned MP material supplier POR |  |  |  |  |  |  |  |
| 20 MP Line Qual plan (update from EVT postmortem) |  |  |  |  |  |  |  |


## Slide 15: V53 UAT1 P1 Postmortem 
V53 UAT1 P1 Postmortem
Luxshare ICT
09-24-2024

## Slide 16
V53 UAT1 P1 build Postmortem Dashboard

| Postmortem Content | V53 UAT1 Flex |
|---|---|
| 1 O-Chart and resource plan |  |
| 2 Configs and Build status |  |
| 3 IQC | 1. APN: 821-05769, vendor Avary, Failure in FAI 5 low CPK, A customer waive for P1 data collect. |
| 4 Process yield of bare flex and flex Assembly |  |
| 5 OQC Issue and ORT |  |
| 6 Downstream/Customer issue review |  |
| 7 Test review |  |
| 8 Flex stackup with 5x cross-section data |  |
| 9 Cp/Cpk histogram of FAI/SPC (32pcs) | 1. FAI148/149/150/151/152/153/154 has risk of low CPK<1.67 |
| 10 Data collection review |  |
| 11 DFMEA, PFMEA Top 5 issue update |  |
| 12 Follow up of DFM “build and collect data” items when OK2Fab, plus monitoring and reject item, which impact quality | 1.FAI148/149/150/151/152/153/154 has risk of low CPK<1.67 2.Clip CL_JINDO_M_TUNER has risk of low peeling force. 3.Pre solder need to be printed on UAT1 pad based V53 UAT1+strobe process,  so small pads should be define in UAT1. |
| 13 DFM on design, MCO, CPP/QCP, automation, quality, efficiency and cost reduction | Same as item12 |
| 14 Flex mishandling and abuse test review |  |
| 15 NPI Soft tool and MP hard tool report |  |
| 16 Cycle time report, MP layout proposal(line QTY), automation and one piece flow line plan (update from EVT) |  |
| 17 Lesson learn from last generation and this build |  |
| 18 EVT readiness(update from P2 postmortem), MP readiness (update from EVT postmortem) + Automation/ traceability scores |  |
| 19 Vendor owned MP material supplier POR |  |
| 20 MP Line Qual plan (update from EVT postmortem) |  |

Low risk
Medium risk
High risk

## Slide 17

| Item | Agenda |
|---|---|
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


## Slide 18

| Items | Last Generation | P1:X06P1-U1-MIYG8-SM | P1:X06P1-U1-MIYG9-SM | P1:X06P1-U1-MINX2-SA | P1:X06P1-U1-MINX2-SA-D1 | P1:X06P1-U1-MIYG8-SM-D1 | P1:X06P1-U1-MIYG9-SM-D1 | P1:X06P1-U1-MINA8-SA-D1 |
|---|---|---|---|---|---|---|---|---|
| FPC | 4layers,Murata | 4layers,Murata | Same | Same | 4layers,DOE Murata | 4layers,DOE Murata | 4layers,DOE Murata | 4layers,DOE Murata |
| LCR | CAP*14,  IND*6,  RES*2 | CAP*22,  IND*21,  RES*7 | Same | Same | CAP*21,  IND*24,  RES*7 | CAP*21,  IND*24,  RES*7 | CAP*21,  IND*24,  RES*7 | CAP*21,  IND*24,  RES*7 |
| IC | U0300:353S0330 (PSEMI) U0310:353S03654 (PSEMI) U0402:353S032651 (QORVO) | U0300:353S03304 (Psemi) U0301:353S03610 (Infineon) U0302:353S03284 (QORVO) U0303:353S03594 (QORVO) U0400:353S04043 (Psemi) | Same | Same | Same | Same | Same | Same |
| Clip | Clip*10（Ennovi/LY） | Clip*13(LY) Clip*2(XTL) | Same | Clip*13(Ennovi) Clip*2(XTL) | Clip*13(Ennovi) Clip*2(XTL) | Same | Same | Clip*13(Ennovi) Clip*2(XTL) |
| Conn. | APN:516S00528 | APN:516S01290 | Same | Same | Same | Same | Same | Same |
| MIC | / | MIC*1, GTK 731-00333 (R-G-P-8) | MIC*1, GTK 731-00333 (R-G-P-9) | MIC*1, IFX 731-00334 (R-X-R-2) | MIC*1, IFX 731-00334 (R-X-R-2) | Same | MIC*1, GTK 731-00333 (R-G-P-9) | MIC*1, AAC 731-00337 (R-A-P-8) |
| PSA | PSA*1 | PSA*5 | Same | Same | Same | Same | Same | Same |
| MIC film | / | MIC  Film*1 | Same | Same | Same | Same | Same | Same |
| PCB | Honeycrisp,4 layer (ICT-UMTC/ICT-LGIT /LGIT-LGIT) | / | / | / | / | / | / | / |
| PI flex | / | Strobe tail, 3 layer (Mflex) | Same | Strobe tail, 3 layer (Avary) | Strobe tail, 3 layer (Avary) | Same | Same | Strobe tail, 3 layer (Avary) |
| 2D Barcode | 7.01*5.00mm,half adhesive | 7.01*4.00mm,half adhesive | Same | Same | Same | Same | Same | Same |
| Diﬀerence / picture |  |  |  |  |  |  |  |  |

2. Configs - Design Highlight and Comparison
D93 UAT1
V53 UAT1

## Slide 19
2. V53 UAT1 P1 build status

| Config | Description | Bareflex | Assembly | Ship to | Shipment Qty | Build Status |  | Remark |
|---|---|---|---|---|---|---|---|---|
| X06P1-U1-MIYG8-SM | 821-05715-01 | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 525 | Finish all shipment |  |  |
| X06P1-U1-MIYG9-SM | 821-05494-01 | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 525 | Finish all shipment |  |  |
| X06P1-U1-MINX2-SA |  | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 525 | Finish all shipment |  |  |
| X06P1-U1-MINX2-SA-D1 | 921-05695-01 | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 250 | Finish all shipment |  |  |
| X06P1-U1-MIYG8-SM-D1 |  | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 250 | Finish all shipment |  |  |
| X06P1-U1-MIYG9-SM-D1 |  | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 250 | Finish all shipment |  |  |
| X06P1-U1-MINA8-SA-D1 |  | Front-end Nomi Back-end Shenzhen | ICT-KS | FXGL | 250 | Finish all shipment |  |  |


## Slide 20

| Item | Agenda |
|---|---|
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


## Slide 21
3.V53 UAT1 IQC Summary and Highlight Summary

| Item | Cosmetic | Dimension | Function/Characteristic | Package |
|---|---|---|---|---|
| Bare Flex (both PI and LCP) |  | APN: 821-05769, vendor Avary, Failure in FAI 5 low CPK, A customer waive for P1 data collect. |  |  |
| Clip |  |  |  |  |
| PSA |  |  |  |  |
| B2B connector |  |  |  |  |
| Barcode |  |  |  |  |
| Chip |  |  |  |  |
| IC |  |  |  |  |
| MIC |  |  |  |  |
| Packing Tray |  |  |  |  |


## Slide 22
3.V53 UAT1 IQC Summary and Highlight
Pass
Fail

| Component type | Supplier | Sampling Size | Checking items | Methodology | Result | Remark |
|---|---|---|---|---|---|---|
| Bare Flex (both PI and LCP) | MURATA Avary Mflex | AQL 0.4 | Cosmetic | CCD | Pass |  |
|  |  | 32pcs | Dimension-FAI | OMM | Avary: 1 dimension low CPK | A customer waived |
|  |  | 32pcs | Dimension-SPC | OMM | Pass |  |
|  |  | 3pcs | Solderability | Solder Oven | Pass |  |
|  |  | 32pcs | Ni/Au Thickness | XRF | Pass |  |
|  |  | 32pcs | Barcode readability | 2DBC grade scanner | Pass |  |
|  |  | 3pcs | WCA | WCA Fixture | Pass |  |
| Clip | ENNOVI TLG XTL | AQL 0.4 | Cosmetic | CCD | Pass |  |
|  |  | 32pcs | Dimension-FAI | OMM | Pass |  |
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


## Slide 23
3.V53 UAT1 IQC Summary and Highlight
Pass
Fail

| Component type | Supplier | Sampling Size | Checking items | Methodology | Result | Remark |
|---|---|---|---|---|---|---|
| B2B connector | MURATA | AQL 0.4 | Cosmetic | CCD | Pass |  |
|  |  | 32pcs | Dimension-FAI | OMM | Pass |  |
|  |  | 32pcs | Dimension-SPC | OMM | Pass |  |
|  |  | 32pcs | Coplanarity & warpage (before & after reflow 2 times) | OMM | Pass |  |
|  |  | 32pcs | Plating Thickness | XRF | Pass |  |
|  |  | 5pcs | Solderability | Solder oven | Pass |  |
| Barcode | FZX LD | 5pcs | Cosmetic | CCD | Pass |  |
|  |  | 32pcs | Dimension | OMM | Pass |  |
|  |  | 32pcs | Thickness | Micrometer | Pass |  |
|  |  | 5pcs | Single pcs Pre-Peel test | Manual | Pass |  |
|  |  | 5pcs | Adhesive Peeling Force | Tension meter | Pass |  |
| Chip | MURATA TDK YAGEO | 5pcs | Cosmetic | CCD | Pass |  |
|  |  | 32pcs | Dimension-SPC | Caliper | Pass |  |
|  |  | 32pcs | Dimension-FAI | Caliper | Pass |  |
|  |  | 10pcs | Solderability | Solder oven | Pass |  |
|  |  | 32pcs | Function | LCR | Pass |  |


## Slide 24
3.V53 UAT1 IQC Summary and Highlight
Pass
Fail

| Component type | Supplier | Sampling Size | Checking items | Methodology | Result | Remark |
|---|---|---|---|---|---|---|
| IC | Qorvo Psemi Infineon | AQL 0.4 | Cosmetic | CCD | Pass |  |
|  |  | 32pcs | Plating thickness | XRF | Pass |  |
|  |  | 5pcs | Solderability | Solder Oven | Pass |  |
|  |  | 32pcs | Dimension-FAI | Caliper | Pass |  |
|  |  | 32pcs | Dimension-SPC | Caliper | Pass |  |
| MIC | GMI AAC Infineon | 5pcs | Cosmetic | CCD | Pass |  |
| Shim | LS MARIAN | 5pcs | Dimension-FAI | OMM | Pass |  |
|  |  | 32pcs | Dimension-SPC | OMM | Pass |  |
|  |  | 32pcs | Thickness | Micrometer | Pass |  |
|  |  | 10pcs | Shear off & peeling test | Tension meter | Pass |  |
| Packing Tray | KD | AQL 0.4 | Cosmetic | CCD | Pass |  |
|  |  | 5pcs | ESD | lmpedancemeter | Pass |  |
|  |  | 5pcs | Dimension | Caliper | Pass |  |


## Slide 25
3. V53 Strobe Tail IQC Summary and Highlight Summary
Dimension issue:
Avary:821-04987, FAI 5 low CPK
FA:
FAI5 2*R0.3±0.20 CPK<1.33，FAI 5-1 is less than 1/4 arc，FAI 5-2 is less than 1/8 arc(Measurement equipment capability>1/4 arc)，Inaccurate point capture leads to unstable measurement.
CA:
1.Avary suggests to waive issues for this build， A customer waive for P1.
2.Avary suggests to remove FAI 5，or change the two dimension as reference.

## Slide 26
3.V53 UAT1 Flex Waiver List

| Item | Vendor | APN | Waiver item | Waiver Description | Analysis | Waiver approval date | Waiver approver | Build Impact |
|---|---|---|---|---|---|---|---|---|
| 1 | Avary | 821-05769 | Dimension | FAI 5 dimension is low cpk | FA:FAI5 2*R0.3±0.20 CPK<1.33，FAI 5-1 is less than 1/4 arc，FAI 5-2 is less than 1/8 arc(Measurement equipment capability>1/4 arc)，Inaccurate point capture leads to unstable measurement.CA:1.Avary suggests to waive issues for this build2.Avary suggests to remove FAI 5，or change the two dimension as reference,please help to confirm | 2024/8/2 | Cus Mueller | No influence |


## Slide 27
3.V53 UAT1 Flex FAI Dimension CPK Distribution Summary
Pass
Fail

| SN | FAI | Nominal | Tol | Tol | CPK(Spec>1.33) |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI40 | 16.880 | 0.100 | 0.100 | 13.157 | 12.481 | Pass |  |
| 2 | FAI41 | 17.630 | 0.100 | 0.100 | 10.909 | 11.913 | Pass |  |
| 3 | FAI44 | 9.610 | 0.100 | 0.100 | 11.493 | 11.880 | Pass |  |
| 4 | FAI45 | 5.580 | 0.100 | 0.100 | 14.843 | 14.314 | Pass |  |
| 5 | FAI49 | 0.500 | 0.100 | 0.100 | 13.277 | 14.309 | Pass |  |
| 6 | FAI51 | 7.490 | 0.100 | 0.100 | 8.667 | 9.246 | Pass |  |
| 7 | FAI53 | 4.910 | 0.100 | 0.100 | 5.114 | 4.711 | Pass |  |
| 8 | FAI54 | 5.030 | 0.100 | 0.100 | 3.651 | 3.331 | Pass |  |
| 9 | FAI55 | 6.740 | 0.100 | 0.100 | 7.473 | 8.074 | Pass |  |
| 10 | FAI58 | 13.780 | 0.100 | 0.100 | 3.666 | 3.920 | Pass |  |
| 11 | FAI59 | 13.540 | 0.100 | 0.100 | 6.947 | 7.555 | Pass |  |
| 12 | FAI60 | 15.890 | 0.100 | 0.100 | 7.479 | 7.044 | Pass |  |
| 13 | FAI61-1 | 17.890 | 0.100 | 0.100 | 16.927 | 15.444 | Pass |  |
| 14 | FAI61-2 | 17.890 | 0.100 | 0.100 | 7.239 | 7.839 | Pass |  |
| 15 | FAI64 | 19.290 | 0.100 | 0.100 | 6.878 | 7.559 | Pass |  |
| 16 | FAI65-1 | 0.250 | 0.100 | 0.100 | 3.324 | 3.117 | Pass |  |
| 17 | FAI67 | 21.120 | 0.100 | 0.100 | 11.771 | 12.895 | Pass |  |
| 18 | FAI72 | 22.790 | 0.100 | 0.100 | 4.345 | 4.021 | Pass |  |


## Slide 28
3.V53 UAT1 Flex FAI Dimension CPK Distribution Summary
Pass
Fail

| SN | FAI | Nominal | Tol | Tol | CPK(Spec>1.33) |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 19 | FAI74 | 25.010 | 0.100 | 0.100 | 10.747 | 11.080 | Pass |  |
| 20 | FAI81-1 | 9.010 | 0.100 | 0.100 | 9.805 | 10.693 | Pass |  |
| 21 | FAI81-2 | 9.010 | 0.100 | 0.100 | 6.932 | 5.971 | Pass |  |
| 22 | FAI87 | 5.020 | 0.100 | 0.100 | 6.261 | 6.865 | Pass |  |
| 23 | FAI88 | 8.180 | 0.100 | 0.100 | 19.167 | 18.822 | Pass |  |
| 24 | FAI90 | 2.900 | 0.100 | 0.100 | 19.239 | 20.456 | Pass |  |
| 25 | FAI91 | 7.710 | 0.100 | 0.100 | 4.942 | 5.184 | Pass |  |
| 26 | FAI105 | 17.860 | 0.100 | 0.100 | 6.618 | 5.307 | Pass |  |
| 27 | FAI107 | 5.330 | 0.100 | 0.100 | 5.474 | 5.972 | Pass |  |
| 28 | FAI108 | 28.910 | 0.100 | 0.100 | 2.995 | 3.143 | Pass |  |
| 29 | FAI109 | 39.430 | 0.100 | 0.100 | 3.806 | 3.473 | Pass |  |
| 30 | FAI110 | 11.650 | 0.100 | 0.100 | 4.036 | 3.701 | Pass |  |
| 31 | FAI113 | 18.630 | 0.100 | 0.100 | 3.234 | 3.648 | Pass |  |
| 32 | FAI115 | 23.990 | 0.100 | 0.100 | 7.711 | 7.358 | Pass |  |
| 33 | FAI116 | 0.950 | 0.030 | 0.030 | 4.549 | 4.844 | Pass |  |
| 34 | FAI147 | 8.710 | 0.100 | 0.100 | 20.935 | 22.827 | Pass |  |
| 35 | FAI172 | 0.700 | 0.100 | 0.100 | 5.944 | 5.500 | Pass |  |
| 36 | FAI211 | 0.250 | 0.200 | 0.200 | 3.309 | 3.025 | Pass |  |


## Slide 29
3.V53 UAT1 Flex SPC Dimension CPK Distribution Summary
Pass
Fail

| SN | SPC | Nominal | Tol | Tol | CPK(Spec>1.67) |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI36SPCAJ | 18.980 | 0.100 | 0.100 | 8.657 | 9.393 | Pass |  |
| 2 | FAI37SPCAK | 20.700 | 0.100 | 0.100 | 11.943 | 10.890 | Pass |  |
| 3 | FAI42SPCAB | 3.480 | 0.100 | 0.100 | 7.739 | 8.380 | Pass |  |
| 4 | FAI43SPCAM | 8.890 | 0.100 | 0.100 | 10.272 | 9.703 | Pass |  |
| 5 | FAI46SPCAL | 4.330 | 0.100 | 0.100 | 10.964 | 10.373 | Pass |  |
| 6 | FAI52SPCAN | 3.070 | 0.100 | 0.100 | 15.555 | 16.047 | Pass |  |
| 7 | FAI57SPCAC | 9.090 | 0.100 | 0.100 | 12.458 | 11.698 | Pass |  |
| 8 | FAI68SPCAI | 20.360 | 0.100 | 0.100 | 3.785 | 3.527 | Pass |  |
| 9 | FAI77SPCAE | 13.110 | 0.100 | 0.100 | 7.353 | 7.928 | Pass |  |
| 10 | FAI78SPCAG | 20.830 | 0.100 | 0.100 | 3.305 | 2.740 | Pass |  |
| 11 | FAI104SPCAF | 15.440 | 0.100 | 0.100 | 3.400 | 3.746 | Pass |  |
| 12 | FAI111SPCAO | 30.140 | 0.100 | 0.100 | 3.369 | 3.141 | Pass |  |
| 13 | FAI112SPCAH | 31.400 | 0.100 | 0.100 | 2.762 | 3.051 | Pass |  |
| 14 | FAI114SPCAD | 6.730 | 0.100 | 0.100 | 5.504 | 5.170 | Pass |  |
| 15 | FAI186SPCAP | 21.830 | 0.100 | 0.100 | 3.574 | 3.958 | Pass |  |
| 16 | FAI187SPCAQ | 22.760 | 0.100 | 0.100 | 1.920 | 1.774 | Pass |  |
| 17 | FAI216SPCBA | 19.190 | 0.100 | 0.100 | 2.605 | 2.837 | Pass |  |


## Slide 30
3.V53 UAT1 Flex Stack-up Dimension CPK Distribution Summary
Pass
Fail

| SN | Thickness | Nominal | Tol | Tol | CPK(Spec>1.67) |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI173/SPCX | 0.260 | 0.020 | 0.020 | 9.782 | 9.989 | Pass |  |
| 2 | FAI174/SPCY | 0.375 | 0.030 | 0.030 | 2.849 | 3.052 | Pass |  |
| 3 | FAI176/SPCAA | 0.200 | 0.020 | 0.020 | 7.016 | 6.916 | Pass |  |
| 4 | FAI175/SPCZ | 0.140 | 0.020 | 0.020 | 8.928 | 8.313 | Pass |  |
| 5 | FAI217/SPCBB | 0.200 | 0.020 | 0.020 | 6.291 | 6.701 | Pass |  |
| 6 | FAI218/SPCBC | 0.285 | 0.030 | 0.030 | 10.688 | 11.047 | Pass |  |


## Slide 31
3.V53 UAT1 Flex Stack-up Dimension CPK Distribution Summary
Pass
Fail

## Slide 32
3.V53 UAT1 Flex DFM Dimension CPK Distribution Summary
Pass
Fail

| SN | FAI | Nominal | Tol | Tol | CPK(Spec>1.33) |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAID01 | 32.445 | 0.050 | 0.050 | 3.340 | 3.116 | Pass |  |
| 2 | FAID02 | 24.413 | 0.050 | 0.050 | 2.525 | 2.296 | Pass |  |
| 3 | FAID03 | 23.155 | 0.050 | 0.050 | 2.918 | 3.217 | Pass |  |
| 4 | FAID04 | 1.956 | 0.050 | 0.050 | 4.498 | 4.203 | Pass |  |
| 5 | FAID05 | 13.371 | 0.050 | 0.050 | 2.511 | 2.664 | Pass |  |
| 6 | FAID06 | 11.319 | 0.050 | 0.050 | 11.997 | 11.067 | Pass |  |
| 7 | FAID07 | 12.305 | 0.050 | 0.050 | 12.044 | 11.298 | Pass |  |
| 8 | FAID08 | 1.260 | 0.075 | 0.075 | 2.950 | 3.093 | Pass |  |
| 9 | FAID09 | 2.095 | 0.075 | 0.075 | 2.747 | 2.927 | Pass |  |
| 10 | FAID10 | 10.209 | 0.050 | 0.050 | 3.842 | 3.014 | Pass |  |
| 11 | FAID11 | 12.037 | 0.050 | 0.050 | 6.283 | 6.454 | Pass |  |
| 12 | FAID12 | 15.928 | 0.050 | 0.050 | 6.920 | 6.708 | Pass |  |
| 13 | FAID13 | 13.415 | 0.050 | 0.050 | 2.584 | 3.349 | Pass |  |
| 14 | FAID14 | 8.716 | 0.050 | 0.050 | 2.377 | 2.229 | Pass |  |
| 15 | FAID15 | 7.716 | 0.050 | 0.050 | 1.865 | 1.773 | Pass |  |
| 16 | FAID16 | 2.200 | 0.050 | 0.050 | 21.255 | 23.457 | Pass |  |
| 17 | FAID17 | 6.384 | 0.050 | 0.050 | 11.415 | 10.793 | Pass |  |
| 18 | FAID20 | 2.420 | 0.050 | 0.050 | 12.614 | 13.708 | Pass |  |


## Slide 33
3.V53 UAT1 Flex DFM Dimension CPK Distribution Summary
Pass
Fail

| SN | FAI | Nominal | Tol | Tol | CPK(Spec>1.33) |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 19 | FAID21 | 4.752 | 0.050 | 0.050 | 2.864 | 2.748 | Pass |  |
| 20 | FAID22 | 5.868 | 0.050 | 0.050 | 4.141 | 3.819 | Pass |  |
| 21 | FAID25 | 20.702 | 0.050 | 0.050 | 3.777 | 4.210 | Pass |  |
| 22 | FAID26 | 3.478 | 0.050 | 0.050 | 4.526 | 4.216 | Pass |  |
| 23 | FAID27 | 2.901 | 0.050 | 0.050 | 4.773 | 4.555 | Pass |  |
| 24 | FAID28 | 8.176 | 0.050 | 0.050 | 5.535 | 5.860 | Pass |  |
| 25 | FAID29 | 5.020 | 0.050 | 0.050 | 3.050 | 3.326 | Pass |  |
| 26 | FAID30 | 7.707 | 0.050 | 0.050 | 2.951 | 3.169 | Pass |  |
| 27 | FAID35 | 5.406 | 0.050 | 0.050 | 7.392 | 7.129 | Pass |  |
| 28 | FAID18 | 2.669 | 0.075 | 0.075 | 1.884 | 1.794 | Pass |  |
| 29 | FAID19 | 4.210 | 0.075 | 0.075 | 1.987 | 1.841 | Pass |  |
| 30 | FAID31 | 1.966 | 0.075 | 0.075 | 1.995 | 2.208 | Pass |  |
| 31 | FAID32 | 1.822 | 0.075 | 0.075 | 2.149 | 1.961 | Pass |  |
| 32 | FAID33 | 1.350 | 0.075 | 0.075 | 2.004 | 2.198 | Pass |  |
| 33 | FAID34 | 1.225 | 0.075 | 0.075 | 1.684 | 1.866 | Pass |  |
| 34 | FAID23 | 2.243 | 0.075 | 0.075 | 1.984 | 1.846 | Pass |  |
| 35 | FAID24 | 5.346 | 0.075 | 0.075 | 1.893 | 1.746 | Pass |  |


## Slide 34
3.V53 UAT1 Flex DFM Dimension CPK Distribution Summary
Pass
Fail

## Slide 35
3.V53 UAT1 DOE Flex FAI Dimension CPK Distribution Summary
Pass
Fail

| SN | FAI | Nominal | Tol | Tol | CPK(Spec>1.33) |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI40 | 16.880 | 0.100 | 0.100 | 13.134 | 12.725 | Pass |  |
| 2 | FAI41 | 17.630 | 0.100 | 0.100 | 10.907 | 11.543 | Pass |  |
| 3 | FAI44 | 9.610 | 0.100 | 0.100 | 11.178 | 11.059 | Pass |  |
| 4 | FAI45 | 5.580 | 0.100 | 0.100 | 9.186 | 10.610 | Pass |  |
| 5 | FAI49 | 0.500 | 0.100 | 0.100 | 8.822 | 9.846 | Pass |  |
| 6 | FAI51 | 7.490 | 0.100 | 0.100 | 8.321 | 7.295 | Pass |  |
| 7 | FAI53 | 4.910 | 0.100 | 0.100 | 2.809 | 3.233 | Pass |  |
| 8 | FAI54 | 5.030 | 0.100 | 0.100 | 2.017 | 2.537 | Pass |  |
| 9 | FAI55 | 6.740 | 0.100 | 0.100 | 10.024 | 9.166 | Pass |  |
| 10 | FAI58 | 13.780 | 0.100 | 0.100 | 3.122 | 2.826 | Pass |  |
| 11 | FAI59 | 13.540 | 0.100 | 0.100 | 5.626 | 6.965 | Pass |  |
| 12 | FAI60 | 15.890 | 0.100 | 0.100 | 4.864 | 6.504 | Pass |  |
| 13 | FAI61.1 | 17.890 | 0.100 | 0.100 | 14.686 | 13.935 | Pass |  |
| 14 | FAI61.2 | 17.890 | 0.100 | 0.100 | 4.938 | 6.652 | Pass |  |
| 15 | FAI64 | 19.290 | 0.100 | 0.100 | 7.561 | 6.585 | Pass |  |
| 16 | FAI65 | 0.250 | 0.100 | 0.100 | 2.611 | 3.195 | Pass |  |
| 17 | FAI67 | 21.120 | 0.100 | 0.100 | 10.815 | 9.869 | Pass |  |
| 18 | FAI72 | 22.790 | 0.100 | 0.100 | 1.898 | 2.397 | Pass |  |


## Slide 36
3.V53 UAT1 DOE Flex FAI Dimension CPK Distribution Summary
Pass
Fail

| SN | FAI | Nominal | Tol | Tol | CPK(Spec>1.33) |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 19 | FAI74 | 25.010 | 0.100 | 0.100 | 9.990 | 10.778 | Pass |  |
| 20 | FAI81.1 | 9.010 | 0.100 | 0.100 | 8.632 | 9.127 | Pass |  |
| 21 | FAI81.2 | 9.010 | 0.100 | 0.100 | 7.154 | 5.237 | Pass |  |
| 22 | FAI88 | 8.180 | 0.100 | 0.100 | 12.542 | 14.073 | Pass |  |
| 23 | FAI87 | 5.020 | 0.100 | 0.100 | 6.890 | 5.547 | Pass |  |
| 24 | FAI91 | 7.710 | 0.100 | 0.100 | 6.338 | 5.012 | Pass |  |
| 25 | FAI90 | 2.900 | 0.100 | 0.100 | 17.207 | 17.696 | Pass |  |
| 26 | FAI105 | 17.860 | 0.100 | 0.100 | 2.684 | 3.905 | Pass |  |
| 27 | FAI107 | 5.330 | 0.100 | 0.100 | 4.653 | 6.306 | Pass |  |
| 28 | FAI108 | 28.910 | 0.100 | 0.100 | 3.617 | 2.010 | Pass |  |
| 29 | FAI109 | 39.430 | 0.100 | 0.100 | 1.941 | 2.200 | Pass |  |
| 30 | FAI110 | 11.650 | 0.100 | 0.100 | 2.601 | 2.463 | Pass |  |
| 31 | FAI113 | 18.630 | 0.100 | 0.100 | 1.906 | 2.206 | Pass |  |
| 32 | FAI115 | 23.990 | 0.100 | 0.100 | 6.144 | 6.930 | Pass |  |
| 33 | FAI116 | 0.950 | 0.030 | 0.030 | 2.601 | 3.728 | Pass |  |
| 34 | FAI147 | 8.710 | 0.200 | 0.200 | 23.780 | 22.313 | Pass |  |
| 35 | FAI172 | 0.700 | 0.100 | 0.100 | 5.532 | 6.169 | Pass |  |
| 36 | FAI211 | 0.250 | 0.200 | 0.200 | 3.656 | 2.920 | Pass |  |


## Slide 37
3.V53 UAT1 DOE Flex SPC Dimension CPK Distribution Summary
Pass
Fail

| SN | SPC | Nominal | Tol | Tol | CPK(Spec>1.67) |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI36SPCAJ | 18.980 | 0.100 | 0.100 | 7.421 | 7.685 | Pass |  |
| 2 | FAI37SPCAK | 20.700 | 0.100 | 0.100 | 8.262 | 9.250 | Pass |  |
| 3 | FAI42SPCAB | 3.480 | 0.100 | 0.100 | 5.994 | 7.280 | Pass |  |
| 4 | FAI43SPCAM | 8.890 | 0.100 | 0.100 | 10.051 | 9.162 | Pass |  |
| 5 | FAI46SPCAL | 4.330 | 0.100 | 0.100 | 8.805 | 10.011 | Pass |  |
| 6 | FAI52SPCAN | 3.070 | 0.100 | 0.100 | 15.929 | 13.169 | Pass |  |
| 7 | FAI57SPCAC | 9.090 | 0.100 | 0.100 | 9.032 | 10.571 | Pass |  |
| 8 | FAI68SPCAI | 20.360 | 0.100 | 0.100 | 3.257 | 2.425 | Pass |  |
| 9 | FAI77SPCAE | 13.110 | 0.100 | 0.100 | 6.415 | 7.479 | Pass |  |
| 10 | FAI78SPCAG | 20.830 | 0.100 | 0.100 | 1.694 | 1.822 | Pass |  |
| 11 | FAI104SPCAF | 15.440 | 0.100 | 0.100 | 2.144 | 2.564 | Pass |  |
| 12 | FAI111SPCAO | 30.140 | 0.100 | 0.100 | 3.564 | 2.115 | Pass |  |
| 13 | FAI112SPCAH | 31.400 | 0.100 | 0.100 | 3.089 | 1.965 | Pass |  |
| 14 | FAI114SPCAD | 6.730 | 0.100 | 0.100 | 3.644 | 4.098 | Pass |  |
| 15 | FAI186SPCAP | 21.830 | 0.100 | 0.100 | 2.323 | 2.508 | Pass |  |
| 16 | FAI187SPCAQ | 22.760 | 0.100 | 0.100 | 2.220 | 1.906 | Pass |  |
| 17 | FAI216SPCBA | 19.190 | 0.100 | 0.100 | 1.827 | 1.862 | Pass |  |


## Slide 38
3.V53 UAT1 DOE Flex Stack-up Dimension CPK Distribution Summary
Pass
Fail

| SN | Thickness | Nominal | Tol | Tol | CPK(Spec>1.67) |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI173/SPCX | 0.260 | 0.020 | 0.020 | 4.039 | 3.033 | Pass |  |
| 2 | FAI174/SPCY | 0.375 | 0.030 | 0.030 | 3.322 | 2.388 | Pass |  |
| 3 | FAI176/SPCAA | 0.200 | 0.020 | 0.020 | 2.349 | 2.950 | Pass |  |
| 4 | FAI175/SPCZ | 0.140 | 0.020 | 0.020 | 3.946 | 4.461 | Pass |  |
| 5 | FAI217/SPCBB | 0.200 | 0.020 | 0.020 | 2.964 | 2.554 | Pass |  |
| 6 | FAI218/SPCBC | 0.285 | 0.030 | 0.030 | 10.840 | 11.409 | Pass |  |


## Slide 39
3.V53 UAT1 DOE Flex Stack-up Dimension CPK Distribution Summary
Pass
Fail

## Slide 40
3.V53 UAT1 DOE Flex DFM Dimension CPK Distribution Summary
Pass
Fail

| SN | FAI | Nominal | Tol | Tol | CPK(Spec>1.33) |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 1 | FAI1 | 32.445 | 0.050 | 0.050 | 2.087 | 1.882 | Pass |  |
| 2 | FAI2 | 24.413 | 0.050 | 0.050 | 1.945 | 1.713 | Pass |  |
| 3 | FAI3 | 23.155 | 0.050 | 0.050 | 1.874 | 2.131 | Pass |  |
| 4 | FAI4 | 1.956 | 0.050 | 0.050 | 4.902 | 4.130 | Pass |  |
| 5 | FAI5 | 13.371 | 0.050 | 0.050 | 2.264 | 1.852 | Pass |  |
| 6 | FAI6 | 11.319 | 0.050 | 0.050 | 3.846 | 4.588 | Pass |  |
| 7 | FAI7 | 12.305 | 0.050 | 0.050 | 9.446 | 10.906 | Pass |  |
| 8 | FAI8 | 1.260 | 0.075 | 0.075 | 4.073 | 2.704 | Pass |  |
| 9 | FAI9 | 2.095 | 0.075 | 0.075 | 2.276 | 2.379 | Pass |  |
| 10 | FAI10 | 10.209 | 0.050 | 0.050 | 3.043 | 1.791 | Pass |  |
| 11 | FAI11 | 12.037 | 0.050 | 0.050 | 5.753 | 6.265 | Pass |  |
| 12 | FAI12 | 15.928 | 0.050 | 0.050 | 5.396 | 5.658 | Pass |  |
| 13 | FAI13 | 13.415 | 0.050 | 0.050 | 2.492 | 2.638 | Pass |  |
| 14 | FAI14 | 8.716 | 0.050 | 0.050 | 2.869 | 2.073 | Pass |  |
| 15 | FAI15 | 7.716 | 0.050 | 0.050 | 2.197 | 1.809 | Pass |  |
| 16 | FAI16 | 2.200 | 0.050 | 0.050 | 13.549 | 14.559 | Pass |  |
| 17 | FAI17 | 6.384 | 0.050 | 0.050 | 7.867 | 7.083 | Pass |  |
| 18 | FAI20 | 2.420 | 0.050 | 0.050 | 5.441 | 6.620 | Pass |  |


## Slide 41
3.V53 UAT1 DOE Flex DFM Dimension CPK Distribution Summary
Pass
Fail

| SN | FAI | Nominal | Tol | Tol | CPK(Spec>1.33) |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Murata |  |  |
| 19 | FAI21 | 4.752 | 0.050 | 0.050 | 3.067 | 2.099 | Pass |  |
| 20 | FAI22 | 5.868 | 0.050 | 0.050 | 1.961 | 2.223 | Pass |  |
| 21 | FAI25 | 20.702 | 0.050 | 0.050 | 3.691 | 2.693 | Pass |  |
| 22 | FAI26 | 3.478 | 0.050 | 0.050 | 3.546 | 3.721 | Pass |  |
| 23 | FAI27 | 2.901 | 0.050 | 0.050 | 2.687 | 3.459 | Pass |  |
| 24 | FAI28 | 8.176 | 0.050 | 0.050 | 3.883 | 3.092 | Pass |  |
| 25 | FAI29 | 5.019 | 0.050 | 0.050 | 2.879 | 2.586 | Pass |  |
| 26 | FAI30 | 7.707 | 0.050 | 0.050 | 2.623 | 2.584 | Pass |  |
| 27 | FAI35 | 5.406 | 0.050 | 0.050 | 8.038 | 9.176 | Pass |  |
| 28 | FAI18 | 2.669 | 0.075 | 0.075 | 2.700 | 2.822 | Pass |  |
| 29 | FAI19 | 4.211 | 0.075 | 0.075 | 2.162 | 1.737 | Pass |  |
| 30 | FAI23 | 2.243 | 0.075 | 0.075 | 4.153 | 4.285 | Pass |  |
| 31 | FAI24 | 5.346 | 0.075 | 0.075 | 2.232 | 1.718 | Pass |  |
| 32 | FAI31 | 1.966 | 0.075 | 0.075 | 1.733 | 2.274 | Pass |  |
| 33 | FAI32 | 1.822 | 0.075 | 0.075 | 3.586 | 3.503 | Pass |  |
| 34 | FAI33 | 1.350 | 0.075 | 0.075 | 4.522 | 3.673 | Pass |  |
| 35 | FAI34 | 1.225 | 0.075 | 0.075 | 1.739 | 2.019 | Pass |  |


## Slide 42
3.V53 UAT1 DOE Flex DFM Dimension CPK Distribution Summary
Pass
Fail

## Slide 43
3.V53 Strobe tail Flex FAI Dimension CPK Distribution Summary
Pass
Fail

| SN | FAI | Nominal | Tol | Tol | CPK(Spec>1.33) |  |  |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Mflex | ICT | Avary |  |  |
| 1 | FAI2 | 13.620 | 0.120 | 0.120 | 3.202 | 3.419 | 2.843 | 3.728 | Pass |  |
| 2 | FAI4 | 0.060 | 0.120 | 0.120 | 2.373 | 2.280 | 6.886 | 5.872 | Pass |  |
| 3 | FAI5.1 | 0.300 | 0.200 | 0.200 | 1.443 | 1.869 | 1.346 | 1.392 | Pass |  |
| 4 | FAI5.2 | 0.300 | 0.200 | 0.200 | 1.459 | 1.855 | 1.259 | 0.774 | NG | A customer waived |
| 5 | FAI10.1 | 0.000 | 0.400 | 0.000 | 54.155 | 54.453 | 51.465 | 52.315 | Pass |  |
| 6 | FAI10.2 | 0.000 | 0.400 | 0.000 | 49.056 | 49.923 | 40.955 | 39.592 | Pass |  |
| 7 | FAI10.3 | 0.000 | 0.400 | 0.000 | 54.432 | 53.733 | 23.184 | 24.548 | Pass |  |
| 8 | FAI10.4 | 0.000 | 0.400 | 0.000 | 50.098 | 48.900 | 27.980 | 28.264 | Pass |  |
| 9 | FAI10.5 | 0.000 | 0.400 | 0.000 | 60.437 | 62.220 | 27.236 | 25.097 | Pass |  |
| 10 | FAI10.6 | 0.000 | 0.400 | 0.000 | 18.881 | 20.641 | 25.080 | 27.977 | Pass |  |
| 11 | FAI10.7 | 0.000 | 0.400 | 0.000 | 21.429 | 19.377 | 39.581 | 37.847 | Pass |  |
| 12 | FAI10.8 | 0.000 | 0.400 | 0.000 | 45.980 | 45.111 | 29.845 | 30.040 | Pass |  |
| 13 | FAI10.9 | 0.000 | 0.400 | 0.000 | 47.006 | 48.106 | 38.092 | 38.902 | Pass |  |
| 14 | FAI11.1 | 0.600 | 0.050 | 0.050 | 8.755 | 8.152 | 7.528 | 6.243 | Pass |  |
| 15 | FAI11.2 | 0.600 | 0.050 | 0.050 | 8.281 | 7.652 | 6.849 | 5.010 | Pass |  |
| 16 | FAI11.3 | 0.600 | 0.050 | 0.050 | 7.523 | 7.802 | 4.827 | 5.707 | Pass |  |
| 17 | FAI11.4 | 0.600 | 0.050 | 0.050 | 8.022 | 7.340 | 6.343 | 5.229 | Pass |  |
| 18 | FAI11.5 | 0.600 | 0.050 | 0.050 | 7.636 | 7.696 | 4.513 | 5.290 | Pass |  |
| 19 | FAI11.6 | 0.600 | 0.050 | 0.050 | 7.592 | 6.565 | 7.014 | 5.581 | Pass |  |
| 20 | FAI11.7 | 0.600 | 0.050 | 0.050 | 6.090 | 6.175 | 4.974 | 5.782 | Pass |  |
| 21 | FAI11.8 | 0.600 | 0.050 | 0.050 | 7.844 | 6.843 | 6.647 | 5.341 | Pass |  |
| 22 | FAI11.9 | 0.600 | 0.050 | 0.050 | 7.255 | 8.159 | 5.171 | 5.383 | Pass |  |
| 23 | FAI11.10 | 0.600 | 0.050 | 0.050 | 7.752 | 6.422 | 6.094 | 4.502 | Pass |  |
| 24 | FAI12.1 | 0.700 | 0.200 | 0.200 | 6.377 | 7.947 | 5.870 | 5.142 | Pass |  |
| 25 | FAI12.2 | 0.700 | 0.200 | 0.200 | 6.633 | 6.224 | 4.063 | 4.651 | Pass |  |
| 26 | FAI17 | 4.100 | 0.200 | 0.200 | 21.863 | 23.613 | 2.475 | 1.987 | Pass |  |


## Slide 44
3.V53 Strobe tail Flex SPC Dimension CPK Distribution Summary
Pass
Fail

| SN | SPC | Nominal | Tol | Tol | CPK(Spec>1.67) |  |  |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Mflex | ICT | Avary |  |  |
| 1 | FAI1.1-SPCA | 0.900 | 0.050 | 0.050 | 3.786 | 4.940 | 11.923 | 10.574 | Pass |  |
| 2 | FAI1.2-SPCA | 0.900 | 0.050 | 0.050 | 2.142 | 1.730 | 10.311 | 11.947 | Pass |  |
| 3 | FAI1.3-SPCA | 0.900 | 0.050 | 0.050 | 8.638 | 9.570 | 5.227 | 4.773 | Pass |  |
| 4 | FAI1.4-SPCA | 0.900 | 0.050 | 0.050 | 10.783 | 9.173 | 11.208 | 13.193 | Pass |  |
| 5 | FAI1.5-SPCA | 0.900 | 0.050 | 0.050 | 8.278 | 7.145 | 9.544 | 10.978 | Pass |  |
| 6 | FAI1.6-SPCA | 0.900 | 0.050 | 0.050 | 6.716 | 7.248 | 7.512 | 7.245 | Pass |  |
| 7 | FAI1.7-SPCA | 0.900 | 0.050 | 0.050 | 8.454 | 7.663 | 9.181 | 10.633 | Pass |  |
| 8 | FAI1.8-SPCA | 0.900 | 0.050 | 0.050 | 6.616 | 7.204 | 11.941 | 10.534 | Pass |  |
| 9 | FAI1.9-SPCA | 0.900 | 0.050 | 0.050 | 2.916 | 3.235 | 8.934 | 9.013 | Pass |  |
| 10 | FAI1.10-SPC | 0.900 | 0.050 | 0.050 | 8.449 | 7.095 | 5.658 | 4.152 | Pass |  |
| 11 | FAI3-SPCB | 5.370 | 0.200 | 0.200 | 9.813 | 9.955 | 11.461 | 13.095 | Pass |  |


## Slide 45
3.V53 Strobe tail Flex Stack-up Dimension CPK Distribution Summary
Pass
Fail

| SN | Thickness | Nominal | Tol | Tol | CPK(Spec>1.67) |  |  |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Mflex | ICT | Avary |  |  |
| 1 | FAI8\SPCC | 0.142 | 0.020 | 0.020 | 3.457 | 2.409 | 5.032 | 4.787 | Pass |  |
| 2 | FAI7\SPCF | 0.106 | 0.020 | 0.020 | 5.279 | 6.457 | 5.087 | 6.266 | Pass |  |
| 3 | FAI9\SPCE | 0.152 | 0.020 | 0.020 | 2.612 | 1.861 | 2.529 | 2.219 | Pass |  |
| 4 | FAI6\SPCD | 0.131 | 0.020 | 0.020 | 2.704 | 1.865 | 2.950 | 3.222 | Pass |  |
| 5 | FAI16\SPCG | 0.123 | 0.020 | 0.020 | 2.856 | 3.163 | 3.069 | 2.094 | Pass |  |


## Slide 46
3.V53 Strobe tail Flex Stack-up Dimension CPK Distribution Summary
Pass
Fail

## Slide 47
3.V53 Strobe tail Flex DFM Dimension CPK Distribution Summary
Pass
Fail

| SN | FAI | Nominal | Tol | Tol | CPK(Spec>1.33) |  |  |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  | (+) | (-) | ICT | Mflex | ICT | Avary |  |  |
| 1 | FAI1 | 4.100 | 0.050 | 0.050 | 12.042 | 13.691 | 5.328 | 5.635 | Pass |  |
| 2 | FAI2 | 1.350 | 0.075 | 0.075 | 2.667 | 2.293 | 4.313 | 3.382 | Pass |  |
| 3 | FAI3 | 1.025 | 0.075 | 0.075 | 2.598 | 2.699 | 2.045 | 2.009 | Pass |  |
| 4 | FAI4 | 12.045 | 0.050 | 0.050 | 1.431 | 1.572 | 1.713 | 1.436 | Pass |  |
| 5 | FAI5 | 135.00 | 1.000 | 1.000 | 3.362 | 3.131 | 1.604 | 1.396 | Pass |  |


## Slide 48
3.V53 UAT1 PSA FAI Dimension CPK Distribution Summary
Pass
Fail

| SN | P/N | Items | Nominal | Tol | Tol | JT |  | DX |  | Result | Remark |
|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  | CPK(Spec>1. 33) |  | CPK(Spec>1. 33) |  |  |  |
|  |  |  | （mm） | （+） | （-） | JT | ICT | DX | ICT |  |  |
| 1 | 029-001H-3138 | Length | 6.24 | 0.100 | 0.100 | 5.312 | 6.116 | 10.419 | 11.061 | Pass |  |
|  |  | Width | 3.61 | 0.100 | 0.100 | 1.547 | 1.441 | 2.162 | 1.745 | Pass |  |
|  |  | Thickness | 0.25 | 0.025 | 0.025 | 7.862 | 8.288 | 4.727 | 4.588 | Pass |  |
| 2 | 029-001H-3139 | Length | 5.28 | 0.100 | 0.100 | 2.714 | 2.393 | 4.480 | 4.569 | Pass |  |
|  |  | Width | 1.22 | 0.100 | 0.100 | 9.174 | 9.780 | 11.138 | 11.704 | Pass |  |
|  |  | Thickness | 0.10 | 0.010 | 0.010 | 2.445 | 1.919 | 3.502 | 3.396 | Pass |  |
| 3 | 029-001H-3141 | Length | 7.00 | 0.100 | 0.100 | 1.758 | 1.709 | 4.801 | 4.026 | Pass |  |
|  |  | Width | 1.65 | 0.100 | 0.100 | 2.803 | 2.719 | 5.097 | 6.212 | Pass |  |
|  |  | Thickness | 0.10 | 0.010 | 0.010 | 6.841 | 7.407 | 5.176 | 5.632 | Pass |  |
| 4 | 029-001H-3142 | Length | 9.61 | 0.100 | 0.100 | 20.586 | 21.737 | 8.054 | 7.900 | Pass |  |
|  |  | Width | 5.15 | 0.100 | 0.100 | 16.248 | 15.176 | 2.147 | 1.683 | Pass |  |
|  |  | Thickness | 0.05 | 0.005 | 0.005 | 2.109 | 1.842 | 1.906 | 1.610 | Pass |  |
| 5 | 029-001H-3143 | Length | 7.59 | 0.100 | 0.100 | 8.253 | 7.447 | 10.579 | 11.190 | Pass |  |
|  |  | Width | 7.09 | 0.100 | 0.100 | 2.328 | 2.486 | 3.753 | 2.985 | Pass |  |
|  |  | Thickness | 0.05 | 0.005 | 0.005 | 4.188 | 4.994 | 5.621 | 6.511 | Pass |  |
| 6 | 029-001H-3144 | Length | 10.02 | 0.100 | 0.100 | 4.827 | 5.515 | 14.615 | 15.824 | Pass |  |
|  |  | Width | 4.42 | 0.100 | 0.100 | 11.976 | 10.754 | 18.104 | 17.729 | Pass |  |
|  |  | Thickness | 0.05 | 0.005 | 0.005 | 2.336 | 2.979 | 1.420 | 1.583 | Pass |  |


## Slide 49
3.V53 UAT1 PSA 029-001H-3138 Peeling force Summary(NITTO 56110B)

## Slide 50
3.V53 UAT1 PSA 029-001H-3139 Peeling force Summary(NITTO 56110B)

## Slide 51
3.V53 UAT1 PSA 029-001H-3141 Peeling force Summary(NITTO 56110B)

## Slide 52
3.V53 UAT1 PSA 029-001H-3142 Peeling force Summary(NITTO 56105)

## Slide 53
3.V53 UAT1 PSA 029-001H-3143 Peeling force Summary(3M9701H-100)

## Slide 54
3.V53 UAT1 PSA 029-001H-3144 Peeling force Summary (SHRETEC 5105SA)

## Slide 55

| Item | Agenda |
|---|---|
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


## Slide 56
4. Assembly Process Flow Chart-UAT1
Panel
Piece
Traceabilty/Shopfloor station

| SMT (BOT) | Remove UV Film |
|---|---|
|  | Panel to Tray |
|  | Tape on metal sheet |
|  | Flex Loading |
|  | HTS Print |
|  | Add metal cover |
|  | SPI |
|  | Pick up& Placement |
|  | Pre-AOI(Link) |
|  | HTS Reflow |
|  | Cooling |
|  | Post-AOI |
|  | Remove metal cover |
|  | VI |
|  | Flipping |


| SMT  (TOP) | Flipping AOI |
|---|---|
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
|  | Flipping |


| CC Glue | Add metal cover |
|---|---|
|  | UV Dispensing |
|  | Glue inspection |
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


## Slide 57

| SMT (BOT) | Tape on metal sheet |
|---|---|
|  | Flex Loading |
|  | 2DBC Link |
|  | Add baking cover |
|  | Baking |
|  | Remove baking cover |
|  | Panel Flex to carrier |
|  | Flipping |
|  | Loading AOI |
|  | LTS Print |
|  | SPI |
|  | LTS Reflow |
|  | Cooling |
|  | SBI |
|  | VI |
| Package | Transfer Carrier |
| Package | Tape Remove |
| Package | VI |
|  | Package scan |
|  | Tray to bonding tray |
|  | Package to box |

4. Assembly Process Flow Chart-Strobe
Panel
Piece
Traceabilty/Shopfloor station

## Slide 58

| Bonding | Strobe P&P |
|---|---|
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
|  | Flipping |
|  | 2DBC&PSA P&P |
|  | Press |
|  | Link |
| Package | Carrier to Tray |
|  | VI |
|  | Scan |


| Backend | Bending |
|---|---|
|  | VI |
|  | MIC Film Remove |
|  | 1K test |
|  | AVI for EB |
|  | Mic film P&P |
|  | RF |
|  | ICT |
|  | FVI |
|  | Package (2DBC scan) |
|  | OQC (FR + THD + Sealing) |
|  | OQC(RF+ICT) |
|  | OQC (VI) |
|  | Package |

4. Assembly Process Flow Chart-UAT1 Bonding
Panel
Piece
Traceabilty/Shopfloor station

## Slide 59
4. Assembly Yield Trend and top5 breakdown

## Slide 60
4. Assembly Yield Trend and top5 breakdown

| Failure Model | Quantity | Fail Rate | Accumulation percentage |
|---|---|---|---|
| Clip deformation | 41 | 0.70% | 24.85% |
| Printing issue | 24 | 0.39% | 38.79% |
| Flex deformation | 23 | 0.36% | 51.52% |
| Flex exposed copper | 21 | 0.34% | 63.64% |
| Testing NTF | 19 | 0.32% | 75.15% |
| Others | 41 | 0.70% | 100.00% |

100.00%

## Slide 61
4. Assembly Yield Trend and top5 breakdown

| Defect | Qty | FA | CA |
|---|---|---|---|
| Component shift | 5 | Wiping the board causes component shift. | Training operator to handle products method. |
| Printing issue | 4 | SMT check no obvious abnormal, Keeping track | Keeping track. |
| Glue infuffient | 3 | The IC path glue amount is not set enough to cause less glue | IC path increase glue volume 0.14→0.16 tracking confirm OK |
| IC glue overflow | 3 | Finger contact with the product wipe cover sheet causes glue overflow. | 1.Require operator to operate according to SOP. 2. Import Automatic press-cover placing machine in EVT |
| Bonding shift | 3 | Flex shaking out the cavity caused bonding shift. | Orbital speed changed from 80 to 50. |
| Barcode broken | 3 | When making the first piece, the conveyor clamp of the NPM machine was used incorrectly, resulting in barcode broken. | SOP defines the requirements for the use of NPM conveyor clamp |
| PSA adhesive shift | 3 | Check PSA raw material, found the PSA adhesive shift. | 1. Clean up the CPSA raw materials with adhesive shift in stock and then put them into the production. 2. Feedback this defect item to the vendor and provide FACA. |
| Bonding defect | 2 | SMT check no obvious abnormal, Keeping track | Keeping track. |
| Printing shift | 2 | When OP remove the printing-try film, resulting in  the flex shifted，and then the printing offset lead to solder insufficient | Request OP to check the flex again on Flipping-AOI after printing-try film removed |
| Component missing | 2 | SMT check no obvious abnormal, Keeping track | Keeping on tracking. |
| Flex glue contamination | 2 | Metal cover adhesive causes flex glue contamination. | 1.Clean the metal cover immediately. 2.Check whether glue residual on cover before production |
| Clip missing | 2 | The wire of the scanning gun causes the clip missing. | 1.Replace and fix the scan camera. 2.Check whether scaner line is fixed before production |
| Side-stand | 1 | SMT check no obvious abnormal, Keeping track | Keeping track. |
| Flex contamination | 2 | Finger cover broken and contaminated flex. | 1.Replace finger cover immediately. 2.Check whether finger-cot is broken before production |
| Barcode defects | 1 | Check PSA  material  it is normal and check process has not found root cause. Conclusion: Not found the root cause of  PSA adhesive winkle and keep on tracking | Follow SOP define to take product Tracking next config build has no this issue. |
| PSA wrinkle | 1 | Check PSA  material  it is normal and check process has not found root cause. Conclusion: Not found the root cause of  PSA adhesive winkle and keep on tracking | Follow SOP define to take product Tracking next config build has no this issue. |
| Reverse | 1 | SMT check no obvious abnormal, Keeping track | Keeping on tracking. |
| Sus contamination | 1 | SMT check no obvious abnormal, Keeping track | Keeping on tracking. |


## Slide 62

| Item | Defect  Description | Picture | Defect Rate % | Previous  build % | FA/Root Cause | Corrective Action | DRI  Due Date | Validation (xxF/input=defect rate%) |
|---|---|---|---|---|---|---|---|---|
| 1 | Clip deformation-（Handling issue） |  | 0.70% (41F/5850) | / | Improper handling of the product and remove metal cover method lead to the clip deformation. | 1.Training the operator should first align the Pin with the round hole，then place the metal cover.2.Import the automatic add metal cover machine in EVT. | Xiaofeng 8/22 | 0.00% （0F/2900T） |
| 2 | Flex deformation-(Handling issue) |  | 0.39% (23F/5850T) | / | The metal tray wall was interference with products during remove the flex resulting in flex deformation. | 1.Optimize the Un-loading tray position for clamp flex and training operator the  method of clamp flex. 2.We will add this issue into lesson learn. 3.Import semi-automatic CCD to inspection flex in EVT. | Xiaofeng 8/26 | 0.00% (0F/3550T) |
| 3 | Flex dent (Process issue) |  | 0.35% (21F/5850T) | / | The MIC film P&P fixture was not  fool-proof cause flex dent | Modify fixture to fool-proof, make cover head and support surface match, and add stopper of cover to avoid over press. | Peng Huang 9/8 | 0.00% (0F/3250T) |
| 4 | Printing issue-(Handling issue) |  | 0.34% (20F/5850) | / | Manual operation during smt process resulted in printing issue. | 1.Training the operator should first align the Pin with the round hole，then place the metal cover. 2.Import the automatic add metal cover machine in EVT. | Xiaofeng 9/2 | 0.00% （0F/1300T） |
| 5 | Testing NTF | NA | 0.32% (19F/5850T) | / | The probe pin is in poor contact with the strobe Pad, resulting in the high NTF issue. | 1.Change the probe design, add for two thinner pogo pins to touch the strobe area for better contact. 2.Take this as lesson for similar flex design. | Yazhou 8/27 | 0% (0F/3550T) |


| Flex/Assembly | Input Qty | Output Qty | Yield | Yield Target QCP | Yield Gap | *Supply Chain MP target commitment to GSM | *MP Yield by ”yield calculation” |
|---|---|---|---|---|---|---|---|
| UAT1 | 5850 | 5685 | 97.18% | 85% | 12.18% | / | / |

4. Assembly Yield Trend and top5 breakdown

## Slide 63

| Component | Flex | Vendor | Murata | APN | 056-20573 | Failure process/station | VI |
|---|---|---|---|---|---|---|---|
| Issue Description | Clip deformation-Handling issue Defected rate:  0.70% (41F/5850T)              Before:  2.10% (26F/1250T)                              0.95% (10F/1050T)                              0.80% (5F/650T)                After :  0.00% (0F/2900T ) |  |  |  |  |  |  |
| FA | VI detected*41pcs of clip deformation and concentrated the carrier edge. Confirm that the Post-AOI image clip has no deformation phenomenon. Confirm X-ray image, clip deformation, the locking risk stands between the back of Post-AOI and the X-Ray. Confirmed that operator handling products may cause clip deformation risk after the reflow. Confirm that operator to remove metal which may cause the clip deformation risk. Simulation：The operator handling products and removing metal cover method , the defect reproduce. Conclusion: Improper handling of the product and remove metal cover method lead to the clip deformation. |  |  |  |  |  |  |
| CA | 1.Training the operator holding carrier and remove metal cover method to avoid the clip. Done 8/22 Xiaofeng 2.Ask operator to follow SOP operation. Done 8/22 Xiaofeng 3.Import the automatic removed metal cover machine in EVT. On-going |  |  |  |  |  |  |
| Validation | Tracked 2900pcs, the defective rate 0.00%(0F/2900T). Done 9/12 Xiaofeng |  |  |  |  |  |  |

X-Ray Image
4. Failure FACA
OK
NG
Simulation
Handling operation
OK
NG
Remove Metal Cover
Mapping
Risk Station
Training list and SOP

## Slide 64

| Component | UAT1 Flex | Vendor | Murata | APN | 056-20573 | Failure process/station | VI |
|---|---|---|---|---|---|---|---|
| Issue Description | Flex deformation-Handling issue Defected rate:  0.39% (23F/5850T)              Before:  1.04% (13F/1250T)                              0.95%(10F/1050)                After :  0.00% (0F/3550T) |  |  |  |  |  |  |
| FA | VI detected flex deformation*23pcs, panel and cavity are not concentrated. Post-AOI images show that flex is not deformed and the locking risk is between Post-AOI and VI. Confirm that the remove cover sheet is used in the base without causing the risk of flex deformation. Confirm the dispensing operation, the product is covered by the cover sheet without deformation risk. Confirm that the flipping and remove tape method is not abnormal. Confirm the metal tray wall interference products when take the flex, so there is a risk of flex deformation. Simulation: Take the product from the metal tray, flex deformation phenomenon is consistent with it. Conclusion: The metal tray wall was interference with products during remove the flex resulting in flex deformation. |  |  |  |  |  |  |
| CA | 1.Optimize the Un-loading tray position for clamp flex and training operator the  method of clamp flex. Done 8/26 Xiaofeng 2.Import semi-automatic CCD to inspection flex in EVT. On-going |  |  |  |  |  |  |
| Validation | Tracked 3550pcs, the defective rate 0.00%(0F/3550T). Done 9/12 Xiaofeng |  |  |  |  |  |  |

4. Failure FACA
OK
NG
Before
After

## Slide 65

| Component | Flex | Vendor | Murata | APN | 056-20573 | Failure process/station | SPI |
|---|---|---|---|---|---|---|---|
| Issue Description | Printing issue---Handling issue Defected rate:  0.34% (20F/5850T)              Before:  0.32% (4F/1250T )                              0.29% (4F/1050T )                              0.74% (7F/950T )                              0.31% (3F/650T )                              0.15% (2F/650T )                After :  0.00% (0F/1300T ) |  |  |  |  |  |  |
| FA | SPI detected*20pcs of printing defect, distributed in different config. SPI image shows that there are not foreign material on the flex surface, but 16pcs of solder paste have wiping marks. Link-AOI images show no abnormalities on the flex surface and no pressure plate at the edges. Confirm that the stencil printing surface and printing parameters and wiping mechanism and block are normal. Confirm that the metal cover is added by manually , so operator add metal cover shift cause solder issue. Conclusion：Manual operation during smt process resulted in printing issue. |  |  |  |  |  |  |
| CA | 1.Training the operator should first align the Pin with the round hole，then place the metal cover. Done 9/2 Xiaofeng 2.Import the automatic add metal cover machine in EVT. On-going |  |  |  |  |  |  |
| Validation | Tracked 1300pcs, the defective rate 0.00%(0F/1300T). Done 9/2 Xiaofeng |  |  |  |  |  |  |

4. Failure FACA
SPI Image
OK
NG
Link- AOI Image
Add metal cover shift
OK
NG
Printing parameters
Mapping
Training list and SOP

## Slide 66

| Component | V53 UAT1 ASSY Flex | Vendor | Murata | APN | 056-20573-37 | Failure process/station | FVI |
|---|---|---|---|---|---|---|---|
| Issue Description | Flex dent--Process issue  Defected rate:0.30% (21F/5850T)             Before:0.81% (21F/2600T)                After:0% (0F/3250T) |  |  |  |  |  |  |
| FA | The defects were found in FVI, flex dent were in same location. Per backend process mapping, the risk station was MIC film P&P.  Check MIC film P&P station: The cover head and support surface of MIC film P&P fixture are mismatched, when OP manual close the cover head and over press have risk cause flex dent.  Conclusion: The MIC film P&P fixture was not  fool-proof cause flex dent. |  |  |  |  |  |  |
| CA | 1.Modify fixture to fool-proof, make cover head and support surface match, and add stopper of cover to avoid over press.    Done   DRI: Ronghui He  9/3 |  |  |  |  |  |  |
| Validation | Keep tracking product, 0F/3250T.    Done  DRI: Shufang Li  9/8 |  |  |  |  |  |  |

4. Failure FACA
OK
NG
The cover head and the support surface are mismatched
Cover head over press cause flex dent
Before
After

## Slide 67

| Component | ICT Test NTF Issue(Misjudgment issue) | Vendor | ICT | Failure process/station | Inline ICT |
|---|---|---|---|---|---|
| Issue Description | ICT Test NTF issue(Misjudgment issue)  Defected rate:0.32%(19F/5850T)             Before:0.88%(11F/1250)(Config1：X06P1-U1-MIYG8-SM)                         0.76% (8/1050T) (config2 : X06P1-U1-MIYG9-SM)               After: 0.0% (0F/950T) (config3 : X06P1-U1-MINX2-SA)                          0.0% (0F/650T) (config4 : X06P1-U1-MINX2-SA-D1)                         0.0% (0F/650T) (config5 : X06P1-U1-MIYG8-SM-D1)                         0.0% (0F/650T) (config6 : X06P1-U1-MIYG9-SM-D1)                         0.0% (0F/650T) (config7 : X06P1-U1-MINA8-SA-D1) |  |  |  |  |
| FA | The high ICT fail rate were found in 1st and 2nd  Configs. Based on the data analysis, the defects were concentrated on Pin3,Pin4 of strobe ICT test. After UAT1 and strobe bonding , the contact area for strobe pin3/pin4 with test probe pin is smaller since there is a little interference for UAT1 and strobe pin3/4 are, it will cause unstable ICT testing while poor contact. Conclusion :The probe pin is in poor contact with the strobe Pad, resulting in the high NTF issue. |  |  |  |  |
| CA/Suggestion | 1.Change the probe design, add for two thinner pogo pins to touch the strobe area for better contact.--8/27 Done  TE :Yazhou Ding 2.Take this as lesson for similar flex design. |  |  |  |  |
| Validation | Tracking the rest of configs, the NTF rate is 0%(F/R:0/3550). Will keep on tracking in P2 build. |  |  |  |  |

After
Before
4. Failure FACA

## Slide 68

| Item | Agenda |
|---|---|
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


## Slide 69
5. ORT Summary
Pass
Ongoing
Fail

| Bareflex / Assembly | Test | Total Q’ty | Input date | 100C | 200C | 300C | 400C | 500C |
|---|---|---|---|---|---|---|---|---|
| X06P1-U1-MIYG9-SM | 1.Heat Soak（500H) | 45 | 9/7 | 9/14 | 9/20 | 9/26 | 10/5 | 10/12 |
|  | 2.Thermal Cycling（500C) | 45 | 9/6 | 9/15 | 9/20 | 9/26 | 10/5 | 10/12 |
|  | 3.Thermal Shock（200C) | 45 | 9/9 |  | 9/18 |  |  |  |
|  | 4.Heat Soak and Flex Bending(168H) | 20 | 9/9 | 9/29 |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 9/9 | 9/29 |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 9/9 | 9/29 |  |  |  |  |
| X06P1-U1-MIYG8-SM | 1.Heat Soak（500H) | 45 | 9/13 | 9/19 | 9/25 | 10/3 | 10/9 | 10/15 |
|  | 2.Thermal Cycling（500C) | 45 | 9/13 | 9/19 | 9/25 | 10/3 | 10/9 | 10/15 |
|  | 3.Thermal Shock（200C) | 45 | 9/13 |  | 9/22 |  |  |  |
|  | 4.Heat Soak and Flex Bending(168H) | 20 | 9/13 | 10/3 |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 9/13 | 10/3 |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 9/13 | 10/3 |  |  |  |  |
| X06P1-U1-MINX2-SA | 1.Heat Soak（500H) | 45 | 9/13 | 9/19 | 9/25 | 10/3 | 10/9 | 10/15 |
|  | 2.Thermal Cycling（500C) | 45 | 9/13 | 9/19 | 9/25 | 10/3 | 10/9 | 10/15 |
|  | 3.Thermal Shock（200C) | 45 | 9/13 |  | 9/22 |  |  |  |
|  | 4.Heat Soak and Flex Bending(168H) | 20 | 9/13 | 10/3 |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 9/13 | 10/3 |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 9/13 | 10/3 |  |  |  |  |


## Slide 70
5. ORT Summary
Pass
Ongoing
Fail

| Bareflex / Assembly | Test | Total Q’ty | Input date | 100C | 200C | 300C | 400C | 500C |
|---|---|---|---|---|---|---|---|---|
| X06P1-U1-MINX2-SA-D1 | 1.Heat Soak（500H) | 45 | 9/14 | 9/20 | 9/26 | 10/4 | 10/10 | 10/16 |
|  | 2.Thermal Cycling（500C) | 45 | 9/14 | 9/20 | 9/26 | 10/4 | 10/10 | 10/16 |
|  | 3.Thermal Shock（200C) | 45 | 9/14 |  | 9/23 |  |  |  |
|  | 4.Heat Soak and Flex Bending(168H) | 20 | 9/14 | 10/4 |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 9/14 | 10/4 |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 9/14 | 10/4 |  |  |  |  |
| X06P1-U1-MIYG8-SM-D1 | 1.Heat Soak（500H) | 45 | 9/14 | 9/20 | 9/26 | 10/4 | 10/10 | 10/16 |
|  | 2.Thermal Cycling（500C) | 45 | 9/14 | 9/20 | 9/26 | 10/4 | 10/10 | 10/16 |
|  | 3.Thermal Shock（200C) | 45 | 9/14 |  | 9/23 |  |  |  |
|  | 4.Heat Soak and Flex Bending(168H) | 20 | 9/14 | 10/4 |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 9/14 | 10/4 |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 9/14 | 10/4 |  |  |  |  |
| X06P1-U1-MIYG9-SM-D1 | 1.Heat Soak（500H) | 45 | 9/14 | 9/20 | 9/26 | 10/4 | 10/10 | 10/16 |
|  | 2.Thermal Cycling（500C) | 45 | 9/14 | 9/20 | 9/26 | 10/4 | 10/10 | 10/16 |
|  | 3.Thermal Shock（200C) | 45 | 9/14 |  | 9/23 |  |  |  |
|  | 4.Heat Soak and Flex Bending(168H) | 20 | 9/14 | 10/4 |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 9/14 | 10/4 |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 9/14 | 10/4 |  |  |  |  |


## Slide 71
5. ORT Summary
Pass
Ongoing
Fail

| Bareflex / Assembly | Test | Total Q’ty | Input date | 100C | 200C | 300C | 400C | 500C |
|---|---|---|---|---|---|---|---|---|
| X06P1-U1-MINA:-SA-D1 | 1.Heat Soak（500H) | 45 | 9/14 | 9/20 | 9/26 | 10/4 | 10/10 | 10/16 |
|  | 2.Thermal Cycling（500C) | 45 | 9/14 | 9/20 | 9/26 | 10/4 | 10/10 | 10/16 |
|  | 3.Thermal Shock（200C) | 45 | 9/14 |  | 9/23 |  |  |  |
|  | 4.Heat Soak and Flex Bending(168H) | 20 | 9/14 | 10/4 |  |  |  |  |
|  | 5.Thermal Cycling  and Flex Bending（100C) | 20 | 9/14 | 10/4 |  |  |  |  |
|  | 6.Flex Bending Test | 20 | 9/14 | 10/4 |  |  |  |  |


## Slide 72

| Item | Agenda |
|---|---|
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


## Slide 73

| Item | Agenda |
|---|---|
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


## Slide 74
7. Test Readiness and Automation Plan

| Test item | ERS/Test Plan | Test SW Readiness | Test HW Readiness | Test Automation | Test  Correlation With FATP IQC | Remark |
|---|---|---|---|---|---|---|
| Inline 1KHZ sensitivity | Y | Y | Y | NA | NA |  |
| Inline RF | Y | Y | Y | NA | NA |  |
| Inline ICT | Y | Y | Y | NA | NA |  |
| OQC  Mic Function  FR/ THD & Sealing | Y | Y | Y | NA | Y |  |
| OQC RF | Y | Y | Y | NA | Y |  |
| OQC ICT | Y | Y | Y | NA | Y |  |


## Slide 75
7. Test CPK and Highlight

| Station | Test item Q’ty | CPK<1.33 | 1.33<=CPK<2.0 | CPK>=2.0 | Comments |
|---|---|---|---|---|---|
| Inline 1KHZ sensitivity | 2 | 0 | 0 | 2 |  |
| Inline RF | 6231 | 0 | 0 | 6231 |  |
| Inline ICT | 58 | 0 | 0 | 58 |  |
| OQC  Mic Function  FR/ THD & Sealing | 30 | 0 | 0 | 30 |  |
| OQC RF | 6231 | 0 | 0 | 6231 |  |
| OQC  ICT | 58 | 0 | 0 | 58 |  |


## Slide 76
7. Test Coverage

| Flex | Station | Coverage | FA | CA |
|---|---|---|---|---|
| V53 UAT1 | RF&ICT &Mic Function | 183/193=94.8% | 1.R0302,R0303,R0304, R0400,R0401,R0402 0 ohm resistor occur short does not affect its resistance. 2.B2B 18,19,20,21Pin,same function pins are in the circuit，Short does not affect their connection. | SMT AOI and visual station will focus on check this position. |

SCH

## Slide 77
Test Coverage RF&ICT

| V53 UAT1 Mic Function +RF+ICT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CAP |  |  | IND |  |  | RES |  |  | IC |  |  |  | J_ UAT1 |  |  | Clip |  |
| Component | Open | Short | Component | Open | Short | Component | Open | Short | Component | Open | Short | ESD | Component | OPEN | Short | Component | Open |
| C0203 | Y | Y | L0305 | Y | Y | R0200 | Y | Y | U0300 | Y | Y | Y | J_ UAT1.PIN1 | Y | Y | CL_JD_M_TUNER | Y |
| C0204 | Y | Y | L0307 | Y | Y | R0302 | Y | N | U0301 | Y | Y | Y | J_ UAT1.PIN2 | Y | Y | PAD_GND_NORTH_BOTTOM | Y |
| C0320 | Y | Y | L0308 | Y | Y | R0303 | Y | N | U0302 | Y | Y | Y | J_ UAT1.PIN3 | Y | Y | CL_JD_M_GND | Y |
| C0322 | Y | Y | L0309 | Y | Y | R0304 | Y | N | U0303 | Y | Y | Y | J_ UAT1.PIN4 | Y | Y | CL_ANT10_GND | Y |
| C0300 | Y | Y | L0301 | Y | Y | R0402 | Y | N | U0400 | Y | Y | Y | J_ UAT1.PIN5 | Y | Y | CL_ANT10_FEED | Y |
| C0325 | Y | Y | L0303 | Y | Y | R0400 | Y | N | U0601 | Y | Y | Y | J_ UAT1.PIN6 | Y | Y | CL_ANT2_VERT_SP | Y |
| C0321 | Y | Y | L0300 | Y | Y | R0401 | Y | N |  |  |  |  | J_ UAT1.PIN7 | Y | Y | CL_ANT2_SHORT | Y |
| C0311 | Y | Y | L0406 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN8 | Y | Y | CL_ANT2_FEED | Y |
| C0319 | Y | Y | L0413 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN9 | Y | Y | CL1_SUS_STIFFENER | Y |
| C0309 | Y | Y | L0416 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN10 | Y | Y | CL2_SUS_STIFFENER | Y |
| C0306 | Y | Y | L0409 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN11 | Y | Y | CL_JINDO_L | Y |
| C0400 | Y | Y | L0411 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN12 | Y | Y | CL_STROBE_GND_EAST | Y |
| C0401 | Y | Y | L0600 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN13 | Y | Y | CL_STROBE_GND_WEST | Y |
| C0418 | Y | Y | L0601 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN14 | Y | Y | SR_SPKR_POS | Y |
| C0302 | Y | Y | L0602 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN15 | Y | Y | SR_SPKR_NEG | Y |
| C0410 | Y | Y | L0603 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN16 | Y | Y |  |  |
| C0411 | Y | Y | L0604 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN17 | Y | Y |  |  |
| C0412 | Y | Y | L0605 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN18 | Y | N |  |  |
| C0403 | Y | Y | L0606 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN19 | Y | N |  |  |
| C0409 | Y | Y | L0607 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN20 | Y | N |  |  |
| C0402 | Y | Y | L0608 | Y | Y |  |  |  |  |  |  |  | J_ UAT1.PIN21 | Y | N |  |  |
| C0600 | Y | Y |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN22 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN23 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN24 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN25 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN26 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN27 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN28 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN29 | Y | Y |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  | J_ UAT1.PIN30 | Y | Y |  |  |


## Slide 78

| Item | Agenda |
|---|---|
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


## Slide 79

| Item | Agenda |
|---|---|
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


## Slide 80
9. MCO FAI / CPK Summary

| Config | Station | Total Qty | CPK<1.33 | 1.33<=CPK<1.67 | CPK>=1.67 | CPK Raw data and chart |
|---|---|---|---|---|---|---|
| X06P1-U1-MIYG8-SM | FAI | 38 | 7 | 0 | 31 | Detail follow as FAI/CPK raw data |
|  | SPC | 30 | 0 | 0 | 30 |  |
| X06P1-U1-MIYG9-SM | FAI | 38 | 7 | 0 | 31 | Detail follow as FAI/CPK raw data |
|  | SPC | 30 | 0 | 0 | 30 |  |
| X06P1-U1-MINX2-SA | FAI | 38 | 7 | 0 | 31 | Detail follow as FAI/CPK raw data |
|  | SPC | 30 | 0 | 0 | 30 |  |
| X06P1-U1-MINX2-SA-D1 | FAI | 38 | 7 | 0 | 31 | Detail follow as FAI/CPK raw data |
|  | SPC | 30 | 0 | 0 | 30 |  |
| X06P1-U1-MIYG8-SM-D1 | FAI | 38 | 7 | 0 | 31 | Detail follow as FAI/CPK raw data |
|  | SPC | 30 | 0 | 0 | 30 |  |
| X06P1-U1-MIYG9-SM-D1 | FAI | 38 | 7 | 0 | 31 | Detail follow as FAI/CPK raw data |
|  | SPC | 30 | 0 | 0 | 30 |  |
| X06P1-U1-MINA8-SA-D1 | FAI | 38 | 7 | 0 | 31 | Detail follow as FAI/CPK raw data |
|  | SPC | 30 | 0 | 0 | 30 |  |


## Slide 81

| MCO# | 056-20573-37 | Gerber# | POR:821-05715-01/DOE:921-05695-01 |
|---|---|---|---|
| Issue Description | FAI148/149/150/151/152/153/154 has risk of low CPK<1.67. |  |  |
| FA | The dimension of UV glue for normal design is a maximum distance of 0.55mm from the component. According to the current MCO definition +/-0.20mm cannot achieve CPK>1.67 |  |  |
| CA/Suggestion | Short term: PD deviate the CPK＜1.67 for P1; Long term: Suggest to modify FAI148/149/150/151/152/153/154                      to use Max/Min for control in P2 |  |  |
| Validation | Proposal for P2 |  |  |

9. Low CPK(CPK<1.67) FACA
Long term
With long term
P1 data collection for reference
UV glue dispensing matrix for reference
V54 UAT2 UV dimension control for reference
UV glue dispensing for reference

## Slide 82

| Item | Agenda |
|---|---|
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


## Slide 83
10. Data Collection summary

| Items | Component | Criteria | 5x Test sample pictures | Result | Note |
|---|---|---|---|---|---|
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


## Slide 84
10. Data Collection summary

| Items | Component | Criteria | 5x Test sample pictures | Result | Note |
|---|---|---|---|---|---|
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


## Slide 85

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | J-UAT1 | Solder void<20% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |

10. Data Collection
Void: 0.15%
Void:0.23%
Void:0.95%
Void: 1.67%
Void: 0.04%
Void: 0.77%
Void: 1.28%
Void: 0.07%
Void:0.40%
Void:1.04%
Void:1.16%
Void:0.13%
Void:0.95%
Void:2.66%
Void:2.04%
Void: 6.23%
Void: 2.77%
Void: 0.31%
Void: 2.98%
Void:5.70%

## Slide 86

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | J-UAT1 | Solder void<20% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |

10. Data Collection
Void: 3.98%
Void:0.64%
Void:1.12%
Void: 2.61%
Void: 1.57%
Void: 0.42%
Void: 1.52%
Void: 2.72%
Void:3.45%
Void:1.40%
Void:1.88%
Void:1.20%
Void:4.14%
Void:1.03%
Void:0.17%
Void: 0.70%
Void: 1.08%
Void: 0.54%
Void:1.32%

## Slide 87

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | U0400 | Solder void<20% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  | U0301 |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |

Data Collection
Void: 0.76%
Void:0.11%
Void: 0.37%
Void: 0.12%
Void: 1.45%
Void: 2.59%
Void:0.20%
Void:0.31%
Void:0.29%
Void:1.50%
Void:0.56%
Void:0.31%
Void:1.72%
Void:0.45%

## Slide 88

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | U303 | Solder void<20% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |

Data Collection
Void: 0.47%
Void:1.94%
Void: 1.90%
Void: 1.51%
Void: 0.12%
Void: 0.08%
Void:0.15%
Void:0.08%
Void:0.15%
Void:1.58%
Void:0.19%

## Slide 89

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | U302 | Solder void<20% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |

Data Collection
Void: 0.76%
Void:0.11%
Void: 0.37%
Void: 0.12%
Void: 1.45%
Void: 2.59%
Void:0.13%
Void:1.72%

## Slide 90

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | CL-ANT10-GND | Solder void<35% |  |  |  |  |  | Pass |  |
|  | CL_ANT10-FEED | Solder void<35% |  |  |  |  |  | Pass |  |
|  | CCL-STROBE-GND-WEST | Solder void<35% |  |  |  |  |  | Pass |  |

Data Collection
Void: 7.40%
Void: 7.35%
Void: 8.86%
Void: 6.55%
Void: 8.22%
Void: 8.69%
Void: 5.53%
Void: 5.25%
Void: 3.73%
Void: 6.54%
Void: 6.41%
Void: 9.44%
Void: 5.53%
Void: 7.49%
Void: 9.20%

## Slide 91

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | CL2-SUS-STIFFENER | Solder void<35% |  |  |  |  |  | Pass |  |
|  | CL-ANT2-VERT-SP |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  | CL-ANT2-SHORT |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Pass |  |

Data Collection
Void: 5.79%
Void: 10.30%
Void: 4.65%
Void: 7.34%
Void: 4.89%
Void: 5.68%
Void: 5.60%
Void: 11.08%
Void: 10.31%
Void: 9.19%
Void: 10.37%
Void: 4.51%
Void: 4.84%
Void: 2.44%
Void: 2.76%

## Slide 92

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | L0406 | Solder void<35% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |

Data Collection
Void: 6.20%
Void:6.57%
Void: 13.93%
Void: 4.15%
Void: 9.23%
Void: 4.49%
Void:9.33%
Void:10.00%
Void:6.50%
Void:8.04%

## Slide 93

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | SP-SPKR-POS | Solder void<35% |  |  |  |  |  | Pass |  |
|  | SP-SPKR-POS |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  | CL-STROBE-GND-ESST |  |  |  |  |  |  | Pass |  |
|  | CL-ANT2-FEED |  |  |  |  |  |  | Pass |  |

Data Collection
Void: 5.81%
Void: 5.72%
Void: 8.62%
Void: 7.92%
Void: 8.68%
Void: 7.53%
Void: 8.83%
Void: 9.00%
Void: 10.80%
Void: 8.93%
Void: 9.00%
Void: 5.95%
Void: 8.98%
Void: 6.86%
Void: 8.14%
Void: 5.59%
Void: 4.69%
Void: 2.06%
Void: 3.29%
Void: 3.17%

## Slide 94

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | CL-JINDO-M-GND | Solder void<35% |  |  |  |  |  | Pass |  |
|  | CL-JINDO-M-TUNER |  |  |  |  |  |  | Pass |  |
|  | CL-JINDO-L |  |  |  |  |  |  | Pass |  |
|  | CL1-SUS-STIFFNER |  |  |  |  |  |  | Pass |  |

Data Collection
Void: 8.13%
Void: 4.32 %
Void: 25.92%
Void: 6.80%
Void: 9.19%
Void: 6.53%
Void: 9.58%
Void: 4.01%
Void: 3.22%
Void:3.86%
Void: 4.86%
Void: 26.97%
Void: 23.93%
Void: 18.86%
Void: 23.06 %
Void: 11.69%
Void: 12.84%
Void: 10.91%
Void: 15.07%
Void: 12.78%

## Slide 95

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | MIC | Solder void<25% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |

Data Collection
Void: 1.86%
Void: 2.86 %
Void: 0.90%
Void: 1.02%
Void: 3.68%
Void: 2.30%
Void: 1.04%
Void: 4.08%
Void: 4.27%
Void:2.17%
Void: 2.07%
Void: 1.45%
Void: 0.72%
Void: 3.35%
Void: 2.24 %
Void: 2.13%
Void: 4.04%
Void: 5.26%
Void: 3.48%
Void: 2.37%

## Slide 96

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | MIC | Solder void<25% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |

Data Collection
Void: 2.90%
Void: 2.20%
Void: 2.66%
Void: 5.52%
Void: 3.09%
Void: 2.66%
Void: 1.28%
Void: 4.96%
Void: 2.24%
Void:7.63%
Void: 3.19%
Void: 3.71%
Void: 1.84%
Void: 3.94%
Void: 4.37%
Void: 3.50%
Void: 1.78%
Void: 3.65%
Void: 3.35%
Void: 5.10%

## Slide 97

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | Bonding | Solder void<35% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |

Data Collection
Void: 15.19%
Void: 2.70%
Void: 0.84%
Void: 20.07%
Void: 22.51%
Void: 14.65%
Void: 13.55%
Void: 14.54%
Void: 10.19%
Void:0.83%
Void: 0.96%
Void: 0.46%
Void: 1.78%
Void: 11.85%
Void: 2.92%
Void: 0.88%
Void: 6.68%
Void: 1.56%
Void: 5.16%
Void: 4.98%

## Slide 98

| Items | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| X-ray | Bonding | Solder void<35% |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  | Pass |  |

Data Collection
Void: 2.13%
Void: 0.92%
Void: 0.97%
Void: 1.76%
Void: 3.01%
Void: 4.58%
Void: 0.77%
Void: 0.51%
Void: 12.68%
Void: 1.83%
Void: 0.91%
Void: 1.22%
Void: 2.19%
Void: 0.68%
Void: 1.04%
Void: 5.23%
Void: 3.51%
Void: 2.58%
Void: 0.62%
Void: 0.85%

## Slide 99

| Items | Component | Criteria | location | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|---|
| X-ray | Bending | Trace no crack in bending area |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |  | Pass |  |

Data Collection
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

## Slide 100

| Items | Component | Criteria | location | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|---|
| X-ray | Bending | Trace no crack in bending area |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |  | Pass |  |

Data Collection
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

## Slide 101

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

G1
G2
P5
P6
P2
P3
P7
P1
P4
Data Collection
Solder Thickness :24.86µm
Solder Thickness :31.96µm
Solder Thickness :26.82µm
Solder Thickness :19.67µm
Solder Thickness :18.09µm
Solder Thickness :18.95µm
IMC Thickness :1.78~3.12µm
IMC Thickness :1.78~3.60µm
IMC Thickness :1.82~3.36µm
IMC Thickness :1.78	~2.74µm
IMC Thickness :1.58~3.74µm
IMC Thickness :1.58~3.65µm
Solder Thickness :20.15µm
IMC Thickness :1.78 ~3.45µm
Solder Thickness :21.79µm
IMC Thickness :1.68~3.36µm
Solder Thickness :19.19µm
IMC Thickness :1.82~3.12µm
G1
P15
G2
P1
G4
G3

## Slide 102

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

P8
P9
P14
P15
P11
P12
G3
P10
P13
Data Collection
Solder Thickness :20.15µm
Solder Thickness :28.17µm
Solder Thickness :29.51µm
Solder Thickness :22.65µm
Solder Thickness :25.58µm
Solder Thickness :22.74µm
IMC Thickness :1.68~3.26µm
IMC Thickness :1.68~3.45µm
IMC Thickness :1.44~3.50µm
IMC Thickness :1.30~2.83µm
IMC Thickness :1.54~3.21µm
IMC Thickness :1.44~3.02µm
Solder Thickness :29.03µm
IMC Thickness :1.87~3.45µm
Solder Thickness :24.23µm
IMC Thickness :1.44~3.26µm
Solder Thickness :22.79µm
IMC Thickness :1.73~3.02µm
G1
P15
G2
P1
G4
G3

## Slide 103

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |

G4
G5
G7
G8
G6
Data Collection
Solder Thickness :18.09µm
Solder Thickness :37.04µm
Solder Thickness :29.13µm
Solder Thickness :43.04µm
IMC Thickness :1.78~3.21µm
IMC Thickness :1.68~3.69µm
IMC Thickness :1.68~3.36µm
IMC Thickness :1.73	~3.12µm
Solder Thickness :23.99µm
IMC Thickness :1.82~3.17µm
G1
P15
G2
P1
G4
G3
G6
G5
G7
G8

## Slide 104

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

G9
G10
P20
P21
P17
P18
P22
P16
P19
Data Collection
Solder Thickness :19.91µm
Solder Thickness :34.88µm
Solder Thickness :27.30µm
Solder Thickness :34.74µm
Solder Thickness :34.74µm
Solder Thickness :25.82µm
IMC Thickness :1.49~3.84µm
IMC Thickness :1.58~3.84µm
IMC Thickness :1.82~3.65µm
IMC Thickness :1.78	~3.26µm
IMC Thickness :1.73~3.74µm
IMC Thickness :1.97~3.17µm
Solder Thickness :26.78µm
IMC Thickness :2.06~3.41µm
Solder Thickness :33.69µm
IMC Thickness :1.68~3.69µm
Solder Thickness :29.08µm
IMC Thickness :1.34~3.17µm
G9
P30
G10
P16
G12
G11

## Slide 105

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

P23
P24
P29
P30
P26
P27
G11
P25
P28
Data Collection
Solder Thickness :37.43µm
Solder Thickness :33.93µm
Solder Thickness :31.91µm
Solder Thickness :32.73µm
Solder Thickness :32.97µm
Solder Thickness :29.27µm
IMC Thickness :1.25~3.69µm
IMC Thickness :1.87~3.69µm
IMC Thickness :1.58~3.84µm
IMC Thickness :1.97	~3.60µm
IMC Thickness :2.11~3.79µm
IMC Thickness :1.87~3.60µm
Solder Thickness :37.04µm
IMC Thickness :1.73 ~3.79µm
Solder Thickness :28.98µm
IMC Thickness :1.97~3.74µm
Solder Thickness :35.65µm
IMC Thickness :2.35~3.84µm
G9
P30
G10
P16
G12
G11

## Slide 106

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

G12
G13
Data Collection
Solder Thickness :24.18µm
Solder Thickness :49.38µm
IMC Thickness :1.97~3.79µm
IMC Thickness :1.82~3.36µm
G9
P30
G10
P16
G12
G11
G13

## Slide 107

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

G1
G9
P1
P16
G2
G10
Data Collection
Solder Thickness :20.54µm
Solder Thickness :25.43µm
Solder Thickness :33.06µm
Solder Thickness :32.92µm
Solder Thickness :28.02µm
Solder Thickness :30.47µm
IMC Thickness :1.34~3.36µm
IMC Thickness :1.54~3.36µm
IMC Thickness :1.73~3.36µm
IMC Thickness :1.82	~2.88µm
IMC Thickness :1.39~3.02µm
IMC Thickness :1.54~3.31µm
G1
P16
P1
G9
G2
G10

## Slide 108

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

P3
P18
P7
P22
P5
Data Collection
Solder Thickness :30.33µm
Solder Thickness :28.98µm
Solder Thickness :31.29µm
Solder Thickness :25.96µm
Solder Thickness :19.91µm
IMC Thickness :1.78~3.12µm
IMC Thickness :1.78~3.12µm
IMC Thickness :1.44~3.65µm
IMC Thickness :1.49~3.26µm
IMC Thickness :1.63~2.93µm
P20
Solder Thickness :29.13µm
IMC Thickness :1.44~3.36µm
P3
P18
P5
P20
P7
P22

## Slide 109

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

P9
P24
P13
P28
P11
Data Collection
Solder Thickness :28.79µm
Solder Thickness :26.63µm
Solder Thickness :18.81µm
IMC Thickness :1.92~3.45µm
IMC Thickness :1.54~3.50µm
IMC Thickness :1.44~3.31µm
P20
Solder Thickness :23.85µm
IMC Thickness :1.68~3.36µm
P11
P26
P13
P28
P9
P24
Solder Thickness :32.87µm
Solder Thickness :30.23µm
IMC Thickness :1.20~2.74µm
IMC Thickness :1.34~3.12µm

## Slide 110

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

P15
P30
G4
G12
G3
Data Collection
Solder Thickness :29.75µm
Solder Thickness :20.97µm
Solder Thickness :34.40µm
Solder Thickness :43.09µm
Solder Thickness :35.17µm
IMC Thickness :1.44~2.98µm
IMC Thickness :1.44~2.88µm
IMC Thickness :1.92~3.69µm
IMC Thickness :1.78~3.07µm
IMC Thickness :1.54~3.12µm
G11
Solder Thickness :25.91µm
IMC Thickness :1.68~3.12µm
G3
G11
G4
G12
P15
P30

## Slide 111

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | JUAT1 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |

G8
Data Collection
Solder Thickness :25.96µm
IMC Thickness :1.49~3.26µm
G8

## Slide 112

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | CL_JINDO_L | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | PAD_GND_NORTH_TOP | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | CL_ANT2_FEED | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |

Pass
Fail
Data Collection
Solder Thickness : 12.64µm
IMC Thickness :1.42~2.98µm
Solder Thickness : 24.16µm
IMC Thickness :1.80~3.56µm
Solder Thickness :14.49µm
IMC Thickness :1.28~3.13µm

## Slide 113

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | CL_ANT2_SHORT | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | CL_ANT2_VERT_SP | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | CL_ANT1_GND | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |

Pass
Fail
Data Collection
Solder Thickness : 14.52µm
IMC Thickness :1.56~2.53µm
Solder Thickness : 19.23µm
IMC Thickness :1.28~2.42µm
Solder Thickness :25.57µm
IMC Thickness :1.42~2.94µm

## Slide 114

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | CL_STROBE_GND_WEST | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | SUS_Stiffener_TOP | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | CL_STROBE_GND_EAST | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |

Pass
Fail
Data Collection
Solder Thickness : 22.16µm
IMC Thickness :1.56~3.17µm
Solder Thickness : 16.39µm
IMC Thickness :1.42~3.27µm
Solder Thickness :30.26µm
IMC Thickness :1.28~2.42µm

## Slide 115

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | SP_SPKR_POS | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | SP_SPKR_NEG | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | PAD_GND_NORTH_BOTTOM | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |

Pass
Fail
Data Collection
Solder Thickness : 20.32µm
IMC Thickness :1.28~2.98µm
Solder Thickness : 18.04µm
IMC Thickness :1.56~3.27µm
Solder Thickness :16.62µm
IMC Thickness :1.28~2.84µm

## Slide 116

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | CL_JINDO_M_TUNER | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  | CL_JINDO_M_GND | 1.Solder thickness (spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |

Pass
Fail
Data Collection
Solder Thickness : 21.31µm
IMC Thickness :1.28~3.40µm
Solder Thickness : 25.29µm
IMC Thickness :1.28~3.27µm

## Slide 117

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | L0406 | 1.Solder thickness(spec:10µm-50µm) 2.IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

Pass
Fail
Data Collection
Solder Thickness : 31.00um
IMC Thickness :1.30~3.36µm
Solder Thickness : 26.34µm
IMC Thickness :1.30~2.98µm

## Slide 118

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | U0300 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

P1
P4
P2
P3
Data Collection
IMC Thickness :1.42~2.56µm
IMC Thickness :1.28~2.27µm
IMC Thickness :1.28~2.13µm
IMC Thickness :1.37~2.70µm
P5
IMC Thickness :1.56~2.70µm
P1
P2
P4
P5
P3

## Slide 119

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | U0301 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

P1
P2
P3
Data Collection
IMC Thickness :1.73～3.12µm
IMC Thickness :1.25~1.54µm
IMC Thickness :1.20~1.78µm
P6
P4
P5
IMC Thickness :2.35～3.12µm
IMC Thickness :1.44~2.69µm
IMC Thickness :1.34~3.36µm

## Slide 120

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | U0302 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

P1
P2
P3
Data Collection
IMC Thickness :1.28～2.42µm
IMC Thickness :1.28~2.42µm
IMC Thickness :1.28~3.27µm
P6
P4
P5
IMC Thickness :1.56～2.84µm
IMC Thickness :1.42~2.84µm
IMC Thickness :1.28~2.98µm
P4
P2
P9
P7

## Slide 121

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | U0302 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |

P7
P8
P9
Data Collection
IMC Thickness :1.70～3.55µm
IMC Thickness :1.42~2.84µm
IMC Thickness :1.56~3.13µm
P10
IMC Thickness :1.28~3.13µm
P4
P2
P9
P7

## Slide 122

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | U0303 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

P1
P2
P3
Data Collection
IMC Thickness :1.92～3.21µm
IMC Thickness :1.25~2.74µm
IMC Thickness :1.49~3.02µm
P4
P6
IMC Thickness :1.39~3.07µm
IMC Thickness :2.21~3.36µm
P1
P2
P3
P4
P6

## Slide 123

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | U0303 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

P5
P7
P8
Data Collection
IMC Thickness :2.35～3.65µm
IMC Thickness :2.16~3.74µm
IMC Thickness :1.58~3.60µm
P11
P9
P10
IMC Thickness :2.45～3.89µm
IMC Thickness :2.06~3.45µm
IMC Thickness :1.82~3.69µm
P5
P7
P11

## Slide 124

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | U0400 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

P1
P2
P3
Data Collection
IMC Thickness :1.49～2.35µm
IMC Thickness :1.73~2.69µm
IMC Thickness :1.25~1.92µm
P6
P4
P5
IMC Thickness :1.28～2.27µm
IMC Thickness :1.39~2.02µm
IMC Thickness :1.42~2.13µm
P4
P8

## Slide 125

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | U0400 | 1. IMC  (spec: 1~4um) |  |  |  | Pass |  |

P7
P8
Data Collection
IMC Thickness :1.28～3.27µm
IMC Thickness :1.42~2.13µm
P8

## Slide 126

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | U0601 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

Data Collection
Solder Thickness :32.82µm
IMC Thickness :1.39~2.45µm
Solder Thickness :32.68µm
IMC Thickness :1.54~2.54µm
Solder Thickness :33.83µm
IMC Thickness :1.49~2.54µm
P1
P3
P2
P1
P4

## Slide 127

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | U0601 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

Data Collection
Solder Thickness :36.42µm
IMC Thickness :1.68~2.78µm
Solder Thickness :28.65µm
IMC Thickness :1.54~3.65µm
Solder Thickness :29.13µm
IMC Thickness :1.44~2.64µm
P4
P6
P5
P5
P8

## Slide 128

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | U0601 | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

Data Collection
Solder Thickness :31.53µm
IMC Thickness :1.44~2.93µm
Solder Thickness :32.10µm
IMC Thickness :1.34~3.07µm
P7
P8
P5
P8

## Slide 129

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | U0601 |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

Data Collection
P1
P8
P2
P1
P3
P4
P2
P3
P3

## Slide 130

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

PP0522
Data Collection
Solder Thickness :32.87µm
IMC Thickness :1.30~2.50µm
PP0521
Solder Thickness :28.69µm
IMC Thickness :1.63~2.93µm
PP0520
Solder Thickness :28.21µm
IMC Thickness :1.39~2.21µm
PP0522
PP0521
PP0520

## Slide 131

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

PP0523
Data Collection
Solder Thickness :40.55µm
IMC Thickness :1.25~3.17µm
PP0503
Solder Thickness :41.79µm
IMC Thickness :1.49~2.50µm
PP0506
Solder Thickness :38.82µm
IMC Thickness :1.54~2.54µm
PP0503
PP0506
PP0523

## Slide 132

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

PP0509
Data Collection
Solder Thickness :38.20µm
IMC Thickness :1.54~2.69µm
PP0518
Solder Thickness :36.61µm
IMC Thickness :1.20~3.36µm
PP0512
Solder Thickness :36.42µm
IMC Thickness :1.25~2.11µm
PP0518
PP0512
PP0509

## Slide 133

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

PP0515
Data Collection
Solder Thickness :39.49µm
IMC Thickness :1.30~2.40µm
PP0519
Solder Thickness :33.40µm
IMC Thickness :1.20~2.50µm
PP0519
PP0515

## Slide 134

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

PP0523
Data Collection
Solder Thickness :40.64µm
IMC Thickness :1.25~2.64µm
PP0502
Solder Thickness :39.64µm
IMC Thickness :1.20~3.02µm
PP0505
Solder Thickness :34.84µm
IMC Thickness :1.20~2.40µm
PP0505
PP0502
PP0523

## Slide 135

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

PP0508
Data Collection
Solder Thickness :33.64µm
IMC Thickness :1.15~2.50µm
PP0511
Solder Thickness :34.55µm
IMC Thickness :1.25~1.58µm
PP0516
Solder Thickness :33.93µm
IMC Thickness :1.58~2.74µm
PP0516
PP0511
PP0508

## Slide 136

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

PP0517
Data Collection
Solder Thickness :29.27µm
IMC Thickness :1.15~2.50µm
PP0519
Solder Thickness :36.13µm
IMC Thickness :1.20~2.06µm
PP0515
PP0519

## Slide 137

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

PP0523
Data Collection
Solder Thickness :38.57µm
IMC Thickness :1.17~2.80µm
PP0501
Solder Thickness :37.31µm
IMC Thickness :1.17~2.89µm
PP0504
Solder Thickness :33.58µm
IMC Thickness :1.26~3.26µm
PP0523
PP0501
PP0504

## Slide 138

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

PP0507
Data Collection
Solder Thickness :32.37µm
IMC Thickness :1.45~2190µm
PP0513
Solder Thickness :32.88µm
IMC Thickness :1.54~2.71µm
PP0510
Solder Thickness :31.02µm
IMC Thickness :1.40~2.94µm
PP0510
PP0513
PP0507

## Slide 139

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

PP0514
Data Collection
Solder Thickness :38.10µm
IMC Thickness :1.49~2.89µm
PP0519
Solder Thickness :34.37µm
IMC Thickness :1.54~2.57µm
PP0519
PP0514

## Slide 140

| Items | Component | Criteria | Test sample pictures |  |  | Result | Note |
|---|---|---|---|---|---|---|---|
| Cross section | Bonding | 1.Solder thickness  (spec: 10~60um)  2. IMC  (spec: 1~4um) |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  | Pass |  |

PP0524
Data Collection
Solder Thickness :26.49µm
IMC Thickness :1.21~2.66µm
PP0525
Solder Thickness :28.40µm
IMC Thickness :1.31~2.66µm
PP0526
Solder Thickness :28.40µm
IMC Thickness :1.31~3.03µm
PP0524
PP0525
PP0526

## Slide 141

| Items | Component | Criteria | location | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|---|
| X-ray | Bending | Trace no crack in bending area |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |  | Pass |  |
|  |  |  |  |  |  |  |  |  | Pass |  |

Data Collection
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
Bending （1）&（2）
Bending （1）&（2）

## Slide 142

| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| Peeling test | CL_STROBE_GND_WEST_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT10_GND_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT10_FEED_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT2_VERT_SP-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |

Pass
Fail
Data Collection
9.24N
10.88N
11.09N
10.53N
11.58N
9.29N
7.75N
8.64N
7.89N
8.26N
5.88N
5.11N
5.20N
5.53N
5.71N
5.69N
6.76N
6.39N
6.68N
5.62N

## Slide 143

| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| Peeling test | CL_ANT2_SHORT_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT2_FEED_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_STROBE_GND_EAST_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_JINDO_L_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |

Pass
Fail
Data Collection
8.81N
8.24N
8.63N
8.47N
9.80N
11.69N
12.00N
13.86N
11.13N
11.44N
9.41N
9.77N
10.35N
12.08N
12.11N
5.57N
5.17N
5.54N
5.92N
5.27N

## Slide 144

| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| Peeling test | CL_JINDO_M_TUNER_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Data collection for P1 |  |
|  | CL_ JINDO_M_GND_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | Bonding - Z(PI) | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | Bonding - Z(LCP) | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |

Pass
Fail
Data Collection
6.77N
8.02N
6.38N
6.64N
7.09N
4.42N
4.37N
5.05N
5.13N
4.79N
10.84N
11.09N
11.24N
10.20N
12.56N
7.64N
8.42N
6.22N
7.20N
7.73N

## Slide 145

| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| Peeling test | MIC_U0600_Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | JUAT1-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |

Pass
Fail
Data Collection
23.22N
20.78N
20.51N
23.74N
23.64N
10.75N
9.29N
9.44N
9.11N
9.49N

## Slide 146

| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| Pull test | CL_STROBE_GND_WEST_Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT10_GND_Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT10_FEED_X | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT2_VERT_SP-X | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |

Pass
Fail
Data Collection
50.55N
591.44N
52.80N
63.81N
57.65N
42.00N
47.07N
45.11N
44.81N
46.55N
61.52N
60.83N
61.59N
61.34N
61.25N
5.85N
6.02N
7.62N
6.20N
6.79N

## Slide 147

| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| Pull test | CL_ANT2_SHORT_Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ANT2_FEED_Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_STROBE_GND_EAST_X | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_JINDO_L_Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |

Pass
Fail
Data Collection
11.79N
15.65N
14.60N
14.49N
12.60N
65.44N
64.24N
63.74N
65.50N
65.67N
35.43N
40.78N
30.97N
32.71N
39.13N
43.94N
65.71N
46.01N
57.59N
60.21N

## Slide 148

| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| Pull test | CL_JINDO_M_TUNER_X | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | CL_ JINDO_M_GND_X | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | Bonding - Y(PI) | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | Bonding - Y（LCP) | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |

Pass
Fail
Data Collection
72.30N
74.13N
71.05N
73.31N
72.41N
44.62N
44.75N
48.18N
47.97N
50.09N
54.01N
59.52N
56.04N
55.56N
54.62N
63.78N
62.13N
63.69N
62.16N
62.01N

## Slide 149

| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| Pull test | MIC -X | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
|  | JUAT1-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |

Pass
Fail
Data Collection
150.36N
145.72N
150.27N
163.84N
136.66N
59.13N
72.11N
58.07N
60.93N
59.21N

## Slide 150

| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| Shear test | JUAT1-Y | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0300-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0301-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0302-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |

Pass
Fail
Data Collection
117.50 N
117.76N
107.51 N
133.85 N
132.65 N
5.74N
6.45 N
6.64 N
6.57 N
6.82 N
5.90N
6.02N
5.78N
5.92N
5.04N
9.26N
8.70N
9.62N
9.68 N
9.21N

## Slide 151

| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| Shear test | BGA U0303-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0400-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0300-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0301-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |

Pass
Fail
Data Collection
11.98 N
12.60N
12.76N
11.21 N
12.56N
11.56 N
9.33 N
11.45 N
10.68 N
9.35 N
5.45N
6.94N
6.68N
6.41N
6.90N
6.23N
5.24 N
5.96N
5.41 N
5.35N

## Slide 152

| Item | Component | Criteria | Test sample pictures |  |  |  |  | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| Shear test | BGA U0302-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0303-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |
| Shear test | BGA U0400-Z | 1. Force >5N 2. flex copper peel off and residual less than 25% |  |  |  |  |  | Pass |  |

Pass
Fail
Data Collection
9.94 N
8.25N
7.74 N
7.62 N
9.13 N
13.33 N
11.15 N
12.33 N
12.27N
12.92 N
11.00N
9.84N
9.66N
9.37N
9.19N

## Slide 153

| Item | Agenda |
|---|---|
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


## Slide 154
11. Assembly DFMEA top5

| Process | Failure Mode | Failure Eﬀects | Sev | Occ | Det | RPN | Current Design | Improved Design | Action Results |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | Sev | Occ | Det | RPN |
| Dispensing | FAI148/149/150/151/152/153/154 has risk of low CPK | Affect FATP assembly | 7 | 4 | 6 | 168 | Tight tolerance | 1.Build and monitor, collect data; 2.Optimize the parameter of dispensing machine3. Suggest to modify FAI148/149/150/151/152/153/154 to use Max/Min for control in P2Result:FAI148 CPK=0.509            FAI149 CPK=1.229            FAI150 CPK=0.305            FAI151 CPK=0.733            FAI152 CPK=-0.337            FAI153 CPK=0.932            FAI154 CPK=-3.706 | 7 | 4 | 6 | 168 |
| SMT | Z direction peeling force is lower than the SPEC.( 5N Min) | Fall off in transfer process and assembly process in FATP. | 7 | 4 | 6 | 168 | Clip peeling start point is at the bottom layer. | 1.Build and monitor, collect data(CL_JINDO_M_TUNER); 2. Change clip structure in P2Result :  Peeling force Z:(range:3.25-5.38N,mean:4.70N) | 7 | 4 | 6 | 168 |
| Bonding | Bonding shift & Rotate | Function NG | 5 | 4 | 7 | 140 | The bonding carrier strobe flex difficult to limit | 1.Build and monitor, collect data; 2.IQC and OQC inspection; 3.Optimize bonding fixture limit.Result: F/R=0F/5850T | 5 | 3 | 7 | 105 |
| Dispensing | UV glue overflow | Cosmetic NG | 7 | 3 | 6 | 126 | Tight tolerance | 1.Build and monitor, collect data; 2.Optimize the parameter of dispensing machineResult: F/R=0F/5850T | 7 | 2 | 6 | 84 |
| Test | B2B Pin deformation | Function issue | 7 | 3 | 5 | 105 | B2B APN:516S01290 | 1.Build and monitor, collect data;2.Improve equipment accuracyResult: F/R=0F/5850T | 7 | 2 | 5 | 70 |


## Slide 155

| Process | Failure Mode | Failure Effects | Sev | Occ | Det | RPN | Current process control | Improved control | Action results |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  | Sev | Occ | Det | RPN |
| SMT | Bonding coverage issue | Affect function | 6 | 5 | 5 | 150 | 1.Stencil opening follow cpp.2.SPI Inspection in spec.3.Bonding fixture and jig pressure in spec.4.Dispense flux parameter and Inspection in spec. | 1.Build and monitor, collect data.2.IQC and OQC inspection flex.3.Optimize bonding fixture & JIG.4.P1 Result: F/R=0F/5850T | 6 | 4 | 5 | 120 |
| SMT | L0406 dispense issue | Affect function | 7 | 3 | 6 | 126 | 1.Dispense Parameter and UV volume follow CPP. 2.Optimize dispense DOE for it.3.Control the component shift issue. | 1.Data collection in LBU build. 2.IQC and OQC inspection flex.3.P1 Result: F/R=0F/5850T | 7 | 2 | 6 | 84 |
| SMT | PI Flex warpage issue | Affect function | 6 | 5 | 4 | 120 | 1.Manual loading and unloading follow SOP.2.Use cover to press the flex in process.3.VI Handling follow SOP. | 1.Build and monitor, collect data(Strobe).2.IQC control.3.Process control.4.P1 Result: F/R=0F/5850T.Max=0.7mm，Min=0mm，Avg：0.3mm | 6 | 4 | 4 | 96 |
| SMT | Bonding area flux residual issue | Cosmetic NG | 6 | 4 | 4 | 96 | 1.Dispensing flux parameter and Inspection in spec.2.fixture design for flux residual.3.Reflow profile set up in spec. | 1.Build and monitor，collect data.2.Optimize SMT carrier.3.Optimize flux dispensing parameter.4.P1 Result: F/R=0F/5850T | 6 | 3 | 4 | 72 |
| SMT | Clip deformation issue | Cosmetic NG | 6 | 4 | 4 | 96 | 1.Op operation follow SOP production;2.Tray and carrier add avoid for clip; | 1.Build and monitor, collect data.2.IQC control deformation.3.Keep safe clearance for carrier and fixture.4.Add NG samples picture in SOP.5.P1 Result: F/R=41F/5850T | 6 | 7 | 4 | 168 |

11. Assembly PFMEA top5

## Slide 156

| Item | Agenda |
|---|---|
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


## Slide 157
12. OK2FAB”build and collect data + Reject” item Follow up

| Item | Issue detail | Category | Apple DFM feed back | Build follow up result | Status / Next step |
|---|---|---|---|---|---|
| 1 | FAI148/149/150/151/152/153/154 has risk of low CPK<1.67. FA: The dimension of UV glue for normal design is a maximum distance of 0.55mm from the component. | Design | Build and monitor | Result:FAI148 CPK=0.509,FAI149 CPK=1.229            FAI150 CPK=0.305,FAI151 CPK=0.733            FAI152 CPK=-0.337,FAI153 CPK=0.932            FAI154 CPK=-3.706 | Change dimension control in P2 |
| 2 | Clip CL_JINDO_M_TUNER has risk of low peeling force in Z-axis direction. | Design | Build and monitor | Result :  Peeling force Z:(range:3.25-5.38N, mean:4.70N) | Change clip structure in P2 |
| 3 | Current bonding pad design is cost up which solder ball in strobe tail flex(small pad). | Design | Build and monitor | Result: F/R=0F/5850T (Solder bump on strobe tail, more line and machine and fixture with this process.) | Change UAT1&strobe pad dimension in P2 |
| 4 | There is a risk of shift after flex and strobe tail bonding FA: The current design of the strobe shape，bonding carrier cannot fully limit the shape of the strobe | Design | Build and monitor | Result: F/R=0F/5850T | Close |
| 5 | Chip L0406 is close to the flex outline and C-PSA pad that the encapsulation width has risk of overflow. FA: For Chip 0603 its full dispensing encapsulation width need 0.8mm which can meet CPK＞1.67, L0406 is much bigger than chip 0603 | Design | Build and monitor | Result: F/R=0F/5850T | Close |
| 6 | There is a risk of low solder coverage or overflow in PAD when UAT1 flex is bonded with strobe flex. FA: The gap need ≥0.3mm from pad to coverlay based on TA. | Design | Build and monitor | Result: F/R=0F/5850T | Close |
| 7 | FM location is abnormal design. FA: There are be flux shift issues. | Design | Build and monitor | Result: F/R=0F/5850T | Close |


## Slide 158

| Item | Agenda |
|---|---|
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


## Slide 159

| MCO# | 056-20573-37 | Gerber# | POR:821-05715-01/DOE:921-05695-01 |
|---|---|---|---|
| Issue Description | FAI148/149/150/151/152/153/154 has risk of low CPK<1.67. |  |  |
| FA | The dimension of UV glue for normal design is a maximum distance of 0.55mm from the component. According to the current MCO definition +/-0.20mm cannot achieve CPK>1.67. |  |  |
| CA/ Suggestion | Short term: PD deviate the CPK＜1.67 for P1; Long term: Suggest to modify FAI148/149/150/151/152/153/154                      to use Max/Min for control in P2 |  |  |
| Validation | Proposal for P2 |  |  |

13. DFM on MCO, CPP, QCP design, automation, Quality, Eﬃciency, Cost reduction

| Item | Category | Issue decription | Suggestions | Status |
|---|---|---|---|---|
| 1 | Design | FAI148/149/150/151/152/153/154 has risk of low CPK<1.67. | Short term: PD deviate the CPK＜1.67 for P1; Long term: Suggest to modify FAI148/149/150/151/152/153/154                      to use Max/Min for control in P2 |  |

P1 data collection for reference
UV glue dispensing for reference
UV glue dispensing matrix for reference
V54 UAT2 UV dimension control for reference
With long term
Long term

## Slide 160

| MCO# | 056-20573-37 | Gerber# |  | POR:821-05715-01/DOE:921-05695-01 |
|---|---|---|---|---|
| Issue Description | Clip CL_JINDO_M_TUNER(JINDO MID TUNER) Z-axis peeling force＜5N. |  |  |  |
| FA | Clip peeling start point is at the bottom layer. |  |  |  |
| CA/ Suggestion | Short term: Deviate the peeling force<5N for P1; Long term: Suggest to change the clip peeling start point form                     bottom layer to top layer in P2. |  |  |  |
| Validation | Proposal for P2 |  |  |  |

13. DFM on MCO, CPP, QCP design, automation, Quality, Eﬃciency, Cost reduction
Current design

| Item | Category | Issue decription | Suggestions | Status |
|---|---|---|---|---|
| 2 | Design | Clip CL_JINDO_M_TUNER has risk of low peeling force in Z-axis direction. | Short term: Deviate the peeling force<5N for P1; Long term: Suggest to change the clip peeling start point form                     bottom layer to top layer in P2. |  |

Proposal design
P1 data collection for reference
●Result: P1 Peeling force ＜5N ;
Z:(range:3.25-5.38N,mean:4.70N)
D7X clip design lesson learn for reference
Peeling force data collection for reference
Lesson learn:
Clip neck design from bottom layer to top layer can improve clip Z direction peeling force, and release stress force in FATP drop test.
Clip neck extend from top side design——Improve z direction peeling force and reduce clip fall off risk in FATP REL and drop test.

## Slide 161

| MCO# | 056-20573-37 | Gerber# |  | POR:821-05715-01/DOE:921-05695-01 |
|---|---|---|---|---|
| Issue Description | Current bonding pad design is cost up which solder ball in UAT1 flex(small pad). |  |  |  |
| FA | If printing pre solder in strobe, will add more line and machine and fixture. |  |  |  |
| CA/ Suggestion | Suggest to exchange the flex pad design and make the solder ball in strobe tail flex with small pad. |  |  |  |
| Validation | Proposal for P2 |  |  |  |

13. DFM on MCO, CPP, QCP design, automation, Quality, Eﬃciency, Cost reduction

| Item | Category | Issue decription | Suggestions | Status |
|---|---|---|---|---|
| 3 | Design | Current bonding pad design is cost up which solder ball in strobe tail flex(small pad). | Suggest to exchange the flex pad design and make the solder ball in UAT1 flex with small pad. |  |

Current design
Strobe flex: Small pad
UAT1 flex:
Big pad
Proposal design
Strobe flex:
Big pad
UAT1 flex:
Small pad
●Increase to large pads
●Decrease small pads
Solder bump on Strobe VS UAT1 flex process comparison
V54 design for reference
Strobe flex:
Big pad
UAT1 flex:
Small pad

## Slide 162

| Item | Agenda |
|---|---|
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
Test instruction

| Location | Test condition | Sample size |
|---|---|---|
| 1 | Bending | 10x |
| 2 | Bending | 10x |
| 3 | Bending | 10x |
| 4 | Bending | 10X |
| 5 | Bending | 10x |
| 6 | Bending | 10x |
| 7 | Pressing | 10x |
| 8 | Pressing | 10x |
| 9 | Pressing | 10x |
| 10 | Pressing | 10x |
| 11 | Twisting | 10x |
| 12 | Twisting | 10x |
| 13 | Twisting | 10x |
| 14 | Twisting | 10x |
| 15 | Twisting | 10x |
| 16 | Twisting | 10x |

Twisting location
Mishandling by engineer
Mis-handling and Abuse Test Review – Test to fail
Bending location
Pressing location

## Slide 164
Bending 45° one cycle
Test method SOP
Bending 90° one cycle
Mis-handling and Abuse Test Review – Test to fail

## Slide 165
Twisting 45° one cycle
Test method SOP
Twisting 90° one cycle
Mis-handling and Abuse Test Review – Test to fail

## Slide 166
Test method SOP
Pressing one cycle
Step 2:
Pressing
Step 3:
Hold flex
Step 1:
Hold flex
Mis-handling and Abuse Test Review – Test to fail

## Slide 167

| Test instruction |  |  | Test items(10 cycles) |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| Location | Test condition |  | Sample Q'ty | Condition | Cosmetic inspection | Full function each time | X-ray inspection when fail | Cross section Validation |
| 1 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 2 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 43 cycles NG (2pcs) 44 cycles NG (2pcs)   46 cycles NG (1pcs） | 43 cycles NG (2pcs) 44 cycles NG (2pcs)   46 cycles NG (1pcs） | NG | NA |
| 3 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 43 cycles NG (2pcs) 45 cycles NG (3pcs) | 43 cycles NG (2pcs) 45 cycles NG (3pcs) | NG | NA |
|  |  | 90° | 5pcs | 10 times | 10 cycles NG(5pcs) | 10 cycles NG(5pcs) | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 21 cycles NG (2pcs) 23 cycles NG (1pcs)   25 cycles NG (2pcs） | 21 cycles NG (2pcs) 23 cycles NG (1pcs)   25 cycles NG (2pcs） | NG | NA |
| 4 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 30 cycles NG(2pcs) 31 cycles NG(1pcs) 33 cycles NG(2pcs) | 30 cycles NG(2pcs) 31 cycles NG(1pcs) 33 cycles NG(2pcs) | NG | NA |
| 5 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
| 6 | Bending | 45° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |
|  |  | 90° | 5pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  |  | 5pcs | Test to fail or max 50 times | 50 cycles pass | 50 cycles pass | OK | OK |

MP condition Fail >10 cycles
Severe test Fail <10 cycles
MP condition Fail <10 cycles
Mis-handling and Abuse Test Review – Test to fail
Bending location

## Slide 168

| Test instruction |  |  | Test items(10 cycles) |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| Location | Test condition |  | Sample Q'ty | Condition | Cosmetic inspection | Full function each time | X-ray inspection when fail | Cross section Validation |
| 7 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 8 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 9 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 10 | pressing | Normal | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
|  |  | High | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | OK |
| 11 | Twisting | 45° | 10pcs | 10 times | 7 cycles NG(4pcs) 8 cycles NG(6pcs) | 7 cycles NG(4pcs) 8 cycles NG(6pcs) | NG | NA |
|  |  | 90° | 10pcs | 10 times | 2 cycles NG(4pcs) 3 cycles NG(6pcs) | 2 cycles NG(4pcs) 3 cycles NG(6pcs) | NG | NA |
| 12 | Twisting | 45° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | NA |
|  |  | 90° | 10pcs | 10 times | 3 cycles NG(4pcs) 4 cycles NG(6pcs) | 3 cycles NG(4pcs) 4 cycles NG(6pcs) | NG | NA |
| 13 | Twisting | 45° | 10pcs | 10 times | 8 cycles NG(4pcs) 9 cycles NG(6pcs) | 8 cycles NG(4pcs) 9 cycles NG(6pcs) | NG | NA |
|  |  | 90° | 10pcs | 10 times | 1 cycles NG(7pcs) 2 cycles NG(3pcs) | 1 cycles NG(7pcs) 2 cycles NG(3pcs) | NG | NA |
| 14 | Twisting | 45° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | NA |
|  |  | 90° | 10pcs | 10 times | 8 cycles NG(5pcs) 9 cycles NG(5pcs) | 8 cycles NG(5pcs) 9 cycles NG(5pcs) | NG | NA |
| 15 | Twisting | 45° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | NA |
|  |  | 90° | 10pcs | 10 times | 3 cycles NG(4pcs) 4 cycles NG(6pcs) | 3 cycles NG(4pcs) 4 cycles NG(6pcs) | NG | NA |
| 16 | Twisting | 45° | 10pcs | 10 times | 10 cycles pass | 10 cycles pass | OK | NA |
|  |  | 90° | 10pcs | 10 times | 9 cycles NG(3pcs) 10 cycles NG(7pcs) | 9 cycles NG(3pcs) 10 cycles NG(7pcs) | NG | NA |

MP condition Fail >10 cycles
Severe test Fail <10 cycles
MP condition Fail <10 cycles
Mis-handling and Abuse Test Review – Test to fail
Pressing location
Twisting location

## Slide 169

| Item | Location 3 | Location 2 | Location 3 | Location 4 |
|---|---|---|---|---|
|  | Bending 45° | Bending 90° | Bending 90° | Bending 90° |
| Cosmetic |  |  |  |  |
| X-ray |  |  |  |  |

Bending location
Failure mode
Mis-handling and Abuse Test Review – Test to fail

## Slide 170

| Item | Location 11 | Location 13 | Location 11 | Location 12 | Location 13 | Location 14 | Location 15 | Location 16 |
|---|---|---|---|---|---|---|---|---|
|  | Twisting 45° | Twisting 45° | Twisting 90° | Twisting 90° | Twisting 90° | Twisting 90° | Twisting 90° | Twisting 90° |
| Cosmetic |  |  |  |  |  |  |  |  |
| X-ray |  |  |  |  |  |  |  |  |

Twisting location
Failure mode
Mis-handling and Abuse Test Review – Test to fail

## Slide 171
Mis-handling and Abuse Test Review – Test to fail

| Design Weakness FACA |  |  |  |  |
|---|---|---|---|---|
| Location | Test  Failure FA | Improve plan | DRI | Due date |
| 11&13 | Location 11&13 failed at 45 degree twisting less than 10 cycles. FA: (1)  Flex thickness of location 11&13 are 0.208mm with 3 layers copper.        (2) The torque of twisting is smaller. Per ICT process review, there are no risk to cause over 45 degree  twisting ,  low risk | Optimize handling SOP for FATP | PQM/Yanmei Lu,  PE/Peng Huang. | 8/21, Done |

Twisting location

## Slide 172

| Item | Agenda |
|---|---|
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
15. NPI / MP Tooling status – From Bareflex to Assembly

| Station |  | Tooling | NPI soft tool | MP hard tool | FACA if not meet MP hard tool |
|---|---|---|---|---|---|
| Assembly | SMT | Carrier |  | V |  |
| Assembly | Glue | Carrier |  | V |  |
| Assembly | Bonding | Carrier |  | V |  |
| Assembly | PSA | Carrier |  | V |  |
| Assembly | Press | Fixture/ Mold | V |  | Semi-auto |
| Assembly | Bending | Fixture/ Mold | V |  | Semi-auto |
| Assembly | Test | ICT test | V |  | Semi-auto |
| Assembly | Test | RF test | V |  | Semi-auto |


## Slide 174

| Item | Agenda |
|---|---|
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


## Slide 175

| Item | Agenda |
|---|---|
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


## Slide 176

| Item | Agenda |
|---|---|
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


## Slide 177

| Item | Agenda |
|---|---|
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


## Slide 178

| Category | Component | Last generation(D93 UAT1) |  | P1 POR |  | P1 DOE |  | Remark |
|---|---|---|---|---|---|---|---|---|
|  |  | Vendor | Type/APN | Vendor | Type/APN | Vendor | Type/APN |  |
| SMT | Flex | Murata | 821-04985-A | Murata | 821-05715-01 | Murata | 921-05695-01 |  |
| SMT | Resistance | Cyntec | 117S00073*2 | TDK | 107S00297*1 | TDK | 107S00297*1 |  |
|  |  | Yageo |  | YAGEO | 118S00267*6 | YAGEO | 118S00267*6 |  |
| SMT | Inductor | Murata | 152S2036,152S2036,152S00542, 152S01156,152S00470,152S2044, 152S2041 | TDK | 152S00401 | TDK | 152S00401 |  |
|  |  |  |  | Murata | 152S00470,152S2036,152S00565, 152S00021*2,152S00153,152S02096, 152S00143*2,152S00026,152S00134, 152S01707*4,152S01708*5 | Murata | 152S00470,152S2036,152S00565, 152S00021*2,152S00153, 152S01156*4, 152S00143*2,152S00026,152S00134, 152S01707*4,152S01708*5 |  |
| SMT | Capacitor | Murata | 131S00017,138S00008,131S00699, 131S00646.131S0551,131S0544, 131S00700,131S0571,131S00697 | Murata | 138S00008*4,131S0278,131S00017*5, 131S00700,131S00646*3,131S0338, 131S00547*2,131S00698*3,131S0562 | Murata | 138S00008*4,131S0278,131S00017*5, 131S00700,131S00646*3,131S0338, 131S00547*2,131S00698*2,131S0562 |  |
|  |  | YAGEO TAIYO SAMSUNG MURATA | 131S00090*2 |  |  |  |  |  |
|  |  | YAGEO TAIYO SAMSUNG MURATA | 131S00090*2 | SAMSUNG | 138S0692 | SAMSUNG | 138S0692 |  |
| SMT | IC | Qorvo | 353S03265 | Qorvo | 353S03284, 353S03594 | Qorvo | 353S03284, 353S03594 |  |
|  |  | PSEMI | 353S03303,353S03654 | PSEMI | 353S04043, 353S03304 | PSEMI | 353S04043, 353S03304 |  |
|  |  |  |  | Infineon | 353S03610 | Infineon | 353S03610 |  |
| SMT | B2B | Murata | 516S00528 | Murata | 516S01290 | Murata | 516S01290 |  |
| SMT | Clip | ENNOVI/LY | 806-47843,806-47842, 806-47844,806-47841, 806-47374,806-44988, 806-47373,806-48707, 806-47375 | ENNOVI/LY | 806-50867,806-50868,806-50869, 806-50870,806-50871,806-50873, 806-51162,806-51201,806-51346, 806-51391,870-23917,870-23918 | ENNOVI/LY | 806-50867,806-50868,806-50869, 806-50870,806-50871,806-50873, 806-51162,806-51201,806-51346, 806-51391,870-23917,870-23918 |  |
| SMT | PCB | ICT-UMTC ICT-LGIT LGIT-LGIT | 820-03572-a | / | / | / | / |  |
| SMT | PI flex | / | / | Mflex Avary | 821-05769-01 | Mflex Avary | 821-05769-01 |  |
| SMT | MIC | / | / | GTK IFX AAC | 731-00333(R-G-P-8) 731-00333(R-G-P-9) 731-00334(R-X-R-2) 731-00337(R-A-P-8) | GTK IFX AAC | 731-00333(R-G-P-8) 731-00333(R-G-P-9) 731-00334(R-X-R-2) 731-00337(R-A-P-8) |  |
| SMT | MIC film | / | / | JT/DX | / | JT/DX | / |  |
| SMT | PSA | JT/DX | / | JT/DX | / | JT/DX | / |  |
| SMT | 2D Barcode | LD/FZX | / | LD/FZX | / | LD/FZX | / |  |

Black: Customer control
Blue: ICT owned
19. Vendor owned MP key part supplier POR Plan

## Slide 179

| Item | Agenda |
|---|---|
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
