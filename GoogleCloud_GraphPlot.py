from google.cloud import bigquery
from google.oauth2 import service_account

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import black,blue
from reportlab.graphics.shapes import Drawing    
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics import renderPDF



credentials = service_account.Credentials.from_service_account_file("taskproj-398609-2926bb2e71c9.json")
project_id = 'taskproj-398609'

client = bigquery.Client(credentials=credentials, project=project_id,)

if __name__ == "__main__":
    query_job_Q5_i = client.query("""
        SELECT
  COUNT(*)+(
  SELECT
    COUNT(*)+(
    SELECT
      COUNT(*)+(
      SELECT
        COUNT(*) AS renal_count4
      FROM
        `bigquery-public-data.medicare.inpatient_charges_2014`
      WHERE
        drg_definition LIKE '%RENAL FAILURE%') AS renal_count3
    FROM
      `bigquery-public-data.medicare.inpatient_charges_2013`
    WHERE
      drg_definition LIKE '%RENAL FAILURE%' ) AS renal_count2
  FROM
    `bigquery-public-data.medicare.inpatient_charges_2012`
  WHERE
    drg_definition LIKE '%RENAL FAILURE%' ) AS total_renal_count
FROM
  `bigquery-public-data.medicare.inpatient_charges_2011`
WHERE
  drg_definition LIKE '%RENAL FAILURE%'

    """)
    total_inpatients = query_job_Q5_i.result()


    query_job_Q5_ii = client.query("""
        SELECT
  COUNT(*)+(
  SELECT
    COUNT(*)+(
    SELECT
      COUNT(*)+(
      SELECT
        COUNT(*) AS renal_count4
      FROM
        `bigquery-public-data.medicare.outpatient_charges_2014`
      WHERE
        apc LIKE '%RENAL FAILURE%') AS renal_count3
    FROM
      `bigquery-public-data.medicare.outpatient_charges_2013`
    WHERE
      apc LIKE '%RENAL FAILURE%' ) AS renal_count2
  FROM
    `bigquery-public-data.medicare.outpatient_charges_2012`
  WHERE
    apc LIKE '%RENAL FAILURE%' ) AS total_renal_count
FROM
  `bigquery-public-data.medicare.outpatient_charges_2011`
WHERE
  apc LIKE '%RENAL FAILURE%'

    """)
    total_outpatients = query_job_Q5_ii.result()



    query_job_Q5_iii = client.query("""
        SELECT
  sum(average_total_payments)+(
  SELECT
    sum(average_total_payments) +(
    SELECT
      sum(average_total_payments)+(
      SELECT
        sum(average_total_payments) AS payment4
      FROM
        `bigquery-public-data.medicare.inpatient_charges_2014`
      WHERE
        drg_definition LIKE '%RENAL FAILURE%') AS payment3
    FROM
      `bigquery-public-data.medicare.inpatient_charges_2013`
    WHERE
      drg_definition LIKE '%RENAL FAILURE%' ) AS payment2
  FROM
    `bigquery-public-data.medicare.inpatient_charges_2012`
  WHERE
    drg_definition LIKE '%RENAL FAILURE%' ) AS total_avg_payment
FROM
  `bigquery-public-data.medicare.inpatient_charges_2011`
WHERE
  drg_definition LIKE '%RENAL FAILURE%'

    """)
    total_inpatients_avg_amount = query_job_Q5_iii.result()




    query_job_Q5_iv = client.query("""
        SELECT
  sum(average_total_payments)+(
  SELECT
    sum(average_total_payments) +(
    SELECT
      sum(average_total_payments)+(
      SELECT
        sum(average_total_payments) AS payment4
      FROM
        `bigquery-public-data.medicare.outpatient_charges_2014`
      WHERE
        apc LIKE '%RENAL FAILURE%') AS payment3
    FROM
      `bigquery-public-data.medicare.outpatient_charges_2013`
    WHERE
      apc LIKE '%RENAL FAILURE%' ) AS payment2
  FROM
    `bigquery-public-data.medicare.outpatient_charges_2012`
  WHERE
    apc LIKE '%RENAL FAILURE%' ) AS total_avg_payment
FROM
  `bigquery-public-data.medicare.outpatient_charges_2011`
WHERE
  apc LIKE '%RENAL FAILURE%'

    """)
    total_outpatients_avg_amount = query_job_Q5_iv.result()



# for plot

  
    query_job_Q5_2014 = client.query("""
        SELECT
        sum(average_total_payments) AS payment_released4
      FROM
        `bigquery-public-data.medicare.inpatient_charges_2014`
      WHERE
        drg_definition LIKE '%RENAL FAILURE%'

    """)
    payment_released_2014 = query_job_Q5_2014.result()


  
    query_job_Q5_2013 = client.query("""
       SELECT
      sum(average_total_payments)
    FROM
      `bigquery-public-data.medicare.inpatient_charges_2013`
    WHERE
      drg_definition LIKE '%RENAL FAILURE%'

    """)
    payment_released_2013= query_job_Q5_2013.result()



    
    query_job_Q5_2012 = client.query("""
         SELECT
        sum(average_total_payments) AS payment_released12
      FROM
        `bigquery-public-data.medicare.inpatient_charges_2012`
      WHERE
        drg_definition LIKE '%RENAL FAILURE%'

    """)
    payment_released_2012 = query_job_Q5_2012.result()


    
    query_job_Q5_2011 = client.query("""
         SELECT
        sum(average_total_payments) AS payment_released12
      FROM
        `bigquery-public-data.medicare.inpatient_charges_2011`
      WHERE
        drg_definition LIKE '%RENAL FAILURE%'

    """)
    payment_released_2011 = query_job_Q5_2011.result()





    """ for row in result_Q5:
         #Row values can be accessed by field name or index.
        print(row[0],row[1]) """

   

    """ for row in result_Q5:
        if (entries == 35):
            c.showPage()
            c.drawString(10, 750, "Column A")
            c.drawString(275, 750, "Column B")
            height = 730
            entries = 0

        c.drawString(10, height, row.game_id)
        c.drawString(275, height, str(row.season))
        height = height - 20
        entries = entries + 1

    c.save() """

for row in total_inpatients:
  total_inpatients=row[0]
  break
for row in total_outpatients:
  total_outpatients=row[0]
  break
for row in total_inpatients_avg_amount:
  total_inpatients_avg_amount=row[0]
  break
for row in total_outpatients_avg_amount:
  total_outpatients_avg_amount=row[0]
  break

# for plots

for row in payment_released_2011:
  payment_released_2011=row[0]
  break
for row in payment_released_2012:
  payment_released_2012=row[0]
  break
for row in payment_released_2013:
  payment_released_2013=row[0]
  break
for row in payment_released_2014:
  payment_released_2014=row[0]
  break


""" print(total_inpatients)
print(total_outpatients)
print(total_inpatients_avg_amount)
print(total_outpatients_avg_amount) """

#pdf code


c = canvas.Canvas("DBLAB7_Graphs_2021_CE_58.pdf")


# Add a bar chart with improved formatting
drawing = Drawing(500, 300)  # Increase the size of the drawing for better chart display

# Define the data and labels
data = [payment_released_2011, payment_released_2012, payment_released_2013, payment_released_2014]
labels = ['2011', '2012', '2013', '2014']

bc = VerticalBarChart()
bc.x = 50
bc.y = 50
bc.width = 400
bc.height = 200
bc.data = [data]
bc.strokeColor = blue
bc.bars[0].fillColor = black  # Bar color
bc.valueAxis.valueMin = 0
# bc.valueAxis.valueMax = max(data) + 20000  # Adjust based on your data
# bc.valueAxis.valueStep = 20000  # Adjust as needed
bc.categoryAxis.categoryNames = labels
bc.categoryAxis.labels.boxAnchor = 'ne'
bc.categoryAxis.labels.dx = 8
bc.categoryAxis.labels.dy = -10  # Increase label spacing for better readability
bc.categoryAxis.labels.angle = 30

drawing.add(bc)

# Save the PDF report
renderPDF.draw(drawing, c, 99, 99, showBoundary=True)
c.save()