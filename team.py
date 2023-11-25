import glob
import os

import pandas as pd
import numpy as np

# green - blue - white

# finds most recent file in specified folder
list_of_files = glob.glob(
    os.path.join('/Users/nathan/Library/Application Support/Sports Interactive/Football Manager 2024/teamsFiles', '*'))
latest_file = max(list_of_files, key=os.path.getctime)

# Read HTML file exported by FM - in this case an example of an output from the squad page
# This reads as a list, not a dataframe
df_list = pd.read_html(latest_file, header=0, encoding="utf-8", keep_default_na=False)

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
print(df.columns)
for k in listAttributes:
    for index, val in enumerate(df[k]):
        if val == "-":
            deleteInd.append(index)
        elif len(str(val)) > 2:
            val = [int(i) for i in val.split('-')]
            val = round(sum(val) / 2)
            df.at[index, k] = int(val)
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
df.gk= df.gk.round(1)

# calculates Wing_back_Support score
df['wb_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
df['wb_green'] = ( df['Cro'] + df['Dri'] + df['Mar'] + df['Tck'] + df['OtB'] + df['Tea'] )
df['wb_blue'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Ant'] + df['Cnt'] + df['Dec'] + df['Pos'] + df['Agi'] + df['Bal'] )
df['wb'] =( ( ( df['wb_key'] * 5) + (df['wb_green'] * 3) + (df['wb_blue'] * 1) ) / 47)
df.wb= df.wb.round(1)

# calculates Ball_playing_defender_Cover score
df['bpdc_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
df['bpdc_green'] = ( df['Mar'] + df['Pas'] + df['Tck'] + df['Pos'] + df['Ant'] + df['Cnt'] + df['Dec'] )
df['bpdc_blue'] = ( df['Fir'] + df['Tec'] + df['Bra'] + df['Vis'] + df['Str'] + df['Hea'] )
df['bpdc'] =( ( ( df['bpdc_key'] * 5) + (df['bpdc_green'] * 3) + (df['bpdc_blue'] * 1) ) / 47)
df.bpdc= df.bpdc.round(1)

# calculates Ball_playing_defender_Defend score
df['bpdd_key'] = ( df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'] )
df['bpdd_green'] = ( df['Hea'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Pos'] + df['Str'] )
df['bpdd_blue'] = ( df['Fir'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] + df['Dec'] + df['Vis'] )
df['bpdd'] =( ( ( df['bpdd_key'] * 5) + (df['bpdd_green'] * 3) + (df['bpdd_blue'] * 1) ) / 46)
df.bpdd= df.bpdd.round(1)

# calculates Deep_lying_playmaker_Defend score
df['dlpd_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
df['dlpd_green'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Tea'] + df['Vis'] )
df['dlpd_blue'] = ( df['Tck'] + df['Ant'] + df['Pos'] + df['Bal'] )
df['dlpd'] =( ( ( df['dlpd_key'] * 5) + (df['dlpd_green'] * 3) + (df['dlpd_blue'] * 1) ) / 45)
df.dlpd= df.dlpd.round(1)

# calculates Segundo_volante_Attack score
df['vola_key'] = ( df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'] )
df['vola_green'] = ( df['Fin'] + df['Lon'] + df['Pas'] + df['Tck'] + df['Ant'] + df['OtB'] + df['Pos'] )
df['vola_blue'] = ( df['Fir'] + df['Mar'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['Bal'] )
df['vola'] =( ( ( df['vola_key'] * 5) + (df['vola_green'] * 3) + (df['vola_blue'] * 1) ) / 47)
df.vola= df.vola.round(1)

# calculates Advanced_playmaker_Support score
df['aps_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
df['aps_green'] = ( df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] + df['Vis'] )
df['aps_blue'] = ( df['Dri'] + df['Ant'] + df['Fla'] + df['Agi'] )
df['aps'] =( ( ( df['aps_key'] * 5) + (df['aps_green'] * 3) + (df['aps_blue'] * 1) ) / 48)
df.aps= df.aps.round(1)

# calculates Inside_forward_Attack score
df['ifa_key'] = ( df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'] )
df['ifa_green'] = ( df['Dri'] + df['Fin'] + df['Fir'] + df['Tec'] + df['Ant'] + df['OtB'] + df['Agi'] )
df['ifa_blue'] = ( df['Lon'] + df['Pas'] + df['Cmp'] + df['Fla'] + df['Bal'] )
df['ifa'] =( ( ( df['ifa_key'] * 5) + (df['ifa_green'] * 3) + (df['ifa_blue'] * 1) ) / 46)
df.ifa= df.ifa.round(1)

# calculates Advanced_forward_Attack score
df['str_key'] = ( df['Acc'] + df['Pac'] + df['Fin'] )
df['str_green'] = ( df['Dri'] + df['Fir'] + df['Tec'] + df['Cmp'] + df['OtB'] )
df['str_blue'] = ( df['Pas'] + df['Ant'] + df['Dec'] + df['Wor'] + df['Agi'] + df['Bal'] + df['Sta'] )
df['str'] =( ( ( df['str_key'] * 5) + (df['str_green'] * 3) + (df['str_blue'] * 1) ) / 37)
df.str= df.str.round(1)

# builds squad dataframe using only columns that will be exported to HTML
# builds squad dataframe using only columns that will be exported to HTML
squad = df[
    ['Name', 'Age', 'Club', 'Transfer Value', 'Wage', 'Position', 'gk', 'wb', 'bpdc', 'bpdd',
     'dlpd', "vola", "aps", "ifa", "str"]]



# squad['cb'] = np.series(squad['cb'].apply(lambda x: round(x, 1)))
def trueRound(i):
    return round(i, 1)



# taken from here: https://www.thepythoncode.com/article/convert-pandas-dataframe-to-html-table-python
# creates a function to make a sortable html export
def generate_html(dataframe: pd.DataFrame):
    # get the table HTML from the dataframe
    table_html = dataframe.to_html(table_id="table", index=False)
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
                order: [[11, 'desc']],
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


for index, val in enumerate(squad["Wage"]) : 
    wage = val[1:-4].split(",")
    if len(wage) == 2 :
        wage = int(wage[0])*1000 + int(wage[1])
    elif len(wage) > 0: 
        wage = int(wage[0])
    squad["Wage"][index] = wage

# generates random file name for write-out of html file
import uuid

filename = str(uuid.uuid4()) + ".html"

# creates a sortable html export from the dataframe 'squad'

html = generate_html(squad)
open(filename, "w", encoding="utf-8").write(html)

import webbrowser

new = 2  # open in a new tab, if possible
# open an HTML file on my own (Windows) computer
url = "file:///Users/nathan/Documents/Code/PYTHON/FM/" + filename
webbrowser.open(url, new=new)

macos_filename = (
            "/Users/nathan/Library/Application Support/Sports Interactive/Football Manager 2024/teamsFiles" + filename)