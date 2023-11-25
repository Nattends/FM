
import glob
import os

import pandas as pd
import uuid
import webbrowser

import calcs



pos = []
df = calcs.getDFRecrutement(pd.read_html("C:/Users/natha/OneDrive/Documents/Sports Interactive/Football Manager 2024/Untitled.html", header=0, encoding="utf-8", keep_default_na=False)[0], pos)
squad = df[
    ['Name', 'Age', 'Club', 'Transfer Value', 'Wage', 'Position']+pos]

def generate_html(dataframe: pd.DataFrame):
    # get the table HTML from the dataframe
    table_html = dataframe.to_html(table_id="table", index=False, justify='center')
    # construct the complete HTML with jQuery Data tables
    # You can disable paging or enable y scrolling on lines 20 and 21 respectively
    html = f"""
    <html> 
    <header>
        <link href="../css/style.css" rel="stylesheet">
    </header>
    <body>
    {table_html}
    
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.13.7/js/jquery.dataTables.min.js"></script>
    
    <script>
        $(document).ready( function () {{
            $('#table').DataTable({{
                paging: false,  
                order: [[1, 'asc']],
            }}); 
        }});
    </script>
    <script>
        $('table tbody').on('mousedown', 'tr', function(e) {{
                $(this).addClass('highlight').siblings().removeClass('highlight');
        }})
    </script>
    <script>
        $("input[@type=button]").click(function(){{
         $("table th:eq(0)").click();
        }});
    </script>
    </body>
    </html>
    """
    # return the html
    return html


# generates random file name for write-out of html file

filename = str(uuid.uuid4()) + ".html"

# creates a sortable html export from the dataframe 'squad'

html = generate_html(squad)
open(f"html/{filename}", "w", encoding="utf-8").write(html)

webbrowser.open("C:/Users/natha/OneDrive/Documents/Code/FM/html/" + filename, new=2)