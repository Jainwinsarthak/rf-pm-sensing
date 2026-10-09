# RF-Based Air Pollution Monitoring Using Channel Estimation

## Project Overview
This project explores the use of Radio Frequency (RF) signals to estimate air pollution concentrations, particularly PM2.5 and PM10, by analyzing changes in wireless channel characteristics.

## Objectives
- Estimate wireless channel coefficients from received signals.
- Compare ZFM/LS and MMSE channel-estimation methods.
- Study how different noise levels affect estimation accuracy.
- Investigate how PM2.5 and PM10 concentrations may affect RF channel characteristics.
- Explore the use of channel measurements to estimate pollution concentrations.

## Current Progress
- Generated complex wireless channel coefficients using NumPy.
- Simulated transmitted and received signals using `y = h * x + noise`.
- Implemented ZFM/LS and MMSE channel estimation.
- Calculated Mean Squared Error (MSE) to compare estimation accuracy.
- Tested estimation performance under different noise levels.

## Technologies Used
- Python
- NumPy
- Google Colab
- Git and GitHub

## Current Methodology
1. Generate a simulated wireless channel.
2. Transmit a known complex pilot symbol.
3. Add Gaussian noise to simulate receiver disturbances.
4. Estimate the channel using ZFM/LS and MMSE.
5. Calculate MSE and compare the two methods.

## Future Work
- Develop a physically justified model of how particulate matter affects RF signals.
- Study channel amplitude and phase changes for different PM2.5 and PM10 concentrations.
- Investigate channel behavior at 28 GHz and 140 GHz.
- Develop and evaluate methods for estimating pollution concentrations from channel measurements.

## Status
**In Progress** — currently focused on channel estimation and noise analysis.

## Disclaimer
The current implementation uses simulated wireless channel data. It does not yet measure or predict actual PM2.5 or PM10 concentrations.
