# healthcare-no-show-analyzer - Clinic Operations Dasbhboard
![Dashboard](Healthcare_NoShow_Dashboard.pbix)
![Dashboard Preview](Healthcare_Noshow_Analyzer/dashboard.png)

## Business Problem
Which appointment patterns are associated with missed visits and what can a clinic do to reduce avoidable no-shows?

## Dataset Overview
- **Total Appointments:** 30,000
- **Total No-shows:** 4,800 (16% No-show Rate)
- **Fields:** appointment_date, specialty, weekday, lead_time_bucket, appointment_time_slot, clinic_id, no_show_flag

## Key Findings
- **Highest Risk Specialty:** Orthopedics - 16.82% no-show rate
-  **Highest Risk Day:** Wednesday - 0.17 rate
-  **Monthly Trend:** Stable 15-16% May peak 0.17
-  **High-Risk Segment:** CL-7752 | Cardiology | Evening | Loss ₹3, 08, 511
-  **Top 5 Segments:** ₹30L+ at-risk revenue

## Dashboard Includes
1. Total Appointments & No-show KPIs
2. No-show Trend by Month & Weekday
3. No-show Trend by Specialty (Donut)
4. No-show Trend by Lead-Time Bucket (Documented: Unknown = Data Limitation)
5. High-Risk Operational Segments Table
6. Slicers: Clinic ID, Specialty, Time-Slot

## Tech Stack
- **Python:** Data cleaning, derived fields (month, weekday, lead bucket)
- **SQL:** N0-show rate by specialty, weekday, lead-time, remainder proxy
- **Power BI:** DAX Measures, Tile slicers

## Recommendation
Targeted reminder workflow for Wednesday Evening appointments in Orthopedics/Cardiology: Associations found, not causation


