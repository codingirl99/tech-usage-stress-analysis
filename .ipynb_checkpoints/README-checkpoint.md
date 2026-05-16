# Tech-Usage-and-Impact-on-Stress-Analysis

**One-Sentence Summary**  
This project explores how technology usage, wellness habits, and work patterns relate to stress, sleep, and mood using Python on a Kaggle dataset.  

---

## Overview
This project investigates patterns and relationships between technology usage (screen time, social media, and gaming), wellness app usage, work hours, and mental health indicators such as stress, sleep, mood, and anxiety. Using the dataset [Tech Use & Stress Wellness](https://www.kaggle.com/datasets/nagpalprabhavalkar/tech-use-and-stress-wellness) by Nagpal Prabhavalkar, the analysis performs **exploratory data analysis (EDA)** and visualizations to uncover trends, correlations, and insights about how technology impacts well-being.  

**Note:** All insights in this project are based on the original dataset.  

---

## Technologies Used
- Python  
- Libraries: pandas, seaborn, matplotlib  
- Analysis performed in **Jupyter Notebook**  

---

## Visualizations

Below are the combined visualizations generated from the dataset:

![visualizations](datavisualizations.png)

---

## Visualizations and Key Insights
1. **Work Related Hours vs Stress Levels (Scatter Plot)**  
   - Lower work hours correlate with lower stress levels (<2/10).  
   - Higher work hours show increasing stress levels.  

2. **Daily Screen Time Hours vs Sleep Duration (Scatter Plot)**  
   - Most participants spend 3–8 hours on screens daily.  
   - Higher screen time is associated with slightly reduced sleep (6.3–8.3 hours).  
   - Very low screen time (<2.3 hours) corresponds to more sleep.  

3. **Social Media Hours vs Mood Rating (Histogram)**  
   - Mood rating tends to increase with higher social media usage.  
   - Distribution is left-skewed, suggesting more people report higher mood ratings with more social media hours.  

4. **Gender vs Wellness App Usage (Count Plot)**  
   - More men than women use wellness apps, though both genders have a significant proportion not using them.  
   - "Other" gender category has significantly lower representation.  

5. **Gaming Hours vs Weekly Anxiety Score (Joint Plot)**  
   - Weekly anxiety score slightly decreases as gaming hours increase, with some outliers.  
   - Gaming hours show a slight right skew; anxiety scores show a slight left skew.  

---

## Conclusions
- Work hours and screen time are positively correlated with stress and negatively correlated with sleep.  
- Social media usage may be associated with higher self-reported mood ratings.  
- Gaming may have a small reducing effect on weekly anxiety scores.  
- Wellness app usage differs across genders, but non-usage is common for all.  

---

## Future Directions
- Apply statistical tests (correlation, regression) to quantify relationships  
- Explore interactive visualizations with dashboards (Plotly/Dash, Streamlit)  
- Segment analysis by demographics (age, occupation)  
- Investigate longitudinal or temporal effects if time-based data is available  

---

## How to Reproduce Results
1. Clone the repository  
2. Download the dataset from Kaggle: [Tech Use & Stress Wellness](https://www.kaggle.com/datasets/nagpalprabhavalkar/tech-use-and-stress-wellness)  
3. Place the dataset in the `/data` folder  
4. Install dependencies:  
   ```bash
   pip install pandas seaborn matplotlib jupyter