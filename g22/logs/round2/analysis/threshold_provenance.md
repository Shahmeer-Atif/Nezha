## Metric files: construction data versus evaluation data

| Date | Files | Byte-identical in construct_data and rca_data | First timestamp | Last timestamp | Rows |
|---|---|---|---|---|---|
| 2022-08-22 | 10 | 10 of 10 | 2022-08-22 03:51:19 | 2022-08-22 23:59:20 | 12090 |
| 2022-08-23 | 10 | 10 of 10 | 2022-08-23 11:59:28 | 2022-08-23 23:59:28 | 7210 |
| 2023-01-29 | 46 | 46 of 46 | 2023-01-29 08:41:09 | 2023-01-29 23:59:11 | 42274 |
| 2023-01-30 | 46 | 46 of 46 | 2023-01-30 11:39:52 | 2023-01-30 23:59:55 | 34086 |

## Shipped statistics versus recomputation (CPU and memory)

Row 1 of each shipped file is read as the mean and row 2 as the standard deviation, as written by generate_threshold.

| System | Service | Closest source | Largest absolute difference | Reproduced (< 1e-6) | mean/std |
|---|---|---|---|---|---|
| hipster | adservice | construct_data 2022-08-22 | 4.98 | no | Cpu shipped 8.15/8.77 recomputed 4.16/3.79; Memory shipped 81.12/6.50 recomputed 85.38/3.51 |
| hipster | cartservice | construct_data 2022-08-22 | 0.93 | no | Cpu shipped 6.32/4.42 recomputed 6.49/4.56; Memory shipped 25.96/2.91 recomputed 26.44/1.98 |
| hipster | checkoutservice | construct_data 2022-08-22 | 6.51 | no | Cpu shipped 6.74/6.15 recomputed 6.73/5.92; Memory shipped 35.39/3.03 recomputed 41.90/3.15 |
| hipster | currencyservice | construct_data 2022-08-22 | 2.08 | no | Cpu shipped 61.28/10.24 recomputed 62.68/10.05; Memory shipped 28.21/2.33 recomputed 28.16/4.40 |
| hipster | emailservice | construct_data 2022-08-22 | 0.444 | no | Cpu shipped 1.20/4.97 recomputed 0.78/5.41; Memory shipped 4.98/0.53 recomputed 4.77/0.55 |
| hipster | frontend | construct_data 2022-08-22 | 34.7 | no | Cpu shipped 45.66/9.71 recomputed 24.81/7.36; Memory shipped 51.40/5.11 recomputed 16.72/1.99 |
| hipster | paymentservice | construct_data 2022-08-22 | 0.785 | no | Cpu shipped 0.55/4.01 recomputed 0.59/4.25; Memory shipped 25.56/3.75 recomputed 25.32/2.97 |
| hipster | productcatalogservice | construct_data 2022-08-23 | 15 | no | Cpu shipped 42.48/8.76 recomputed 36.71/10.51; Memory shipped 26.42/2.74 recomputed 11.47/2.92 |
| hipster | recommendationservice | construct_data 2022-08-22 | 6.42 | no | Cpu shipped 13.76/7.57 recomputed 7.34/6.70; Memory shipped 6.03/0.53 recomputed 5.52/0.74 |
| hipster | shippingservice | construct_data 2022-08-22 | 16.7 | no | Cpu shipped 3.40/7.69 recomputed 3.04/5.89; Memory shipped 30.78/3.78 recomputed 14.07/8.91 |
| ts | ts-admin-basic-info-service | construct_data both dates | 0.254 | no | Cpu shipped 0.35/0.18 recomputed 0.34/0.21; Memory shipped 18.29/0.43 recomputed 18.04/0.35 |
| ts | ts-admin-order-service | construct_data 2023-01-29 | 0.22 | no | Cpu shipped 0.79/0.50 recomputed 0.69/0.49; Memory shipped 17.93/0.46 recomputed 18.11/0.24 |
| ts | ts-admin-route-service | construct_data 2023-01-29 | 0.179 | no | Cpu shipped 0.81/0.47 recomputed 0.66/0.37; Memory shipped 17.98/0.28 recomputed 18.16/0.25 |
| ts | ts-admin-travel-service | construct_data both dates | 0.131 | no | Cpu shipped 0.34/0.18 recomputed 0.30/0.21; Memory shipped 18.18/0.36 recomputed 18.31/0.30 |
| ts | ts-admin-user-service | construct_data both dates | 0.175 | no | Cpu shipped 0.38/0.22 recomputed 0.34/0.22; Memory shipped 18.02/0.44 recomputed 18.19/0.49 |
| ts | ts-assurance-service | construct_data 2023-01-29 | 0.764 | no | Cpu shipped 0.47/0.64 recomputed 0.42/0.36; Memory shipped 21.81/0.66 recomputed 21.04/0.23 |
| ts | ts-auth-service | construct_data 2023-01-29 | 1.37 | no | Cpu shipped 1.87/1.07 recomputed 1.72/1.00; Memory shipped 21.71/0.43 recomputed 23.08/0.45 |
| ts | ts-avatar-service | construct_data 2023-01-29 | 0 | yes | Cpu shipped 0.00/0.00 recomputed 0.00/0.00; Memory shipped 0.00/0.00 recomputed 0.00/0.00 |
| ts | ts-basic-service | construct_data 2023-01-29 | 4.58 | no | Cpu shipped 1.23/1.16 recomputed 1.36/5.74; Memory shipped 23.26/1.74 recomputed 23.34/1.69 |
| ts | ts-cancel-service | construct_data 2023-01-29 | 1.06 | no | Cpu shipped 1.57/1.02 recomputed 1.29/0.89; Memory shipped 22.64/1.34 recomputed 21.59/0.64 |
| ts | ts-config-service | construct_data 2023-01-29 | 0.27 | no | Cpu shipped 0.75/0.80 recomputed 0.57/0.56; Memory shipped 22.08/0.92 recomputed 22.35/0.75 |
| ts | ts-consign-price-service | construct_data both dates | 0.0702 | no | Cpu shipped 0.82/0.48 recomputed 0.75/0.51; Memory shipped 20.70/0.32 recomputed 20.64/0.25 |
| ts | ts-consign-service | construct_data 2023-01-29 | 0.292 | no | Cpu shipped 0.39/0.22 recomputed 0.34/0.23; Memory shipped 20.14/0.44 recomputed 20.43/0.21 |
| ts | ts-contacts-service | construct_data both dates | 0.61 | no | Cpu shipped 1.39/5.16 recomputed 1.20/4.55; Memory shipped 22.18/0.49 recomputed 22.60/0.31 |
| ts | ts-delivery-service | construct_data 2023-01-29 | 1.89 | no | Cpu shipped 1.20/8.39 recomputed 1.01/6.50; Memory shipped 21.29/0.32 recomputed 22.02/0.51 |
| ts | ts-execute-service | construct_data 2023-01-30 | 0.517 | no | Cpu shipped 0.63/0.47 recomputed 0.46/0.40; Memory shipped 21.53/0.66 recomputed 21.01/0.18 |
| ts | ts-food-delivery-service | construct_data 2023-01-30 | 0.786 | no | Cpu shipped 0.38/0.23 recomputed 0.35/0.30; Memory shipped 20.27/0.40 recomputed 21.05/0.08 |
| ts | ts-food-service | construct_data 2023-01-29 | 0.874 | no | Cpu shipped 1.21/4.54 recomputed 1.04/5.42; Memory shipped 26.27/1.39 recomputed 26.57/1.16 |
| ts | ts-gateway-service | construct_data 2023-01-30 | 2.01 | no | Cpu shipped 10.34/1.91 recomputed 8.98/1.95; Memory shipped 41.36/3.24 recomputed 39.35/3.07 |
| ts | ts-inside-payment-service | construct_data 2023-01-29 | 0.473 | no | Cpu shipped 1.81/1.30 recomputed 1.34/1.19; Memory shipped 26.72/1.76 recomputed 26.52/1.32 |
| ts | ts-news-service | construct_data 2023-01-29 | 0.0144 | no | Cpu shipped 0.01/0.01 recomputed 0.01/0.01; Memory shipped 0.10/0.04 recomputed 0.11/0.04 |
| ts | ts-notification-service | construct_data 2023-01-29 | 0.479 | no | Cpu shipped 0.35/0.19 recomputed 0.41/0.22; Memory shipped 20.19/0.30 recomputed 19.71/0.12 |
| ts | ts-order-other-service | construct_data 2023-01-29 | 2.28 | no | Cpu shipped 3.49/2.13 recomputed 1.20/0.93; Memory shipped 25.05/1.71 recomputed 23.72/1.51 |
| ts | ts-order-service | construct_data 2023-01-29 | 1.19 | no | Cpu shipped 3.18/1.66 recomputed 1.98/1.13; Memory shipped 25.27/1.82 recomputed 24.63/1.80 |
| ts | ts-payment-service | construct_data both dates | 0.393 | no | Cpu shipped 0.96/0.92 recomputed 0.77/0.52; Memory shipped 22.63/0.71 recomputed 22.41/0.40 |
| ts | ts-preserve-other-service | construct_data 2023-01-29 | 0.586 | no | Cpu shipped 1.04/0.59 recomputed 0.85/0.62; Memory shipped 24.46/1.65 recomputed 23.87/1.36 |
| ts | ts-preserve-service | construct_data 2023-01-29 | 0.584 | no | Cpu shipped 1.43/6.79 recomputed 1.41/7.37; Memory shipped 24.12/1.05 recomputed 24.35/1.44 |
| ts | ts-price-service | construct_data 2023-01-30 | 0.352 | no | Cpu shipped 0.63/0.72 recomputed 0.98/1.00; Memory shipped 22.97/0.52 recomputed 22.87/0.19 |
| ts | ts-rebook-service | construct_data 2023-01-29 | 0.265 | no | Cpu shipped 0.34/0.22 recomputed 0.33/0.22; Memory shipped 18.19/0.44 recomputed 17.95/0.18 |
| ts | ts-route-plan-service | construct_data 2023-01-29 | 0.104 | no | Cpu shipped 0.35/0.21 recomputed 0.29/0.28; Memory shipped 18.15/0.40 recomputed 18.04/0.34 |
| ts | ts-route-service | construct_data 2023-01-29 | 0.545 | no | Cpu shipped 2.24/7.40 recomputed 2.02/7.94; Memory shipped 22.80/0.86 recomputed 22.74/0.56 |
| ts | ts-seat-service | construct_data 2023-01-29 | 0.653 | no | Cpu shipped 2.52/1.96 recomputed 1.87/1.66; Memory shipped 24.04/1.74 recomputed 24.25/1.86 |
| ts | ts-security-service | construct_data 2023-01-29 | 0 | yes | Cpu shipped 0.00/0.00 recomputed 0.00/0.00; Memory shipped 0.00/0.00 recomputed 0.00/0.00 |
| ts | ts-station-food-service | construct_data both dates | 0.281 | no | Cpu shipped 0.93/0.55 recomputed 0.79/0.56; Memory shipped 21.73/0.55 recomputed 21.91/0.27 |
| ts | ts-station-service | construct_data both dates | 0.21 | no | Cpu shipped 0.71/0.63 recomputed 0.61/0.84; Memory shipped 21.83/0.38 recomputed 21.93/0.24 |
| ts | ts-ticket-office-service | construct_data 2023-01-29 | 0.0279 | no | Cpu shipped 0.06/0.60 recomputed 0.06/0.62; Memory shipped 2.55/0.64 recomputed 2.52/0.64 |
| ts | ts-train-food-service | construct_data 2023-01-29 | 0.274 | no | Cpu shipped 0.43/0.32 recomputed 0.49/0.36; Memory shipped 20.34/0.43 recomputed 20.61/0.30 |
| ts | ts-train-service | construct_data both dates | 0.757 | no | Cpu shipped 0.66/0.91 recomputed 0.81/1.06; Memory shipped 23.52/0.93 recomputed 22.77/0.36 |
| ts | ts-travel-plan-service | construct_data 2023-01-29 | 0.154 | no | Cpu shipped 0.34/0.19 recomputed 0.36/0.24; Memory shipped 17.59/0.29 recomputed 17.74/0.28 |
| ts | ts-travel-service | construct_data 2023-01-29 | 1.53 | no | Cpu shipped 2.57/1.74 recomputed 1.04/0.70; Memory shipped 26.07/1.50 recomputed 25.99/1.41 |
| ts | ts-travel2-service | construct_data 2023-01-30 | 0.509 | no | Cpu shipped 1.11/0.70 recomputed 1.12/0.72; Memory shipped 26.39/1.67 recomputed 25.88/1.17 |
| ts | ts-ui-dashboard | construct_data 2023-01-29 | 0.0637 | no | Cpu shipped 0.26/0.09 recomputed 0.20/0.06; Memory shipped 0.25/0.00 recomputed 0.23/0.00 |
| ts | ts-user-service | construct_data both dates | 0.612 | no | Cpu shipped 1.04/6.31 recomputed 0.88/5.70; Memory shipped 22.40/0.53 recomputed 22.35/0.40 |
| ts | ts-verification-code-service | construct_data 2023-01-29 | 0.449 | no | Cpu shipped 1.30/5.08 recomputed 0.85/5.47; Memory shipped 19.51/0.51 recomputed 19.33/0.33 |
| ts | ts-voucher-service | construct_data 2023-01-29 | 0.00898 | no | Cpu shipped 0.00/0.00 recomputed 0.00/0.00; Memory shipped 0.88/0.00 recomputed 0.87/0.00 |
| ts | ts-wait-order-service | construct_data 2023-01-29 | 0.513 | no | Cpu shipped 0.35/0.18 recomputed 0.73/0.41; Memory shipped 19.72/0.15 recomputed 20.23/0.38 |

Services per outcome: construct_data 2023-01-29: 2, no exact source: 54
Shipped threshold files with no metric data in either folder: 3 ['front_service_total', 'mysql', 'redis']
