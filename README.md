# daZ
Simple data analysis tool with some visualization option using streamlit.
You can upload your onw datasets in this app. However, there is some limitations, you can only upload file which are only 200mb or below 200 mb.  
### File type
This app support .xlsx and .CSV file. 

### Options 
This app has  two analzying option which are following:
- Overall columns
 - Analyze
 - chart type
#### Overall columns
You can check the datasets by droping the whichever columns you want. Also you can sort the column by clicking the columns name in the table 

```mermaid
graph LR
A[Analyze] --> B[Info about datasets] --> C[Describe datasets]--> D[Find missing value]--> E[Correlation Matrix]
```
```mermaid
graph LR
A[Chart type] --> B[Scatterplots] --> C[Lineplots]--> D[Histogram]--> E[Boxplot]-->F[Barchart]-->G[Funnel]
```
