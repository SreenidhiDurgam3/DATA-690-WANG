<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture1.png">
</p>

[**https://datatopics.worldbank.org/world-development-indicators/**](https://datatopics.worldbank.org/world-development-indicators/) **-** I had a skim through the webpage and really liked the UI and the way they are presenting open source data along with data indicators understanding and data types , time , location information. The best part of this webpage is[http://www.worlddev.xyz/](http://www.worlddev.xyz/) - where we can actually visualize the data on cloud and without any third party tool like python, R and tableau we can do actual visualizations and analyze this data – I loved the way this website is built and I really appreciate this and thanks to Chaoji Wang for sharing this webpage with us – I am very sure most of us would use this open source data in many future projects and for our career development establishment.

<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture2.png">
</p>

<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture3.png">
</p>
<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture4.png">
</p>

<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture5.png">
</p>

**After a deep analysis of these indicators :**

- Questions I encountered in my mind :
  - Is the Literacy rate dependent on GDP total ?
  - Is the children employment going to affect the literacy rate ?
  - Is school enrollment GPI proportional to a country&#39;s GDP ?
  - How does alcohol consumption per capita have an affect on GDP and is it relevant to Literacy rate ?
- Major Data Sources to answer my questions :
  - Social Development Indicator had most of the data necessary such as,
    - Children Employment
    - Literacy rate
  - Health Data indicators had :
    - Alcohol consumption per capita
    - Population, Total
  - Economy and Growth had:
    - GDP ,PPP %
- Steps I used to analyze these situations:
  - A bubble chart – This helped me better understand the situations and find the data pattern/trend
  - A Bar chart – Helps me provide relationships and understand dependencies between the indicators I chose
  - A scatter plot – Helps me find any outliers (if any)

**Literacy Rate, Total Alcohol consumption per capita vs GDP per capita visualization**

<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture6-Literacy Rate, Total Alcohol consumption per capita vs GDP per capita visualization.png">
</p>

- **Bubble size :** Literacy rate, youth(15-24)
- **X-axis :** GDP per capita, PPP (current international $)
- **Y-axis:** Total alcohol consumption per capita

This is one of the visualizations that seemed very interesting to me – I was expecting that literacy rate should be indirectly proportional to the Total Alcohol consumption per capita i.e. If Literacy rate is high Total Alcohol consumption per capita must be low resulting lower GDP, but in some cases such as Spain has high Total alcohol consumption and high literacy rate too. But in country in Sub-Saharan Africa in top left corner in the graph Tanzania has Total alcohol consumption per capita very high 11.03 and low Literacy rate GPI 0.91, similarly for central African republic has very low Literacy rate 0.60 and high alcohol consumption rate. So not for all countries but for most of the cases – **The total GDP is directly proportional to alcohol consumption rate which Is indirectly proportional to the literacy rate.**

<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture7.png">
</p>
<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture8.png">
</p>

I chose the data viz to be between 2015 to 2020 and for the following country&#39;s:

- Central African Republic
- Spain
- Singapore
- UAE
- India
- Chile
- Tanzania
- Chad
- Indonesia
- Pakisthan
- Azerbaijan
- Turkey
- Oman

The Bar charts in the next page explain more detail about these relationships. _ **Total alcohol consumption per capita is mostly high where litercay rate is low** _ and vice versa.

And the scatter plot represents how alcohol consumption rate per capita is effecting the GDP total. _ **Wherever alcohol consumption per capita is high GDP is also high** _ and vice versa – there are no outliers in the data filters I have applied. !
<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture9.png">
</p>

<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture10.png">
</p>

<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture11.png">
</p>

**Literacy Rate vs Children working (15-24yrs)**


<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture12.png">
</p>

For this scenario , a scatterplot answers my questions – Yes literacy rate is dependent upon Children employment – which means most of the students that are working might not be educated, illiterates and have never been to school. Whenever the children in employment is high the literacy rate is low and whenever the literacy rate is high , the children employment rate is low – which is also indirectly affective on GDP of a country from previous visualization.

So, from the analysis :

- Children employment rate∝ (1/ Literacy rate)
- Literacy rate∝ GDP
- Children employment rate ∝ 1/GDP
- So, Whenever there are more child employees in a country , its GDP decreases.

**Literacy rate GPI vs GDP**


<p align="center">
  <img width="500" height ="300" src="https://github.com/SreenidhiDurgam3/DATA-690-WANG/blob/main/world_development_explorer/charts/Picture13.png">
</p>

From this analysis, The GDP doesn&#39;t seem to be relevant with Literacy rate(15-24 yrs) GPI . So country&#39;s GDP is not dependent on GPI.
