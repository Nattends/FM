
import glob
import os

import pandas as pd
import numpy as np

df_list = pd.read_html("C:/Users/natha/OneDrive/Documents/Sports Interactive/Football Manager 2024/Untitled.html", header=0, encoding="utf-8", keep_default_na=False)

# turn the list into a dataframe
df = df_list[0]
for k in ["Min AP", "Expires", 'Av Rat', "Apps", "Ability", "Days Old", "Height", "UID", "Inf"]:
    try:
        df = df.drop(columns=k)
    except:
        pass
ogDf = df
listAttributes = [i for i in df.columns if len(i) == 3 and i not in "Inf Nat Age UID Wage"]

newDf = df
i = 0
deleteInd = []
for k in listAttributes:
    for index, val in enumerate(df[k]):
        if val == "-":
            deleteInd.append(index)
        elif len(str(val)) > 2:
            try : 
                val = [int(i) for i in val.split('-')]
                val = round(sum(val) / 2)
                df.at[index, k] = int(val)
            except : 
                pass 
        elif val != '':
            df.at[index, k] = int(val)




df = df.drop(index=deleteInd)

# Calculate simple speed and workrate scores
df['Spd'] = (df['Pac'] + df['Acc']) / 2
df['Work'] = (df['Wor'] + df['Sta']) / 2
df['SetP'] = (df['Jum'] + df['Bra']) / 2

# calculates Sweeper_keeper_Support score
df['gk_key'] = ( df['Agi'] + df['Ref'] )
df['gk_green'] = ( df['Cmd'] + df['Kic'] + df['1v1'] + df['Ant'] + df['Cnt'] + df['Pos'] )
df['gk_blue'] = ( df['Aer'] + df['Fir'] + df['Han'] + df['Pas'] + df['TRO'] + df['Dec'] + df['Vis'] + df['Acc'] )
df['gk'] =( ( ( df['gk_key'] * 5) + (df['gk_green'] * 3) + (df['gk_blue'] * 1) ) / 36)


# calculates Wing_back_Support score
df['wb_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
df['wb_green'] = ( df['Cro'] + df['Dri'] + df['Mar'] + df['Tck'] + df['OtB'] + df['Tea'] )
df['wb_blue'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Ant'] + df['Cnt'] + df['Dec'] + df['Pos'] + df['Agi'] + df['Bal'] )
df['wb'] =( ( ( df['wb_key'] * 5) + (df['wb_green'] * 3) + (df['wb_blue'] * 1) ) / 47)



# calculates Ball_playing_defender_Defend score
df['bpdd_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
df['bpdd_green'] = ( df['Hea'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Pos'] + df['Str'] )
df['bpdd_blue'] = ( df['Fir'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] + df['Dec'] + df['Vis'] )
df['bpdd'] =( ( ( df['bpdd_key'] * 5) + (df['bpdd_green'] * 3) + (df['bpdd_blue'] * 1) ) / 46)


# calculates Ball_winning_midfielder_Support score
df['bwms_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
df['bwms_green'] = ( df['Tck'] + df['Agg'] + df['Ant'] + df['Tea'] )
df['bwms_blue'] = ( df['Mar'] + df['Pas'] + df['Bra'] + df['Cnt'] + df['Agi'] + df['Str'] )
df['bwms'] =( ( ( df['bwms_key'] * 5) + (df['bwms_green'] * 3) + (df['bwms_blue'] * 1) ) / 38)
df.bwms= df.bwms.round(1)


# calculates Box_to_box_midfielder_Support score
df['b2bs_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
df['b2bs_green'] = ( df['Pas'] + df['Tck'] + df['OtB'] + df['Tea'] )
df['b2bs_blue'] = ( df['Dri'] + df['Fin'] + df['Fir'] + df['Lon'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Cmp'] + df['Dec'] + df['Pos'] + df['Bal'] + df['Str'] )
df['b2bs'] =( ( ( df['b2bs_key'] * 5) + (df['b2bs_green'] * 3) + (df['b2bs_blue'] * 1) ) / 44)
df.b2bs= df.b2bs.round(1)


# calculates Trequartista_Attack score
df['trea_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
df['trea_green'] = ( df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Fla'] + df['OtB'] + df['Vis'] )
df['trea_blue'] = ( df['Ant'] + df['Agi'] + df['Bal'] )
df['trea'] =( ( ( df['trea_key'] * 5) + (df['trea_green'] * 3) + (df['trea_blue'] * 1) ) / 45)
df.trea= df.trea.round(1)


# calculates Inside_forward_Attack score
# calculates Inside_forward_Support score
df['ifs_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
df['ifs_green'] = ( df['Dri'] + df['Fin'] + df['Fir'] + df['Tec'] + df['OtB'] + df['Agi'] )
df['ifs_blue'] = ( df['Lon'] + df['Pas'] + df['Ant'] + df['Cmp'] + df['Fla'] + df['Vis'] + df['Bal'] )
df['ifs'] =( ( ( df['ifs_key'] * 5) + (df['ifs_green'] * 3) + (df['ifs_blue'] * 1) ) / 45)
df.ifs= df.ifs.round(1)


# calculates Advanced_forward_Attack score
df['str_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
df['str_green'] = ( df['Dri'] + df['Fir'] + df['Tec'] + df['Cmp'] + df['OtB'] )
df['str_blue'] = ( df['Pas'] + df['Ant'] + df['Dec'] + df['Wor'] + df['Agi'] + df['Bal'] + df['Sta'] )
df['str'] =( ( ( df['str_key'] * 5) + (df['str_green'] * 3) + (df['str_blue'] * 1) ) / 37)


# builds squad dataframe using only columns that will be exported to HTML
# builds squad dataframe using only columns that will be exported to HTML

positionList : list = "gk wb bpdd bwms b2bs trea ifs str".split(' ')
squad = df[
    ['Name', 'Age', 'Club', 'Transfer Value', 'Wage', 'Position']+positionList]


for k in positionList : 
    squad[k] = squad[k].apply(lambda x: round(x,1))



# taken from here: https://www.thepythoncode.com/article/convert-pandas-dataframe-to-html-table-python
# creates a function to make a sortable html export
def generate_html(dataframe: pd.DataFrame):
    # get the table HTML from the dataframe
    table_html = dataframe.to_html(table_id="table", index=False, justify='center')
    # construct the complete HTML with jQuery Data tables
    # You can disable paging or enable y scrolling on lines 20 and 21 respectively
    html = f"""
    <html> 
    <header>
        <link href="style.css" rel="stylesheet">
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
import uuid

filename = str(uuid.uuid4()) + ".html"

# creates a sortable html export from the dataframe 'squad'

html = generate_html(squad)
open(filename, "w", encoding="utf-8").write(html)

import webbrowser

new = 2  # open in a new tab, if possible
# open an HTML file on my own (Windows) computer
url = "C:/Users/natha/OneDrive/Documents/Code/FM/" + filename
webbrowser.open(url, new=new)
