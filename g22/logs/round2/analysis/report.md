# Round 2 analysis

Generated 2026-11-19 05:53 by `g22/scripts/analyze_round2.py` from `g22/logs/round2`.

## 0. Completion

- `ROUND2 DONE` present: **True**; start lines: 2
- jobs with exit=0: **22 of 22**; logs parsed: 22 of 22
- problems: **none**

## 1. Q0: switches off and reruns against round 1 (per case)

| Round-2 run | Round-1 log | Cases | Differing ranks | Role |
|---|---|---|---|---|
| 01_hipster_service_baseline | reproduction/OnlineBoutique_service_nezha.log | 56 | 0 | Q0 stop condition |
| 02_ts_service_baseline | reproduction/TrainTicket_service_nezha.log | 45 | 0 | Q0 stop condition |
| 21_ts_inner_baseline | reproduction/TrainTicket_inner_nezha.log | 45 | 0 | additional check (Amendment 1) |
| 22_hipster_inner_baseline | reproduction/OnlineBoutique_inner_nezha.log | 56 | 0 | additional check (Amendment 1) |
| 18_hipster_service_A | ablation/A_k3_hipster_service_nezha.log | 56 | 0 | additional check (Amendment 1) |
| 19_hipster_service_B_k3 | ablation/B_k3_hipster_service_nezha.log | 56 | 0 | additional check (Amendment 1) |
| 20_hipster_service_AB_k3 | ablation/AB_k3_hipster_service_nezha.log | 56 | 0 | additional check (Amendment 1) |

**Q0 stop condition (runs 1 and 2 equal round 1 per case): PASS**

## 2. Accuracy per run (analysis 1, analysis 4, Amendment A1)

Original = released evaluator. Strict, ordinal and pod-only come from the `G22-AUDIT` lines. AIS for the inner-level runs 21 and 22.

| Run | System | Level | Mode | k | Attr | Original @1 | @3 | @5 | Log says @1/@3/@5 | Strict @1 | @3 | @5 | Ordinal @1 | @3 | @5 | Pod-only @1 | @3 | @5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | OnlineBoutique | service | baseline | n/a | first | 52/56 (92.86%) | 54/56 (96.43%) | 54/56 (96.43%) | 92.86 / 96.43 / 96.43 | 52/56 (92.86%) | 54/56 (96.43%) | 54/56 (96.43%) | 52/56 (92.86%) | 52/56 (92.86%) | 54/56 (96.43%) | 52/56 (92.86%) | 52/56 (92.86%) | 54/56 (96.43%) |
| 02 | TrainTicket | service | baseline | n/a | first | 39/45 (86.67%) | 44/45 (97.78%) | 44/45 (97.78%) | 86.67 / 97.78 / 97.78 | 39/45 (86.67%) | 44/45 (97.78%) | 44/45 (97.78%) | 39/45 (86.67%) | 43/45 (95.56%) | 44/45 (97.78%) | 39/45 (86.67%) | 43/45 (95.56%) | 44/45 (97.78%) |
| 03 | OnlineBoutique | service | A | n/a | ratio | 49/56 (87.50%) | 51/56 (91.07%) | 51/56 (91.07%) | 87.50 / 91.07 / 91.07 | 49/56 (87.50%) | 51/56 (91.07%) | 51/56 (91.07%) | 49/56 (87.50%) | 49/56 (87.50%) | 51/56 (91.07%) | 53/56 (94.64%) | 53/56 (94.64%) | 55/56 (98.21%) |
| 04 | TrainTicket | service | A | n/a | ratio | 39/45 (86.67%) | 44/45 (97.78%) | 44/45 (97.78%) | 86.67 / 97.78 / 97.78 | 39/45 (86.67%) | 44/45 (97.78%) | 44/45 (97.78%) | 39/45 (86.67%) | 43/45 (95.56%) | 44/45 (97.78%) | 39/45 (86.67%) | 43/45 (95.56%) | 44/45 (97.78%) |
| 05 | OnlineBoutique | service | AB | 3 | ratio | 51/56 (91.07%) | 53/56 (94.64%) | 53/56 (94.64%) | 91.07 / 94.64 / 94.64 | 51/56 (91.07%) | 53/56 (94.64%) | 53/56 (94.64%) | 51/56 (91.07%) | 51/56 (91.07%) | 53/56 (94.64%) | 53/56 (94.64%) | 53/56 (94.64%) | 55/56 (98.21%) |
| 06 | TrainTicket | service | AB | 3 | ratio | 17/45 (37.78%) | 23/45 (51.11%) | 41/45 (91.11%) | 37.78 / 51.11 / 91.11 | 13/45 (28.89%) | 23/45 (51.11%) | 40/45 (88.89%) | 13/45 (28.89%) | 23/45 (51.11%) | 23/45 (51.11%) | 13/45 (28.89%) | 23/45 (51.11%) | 23/45 (51.11%) |
| 07 | TrainTicket | service | A | n/a | first | 39/45 (86.67%) | 44/45 (97.78%) | 44/45 (97.78%) | 86.67 / 97.78 / 97.78 | 39/45 (86.67%) | 44/45 (97.78%) | 44/45 (97.78%) | 39/45 (86.67%) | 43/45 (95.56%) | 44/45 (97.78%) | 39/45 (86.67%) | 43/45 (95.56%) | 44/45 (97.78%) |
| 08 | TrainTicket | service | B | 3 | first | 17/45 (37.78%) | 23/45 (51.11%) | 41/45 (91.11%) | 37.78 / 51.11 / 91.11 | 13/45 (28.89%) | 23/45 (51.11%) | 40/45 (88.89%) | 13/45 (28.89%) | 23/45 (51.11%) | 23/45 (51.11%) | 13/45 (28.89%) | 23/45 (51.11%) | 23/45 (51.11%) |
| 09 | TrainTicket | service | AB | 3 | first | 17/45 (37.78%) | 23/45 (51.11%) | 41/45 (91.11%) | 37.78 / 51.11 / 91.11 | 13/45 (28.89%) | 23/45 (51.11%) | 40/45 (88.89%) | 13/45 (28.89%) | 23/45 (51.11%) | 23/45 (51.11%) | 13/45 (28.89%) | 23/45 (51.11%) | 23/45 (51.11%) |
| 10 | OnlineBoutique | service | B | 1 | first | 46/56 (82.14%) | 50/56 (89.29%) | 50/56 (89.29%) | 82.14 / 89.29 / 89.29 | 37/56 (66.07%) | 50/56 (89.29%) | 50/56 (89.29%) | 37/56 (66.07%) | 48/56 (85.71%) | 50/56 (89.29%) | 41/56 (73.21%) | 53/56 (94.64%) | 55/56 (98.21%) |
| 11 | OnlineBoutique | service | B | 2 | first | 47/56 (83.93%) | 51/56 (91.07%) | 51/56 (91.07%) | 83.93 / 91.07 / 91.07 | 42/56 (75.00%) | 51/56 (91.07%) | 51/56 (91.07%) | 42/56 (75.00%) | 49/56 (87.50%) | 51/56 (91.07%) | 45/56 (80.36%) | 53/56 (94.64%) | 55/56 (98.21%) |
| 12 | OnlineBoutique | service | B | 4 | first | 49/56 (87.50%) | 51/56 (91.07%) | 51/56 (91.07%) | 87.50 / 91.07 / 91.07 | 49/56 (87.50%) | 51/56 (91.07%) | 51/56 (91.07%) | 49/56 (87.50%) | 49/56 (87.50%) | 51/56 (91.07%) | 52/56 (92.86%) | 52/56 (92.86%) | 54/56 (96.43%) |
| 13 | OnlineBoutique | service | B | 5 | first | 47/56 (83.93%) | 49/56 (87.50%) | 49/56 (87.50%) | 83.93 / 87.50 / 87.50 | 47/56 (83.93%) | 49/56 (87.50%) | 49/56 (87.50%) | 47/56 (83.93%) | 47/56 (83.93%) | 49/56 (87.50%) | 49/56 (87.50%) | 49/56 (87.50%) | 51/56 (91.07%) |
| 14 | TrainTicket | service | B | 1 | first | 6/45 (13.33%) | 17/45 (37.78%) | 27/45 (60.00%) | 13.33 / 37.78 / 60.00 | 3/45 (6.67%) | 11/45 (24.44%) | 25/45 (55.56%) | 3/45 (6.67%) | 10/45 (22.22%) | 15/45 (33.33%) | 4/45 (8.89%) | 16/45 (35.56%) | 21/45 (46.67%) |
| 15 | TrainTicket | service | B | 2 | first | 2/45 (4.44%) | 4/45 (8.89%) | 31/45 (68.89%) | 4.44 / 8.89 / 68.89 | 2/45 (4.44%) | 3/45 (6.67%) | 31/45 (68.89%) | 2/45 (4.44%) | 3/45 (6.67%) | 8/45 (17.78%) | 2/45 (4.44%) | 3/45 (6.67%) | 8/45 (17.78%) |
| 16 | TrainTicket | service | B | 4 | first | 36/45 (80.00%) | 44/45 (97.78%) | 44/45 (97.78%) | 80.00 / 97.78 / 97.78 | 32/45 (71.11%) | 44/45 (97.78%) | 44/45 (97.78%) | 32/45 (71.11%) | 43/45 (95.56%) | 44/45 (97.78%) | 32/45 (71.11%) | 43/45 (95.56%) | 44/45 (97.78%) |
| 17 | TrainTicket | service | B | 5 | first | 36/45 (80.00%) | 44/45 (97.78%) | 44/45 (97.78%) | 80.00 / 97.78 / 97.78 | 33/45 (73.33%) | 44/45 (97.78%) | 44/45 (97.78%) | 33/45 (73.33%) | 43/45 (95.56%) | 44/45 (97.78%) | 33/45 (73.33%) | 43/45 (95.56%) | 44/45 (97.78%) |
| 18 | OnlineBoutique | service | A | n/a | first | 52/56 (92.86%) | 54/56 (96.43%) | 54/56 (96.43%) | 92.86 / 96.43 / 96.43 | 52/56 (92.86%) | 54/56 (96.43%) | 54/56 (96.43%) | 52/56 (92.86%) | 52/56 (92.86%) | 54/56 (96.43%) | 53/56 (94.64%) | 53/56 (94.64%) | 55/56 (98.21%) |
| 19 | OnlineBoutique | service | B | 3 | first | 51/56 (91.07%) | 53/56 (94.64%) | 53/56 (94.64%) | 91.07 / 94.64 / 94.64 | 51/56 (91.07%) | 53/56 (94.64%) | 53/56 (94.64%) | 51/56 (91.07%) | 51/56 (91.07%) | 53/56 (94.64%) | 53/56 (94.64%) | 53/56 (94.64%) | 55/56 (98.21%) |
| 20 | OnlineBoutique | service | AB | 3 | first | 51/56 (91.07%) | 53/56 (94.64%) | 53/56 (94.64%) | 91.07 / 94.64 / 94.64 | 51/56 (91.07%) | 53/56 (94.64%) | 53/56 (94.64%) | 51/56 (91.07%) | 51/56 (91.07%) | 53/56 (94.64%) | 53/56 (94.64%) | 53/56 (94.64%) | 55/56 (98.21%) |
| 21 | TrainTicket | inner | baseline | n/a | first | 39/45 (86.67%) | 44/45 (97.78%) | 44/45 (97.78%) | 86.67 / 97.78 / 97.78 | 39/45 (86.67%) | 44/45 (97.78%) | 44/45 (97.78%) | 39/45 (86.67%) | 43/45 (95.56%) | 44/45 (97.78%) | 39/45 (86.67%) | 43/45 (95.56%) | 44/45 (97.78%) |
| 22 | OnlineBoutique | inner | baseline | n/a | first | 52/56 (92.86%) | 54/56 (96.43%) | 54/56 (96.43%) | 92.86 / 96.43 / 96.43 | 52/56 (92.86%) | 54/56 (96.43%) | 54/56 (96.43%) | 52/56 (92.86%) | 52/56 (92.86%) | 54/56 (96.43%) | 52/56 (92.86%) | 52/56 (92.86%) | 54/56 (96.43%) |

Cases where the original rank and the strict rank or ordinal position disagree:

| Run | Case | Service | Fault | Original | Strict | Ordinal | Pod position |
|---|---|---|---|---|---|---|---|
| 01 | 2022-08-22 04:02:07 | frontend | return | 2 | 2 | 4 | 4 |
| 01 | 2022-08-23 12:10:21 | frontend | return | 2 | 2 | 4 | 4 |
| 02 | 2023-01-29 09:34:19 | ts-food-service | return | 3 | 3 | 4 | 4 |
| 03 | 2022-08-22 04:02:07 | frontend | return | 2 | 2 | 4 | 4 |
| 03 | 2022-08-23 12:10:21 | frontend | return | 2 | 2 | 4 | 4 |
| 04 | 2023-01-29 09:34:19 | ts-food-service | return | 3 | 3 | 4 | 4 |
| 05 | 2022-08-22 04:02:07 | frontend | return | 3 | 3 | 4 | 4 |
| 05 | 2022-08-23 12:10:21 | frontend | return | 3 | 3 | 4 | 4 |
| 06 | 2023-01-29 08:43:04 | ts-contacts-service | return | 5 | 5 | 11 | 11 |
| 06 | 2023-01-29 08:52:06 | ts-contacts-service | return | 5 | 5 | 9 | 9 |
| 06 | 2023-01-29 09:12:56 | ts-basic-service | return | 5 | 5 | 9 | 9 |
| 06 | 2023-01-29 09:25:39 | ts-basic-service | exception | 5 | 5 | 9 | 9 |
| 06 | 2023-01-29 09:30:09 | ts-food-service | return | 5 | 5 | 9 | 9 |
| 06 | 2023-01-29 09:34:19 | ts-food-service | return | 7 | 7 | 12 | 12 |
| 06 | 2023-01-29 09:42:26 | ts-verification-code-service | return | 5 | 5 | 9 | 9 |
| 06 | 2023-01-29 09:49:34 | ts-verification-code-service | return | 5 | 5 | 9 | 9 |
| 06 | 2023-01-29 09:58:04 | ts-verification-code-service | return | 6 | 6 | 10 | 10 |
| 06 | 2023-01-29 10:04:34 | ts-travel-service | exception | 5 | 5 | 9 | 9 |
| 06 | 2023-01-29 10:12:48 | ts-travel-service | exception | 5 | 5 | 9 | 9 |
| 06 | 2023-01-29 10:26:20 | ts-travel2-service | exception | 5 | 5 | 9 | 9 |
| 06 | 2023-01-29 10:45:10 | ts-travel2-service | exception | 5 | 5 | 11 | 11 |
| 06 | 2023-01-29 10:50:16 | ts-travel2-service | exception | 5 | 5 | 9 | 9 |
| 06 | 2023-01-29 10:56:45 | ts-route-service | exception | 4 | 4 | 8 | 8 |
| 06 | 2023-01-29 11:04:05 | ts-route-service | exception | 4 | 4 | 8 | 8 |
| 06 | 2023-01-29 11:13:56 | ts-route-service | exception | 4 | 4 | 8 | 8 |
| 06 | 2023-01-29 11:19:59 | ts-price-service | exception | 2 | 2 | 3 | 3 |
| 06 | 2023-01-29 11:29:03 | ts-price-service | exception | 2 | 2 | 3 | 3 |
| 06 | 2023-01-29 11:36:06 | ts-price-service | exception | 2 | 2 | 3 | 3 |
| 06 | 2023-01-29 13:31:54 | ts-contacts-service | cpu_contention | 5 | 5 | 9 | 9 |
| 06 | 2023-01-29 14:23:31 | ts-verification-code-service | cpu_contention | 5 | 5 | 9 | 9 |
| 06 | 2023-01-29 14:49:57 | ts-food-service | cpu_contention | 6 | 7 | 11 | 11 |
| 06 | 2023-01-29 15:42:00 | ts-preserve-service | cpu_contention | 5 | 6 | 10 | 10 |
| 06 | 2023-01-30 11:51:46 | ts-contacts-service | network_delay | 1 | 2 | 2 | 2 |
| 06 | 2023-01-30 12:29:29 | ts-verification-code-service | network_delay | 1 | 2 | 2 | 2 |
| 06 | 2023-01-30 12:36:54 | ts-verification-code-service | network_delay | 1 | 2 | 2 | 2 |
| 06 | 2023-01-30 14:08:19 | ts-security-service | network_delay | 1 | 2 | 2 | 2 |
| 07 | 2023-01-29 09:34:19 | ts-food-service | return | 3 | 3 | 4 | 4 |
| 08 | 2023-01-29 08:43:04 | ts-contacts-service | return | 5 | 5 | 11 | 11 |
| 08 | 2023-01-29 08:52:06 | ts-contacts-service | return | 5 | 5 | 9 | 9 |
| 08 | 2023-01-29 09:12:56 | ts-basic-service | return | 5 | 5 | 9 | 9 |
| 08 | 2023-01-29 09:25:39 | ts-basic-service | exception | 5 | 5 | 9 | 9 |
| 08 | 2023-01-29 09:30:09 | ts-food-service | return | 5 | 5 | 9 | 9 |
| 08 | 2023-01-29 09:34:19 | ts-food-service | return | 7 | 7 | 12 | 12 |
| 08 | 2023-01-29 09:42:26 | ts-verification-code-service | return | 5 | 5 | 9 | 9 |
| 08 | 2023-01-29 09:49:34 | ts-verification-code-service | return | 5 | 5 | 9 | 9 |
| 08 | 2023-01-29 09:58:04 | ts-verification-code-service | return | 6 | 6 | 10 | 10 |
| 08 | 2023-01-29 10:04:34 | ts-travel-service | exception | 5 | 5 | 9 | 9 |
| 08 | 2023-01-29 10:12:48 | ts-travel-service | exception | 5 | 5 | 9 | 9 |
| 08 | 2023-01-29 10:26:20 | ts-travel2-service | exception | 5 | 5 | 9 | 9 |
| 08 | 2023-01-29 10:45:10 | ts-travel2-service | exception | 5 | 5 | 11 | 11 |
| 08 | 2023-01-29 10:50:16 | ts-travel2-service | exception | 5 | 5 | 9 | 9 |
| 08 | 2023-01-29 10:56:45 | ts-route-service | exception | 4 | 4 | 8 | 8 |
| 08 | 2023-01-29 11:04:05 | ts-route-service | exception | 4 | 4 | 8 | 8 |
| 08 | 2023-01-29 11:13:56 | ts-route-service | exception | 4 | 4 | 8 | 8 |
| 08 | 2023-01-29 11:19:59 | ts-price-service | exception | 2 | 2 | 3 | 3 |
| 08 | 2023-01-29 11:29:03 | ts-price-service | exception | 2 | 2 | 3 | 3 |
| 08 | 2023-01-29 11:36:06 | ts-price-service | exception | 2 | 2 | 3 | 3 |
| 08 | 2023-01-29 13:31:54 | ts-contacts-service | cpu_contention | 5 | 5 | 9 | 9 |
| 08 | 2023-01-29 14:23:31 | ts-verification-code-service | cpu_contention | 5 | 5 | 9 | 9 |
| 08 | 2023-01-29 14:49:57 | ts-food-service | cpu_contention | 6 | 7 | 11 | 11 |
| 08 | 2023-01-29 15:42:00 | ts-preserve-service | cpu_contention | 5 | 6 | 10 | 10 |
| 08 | 2023-01-30 11:51:46 | ts-contacts-service | network_delay | 1 | 2 | 2 | 2 |
| 08 | 2023-01-30 12:29:29 | ts-verification-code-service | network_delay | 1 | 2 | 2 | 2 |
| 08 | 2023-01-30 12:36:54 | ts-verification-code-service | network_delay | 1 | 2 | 2 | 2 |
| 08 | 2023-01-30 14:08:19 | ts-security-service | network_delay | 1 | 2 | 2 | 2 |
| 09 | 2023-01-29 08:43:04 | ts-contacts-service | return | 5 | 5 | 11 | 11 |
| 09 | 2023-01-29 08:52:06 | ts-contacts-service | return | 5 | 5 | 9 | 9 |
| 09 | 2023-01-29 09:12:56 | ts-basic-service | return | 5 | 5 | 9 | 9 |
| 09 | 2023-01-29 09:25:39 | ts-basic-service | exception | 5 | 5 | 9 | 9 |
| 09 | 2023-01-29 09:30:09 | ts-food-service | return | 5 | 5 | 9 | 9 |
| 09 | 2023-01-29 09:34:19 | ts-food-service | return | 7 | 7 | 12 | 12 |
| 09 | 2023-01-29 09:42:26 | ts-verification-code-service | return | 5 | 5 | 9 | 9 |
| 09 | 2023-01-29 09:49:34 | ts-verification-code-service | return | 5 | 5 | 9 | 9 |
| 09 | 2023-01-29 09:58:04 | ts-verification-code-service | return | 6 | 6 | 10 | 10 |
| 09 | 2023-01-29 10:04:34 | ts-travel-service | exception | 5 | 5 | 9 | 9 |
| 09 | 2023-01-29 10:12:48 | ts-travel-service | exception | 5 | 5 | 9 | 9 |
| 09 | 2023-01-29 10:26:20 | ts-travel2-service | exception | 5 | 5 | 9 | 9 |
| 09 | 2023-01-29 10:45:10 | ts-travel2-service | exception | 5 | 5 | 11 | 11 |
| 09 | 2023-01-29 10:50:16 | ts-travel2-service | exception | 5 | 5 | 9 | 9 |
| 09 | 2023-01-29 10:56:45 | ts-route-service | exception | 4 | 4 | 8 | 8 |
| 09 | 2023-01-29 11:04:05 | ts-route-service | exception | 4 | 4 | 8 | 8 |
| 09 | 2023-01-29 11:13:56 | ts-route-service | exception | 4 | 4 | 8 | 8 |
| 09 | 2023-01-29 11:19:59 | ts-price-service | exception | 2 | 2 | 3 | 3 |
| 09 | 2023-01-29 11:29:03 | ts-price-service | exception | 2 | 2 | 3 | 3 |
| 09 | 2023-01-29 11:36:06 | ts-price-service | exception | 2 | 2 | 3 | 3 |
| 09 | 2023-01-29 13:31:54 | ts-contacts-service | cpu_contention | 5 | 5 | 9 | 9 |
| 09 | 2023-01-29 14:23:31 | ts-verification-code-service | cpu_contention | 5 | 5 | 9 | 9 |
| 09 | 2023-01-29 14:49:57 | ts-food-service | cpu_contention | 6 | 7 | 11 | 11 |
| 09 | 2023-01-29 15:42:00 | ts-preserve-service | cpu_contention | 5 | 6 | 10 | 10 |
| 09 | 2023-01-30 11:51:46 | ts-contacts-service | network_delay | 1 | 2 | 2 | 2 |
| 09 | 2023-01-30 12:29:29 | ts-verification-code-service | network_delay | 1 | 2 | 2 | 2 |
| 09 | 2023-01-30 12:36:54 | ts-verification-code-service | network_delay | 1 | 2 | 2 | 2 |
| 09 | 2023-01-30 14:08:19 | ts-security-service | network_delay | 1 | 2 | 2 | 2 |
| 10 | 2022-08-22 04:02:07 | frontend | return | 3 | 3 | 4 | 4 |
| 10 | 2022-08-22 04:52:55 | checkoutservice | network_delay | 1 | 2 | 2 | 2 |
| 10 | 2022-08-22 05:18:09 | currencyservice | cpu_contention | 1 | 2 | 2 | 2 |
| 10 | 2022-08-22 05:27:06 | currencyservice | network_delay | 1 | 2 | 2 | 2 |
| 10 | 2022-08-22 06:52:56 | recommendationservice | network_delay | 1 | 2 | 2 | 2 |
| 10 | 2022-08-22 07:01:25 | recommendationservice | cpu_contention | 1 | 2 | 2 | 2 |
| 10 | 2022-08-22 07:10:43 | recommendationservice | cpu_consumed | 1 | 2 | 2 | 2 |
| 10 | 2022-08-23 12:01:25 | frontend | cpu_contention | 1 | 2 | 2 | 2 |
| 10 | 2022-08-23 12:10:21 | frontend | return | 3 | 3 | 5 | 5 |
| 10 | 2022-08-23 12:18:23 | frontend | cpu_consumed | 1 | 2 | 2 | 2 |
| 10 | 2022-08-23 14:03:48 | emailservice | cpu_consumed | 1 | 2 | 2 | 2 |
| 11 | 2022-08-22 04:02:07 | frontend | return | 3 | 3 | 4 | 4 |
| 11 | 2022-08-22 06:52:56 | recommendationservice | network_delay | 1 | 2 | 2 | 2 |
| 11 | 2022-08-22 07:01:25 | recommendationservice | cpu_contention | 1 | 2 | 2 | 2 |
| 11 | 2022-08-22 07:10:43 | recommendationservice | cpu_consumed | 1 | 2 | 2 | 2 |
| 11 | 2022-08-23 12:01:25 | frontend | cpu_contention | 1 | 2 | 2 | 2 |
| 11 | 2022-08-23 12:10:21 | frontend | return | 3 | 3 | 5 | 5 |
| 11 | 2022-08-23 12:18:23 | frontend | cpu_consumed | 1 | 2 | 2 | 2 |
| 12 | 2022-08-22 04:02:07 | frontend | return | 3 | 3 | 4 | 4 |
| 12 | 2022-08-23 12:10:21 | frontend | return | 3 | 3 | 4 | 4 |
| 13 | 2022-08-22 04:02:07 | frontend | return | 3 | 3 | 4 | 4 |
| 13 | 2022-08-23 12:10:21 | frontend | return | 3 | 3 | 4 | 4 |
| 14 | 2023-01-29 08:43:04 | ts-contacts-service | return | 5 | 5 | 15 | 15 |
| 14 | 2023-01-29 08:52:06 | ts-contacts-service | return | 5 | 5 | 15 | 15 |
| 14 | 2023-01-29 09:03:53 | ts-basic-service | return | 6 | 6 | 30 | 3 |
| 14 | 2023-01-29 09:12:56 | ts-basic-service | return | 4 | 4 | 10 | 1 |
| 14 | 2023-01-29 09:21:39 | ts-basic-service | return | 6 | 6 | 21 | 2 |
| 14 | 2023-01-29 09:25:39 | ts-basic-service | exception | 9 | 9 | 41 | 3 |
| 14 | 2023-01-29 09:30:09 | ts-food-service | return | 7 | 7 | 28 | 28 |
| 14 | 2023-01-29 09:34:19 | ts-food-service | return | 7 | 7 | 24 | 24 |
| 14 | 2023-01-29 09:42:26 | ts-verification-code-service | return | 6 | 6 | 17 | 17 |
| 14 | 2023-01-29 09:49:34 | ts-verification-code-service | return | 6 | 6 | 37 | 37 |
| 14 | 2023-01-29 09:58:04 | ts-verification-code-service | return | 6 | 6 | 30 | 30 |
| 14 | 2023-01-29 10:04:34 | ts-travel-service | exception | 3 | 3 | 8 | 8 |
| 14 | 2023-01-29 10:12:48 | ts-travel-service | exception | 4 | 4 | 6 | 6 |
| 14 | 2023-01-29 10:20:10 | ts-travel-service | exception | 4 | 4 | 13 | 13 |
| 14 | 2023-01-29 10:26:20 | ts-travel2-service | exception | 9 | 9 | 32 | 32 |
| 14 | 2023-01-29 10:45:10 | ts-travel2-service | exception | 9 | 9 | 41 | 34 |
| 14 | 2023-01-29 10:50:16 | ts-travel2-service | exception | 7 | 7 | 18 | 11 |
| 14 | 2023-01-29 10:56:45 | ts-route-service | exception | 4 | 4 | 17 | 17 |
| 14 | 2023-01-29 11:04:05 | ts-route-service | exception | 4 | 4 | 6 | 6 |
| 14 | 2023-01-29 11:13:56 | ts-route-service | exception | 4 | 4 | 17 | 17 |
| 14 | 2023-01-29 13:31:54 | ts-contacts-service | cpu_contention | 5 | 5 | 20 | 20 |
| 14 | 2023-01-29 14:23:31 | ts-verification-code-service | cpu_contention | 6 | 7 | 37 | 37 |
| 14 | 2023-01-29 14:49:57 | ts-food-service | cpu_contention | 7 | 7 | 35 | 35 |
| 14 | 2023-01-29 15:42:00 | ts-preserve-service | cpu_contention | 7 | 7 | 43 | 43 |
| 14 | 2023-01-30 11:51:46 | ts-contacts-service | network_delay | 2 | 4 | 4 | 4 |
| 14 | 2023-01-30 12:06:12 | ts-basic-service | network_delay | 2 | 3 | 3 | 3 |
| 14 | 2023-01-30 12:15:56 | ts-basic-service | network_delay | 3 | 4 | 5 | 5 |
| 14 | 2023-01-30 12:29:29 | ts-verification-code-service | network_delay | 1 | 2 | 2 | 2 |
| 14 | 2023-01-30 12:36:54 | ts-verification-code-service | network_delay | 3 | 7 | 8 | 8 |
| 14 | 2023-01-30 12:44:36 | ts-food-service | cpu_contention | 2 | 3 | 3 | 3 |
| 14 | 2023-01-30 12:52:04 | ts-food-service | network_delay | 1 | 2 | 2 | 2 |
| 14 | 2023-01-30 12:59:36 | ts-food-service | network_delay | 1 | 2 | 2 | 2 |
| 14 | 2023-01-30 13:06:49 | ts-travel-service | cpu_contention | 2 | 4 | 4 | 4 |
| 14 | 2023-01-30 13:15:43 | ts-travel-service | network_delay | 5 | 6 | 7 | 7 |
| 14 | 2023-01-30 13:22:22 | ts-travel-service | network_delay | 2 | 3 | 3 | 3 |
| 14 | 2023-01-30 14:00:16 | ts-security-service | network_delay | 3 | 4 | 5 | 5 |
| 14 | 2023-01-30 14:08:19 | ts-security-service | network_delay | 2 | 4 | 4 | 4 |
| 15 | 2023-01-29 08:43:04 | ts-contacts-service | return | 5 | 5 | 13 | 13 |
| 15 | 2023-01-29 08:52:06 | ts-contacts-service | return | 5 | 5 | 21 | 21 |
| 15 | 2023-01-29 08:58:16 | ts-contacts-service | return | 4 | 4 | 7 | 7 |
| 15 | 2023-01-29 09:03:53 | ts-basic-service | return | 4 | 4 | 5 | 5 |
| 15 | 2023-01-29 09:12:56 | ts-basic-service | return | 4 | 4 | 5 | 5 |
| 15 | 2023-01-29 09:21:39 | ts-basic-service | return | 4 | 4 | 5 | 5 |
| 15 | 2023-01-29 09:25:39 | ts-basic-service | exception | 7 | 7 | 26 | 26 |
| 15 | 2023-01-29 09:30:09 | ts-food-service | return | 8 | 8 | 28 | 28 |
| 15 | 2023-01-29 09:34:19 | ts-food-service | return | 8 | 8 | 29 | 29 |
| 15 | 2023-01-29 09:42:26 | ts-verification-code-service | return | 5 | 5 | 21 | 21 |
| 15 | 2023-01-29 10:04:34 | ts-travel-service | exception | 4 | 4 | 5 | 5 |
| 15 | 2023-01-29 10:12:48 | ts-travel-service | exception | 5 | 5 | 21 | 21 |
| 15 | 2023-01-29 10:26:20 | ts-travel2-service | exception | 6 | 6 | 14 | 13 |
| 15 | 2023-01-29 10:45:10 | ts-travel2-service | exception | 5 | 5 | 13 | 13 |
| 15 | 2023-01-29 10:50:16 | ts-travel2-service | exception | 4 | 4 | 5 | 5 |
| 15 | 2023-01-29 10:56:45 | ts-route-service | exception | 4 | 4 | 18 | 18 |
| 15 | 2023-01-29 11:04:05 | ts-route-service | exception | 4 | 4 | 18 | 18 |
| 15 | 2023-01-29 11:13:56 | ts-route-service | exception | 4 | 4 | 18 | 18 |
| 15 | 2023-01-29 13:31:54 | ts-contacts-service | cpu_contention | 5 | 5 | 21 | 21 |
| 15 | 2023-01-29 14:23:31 | ts-verification-code-service | cpu_contention | 6 | 6 | 25 | 25 |
| 15 | 2023-01-29 14:49:57 | ts-food-service | cpu_contention | 8 | 9 | 26 | 26 |
| 15 | 2023-01-29 15:42:00 | ts-preserve-service | cpu_contention | 7 | 8 | 27 | 27 |
| 15 | 2023-01-30 11:51:46 | ts-contacts-service | network_delay | 5 | 5 | 10 | 10 |
| 15 | 2023-01-30 11:59:21 | ts-basic-service | cpu_contention | 3 | 4 | 12 | 12 |
| 15 | 2023-01-30 12:06:12 | ts-basic-service | network_delay | 5 | 5 | 18 | 18 |
| 15 | 2023-01-30 12:15:56 | ts-basic-service | network_delay | 5 | 5 | 18 | 18 |
| 15 | 2023-01-30 12:29:29 | ts-verification-code-service | network_delay | 5 | 5 | 10 | 10 |
| 15 | 2023-01-30 12:36:54 | ts-verification-code-service | network_delay | 4 | 5 | 11 | 11 |
| 15 | 2023-01-30 12:44:36 | ts-food-service | cpu_contention | 5 | 5 | 17 | 17 |
| 15 | 2023-01-30 12:52:04 | ts-food-service | network_delay | 4 | 5 | 17 | 17 |
| 15 | 2023-01-30 12:59:36 | ts-food-service | network_delay | 4 | 4 | 9 | 9 |
| 15 | 2023-01-30 13:06:49 | ts-travel-service | cpu_contention | 5 | 5 | 18 | 18 |
| 15 | 2023-01-30 13:15:43 | ts-travel-service | network_delay | 6 | 6 | 20 | 20 |
| 15 | 2023-01-30 13:22:22 | ts-travel-service | network_delay | 5 | 5 | 18 | 18 |
| 15 | 2023-01-30 14:00:16 | ts-security-service | network_delay | 5 | 5 | 18 | 18 |
| 15 | 2023-01-30 14:08:19 | ts-security-service | network_delay | 5 | 5 | 19 | 19 |
| 16 | 2023-01-29 08:58:16 | ts-contacts-service | return | 2 | 2 | 3 | 3 |
| 16 | 2023-01-29 09:34:19 | ts-food-service | return | 3 | 3 | 4 | 4 |
| 16 | 2023-01-29 10:20:10 | ts-travel-service | exception | 2 | 2 | 3 | 3 |
| 16 | 2023-01-29 15:42:00 | ts-preserve-service | cpu_contention | 1 | 2 | 2 | 2 |
| 16 | 2023-01-30 12:29:29 | ts-verification-code-service | network_delay | 1 | 2 | 2 | 2 |
| 16 | 2023-01-30 12:36:54 | ts-verification-code-service | network_delay | 1 | 2 | 2 | 2 |
| 16 | 2023-01-30 14:08:19 | ts-security-service | network_delay | 1 | 2 | 2 | 2 |
| 17 | 2023-01-29 08:58:16 | ts-contacts-service | return | 2 | 2 | 3 | 3 |
| 17 | 2023-01-29 09:34:19 | ts-food-service | return | 3 | 3 | 4 | 4 |
| 17 | 2023-01-29 10:20:10 | ts-travel-service | exception | 2 | 2 | 3 | 3 |
| 17 | 2023-01-30 12:29:29 | ts-verification-code-service | network_delay | 1 | 2 | 2 | 2 |
| 17 | 2023-01-30 12:36:54 | ts-verification-code-service | network_delay | 1 | 2 | 2 | 2 |
| 17 | 2023-01-30 14:08:19 | ts-security-service | network_delay | 1 | 2 | 2 | 2 |
| 18 | 2022-08-22 04:02:07 | frontend | return | 2 | 2 | 4 | 4 |
| 18 | 2022-08-23 12:10:21 | frontend | return | 2 | 2 | 4 | 4 |
| 19 | 2022-08-22 04:02:07 | frontend | return | 3 | 3 | 4 | 4 |
| 19 | 2022-08-23 12:10:21 | frontend | return | 3 | 3 | 4 | 4 |
| 20 | 2022-08-22 04:02:07 | frontend | return | 3 | 3 | 4 | 4 |
| 20 | 2022-08-23 12:10:21 | frontend | return | 3 | 3 | 4 | 4 |
| 21 | 2023-01-29 09:34:19 | ts-food-service | return | 3 | 3 | 4 | 4 |
| 22 | 2022-08-22 04:02:07 | frontend | return | 2 | 2 | 4 | 4 |
| 22 | 2022-08-23 12:10:21 | frontend | return | 2 | 2 | 4 | 4 |

Total disagreeing case-runs: 210

## 3. Per-case rank changes against the baseline of the same system (analysis 2)

**03_hipster_service_A_ratio**: 5 of 56 cases changed
- 2022-08-22 05:18:09 currencyservice cpu_contention: 1 -> MISS
- 2022-08-23 13:27:51 currencyservice cpu_contention: 1 -> MISS
- 2022-08-23 16:05:02 adservice network_delay: MISS -> 1
- 2022-08-23 16:31:35 adservice cpu_contention: 1 -> MISS
- 2022-08-23 16:40:57 adservice cpu_consumed: 1 -> MISS

**04_ts_service_A_ratio**: 0 of 45 cases changed

**05_hipster_service_AB_k3_ratio**: 5 of 56 cases changed
- 2022-08-22 04:02:07 frontend return: 2 -> 3
- 2022-08-22 05:18:09 currencyservice cpu_contention: 1 -> MISS
- 2022-08-23 12:10:21 frontend return: 2 -> 3
- 2022-08-23 13:27:51 currencyservice cpu_contention: 1 -> MISS
- 2022-08-23 16:05:02 adservice network_delay: MISS -> 1

**06_ts_service_AB_k3_ratio**: 25 of 45 cases changed
- 2023-01-29 08:43:04 ts-contacts-service return: 1 -> 5
- 2023-01-29 08:52:06 ts-contacts-service return: 1 -> 5
- 2023-01-29 08:58:16 ts-contacts-service return: 1 -> 2
- 2023-01-29 09:12:56 ts-basic-service return: 1 -> 5
- 2023-01-29 09:25:39 ts-basic-service exception: 1 -> 5
- 2023-01-29 09:30:09 ts-food-service return: 1 -> 5
- 2023-01-29 09:34:19 ts-food-service return: 3 -> 7
- 2023-01-29 09:42:26 ts-verification-code-service return: 1 -> 5
- 2023-01-29 09:49:34 ts-verification-code-service return: 1 -> 5
- 2023-01-29 09:58:04 ts-verification-code-service return: 2 -> 6
- 2023-01-29 10:04:34 ts-travel-service exception: 1 -> 5
- 2023-01-29 10:12:48 ts-travel-service exception: 1 -> 5
- 2023-01-29 10:26:20 ts-travel2-service exception: 1 -> 5
- 2023-01-29 10:45:10 ts-travel2-service exception: 1 -> 5
- 2023-01-29 10:50:16 ts-travel2-service exception: 1 -> 5
- 2023-01-29 10:56:45 ts-route-service exception: 1 -> 4
- 2023-01-29 11:04:05 ts-route-service exception: 1 -> 4
- 2023-01-29 11:13:56 ts-route-service exception: 1 -> 4
- 2023-01-29 11:19:59 ts-price-service exception: 1 -> 2
- 2023-01-29 11:29:03 ts-price-service exception: 1 -> 2
- 2023-01-29 11:36:06 ts-price-service exception: 1 -> 2
- 2023-01-29 13:31:54 ts-contacts-service cpu_contention: 1 -> 5
- 2023-01-29 14:23:31 ts-verification-code-service cpu_contention: 1 -> 5
- 2023-01-29 14:49:57 ts-food-service cpu_contention: 2 -> 6
- 2023-01-29 15:42:00 ts-preserve-service cpu_contention: 1 -> 5

**07_ts_service_A**: 0 of 45 cases changed

**08_ts_service_B_k3**: 25 of 45 cases changed
- 2023-01-29 08:43:04 ts-contacts-service return: 1 -> 5
- 2023-01-29 08:52:06 ts-contacts-service return: 1 -> 5
- 2023-01-29 08:58:16 ts-contacts-service return: 1 -> 2
- 2023-01-29 09:12:56 ts-basic-service return: 1 -> 5
- 2023-01-29 09:25:39 ts-basic-service exception: 1 -> 5
- 2023-01-29 09:30:09 ts-food-service return: 1 -> 5
- 2023-01-29 09:34:19 ts-food-service return: 3 -> 7
- 2023-01-29 09:42:26 ts-verification-code-service return: 1 -> 5
- 2023-01-29 09:49:34 ts-verification-code-service return: 1 -> 5
- 2023-01-29 09:58:04 ts-verification-code-service return: 2 -> 6
- 2023-01-29 10:04:34 ts-travel-service exception: 1 -> 5
- 2023-01-29 10:12:48 ts-travel-service exception: 1 -> 5
- 2023-01-29 10:26:20 ts-travel2-service exception: 1 -> 5
- 2023-01-29 10:45:10 ts-travel2-service exception: 1 -> 5
- 2023-01-29 10:50:16 ts-travel2-service exception: 1 -> 5
- 2023-01-29 10:56:45 ts-route-service exception: 1 -> 4
- 2023-01-29 11:04:05 ts-route-service exception: 1 -> 4
- 2023-01-29 11:13:56 ts-route-service exception: 1 -> 4
- 2023-01-29 11:19:59 ts-price-service exception: 1 -> 2
- 2023-01-29 11:29:03 ts-price-service exception: 1 -> 2
- 2023-01-29 11:36:06 ts-price-service exception: 1 -> 2
- 2023-01-29 13:31:54 ts-contacts-service cpu_contention: 1 -> 5
- 2023-01-29 14:23:31 ts-verification-code-service cpu_contention: 1 -> 5
- 2023-01-29 14:49:57 ts-food-service cpu_contention: 2 -> 6
- 2023-01-29 15:42:00 ts-preserve-service cpu_contention: 1 -> 5

**09_ts_service_AB_k3**: 25 of 45 cases changed
- 2023-01-29 08:43:04 ts-contacts-service return: 1 -> 5
- 2023-01-29 08:52:06 ts-contacts-service return: 1 -> 5
- 2023-01-29 08:58:16 ts-contacts-service return: 1 -> 2
- 2023-01-29 09:12:56 ts-basic-service return: 1 -> 5
- 2023-01-29 09:25:39 ts-basic-service exception: 1 -> 5
- 2023-01-29 09:30:09 ts-food-service return: 1 -> 5
- 2023-01-29 09:34:19 ts-food-service return: 3 -> 7
- 2023-01-29 09:42:26 ts-verification-code-service return: 1 -> 5
- 2023-01-29 09:49:34 ts-verification-code-service return: 1 -> 5
- 2023-01-29 09:58:04 ts-verification-code-service return: 2 -> 6
- 2023-01-29 10:04:34 ts-travel-service exception: 1 -> 5
- 2023-01-29 10:12:48 ts-travel-service exception: 1 -> 5
- 2023-01-29 10:26:20 ts-travel2-service exception: 1 -> 5
- 2023-01-29 10:45:10 ts-travel2-service exception: 1 -> 5
- 2023-01-29 10:50:16 ts-travel2-service exception: 1 -> 5
- 2023-01-29 10:56:45 ts-route-service exception: 1 -> 4
- 2023-01-29 11:04:05 ts-route-service exception: 1 -> 4
- 2023-01-29 11:13:56 ts-route-service exception: 1 -> 4
- 2023-01-29 11:19:59 ts-price-service exception: 1 -> 2
- 2023-01-29 11:29:03 ts-price-service exception: 1 -> 2
- 2023-01-29 11:36:06 ts-price-service exception: 1 -> 2
- 2023-01-29 13:31:54 ts-contacts-service cpu_contention: 1 -> 5
- 2023-01-29 14:23:31 ts-verification-code-service cpu_contention: 1 -> 5
- 2023-01-29 14:49:57 ts-food-service cpu_contention: 2 -> 6
- 2023-01-29 15:42:00 ts-preserve-service cpu_contention: 1 -> 5

**10_hipster_service_B_k1**: 10 of 56 cases changed
- 2022-08-22 04:02:07 frontend return: 2 -> 3
- 2022-08-22 05:09:50 checkoutservice return: 1 -> MISS
- 2022-08-22 07:44:20 adservice return: 1 -> MISS
- 2022-08-22 07:53:33 adservice exception: 1 -> 2
- 2022-08-23 12:10:21 frontend return: 2 -> 3
- 2022-08-23 12:27:23 frontend exception: 1 -> 2
- 2022-08-23 12:53:52 checkoutservice network_delay: 1 -> MISS
- 2022-08-23 16:05:02 adservice network_delay: MISS -> 1
- 2022-08-23 16:13:38 adservice return: 1 -> MISS
- 2022-08-23 16:22:53 adservice exception: 1 -> MISS

**11_hipster_service_B_k2**: 9 of 56 cases changed
- 2022-08-22 04:02:07 frontend return: 2 -> 3
- 2022-08-22 07:44:20 adservice return: 1 -> MISS
- 2022-08-22 07:53:33 adservice exception: 1 -> 2
- 2022-08-23 12:10:21 frontend return: 2 -> 3
- 2022-08-23 12:27:23 frontend exception: 1 -> 2
- 2022-08-23 12:53:52 checkoutservice network_delay: 1 -> MISS
- 2022-08-23 16:05:02 adservice network_delay: MISS -> 1
- 2022-08-23 16:13:38 adservice return: 1 -> MISS
- 2022-08-23 16:22:53 adservice exception: 1 -> MISS

**12_hipster_service_B_k4**: 7 of 56 cases changed
- 2022-08-22 03:53:54 frontend cpu_contention: 1 -> MISS
- 2022-08-22 04:02:07 frontend return: 2 -> 3
- 2022-08-22 05:18:09 currencyservice cpu_contention: 1 -> MISS
- 2022-08-23 12:10:21 frontend return: 2 -> 3
- 2022-08-23 12:53:52 checkoutservice network_delay: 1 -> MISS
- 2022-08-23 13:27:51 currencyservice cpu_contention: 1 -> MISS
- 2022-08-23 16:05:02 adservice network_delay: MISS -> 1

**13_hipster_service_B_k5**: 9 of 56 cases changed
- 2022-08-22 03:53:54 frontend cpu_contention: 1 -> MISS
- 2022-08-22 04:02:07 frontend return: 2 -> 3
- 2022-08-22 05:18:09 currencyservice cpu_contention: 1 -> MISS
- 2022-08-23 12:01:25 frontend cpu_contention: 1 -> MISS
- 2022-08-23 12:10:21 frontend return: 2 -> 3
- 2022-08-23 12:18:23 frontend cpu_consumed: 1 -> MISS
- 2022-08-23 13:27:51 currencyservice cpu_contention: 1 -> MISS
- 2022-08-23 14:55:55 productcatalogservice cpu_consumed: 1 -> MISS
- 2022-08-23 16:05:02 adservice network_delay: MISS -> 1

**14_ts_service_B_k1**: 37 of 45 cases changed
- 2023-01-29 08:43:04 ts-contacts-service return: 1 -> 5
- 2023-01-29 08:52:06 ts-contacts-service return: 1 -> 5
- 2023-01-29 08:58:16 ts-contacts-service return: 1 -> 2
- 2023-01-29 09:03:53 ts-basic-service return: 1 -> 6
- 2023-01-29 09:12:56 ts-basic-service return: 1 -> 4
- 2023-01-29 09:21:39 ts-basic-service return: 1 -> 6
- 2023-01-29 09:25:39 ts-basic-service exception: 1 -> 9
- 2023-01-29 09:30:09 ts-food-service return: 1 -> 7
- 2023-01-29 09:34:19 ts-food-service return: 3 -> 7
- 2023-01-29 09:42:26 ts-verification-code-service return: 1 -> 6
- 2023-01-29 09:49:34 ts-verification-code-service return: 1 -> 6
- 2023-01-29 09:58:04 ts-verification-code-service return: 2 -> 6
- 2023-01-29 10:04:34 ts-travel-service exception: 1 -> 3
- 2023-01-29 10:12:48 ts-travel-service exception: 1 -> 4
- 2023-01-29 10:20:10 ts-travel-service exception: 1 -> 4
- 2023-01-29 10:26:20 ts-travel2-service exception: 1 -> 9
- 2023-01-29 10:45:10 ts-travel2-service exception: 1 -> 9
- 2023-01-29 10:50:16 ts-travel2-service exception: 1 -> 7
- 2023-01-29 10:56:45 ts-route-service exception: 1 -> 4
- 2023-01-29 11:04:05 ts-route-service exception: 1 -> 4
- 2023-01-29 11:13:56 ts-route-service exception: 1 -> 4
- 2023-01-29 11:19:59 ts-price-service exception: 1 -> MISS
- 2023-01-29 11:29:03 ts-price-service exception: 1 -> MISS
- 2023-01-29 11:36:06 ts-price-service exception: 1 -> MISS
- 2023-01-29 13:31:54 ts-contacts-service cpu_contention: 1 -> 5
- 2023-01-29 14:23:31 ts-verification-code-service cpu_contention: 1 -> 6
- 2023-01-29 14:49:57 ts-food-service cpu_contention: 2 -> 7
- 2023-01-29 15:42:00 ts-preserve-service cpu_contention: 1 -> 7
- 2023-01-30 11:51:46 ts-contacts-service network_delay: 1 -> 2
- 2023-01-30 12:06:12 ts-basic-service network_delay: 1 -> 2
- 2023-01-30 12:15:56 ts-basic-service network_delay: 1 -> 3
- 2023-01-30 12:36:54 ts-verification-code-service network_delay: 1 -> 3
- 2023-01-30 13:06:49 ts-travel-service cpu_contention: 1 -> 2
- 2023-01-30 13:15:43 ts-travel-service network_delay: 3 -> 5
- 2023-01-30 13:22:22 ts-travel-service network_delay: 1 -> 2
- 2023-01-30 14:00:16 ts-security-service network_delay: 1 -> 3
- 2023-01-30 14:08:19 ts-security-service network_delay: 1 -> 2

**15_ts_service_B_k2**: 42 of 45 cases changed
- 2023-01-29 08:43:04 ts-contacts-service return: 1 -> 5
- 2023-01-29 08:52:06 ts-contacts-service return: 1 -> 5
- 2023-01-29 08:58:16 ts-contacts-service return: 1 -> 4
- 2023-01-29 09:03:53 ts-basic-service return: 1 -> 4
- 2023-01-29 09:12:56 ts-basic-service return: 1 -> 4
- 2023-01-29 09:21:39 ts-basic-service return: 1 -> 4
- 2023-01-29 09:25:39 ts-basic-service exception: 1 -> 7
- 2023-01-29 09:30:09 ts-food-service return: 1 -> 8
- 2023-01-29 09:34:19 ts-food-service return: 3 -> 8
- 2023-01-29 09:42:26 ts-verification-code-service return: 1 -> 5
- 2023-01-29 09:49:34 ts-verification-code-service return: 1 -> MISS
- 2023-01-29 09:58:04 ts-verification-code-service return: 2 -> MISS
- 2023-01-29 10:04:34 ts-travel-service exception: 1 -> 4
- 2023-01-29 10:12:48 ts-travel-service exception: 1 -> 5
- 2023-01-29 10:20:10 ts-travel-service exception: 1 -> 3
- 2023-01-29 10:26:20 ts-travel2-service exception: 1 -> 6
- 2023-01-29 10:45:10 ts-travel2-service exception: 1 -> 5
- 2023-01-29 10:50:16 ts-travel2-service exception: 1 -> 4
- 2023-01-29 10:56:45 ts-route-service exception: 1 -> 4
- 2023-01-29 11:04:05 ts-route-service exception: 1 -> 4
- 2023-01-29 11:13:56 ts-route-service exception: 1 -> 4
- 2023-01-29 11:19:59 ts-price-service exception: 1 -> MISS
- 2023-01-29 11:29:03 ts-price-service exception: 1 -> MISS
- 2023-01-29 11:36:06 ts-price-service exception: 1 -> MISS
- 2023-01-29 13:31:54 ts-contacts-service cpu_contention: 1 -> 5
- 2023-01-29 14:23:31 ts-verification-code-service cpu_contention: 1 -> 6
- 2023-01-29 14:49:57 ts-food-service cpu_contention: 2 -> 8
- 2023-01-29 15:42:00 ts-preserve-service cpu_contention: 1 -> 7
- 2023-01-30 11:51:46 ts-contacts-service network_delay: 1 -> 5
- 2023-01-30 11:59:21 ts-basic-service cpu_contention: 1 -> 3
- 2023-01-30 12:06:12 ts-basic-service network_delay: 1 -> 5
- 2023-01-30 12:15:56 ts-basic-service network_delay: 1 -> 5
- 2023-01-30 12:29:29 ts-verification-code-service network_delay: 1 -> 5
- 2023-01-30 12:36:54 ts-verification-code-service network_delay: 1 -> 4
- 2023-01-30 12:44:36 ts-food-service cpu_contention: 2 -> 5
- 2023-01-30 12:52:04 ts-food-service network_delay: 1 -> 4
- 2023-01-30 12:59:36 ts-food-service network_delay: 1 -> 4
- 2023-01-30 13:06:49 ts-travel-service cpu_contention: 1 -> 5
- 2023-01-30 13:15:43 ts-travel-service network_delay: 3 -> 6
- 2023-01-30 13:22:22 ts-travel-service network_delay: 1 -> 5
- 2023-01-30 14:00:16 ts-security-service network_delay: 1 -> 5
- 2023-01-30 14:08:19 ts-security-service network_delay: 1 -> 5

**16_ts_service_B_k4**: 3 of 45 cases changed
- 2023-01-29 08:58:16 ts-contacts-service return: 1 -> 2
- 2023-01-29 09:21:39 ts-basic-service return: 1 -> 2
- 2023-01-29 10:20:10 ts-travel-service exception: 1 -> 2

**17_ts_service_B_k5**: 3 of 45 cases changed
- 2023-01-29 08:58:16 ts-contacts-service return: 1 -> 2
- 2023-01-29 09:21:39 ts-basic-service return: 1 -> 2
- 2023-01-29 10:20:10 ts-travel-service exception: 1 -> 2

**18_hipster_service_A**: 0 of 56 cases changed

**19_hipster_service_B_k3**: 5 of 56 cases changed
- 2022-08-22 04:02:07 frontend return: 2 -> 3
- 2022-08-23 12:10:21 frontend return: 2 -> 3
- 2022-08-23 12:53:52 checkoutservice network_delay: 1 -> MISS
- 2022-08-23 13:27:51 currencyservice cpu_contention: 1 -> MISS
- 2022-08-23 16:05:02 adservice network_delay: MISS -> 1

**20_hipster_service_AB_k3**: 5 of 56 cases changed
- 2022-08-22 04:02:07 frontend return: 2 -> 3
- 2022-08-23 12:10:21 frontend return: 2 -> 3
- 2022-08-23 12:53:52 checkoutservice network_delay: 1 -> MISS
- 2022-08-23 13:27:51 currencyservice cpu_contention: 1 -> MISS
- 2022-08-23 16:05:02 adservice network_delay: MISS -> 1

## 4. McNemar exact test on top-1 correctness, variant against baseline (analysis 3)

Two-sided exact binomial on discordant pairs, original rank. 18 tests, no multiple-comparison correction. With 56 and 45 faults the test has low power: a non-significant result is not evidence of no effect.

| Variant run | Baseline right, variant wrong | Baseline wrong, variant right | p |
|---|---|---|---|
| 03_hipster_service_A_ratio | 4 | 1 | 0.3750 |
| 04_ts_service_A_ratio | 0 | 0 | 1.0000 (no discordant pairs) |
| 05_hipster_service_AB_k3_ratio | 2 | 1 | 1.0000 |
| 06_ts_service_AB_k3_ratio | 22 | 0 | 0.0000 |
| 07_ts_service_A | 0 | 0 | 1.0000 (no discordant pairs) |
| 08_ts_service_B_k3 | 22 | 0 | 0.0000 |
| 09_ts_service_AB_k3 | 22 | 0 | 0.0000 |
| 10_hipster_service_B_k1 | 7 | 1 | 0.0703 |
| 11_hipster_service_B_k2 | 6 | 1 | 0.1250 |
| 12_hipster_service_B_k4 | 4 | 1 | 0.3750 |
| 13_hipster_service_B_k5 | 6 | 1 | 0.1250 |
| 14_ts_service_B_k1 | 33 | 0 | 0.0000 |
| 15_ts_service_B_k2 | 37 | 0 | 0.0000 |
| 16_ts_service_B_k4 | 3 | 0 | 0.2500 |
| 17_ts_service_B_k5 | 3 | 0 | 0.2500 |
| 18_hipster_service_A | 0 | 0 | 1.0000 (no discordant pairs) |
| 19_hipster_service_B_k3 | 2 | 1 | 1.0000 |
| 20_hipster_service_AB_k3 | 2 | 1 | 1.0000 |

## 5. Error split at position 1 for resource faults (analysis 4)

Error set: resource faults with no match at list position 1. Localization = pod position > 1; attribution = pod position 1; pod absent = injected pod not in the candidate list.

| Run | Resource faults | Errors | Localization | Attribution | Pod absent |
|---|---|---|---|---|---|
| 01_hipster_service_baseline | 42 | 2 | 0 | 0 | 2 |
| 02_ts_service_baseline | 21 | 4 | 3 | 0 | 1 |
| 03_hipster_service_A_ratio | 42 | 5 | 0 | 4 | 1 |
| 04_ts_service_A_ratio | 21 | 4 | 3 | 0 | 1 |
| 05_hipster_service_AB_k3_ratio | 42 | 3 | 0 | 2 | 1 |
| 06_ts_service_AB_k3_ratio | 21 | 11 | 10 | 0 | 1 |
| 07_ts_service_A | 21 | 4 | 3 | 0 | 1 |
| 08_ts_service_B_k3 | 21 | 11 | 10 | 0 | 1 |
| 09_ts_service_AB_k3 | 21 | 11 | 10 | 0 | 1 |
| 10_hipster_service_B_k1 | 42 | 11 | 9 | 1 | 1 |
| 11_hipster_service_B_k2 | 42 | 7 | 5 | 1 | 1 |
| 12_hipster_service_B_k4 | 42 | 5 | 0 | 3 | 2 |
| 13_hipster_service_B_k5 | 42 | 7 | 0 | 2 | 5 |
| 14_ts_service_B_k1 | 21 | 18 | 17 | 0 | 1 |
| 15_ts_service_B_k2 | 21 | 19 | 18 | 0 | 1 |
| 16_ts_service_B_k4 | 21 | 8 | 7 | 0 | 1 |
| 17_ts_service_B_k5 | 21 | 7 | 6 | 0 | 1 |
| 18_hipster_service_A | 42 | 2 | 0 | 1 | 1 |
| 19_hipster_service_B_k3 | 42 | 3 | 0 | 2 | 1 |
| 20_hipster_service_AB_k3 | 42 | 3 | 0 | 2 | 1 |
| 21_ts_inner_baseline | 21 | 4 | 3 | 0 | 1 |
| 22_hipster_inner_baseline | 42 | 2 | 0 | 0 | 2 |

## 6. Component C success criteria (analysis 5)

Recorded prediction: A+C recovers adservice and loses currencyservice cpu_contention, so (b) fails on OnlineBoutique. OnlineBoutique is in-sample, TrainTicket is held-out.

**A+C**

- (a) adservice 2022-08-23 16:05:02 at rank 1: **HOLDS** (rank 1)
- (b) no baseline rank-1 fault lost, OnlineBoutique: **FAILS**
  - lost: 2022-08-22 05:18:09 currencyservice cpu_contention -> MISS
  - lost: 2022-08-23 13:27:51 currencyservice cpu_contention -> MISS
  - lost: 2022-08-23 16:31:35 adservice cpu_contention -> MISS
  - lost: 2022-08-23 16:40:57 adservice cpu_consumed -> MISS
- (b) no baseline rank-1 fault lost, TrainTicket: **HOLDS**
- (c) AS@1 not below baseline, OnlineBoutique: **FAILS** (52 -> 49)
- (c) AS@1 not below baseline, TrainTicket: **HOLDS** (39 -> 39)

**C successful (all three criteria hold): NO**

**A+B+C at k=3 (descriptive; the criteria are defined for A+C)**

- (a) adservice 2022-08-23 16:05:02 at rank 1: **HOLDS** (rank 1)
- (b) no baseline rank-1 fault lost, OnlineBoutique: **FAILS**
  - lost: 2022-08-22 05:18:09 currencyservice cpu_contention -> MISS
  - lost: 2022-08-23 13:27:51 currencyservice cpu_contention -> MISS
- (b) no baseline rank-1 fault lost, TrainTicket: **FAILS**
  - lost: 2023-01-29 08:43:04 ts-contacts-service return -> 5
  - lost: 2023-01-29 08:52:06 ts-contacts-service return -> 5
  - lost: 2023-01-29 08:58:16 ts-contacts-service return -> 2
  - lost: 2023-01-29 09:12:56 ts-basic-service return -> 5
  - lost: 2023-01-29 09:25:39 ts-basic-service exception -> 5
  - lost: 2023-01-29 09:30:09 ts-food-service return -> 5
  - lost: 2023-01-29 09:42:26 ts-verification-code-service return -> 5
  - lost: 2023-01-29 09:49:34 ts-verification-code-service return -> 5
  - lost: 2023-01-29 10:04:34 ts-travel-service exception -> 5
  - lost: 2023-01-29 10:12:48 ts-travel-service exception -> 5
  - lost: 2023-01-29 10:26:20 ts-travel2-service exception -> 5
  - lost: 2023-01-29 10:45:10 ts-travel2-service exception -> 5
  - lost: 2023-01-29 10:50:16 ts-travel2-service exception -> 5
  - lost: 2023-01-29 10:56:45 ts-route-service exception -> 4
  - lost: 2023-01-29 11:04:05 ts-route-service exception -> 4
  - lost: 2023-01-29 11:13:56 ts-route-service exception -> 4
  - lost: 2023-01-29 11:19:59 ts-price-service exception -> 2
  - lost: 2023-01-29 11:29:03 ts-price-service exception -> 2
  - lost: 2023-01-29 11:36:06 ts-price-service exception -> 2
  - lost: 2023-01-29 13:31:54 ts-contacts-service cpu_contention -> 5
  - lost: 2023-01-29 14:23:31 ts-verification-code-service cpu_contention -> 5
  - lost: 2023-01-29 15:42:00 ts-preserve-service cpu_contention -> 5
- (c) AS@1 not below baseline, OnlineBoutique: **FAILS** (52 -> 51)
- (c) AS@1 not below baseline, TrainTicket: **FAILS** (39 -> 17)

## 7. Threshold multiplier k, alarm counts and fault-free windows (Q2, Q5)

| System | Variant | Original @1 | @3 | @5 | Alarms in fault windows | Alarms in the 2 fault-free windows |
|---|---|---|---|---|---|---|
| OnlineBoutique | baseline | 52/56 (92.86%) | 54/56 (96.43%) | 54/56 (96.43%) | 95 | 2 |
| OnlineBoutique | B, k=1 | 46/56 (82.14%) | 50/56 (89.29%) | 50/56 (89.29%) | 69 | 0 |
| OnlineBoutique | B, k=2 | 47/56 (83.93%) | 51/56 (91.07%) | 51/56 (91.07%) | 58 | 0 |
| OnlineBoutique | B, k=3 | 51/56 (91.07%) | 53/56 (94.64%) | 53/56 (94.64%) | 41 | 0 |
| OnlineBoutique | B, k=4 | 49/56 (87.50%) | 51/56 (91.07%) | 51/56 (91.07%) | 40 | 0 |
| OnlineBoutique | B, k=5 | 47/56 (83.93%) | 49/56 (87.50%) | 49/56 (87.50%) | 37 | 0 |
| TrainTicket | baseline | 39/45 (86.67%) | 44/45 (97.78%) | 44/45 (97.78%) | 21 | 0 |
| TrainTicket | B, k=1 | 6/45 (13.33%) | 17/45 (37.78%) | 27/45 (60.00%) | 463 | 22 |
| TrainTicket | B, k=2 | 2/45 (4.44%) | 4/45 (8.89%) | 31/45 (68.89%) | 206 | 14 |
| TrainTicket | B, k=3 | 17/45 (37.78%) | 23/45 (51.11%) | 41/45 (91.11%) | 135 | 8 |
| TrainTicket | B, k=4 | 36/45 (80.00%) | 44/45 (97.78%) | 44/45 (97.78%) | 102 | 6 |
| TrainTicket | B, k=5 | 36/45 (80.00%) | 44/45 (97.78%) | 44/45 (97.78%) | 70 | 5 |

Alarm-list equivalence of the current `alarm.py` with the round-1 implementation (B at k = 1, 2, 4, 5):

- k=1: IDENTICAL; windows 105 and 105 (expected 105)
- k=2: IDENTICAL; windows 105 and 105 (expected 105)
- k=4: IDENTICAL; windows 105 and 105 (expected 105)
- k=5: IDENTICAL; windows 105 and 105 (expected 105)

False-alarm probes (alarms in each fault-free construction minute):

| Probe file | Mode | Minute: pods / alarms |
|---|---|---|
| fa_baseline_k3.json | baseline | 2022-08-22 03:51 (hipster): 1 / 1; 2022-08-23 17:00 (hipster): 1 / 1; 2023-01-29 08:50 (ts): 0 / 0; 2023-01-30 11:39 (ts): 0 / 0 |
| fa_A_k3.json | A | 2022-08-22 03:51 (hipster): 1 / 1; 2022-08-23 17:00 (hipster): 1 / 1; 2023-01-29 08:50 (ts): 0 / 0; 2023-01-30 11:39 (ts): 0 / 0 |
| fa_B_k1.json | B | 2022-08-22 03:51 (hipster): 0 / 0; 2022-08-23 17:00 (hipster): 0 / 0; 2023-01-29 08:50 (ts): 12 / 12; 2023-01-30 11:39 (ts): 10 / 10 |
| fa_B_k2.json | B | 2022-08-22 03:51 (hipster): 0 / 0; 2022-08-23 17:00 (hipster): 0 / 0; 2023-01-29 08:50 (ts): 7 / 7; 2023-01-30 11:39 (ts): 7 / 7 |
| fa_B_k3.json | B | 2022-08-22 03:51 (hipster): 0 / 0; 2022-08-23 17:00 (hipster): 0 / 0; 2023-01-29 08:50 (ts): 3 / 3; 2023-01-30 11:39 (ts): 5 / 5 |
| fa_B_k4.json | B | 2022-08-22 03:51 (hipster): 0 / 0; 2022-08-23 17:00 (hipster): 0 / 0; 2023-01-29 08:50 (ts): 2 / 2; 2023-01-30 11:39 (ts): 4 / 4 |
| fa_B_k5.json | B | 2022-08-22 03:51 (hipster): 0 / 0; 2022-08-23 17:00 (hipster): 0 / 0; 2023-01-29 08:50 (ts): 2 / 2; 2023-01-30 11:39 (ts): 3 / 3 |
| fa_AB_k3.json | AB | 2022-08-22 03:51 (hipster): 0 / 0; 2022-08-23 17:00 (hipster): 0 / 0; 2023-01-29 08:50 (ts): 3 / 3; 2023-01-30 11:39 (ts): 5 / 6 |

## 8. Per-fault-type recoveries and regressions at rank 1 (Amendment A2)

| Variant run | Fault type | Cases | Baseline right | Variant right | Recoveries | Regressions |
|---|---|---|---|---|---|---|
| 03_hipster_service_A_ratio | cpu_consumed | 10 | 10 | 9 | 0 | 1 |
| 03_hipster_service_A_ratio | cpu_contention | 16 | 16 | 13 | 0 | 3 |
| 03_hipster_service_A_ratio | exception | 7 | 7 | 7 | 0 | 0 |
| 03_hipster_service_A_ratio | network_delay | 16 | 14 | 15 | 1 | 0 |
| 03_hipster_service_A_ratio | return | 7 | 5 | 5 | 0 | 0 |
| 04_ts_service_A_ratio | cpu_contention | 7 | 5 | 5 | 0 | 0 |
| 04_ts_service_A_ratio | exception | 13 | 13 | 13 | 0 | 0 |
| 04_ts_service_A_ratio | network_delay | 14 | 12 | 12 | 0 | 0 |
| 04_ts_service_A_ratio | return | 11 | 9 | 9 | 0 | 0 |
| 05_hipster_service_AB_k3_ratio | cpu_consumed | 10 | 10 | 10 | 0 | 0 |
| 05_hipster_service_AB_k3_ratio | cpu_contention | 16 | 16 | 14 | 0 | 2 |
| 05_hipster_service_AB_k3_ratio | exception | 7 | 7 | 7 | 0 | 0 |
| 05_hipster_service_AB_k3_ratio | network_delay | 16 | 14 | 15 | 1 | 0 |
| 05_hipster_service_AB_k3_ratio | return | 7 | 5 | 5 | 0 | 0 |
| 06_ts_service_AB_k3_ratio | cpu_contention | 7 | 5 | 2 | 0 | 3 |
| 06_ts_service_AB_k3_ratio | exception | 13 | 13 | 1 | 0 | 12 |
| 06_ts_service_AB_k3_ratio | network_delay | 14 | 12 | 12 | 0 | 0 |
| 06_ts_service_AB_k3_ratio | return | 11 | 9 | 2 | 0 | 7 |
| 07_ts_service_A | cpu_contention | 7 | 5 | 5 | 0 | 0 |
| 07_ts_service_A | exception | 13 | 13 | 13 | 0 | 0 |
| 07_ts_service_A | network_delay | 14 | 12 | 12 | 0 | 0 |
| 07_ts_service_A | return | 11 | 9 | 9 | 0 | 0 |
| 08_ts_service_B_k3 | cpu_contention | 7 | 5 | 2 | 0 | 3 |
| 08_ts_service_B_k3 | exception | 13 | 13 | 1 | 0 | 12 |
| 08_ts_service_B_k3 | network_delay | 14 | 12 | 12 | 0 | 0 |
| 08_ts_service_B_k3 | return | 11 | 9 | 2 | 0 | 7 |
| 09_ts_service_AB_k3 | cpu_contention | 7 | 5 | 2 | 0 | 3 |
| 09_ts_service_AB_k3 | exception | 13 | 13 | 1 | 0 | 12 |
| 09_ts_service_AB_k3 | network_delay | 14 | 12 | 12 | 0 | 0 |
| 09_ts_service_AB_k3 | return | 11 | 9 | 2 | 0 | 7 |
| 10_hipster_service_B_k1 | cpu_consumed | 10 | 10 | 10 | 0 | 0 |
| 10_hipster_service_B_k1 | cpu_contention | 16 | 16 | 16 | 0 | 0 |
| 10_hipster_service_B_k1 | exception | 7 | 7 | 4 | 0 | 3 |
| 10_hipster_service_B_k1 | network_delay | 16 | 14 | 14 | 1 | 1 |
| 10_hipster_service_B_k1 | return | 7 | 5 | 2 | 0 | 3 |
| 11_hipster_service_B_k2 | cpu_consumed | 10 | 10 | 10 | 0 | 0 |
| 11_hipster_service_B_k2 | cpu_contention | 16 | 16 | 16 | 0 | 0 |
| 11_hipster_service_B_k2 | exception | 7 | 7 | 4 | 0 | 3 |
| 11_hipster_service_B_k2 | network_delay | 16 | 14 | 14 | 1 | 1 |
| 11_hipster_service_B_k2 | return | 7 | 5 | 3 | 0 | 2 |
| 12_hipster_service_B_k4 | cpu_consumed | 10 | 10 | 10 | 0 | 0 |
| 12_hipster_service_B_k4 | cpu_contention | 16 | 16 | 13 | 0 | 3 |
| 12_hipster_service_B_k4 | exception | 7 | 7 | 7 | 0 | 0 |
| 12_hipster_service_B_k4 | network_delay | 16 | 14 | 14 | 1 | 1 |
| 12_hipster_service_B_k4 | return | 7 | 5 | 5 | 0 | 0 |
| 13_hipster_service_B_k5 | cpu_consumed | 10 | 10 | 8 | 0 | 2 |
| 13_hipster_service_B_k5 | cpu_contention | 16 | 16 | 12 | 0 | 4 |
| 13_hipster_service_B_k5 | exception | 7 | 7 | 7 | 0 | 0 |
| 13_hipster_service_B_k5 | network_delay | 16 | 14 | 15 | 1 | 0 |
| 13_hipster_service_B_k5 | return | 7 | 5 | 5 | 0 | 0 |
| 14_ts_service_B_k1 | cpu_contention | 7 | 5 | 1 | 0 | 4 |
| 14_ts_service_B_k1 | exception | 13 | 13 | 0 | 0 | 13 |
| 14_ts_service_B_k1 | network_delay | 14 | 12 | 5 | 0 | 7 |
| 14_ts_service_B_k1 | return | 11 | 9 | 0 | 0 | 9 |
| 15_ts_service_B_k2 | cpu_contention | 7 | 5 | 0 | 0 | 5 |
| 15_ts_service_B_k2 | exception | 13 | 13 | 0 | 0 | 13 |
| 15_ts_service_B_k2 | network_delay | 14 | 12 | 2 | 0 | 10 |
| 15_ts_service_B_k2 | return | 11 | 9 | 0 | 0 | 9 |
| 16_ts_service_B_k4 | cpu_contention | 7 | 5 | 5 | 0 | 0 |
| 16_ts_service_B_k4 | exception | 13 | 13 | 12 | 0 | 1 |
| 16_ts_service_B_k4 | network_delay | 14 | 12 | 12 | 0 | 0 |
| 16_ts_service_B_k4 | return | 11 | 9 | 7 | 0 | 2 |
| 17_ts_service_B_k5 | cpu_contention | 7 | 5 | 5 | 0 | 0 |
| 17_ts_service_B_k5 | exception | 13 | 13 | 12 | 0 | 1 |
| 17_ts_service_B_k5 | network_delay | 14 | 12 | 12 | 0 | 0 |
| 17_ts_service_B_k5 | return | 11 | 9 | 7 | 0 | 2 |
| 18_hipster_service_A | cpu_consumed | 10 | 10 | 10 | 0 | 0 |
| 18_hipster_service_A | cpu_contention | 16 | 16 | 16 | 0 | 0 |
| 18_hipster_service_A | exception | 7 | 7 | 7 | 0 | 0 |
| 18_hipster_service_A | network_delay | 16 | 14 | 14 | 0 | 0 |
| 18_hipster_service_A | return | 7 | 5 | 5 | 0 | 0 |
| 19_hipster_service_B_k3 | cpu_consumed | 10 | 10 | 10 | 0 | 0 |
| 19_hipster_service_B_k3 | cpu_contention | 16 | 16 | 15 | 0 | 1 |
| 19_hipster_service_B_k3 | exception | 7 | 7 | 7 | 0 | 0 |
| 19_hipster_service_B_k3 | network_delay | 16 | 14 | 14 | 1 | 1 |
| 19_hipster_service_B_k3 | return | 7 | 5 | 5 | 0 | 0 |
| 20_hipster_service_AB_k3 | cpu_consumed | 10 | 10 | 10 | 0 | 0 |
| 20_hipster_service_AB_k3 | cpu_contention | 16 | 16 | 15 | 0 | 1 |
| 20_hipster_service_AB_k3 | exception | 7 | 7 | 7 | 0 | 0 |
| 20_hipster_service_AB_k3 | network_delay | 16 | 14 | 14 | 1 | 1 |
| 20_hipster_service_AB_k3 | return | 7 | 5 | 5 | 0 | 0 |

## 9. Attribution bound from the alarm lists (Amendment A3)

For each resource fault: does the injected pod's alarm list in the analysed minute contain the true resource type? No rule that picks among the pod's own alarms can match more faults than this.

| System | Alarm mode (k=3) | Resource faults | Pod has any alarm | True resource among its alarms (bound) | True resource is the first alarm |
|---|---|---|---|---|---|
| OnlineBoutique | baseline | 42 | 41 | 40 | 40 |
| OnlineBoutique | A | 42 | 41 | 41 | 40 |
| OnlineBoutique | B | 42 | 41 | 39 | 39 |
| OnlineBoutique | AB | 42 | 41 | 40 | 39 |
| TrainTicket | baseline | 21 | 21 | 21 | 21 |
| TrainTicket | A | 21 | 21 | 21 | 21 |
| TrainTicket | B | 21 | 21 | 21 | 21 |
| TrainTicket | AB | 21 | 21 | 21 | 21 |

