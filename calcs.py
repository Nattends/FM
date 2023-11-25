import pandas as pd


def getDFRecrutement(df: pd.DataFrame, positions: list) -> None:
    """
    ['Days Old', 'Inf', 'Name', 'Position', 'Nat', 'Age', 'Club', 'Ability',
       'Potential', 'Transfer Value', 'Wage', 'Min AP', 'Min Fee Rls',
       'Min Fee Rls to Foreign Clubs', 'Personality', 'Media Handling',
       'Media Description', 'Expires', 'Left Foot', 'Right Foot', 'Av Rat',
       'Apps', '1v1', 'Acc', 'Aer', 'Agg', 'Agi', 'Ant', 'Bal', 'Bra', 'Cmd',
       'Cnt', 'Cmp', 'Cro', 'Dec', 'Det', 'Dri', 'Fin', 'Fir', 'Fla', 'Han',
       'Hea', 'Jum', 'Kic', 'Ldr', 'Lon', 'Mar', 'OtB', 'Pac', 'Pas', 'Pos',
       'Ref', 'Sta', 'Str', 'Tck', 'Tea', 'Tec', 'Thr', 'TRO', 'Vis', 'Wor',
       'UID', 'Cor', 'Height']
    """

    if not positions : 
        raise ValueError("No position given.")
    df = df[
        [
            "Name",
            "Position",
            "Age",
            "Club",
            "Transfer Value",
            "Wage",
            "Min AP",
            "Av Rat",
            "Apps",
            "1v1",
            "Acc",
            "Aer",
            "Agg",
            "Agi",
            "Ant",
            "Bal",
            "Bra",
            "Cmd",
            "Cnt",
            "Cmp",
            "Cro",
            "Dec",
            "Det",
            "Dri",
            "Fin",
            "Fir",
            "Fla",
            "Han",
            "Hea",
            "Jum",
            "Kic",
            "Ldr",
            "Lon",
            "Mar",
            "OtB",
            "Pac",
            "Pas",
            "Pos",
            "Ref",
            "Sta",
            "Str",
            "Tck",
            "Tea",
            "Tec",
            "Thr",
            "TRO",
            "Vis",
            "Wor",
        ]
    ]


    reformatList: list = [
                             "Name",
                             "Club",
                             "Age",
                             "Position",
                             "Transfer Value",
                             "Wage",
                             "Min AP",
                             "Av Rat",
                             "Apps",
                         ] + positions

    for pos in positions:
        match pos:
            case "gkd":
                key = (df['Agi'] + df['Ref'])
                green = (df['Aer'] + df['Cmd'] + df['Han'] + df['Kic'] + df['Cnt'] + df['Pos'])
                blue = (df['1v1'] + df['Thr'] + df['Ant'] + df['Dec'])
                df['gkd'] = (((key * 5) + green * 3) + blue * 1) / 32
                df.gkd = df.gkd.round(1)

            case "skd":
                key = (df['Agi'] + df['Ref'])
                green = (df['Cmd'] + df['Kic'] + df['1v1'] + df['Ant'] + df['Cnt'] + df['Pos'])
                blue = (df['Aer'] + df['Fir'] + df['Han'] + df['Pas'] + df['TRO'] + df['Dec'] + df['Vis'] + df['Acc'])
                df['skd'] = (((key * 5) + green * 3) + blue * 1) / 36
                df.skd = df.skd.round(1)

            case "sks":
                key = (df['Agi'] + df['Ref'])
                green = (df['Cmd'] + df['Kic'] + df['1v1'] + df['Ant'] + df['Cnt'] + df['Pos'])
                blue = (df['Aer'] + df['Fir'] + df['Han'] + df['Pas'] + df['TRO'] + df['Dec'] + df['Vis'] + df['Acc'])
                df['sks'] = (((key * 5) + green * 3) + blue * 1) / 36
                df.sks = df.sks.round(1)

            case "ska":
                key = (df['Agi'] + df['Ref'])
                green = (df['Cmd'] + df['Kic'] + df['1v1'] + df['Ant'] + df['Cnt'] + df['Pos'])
                blue = (df['Aer'] + df['Fir'] + df['Han'] + df['Pas'] + df['TRO'] + df['Dec'] + df['Vis'] + df['Acc'])
                df['ska'] = (((key * 5) + green * 3) + blue * 1) / 36
                df.ska = df.ska.round(1)

            case "bpdd":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Hea'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Pos'] + df['Str'])
                blue = (df['Fir'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] + df['Dec'] + df['Vis'])
                df['bpdd'] = (((key * 5) + green * 3) + blue * 1) / 46
                df.bpdd = df.bpdd.round(1)

            case "bpds":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Hea'] + df['Pas'] + df['Tck'] + df['Pos'] + df['Str'] + df['Agg'] + df['Bra'] + df['Dec'])
                blue = (df['Fir'] + df['Tec'] + df['Ant'] + df['Cnt'] + df['Vis'] + df['Mar'])
                df['bpds'] = (((key * 5) + green * 3) + blue * 1) / 50
                df.bpds = df.bpds.round(1)

            case "bpdc":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Mar'] + df['Pas'] + df['Tck'] + df['Pos'] + df['Ant'] + df['Cnt'] + df['Dec'])
                blue = (df['Fir'] + df['Tec'] + df['Bra'] + df['Vis'] + df['Str'] + df['Hea'])
                df['bpdc'] = (((key * 5) + green * 3) + blue * 1) / 47
                df.bpdc = df.bpdc.round(1)

            case "cdd":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Hea'] + df['Mar'] + df['Tck'] + df['Pos'] + df['Str'])
                blue = (df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] + df['Dec'])
                df['cdd'] = (((key * 5) + green * 3) + blue * 1) / 40
                df.cdd = df.cdd.round(1)

            case "cds":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Hea'] + df['Tck'] + df['Agg'] + df['Bra'] + df['Dec'] + df['Pos'] + df['Str'])
                blue = (df['Mar'] + df['Ant'] + df['Cnt'])
                df['cds'] = (((key * 5) + green * 3) + blue * 1) / 44
                df.cds = df.cds.round(1)

            case "cdc":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Mar'] + df['Tck'] + df['Ant'] + df['Cnt'] + df['Dec'] + df['Pos'])
                blue = (df['Hea'] + df['Bra'] + df['Str'])
                df['cdc'] = (((key * 5) + green * 3) + blue * 1) / 41
                df.cdc = df.cdc.round(1)

            case "cwbs":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Cro'] + df['Dri'] + df['Tec'] + df['OtB'] + df['Tea'])
                blue = (df['Fir'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Ant'] + df['Dec'] + df['Fla'] + df['Pos'] +
                        df['Agi'] + df['Bal'])
                df['cwbs'] = (((key * 5) + green * 3) + blue * 1) / 45
                df.cwbs = df.cwbs.round(1)

            case "cwba":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Cro'] + df['Dri'] + df['Tec'] + df['Fla'] + df['OtB'] + df['Tea'])
                blue = (df['Fir'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Ant'] + df['Dec'] + df['Pos'] + df['Agi'] +
                        df['Bal'])
                df['cwba'] = (((key * 5) + green * 3) + blue * 1) / 47
                df.cwba = df.cwba.round(1)

            case "fbd":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Mar'] + df['Tck'] + df['Ant'] + df['Cnt'] + df['Pos'] + df['Pos'])
                blue = (df['Cro'] + df['Pas'] + df['Dec'] + df['Tea'])
                df['fbd'] = (((key * 5) + green * 3) + blue * 1) / 42
                df.fbd = df.fbd.round(1)

            case "fbs":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Mar'] + df['Tck'] + df['Ant'] + df['Cnt'] + df['Pos'] + df['Tea'])
                blue = (df['Cro'] + df['Dri'] + df['Pas'] + df['Tec'] + df['Dec'])
                df['fbs'] = (((key * 5) + green * 3) + blue * 1) / 43
                df.fbs = df.fbs.round(1)

            case "fba":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Cro'] + df['Mar'] + df['Tck'] + df['Ant'] + df['Pos'] + df['Tea'])
                blue = (df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Cnt'] + df['Dec'] + df['OtB'] + df['Agi'])
                df['fba'] = (((key * 5) + green * 3) + blue * 1) / 46
                df.fba = df.fba.round(1)

            case "ifbd":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Hea'] + df['Mar'] + df['Tck'] + df['Pos'] + df['Str'])
                blue = (df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Cmp'] +
                        df['Cnt'] + df['Dec'] + df['Agi'] + df['Jum'])
                df['ifbd'] = (((key * 5) + green * 3) + blue * 1) / 47
                df.ifbd = df.ifbd.round(1)

            case "iwbd":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Pas'] + df['Tck'] + df['Ant'] + df['Dec'] + df['Pos'] + df['Tea'])
                blue = (df['Fir'] + df['Mar'] + df['Tec'] + df['Cmp'] + df['Cnt'] + df['OtB'] + df['Agi'])
                df['iwbd'] = (((key * 5) + green * 3) + blue * 1) / 45
                df.iwbd = df.iwbd.round(1)

            case "iwbs":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Fir'] + df['Pas'] + df['Tck'] + df['Cmp'] + df['Dec'] + df['Tea'])
                blue = (df['Mar'] + df['Tec'] + df['Ant'] + df['Cnt'] + df['OtB'] + df['Pos'] + df['Vis'] + df['Agi'])
                df['iwbs'] = (((key * 5) + green * 3) + blue * 1) / 46
                df.iwbs = df.iwbs.round(1)

            case "iwba":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Fir'] + df['Pas'] + df['Tck'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] +
                         df['Vis'])
                blue = (df['Cro'] + df['Dri'] + df['Lon'] + df['Mar'] + df['Ant'] + df['Cnt'] + df['Fla'] + df['Pos'] +
                        df['Agi'])
                df['iwba'] = (((key * 5) + green * 3) + blue * 1) / 56
                df.iwba = df.iwba.round(1)

            case "ld":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Fir'] + df['Hea'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Tec'] + df['Dec'] + df['Pos'] +
                         df['Tea'] + df['Str'])
                blue = (df['Ant'] + df['Bra'] + df['Cnt'] + df['Sta'])
                df['ld'] = (((key * 5) + green * 3) + blue * 1) / 54
                df.ld = df.ld.round(1)

            case "ls":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Fir'] + df['Hea'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Tec'] + df['Dec'] + df['Pos'] +
                         df['Tea'] + df['Str'])
                blue = (df['Dri'] + df['Ant'] + df['Bra'] + df['Cnt'] + df['Vis'] + df['Sta'])
                df['ls'] = (((key * 5) + green * 3) + blue * 1) / 56
                df.ls = df.ls.round(1)

            case "ncbd":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Hea'] + df['Mar'] + df['Tck'] + df['Pos'] + df['Str'])
                blue = (df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'])
                df['ncbd'] = (((key * 5) + green * 3) + blue * 1) / 39
                df.ncbd = df.ncbd.round(1)

            case "ncbs":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Hea'] + df['Tck'] + df['Agg'] + df['Bra'] + df['Pos'] + df['Str'])
                blue = (df['Mar'] + df['Ant'] + df['Cnt'])
                df['ncbs'] = (((key * 5) + green * 3) + blue * 1) / 41
                df.ncbs = df.ncbs.round(1)

            case "ncbc":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Mar'] + df['Tck'] + df['Ant'] + df['Cnt'] + df['Pos'])
                blue = (df['Hea'] + df['Bra'] + df['Str'])
                df['ncbc'] = (((key * 5) + green * 3) + blue * 1) / 38
                df.ncbc = df.ncbc.round(1)

            case "nfbd":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Mar'] + df['Tck'] + df['Ant'] + df['Pos'] + df['Str'])
                blue = (df['Hea'] + df['Agg'] + df['Bra'] + df['Cnt'] + df['Tea'])
                df['nfbd'] = (((key * 5) + green * 3) + blue * 1) / 40
                df.nfbd = df.nfbd.round(1)

            case "wcbd":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Hea'] + df['Mar'] + df['Tck'] + df['Pos'] + df['Str'])
                blue = (df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] +
                        df['Dec'] + df['Wor'] + df['Agi'])
                df['wcbd'] = (((key * 5) + green * 3) + blue * 1) / 46
                df.wcbd = df.wcbd.round(1)

            case "wcbs":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Dri'] + df['Hea'] + df['Mar'] + df['Tck'] + df['Pos'] + df['Str'])
                blue = (df['Cro'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] +
                        df['Dec'] + df['OtB'] + df['Wor'] + df['Agi'] + df['Sta'])
                df['wcbs'] = (((key * 5) + green * 3) + blue * 1) / 51
                df.wcbs = df.wcbs.round(1)

            case "wcba":
                key = (df['Acc'] + df['Pac'] + df['Jum'] + df['Cmp'])
                green = (df['Cro'] + df['Dri'] + df['Hea'] + df['Mar'] + df['Tck'] + df['OtB'] + df['Sta'] + df['Str'])
                blue = (df['Fir'] + df['Pas'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Bra'] + df['Cnt'] + df['Dec'] +
                        df['Pos'] + df['Wor'] + df['Agi'])
                df['wcba'] = (((key * 5) + green * 3) + blue * 1) / 55
                df.wcba = df.wcba.round(1)

            case "wbd":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Mar'] + df['Tck'] + df['Ant'] + df['Pos'] + df['Tea'])
                blue = (df['Cro'] + df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Cnt'] + df['Dec'] + df['OtB'] +
                        df['Agi'] + df['Bal'])
                df['wbd'] = (((key * 5) + green * 3) + blue * 1) / 45
                df.wbd = df.wbd.round(1)

            case "wbs":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Cro'] + df['Dri'] + df['Mar'] + df['Tck'] + df['OtB'] + df['Tea'])
                blue = (df['Fir'] + df['Pas'] + df['Tec'] + df['Ant'] + df['Cnt'] + df['Dec'] + df['Pos'] + df['Agi'] +
                        df['Bal'])
                df['wbs'] = (((key * 5) + green * 3) + blue * 1) / 47
                df.wbs = df.wbs.round(1)

            case "wba":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Cro'] + df['Dri'] + df['Tck'] + df['Tec'] + df['OtB'] + df['Tea'])
                blue = (df['Fir'] + df['Mar'] + df['Pas'] + df['Ant'] + df['Cnt'] + df['Dec'] + df['Fla'] + df['Pos'] +
                        df['Agi'] + df['Bal'])
                df['wba'] = (((key * 5) + green * 3) + blue * 1) / 48
                df.wba = df.wba.round(1)

            case "aps":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] + df['Vis'])
                blue = (df['Dri'] + df['Ant'] + df['Fla'] + df['Agi'])
                df['aps'] = (((key * 5) + green * 3) + blue * 1) / 48
                df.aps = df.aps.round(1)

            case "apa":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] + df['Vis'])
                blue = (df['Dri'] + df['Ant'] + df['Fla'] + df['Agi'])
                df['apa'] = (((key * 5) + green * 3) + blue * 1) / 48
                df.apa = df.apa.round(1)

            case "ad":
                key = (df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'])
                green = (df['Mar'] + df['Tck'] + df['Ant'] + df['Cnt'] + df['Dec'] + df['Pos'])
                blue = (df['Cmp'] + df['Tea'] + df['Str'])
                df['ad'] = (((key * 5) + green * 3) + blue * 1) / 41
                df.ad = df.ad.round(1)

            case "ams":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Fir'] + df['Lon'] + df['Pas'] + df['Tec'] + df['Ant'] + df['Dec'] + df['Fla'] + df['OtB'])
                blue = (df['Dri'] + df['Cmp'] + df['Vis'] + df['Agi'])
                df['ams'] = (((key * 5) + green * 3) + blue * 1) / 48
                df.ams = df.ams.round(1)

            case "bwmd":
                key = (df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'])
                green = (df['Tck'] + df['Agg'] + df['Ant'] + df['Tea'])
                blue = (df['Mar'] + df['Bra'] + df['Cnt'] + df['Pos'] + df['Agi'] + df['Str'])
                df['bwmd'] = (((key * 5) + green * 3) + blue * 1) / 38
                df.bwmd = df.bwmd.round(1)

            case "bwms":
                key = (df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'])
                green = (df['Tck'] + df['Agg'] + df['Ant'] + df['Tea'])
                blue = (df['Mar'] + df['Pas'] + df['Bra'] + df['Cnt'] + df['Agi'] + df['Str'])
                df['bwms'] = (((key * 5) + green * 3) + blue * 1) / 38
                df.bwms = df.bwms.round(1)

            case "b2bs":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Pas'] + df['Tck'] + df['OtB'] + df['Tea'])
                blue = (df['Dri'] + df['Fin'] + df['Fir'] + df['Lon'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Cmp'] +
                        df['Dec'] + df['Pos'] + df['Bal'] + df['Str'])
                df['b2bs'] = (((key * 5) + green * 3) + blue * 1) / 44
                df.b2bs = df.b2bs.round(1)

            case "cars":
                key = (df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'])
                green = (df['Fir'] + df['Pas'] + df['Tck'] + df['Dec'] + df['Pos'] + df['Tea'])
                blue = (df['Tec'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['OtB'] + df['Vis'])
                df['cars'] = (((key * 5) + green * 3) + blue * 1) / 44
                df.cars = df.cars.round(1)

            case "cmd":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Tck'] + df['Cnt'] + df['Dec'] + df['Pos'] + df['Tea'])
                blue = (df['Fir'] + df['Mar'] + df['Pas'] + df['Tec'] + df['Agg'] + df['Ant'] + df['Cmp'])
                df['cmd'] = (((key * 5) + green * 3) + blue * 1) / 42
                df.cmd = df.cmd.round(1)

            case "cms":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Fir'] + df['Pas'] + df['Tck'] + df['Dec'] + df['Tea'])
                blue = (df['Tec'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['OtB'] + df['Vis'])
                df['cms'] = (((key * 5) + green * 3) + blue * 1) / 41
                df.cms = df.cms.round(1)

            case "cma":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Fir'] + df['Pas'] + df['Dec'] + df['OtB'])
                blue = (df['Lon'] + df['Tck'] + df['Tec'] + df['Ant'] + df['Cmp'] + df['Tea'] + df['Vis'])
                df['cma'] = (((key * 5) + green * 3) + blue * 1) / 39
                df.cma = df.cma.round(1)

            case "dlpd":
                key = (df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'])
                green = (df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Tea'] + df['Vis'])
                blue = (df['Tck'] + df['Ant'] + df['Pos'] + df['Bal'])
                df['dlpd'] = (((key * 5) + green * 3) + blue * 1) / 45
                df.dlpd = df.dlpd.round(1)

            case "dlps":
                key = (df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'])
                green = (df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Tea'] + df['Vis'])
                blue = (df['Ant'] + df['OtB'] + df['Pos'] + df['Bal'])
                df['dlps'] = (((key * 5) + green * 3) + blue * 1) / 45
                df.dlps = df.dlps.round(1)

            case "dmd":
                key = (df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'])
                green = (df['Tck'] + df['Ant'] + df['Cnt'] + df['Pos'] + df['Tea'])
                blue = (df['Mar'] + df['Pas'] + df['Agg'] + df['Cmp'] + df['Str'] + df['Dec'])
                df['dmd'] = (((key * 5) + green * 3) + blue * 1) / 41
                df.dmd = df.dmd.round(1)

            case "dms":
                key = (df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'])
                green = (df['Tck'] + df['Ant'] + df['Cnt'] + df['Pos'] + df['Tea'])
                blue = (df['Fir'] + df['Mar'] + df['Pas'] + df['Agg'] + df['Cmp'] + df['Dec'] + df['Str'])
                df['dms'] = (((key * 5) + green * 3) + blue * 1) / 42
                df.dms = df.dms.round(1)

            case "dwd":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Tec'] + df['Ant'] + df['OtB'] + df['Pos'] + df['Tea'])
                blue = (df['Cro'] + df['Dri'] + df['Fir'] + df['Mar'] + df['Tck'] + df['Agg'] + df['Cnt'] + df['Dec'])
                df['dwd'] = (((key * 5) + green * 3) + blue * 1) / 43
                df.dwd = df.dwd.round(1)

            case "dws":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Cro'] + df['Pas'] + df['Tec'] + df['OtB'] + df['Tea'])
                blue = (df['Dri'] + df['Fir'] + df['Mar'] + df['Pas'] + df['Tck'] + df['Agg'] + df['Ant'] + df['Cmp'] +
                        df['Cnt'] + df['Dec'] + df['Pos'])
                df['dws'] = (((key * 5) + green * 3) + blue * 1) / 46
                df.dws = df.dws.round(1)

            case "engs":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Vis'])
                blue = (df['Dri'] + df['Ant'] + df['Fla'] + df['OtB'] + df['Tea'] + df['Agi'])
                df['engs'] = (((key * 5) + green * 3) + blue * 1) / 44
                df.engs = df.engs.round(1)

            case "hbd":
                key = (df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'])
                green = (df['Mar'] + df['Tck'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['Pos'] + df['Tea'])
                blue = (df['Fir'] + df['Pas'] + df['Agg'] + df['Bra'] + df['Jum'] + df['Str'])
                df['hbd'] = (((key * 5) + green * 3) + blue * 1) / 50
                df.hbd = df.hbd.round(1)

            case "ifs":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Dri'] + df['Fin'] + df['Fir'] + df['Tec'] + df['OtB'] + df['Agi'])
                blue = (df['Lon'] + df['Pas'] + df['Ant'] + df['Cmp'] + df['Fla'] + df['Vis'] + df['Bal'])
                df['ifs'] = (((key * 5) + green * 3) + blue * 1) / 45
                df.ifs = df.ifs.round(1)

            case "ifa":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Dri'] + df['Fin'] + df['Fir'] + df['Tec'] + df['Ant'] + df['OtB'] + df['Agi'])
                blue = (df['Lon'] + df['Pas'] + df['Cmp'] + df['Fla'] + df['Bal'])
                df['ifa'] = (((key * 5) + green * 3) + blue * 1) / 46
                df.ifa = df.ifa.round(1)

            case "iws":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Cro'] + df['Dri'] + df['Pas'] + df['Tec'] + df['Agi'])
                blue = (df['Fir'] + df['Lon'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Vis'] + df['Bal'])
                df['iws'] = (((key * 5) + green * 3) + blue * 1) / 42
                df.iws = df.iws.round(1)

            case "iwa":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Cro'] + df['Dri'] + df['Pas'] + df['Tec'] + df['Agi'])
                blue = (df['Fir'] + df['Lon'] + df['Ant'] + df['Cmp'] + df['Dec'] + df['Fla'] + df['OtB'] + df['Vis'] +
                        df['Bal'])
                df['iwa'] = (((key * 5) + green * 3) + blue * 1) / 44
                df.iwa = df.iwa.round(1)

            case "mezs":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Pas'] + df['Tec'] + df['Dec'] + df['OtB'])
                blue = (df['Dri'] + df['Fir'] + df['Lon'] + df['Tck'] + df['Ant'] + df['Cmp'] + df['Vis'] + df['Bal'])
                df['mezs'] = (((key * 5) + green * 3) + blue * 1) / 40
                df.mezs = df.mezs.round(1)

            case "meza":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Dri'] + df['Pas'] + df['Tec'] + df['Dec'] + df['OtB'] + df['Vis'])
                blue = (df['Fin'] + df['Fir'] + df['Lon'] + df['Ant'] + df['Cmp'] + df['Fla'] + df['Bal'])
                df['meza'] = (((key * 5) + green * 3) + blue * 1) / 45
                df.meza = df.meza.round(1)

            case "raua":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Fin'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['OtB'] + df['Bal'])
                blue = (df['Fir'] + df['Tec'])
                df['raua'] = (((key * 5) + green * 3) + blue * 1) / 43
                df.raua = df.raua.round(1)

            case "regs":
                key = (df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'])
                green = (df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Fla'] + df['OtB'] + df['Tea'] +
                         df['Vis'])
                blue = (df['Dri'] + df['Lon'] + df['Ant'] + df['Bal'])
                df['regs'] = (((key * 5) + green * 3) + blue * 1) / 51
                df.regs = df.regs.round(1)

            case "rps":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Fir'] + df['Pas'] + df['Tec'] + df['Ant'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] +
                         df['Vis'])
                blue = (df['Dri'] + df['Lon'] + df['Cnt'] + df['Pos'] + df['Agi'] + df['Bal'])
                df['rps'] = (((key * 5) + green * 3) + blue * 1) / 53
                df.rps = df.rps.round(1)

            case "svs":
                key = (df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'])
                green = (df['Mar'] + df['Pas'] + df['Tck'] + df['OtB'] + df['Pos'])
                blue = (df['Fin'] + df['Fir'] + df['Lon'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['Bal'] +
                        df['Str'])
                df['svs'] = (((key * 5) + green * 3) + blue * 1) / 44
                df.svs = df.svs.round(1)

            case "sva":
                key = (df['Wor'] + df['Sta'] + df['Acc'] + df['Pac'])
                green = (df['Fin'] + df['Lon'] + df['Pas'] + df['Tck'] + df['Ant'] + df['OtB'] + df['Pos'])
                blue = (df['Fir'] + df['Mar'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['Bal'])
                df['sva'] = (((key * 5) + green * 3) + blue * 1) / 47
                df.sva = df.sva.round(1)

            case "ssa":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Dri'] + df['Fin'] + df['Fir'] + df['Ant'] + df['Cmp'] + df['OtB'])
                blue = (df['Pas'] + df['Tec'] + df['Cnt'] + df['Dec'] + df['Agi'] + df['Bal'])
                df['ssa'] = (((key * 5) + green * 3) + blue * 1) / 44
                df.ssa = df.ssa.round(1)

            case "wmd":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Pas'] + df['Tck'] + df['Cnt'] + df['Dec'] + df['Pos'] + df['Tea'])
                blue = (df['Cro'] + df['Fir'] + df['Mar'] + df['Tec'] + df['Ant'] + df['Cmp'])
                df['wmd'] = (((key * 5) + green * 3) + blue * 1) / 44
                df.wmd = df.wmd.round(1)

            case "wms":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Pas'] + df['Tck'] + df['Dec'] + df['Tea'])
                blue = (df['Cro'] + df['Fir'] + df['Tec'] + df['Ant'] + df['Cmp'] + df['Cnt'] + df['OtB'] + df['Pos'] +
                        df['Vis'])
                df['wms'] = (((key * 5) + green * 3) + blue * 1) / 41
                df.wms = df.wms.round(1)

            case "wma":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Cro'] + df['Fir'] + df['Pas'] + df['Dec'] + df['Tea'])
                blue = (df['Tck'] + df['Tec'] + df['Ant'] + df['Cmp'] + df['OtB'] + df['Vis'])
                df['wma'] = (((key * 5) + green * 3) + blue * 1) / 41
                df.wma = df.wma.round(1)

            case "wps":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Tea'] + df['Vis'])
                blue = (df['Dri'] + df['OtB'] + df['Agi'])
                df['wps'] = (((key * 5) + green * 3) + blue * 1) / 44
                df.wps = df.wps.round(1)

            case "wpa":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'] +
                         df['Vis'])
                blue = (df['Ant'] + df['Fla'] + df['Agi'])
                df['wpa'] = (((key * 5) + green * 3) + blue * 1) / 50
                df.wpa = df.wpa.round(1)

            case "wtfs":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Hea'] + df['Bra'] + df['Tea'] + df['Jum'] + df['Str'])
                blue = (df['Cro'] + df['Fir'] + df['Ant'] + df['OtB'] + df['Bal'])
                df['wtfs'] = (((key * 5) + green * 3) + blue * 1) / 40
                df.wtfs = df.wtfs.round(1)

            case "wtfa":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Hea'] + df['Bra'] + df['OtB'] + df['Jum'] + df['Str'])
                blue = (df['Cro'] + df['Fin'] + df['Fir'] + df['Ant'] + df['Tea'] + df['Bal'])
                df['wtfa'] = (((key * 5) + green * 3) + blue * 1) / 41
                df.wtfa = df.wtfa.round(1)

            case "ws":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Cro'] + df['Dri'] + df['Tec'] + df['Agi'])
                blue = (df['Fir'] + df['Pas'] + df['OtB'] + df['Bal'])
                df['ws'] = (((key * 5) + green * 3) + blue * 1) / 36
                df.ws = df.ws.round(1)

            case "wa":
                key = (df['Acc'] + df['Pac'] + df['Sta'] + df['Wor'])
                green = (df['Cro'] + df['Dri'] + df['Tec'] + df['Agi'])
                blue = (df['Fir'] + df['Pas'] + df['Ant'] + df['Fla'] + df['OtB'] + df['Bal'])
                df['wa'] = (((key * 5) + green * 3) + blue * 1) / 38
                df.wa = df.wa.round(1)

            case "afa":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Dri'] + df['Fir'] + df['Tec'] + df['Cmp'] + df['OtB'])
                blue = (df['Pas'] + df['Ant'] + df['Dec'] + df['Wor'] + df['Agi'] + df['Bal'] + df['Sta'])
                df['afa'] = (((key * 5) + green * 3) + blue * 1) / 37
                df.afa = df.afa.round(1)

            case "cfs":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Dri'] + df['Fir'] + df['Hea'] + df['Lon'] + df['Pas'] + df['Tec'] + df['Ant'] + df['Cmp'] +
                         df['Dec'] + df['OtB'] + df['Vis'] + df['Agi'] + df['Str'])
                blue = (df['Tea'] + df['Wor'] + df['Bal'] + df['Jum'] + df['Sta'])
                df['cfs'] = (((key * 5) + green * 3) + blue * 1) / 59
                df.cfs = df.cfs.round(1)

            case "cfa":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Dri'] + df['Fir'] + df['Hea'] + df['Tec'] + df['Ant'] + df['Cmp'] + df['OtB'] + df['Agi'] +
                         df['Str'])
                blue = (df['Lon'] + df['Pas'] + df['Dec'] + df['Tea'] + df['Vis'] + df['Wor'] + df['Bal'] + df['Jum'] +
                        df['Sta'])
                df['cfa'] = (((key * 5) + green * 3) + blue * 1) / 51
                df.cfa = df.cfa.round(1)

            case "dlfs":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'])
                blue = (df['Ant'] + df['Fla'] + df['Vis'] + df['Bal'] + df['Str'])
                df['dlfs'] = (((key * 5) + green * 3) + blue * 1) / 41
                df.dlfs = df.dlfs.round(1)

            case "dlfa":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Tea'])
                blue = (df['Dri'] + df['Ant'] + df['Fla'] + df['Vis'] + df['Bal'] + df['Str'])
                df['dlfa'] = (((key * 5) + green * 3) + blue * 1) / 42
                df.dlfa = df.dlfa.round(1)

            case "f9s":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['OtB'] + df['Vis'] +
                         df['Agi'])
                blue = (df['Ant'] + df['Fla'] + df['Tea'] + df['Bal'])
                df['f9s'] = (((key * 5) + green * 3) + blue * 1) / 46
                df.f9s = df.f9s.round(1)

            case "pa":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Ant'] + df['Cmp'] + df['OtB'])
                blue = (df['Fir'] + df['Hea'] + df['Tec'] + df['Dec'])
                df['pa'] = (((key * 5) + green * 3) + blue * 1) / 28
                df.pa = df.pa.round(1)

            case "pfd":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Agg'] + df['Ant'] + df['Bra'] + df['Dec'] + df['Tea'] + df['Wor'] + df['Sta'])
                blue = (df['Fir'] + df['Cmp'] + df['Cnt'] + df['Agi'] + df['Bal'] + df['Str'])
                df['pfd'] = (((key * 5) + green * 3) + blue * 1) / 42
                df.pfd = df.pfd.round(1)

            case "pfs":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Agg'] + df['Ant'] + df['Bra'] + df['Dec'] + df['Tea'] + df['Wor'] + df['Sta'])
                blue = (df['Fir'] + df['Pas'] + df['Cmp'] + df['Cnt'] + df['OtB'] + df['Agi'] + df['Bal'] + df['Str'])
                df['pfs'] = (((key * 5) + green * 3) + blue * 1) / 44
                df.pfs = df.pfs.round(1)

            case "pfa":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Agg'] + df['Ant'] + df['Bra'] + df['OtB'] + df['Tea'] + df['Wor'] + df['Sta'])
                blue = (df['Fir'] + df['Cmp'] + df['Cnt'] + df['Dec'] + df['Agi'] + df['Bal'] + df['Str'])
                df['pfa'] = (((key * 5) + green * 3) + blue * 1) / 43
                df.pfa = df.pfa.round(1)

            case "tfs":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Hea'] + df['Bra'] + df['Tea'] + df['Bal'] + df['Jum'] + df['Str'])
                blue = (df['Fir'] + df['Agg'] + df['Ant'] + df['Cmp'] + df['Dec'] + df['OtB'])
                df['tfs'] = (((key * 5) + green * 3) + blue * 1) / 39
                df.tfs = df.tfs.round(1)

            case "tfa":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Hea'] + df['Bra'] + df['Cmp'] + df['OtB'] + df['Bal'] + df['Jum'] + df['Str'])
                blue = (df['Fir'] + df['Agg'] + df['Ant'] + df['Dec'] + df['Tea'])
                df['tfa'] = (((key * 5) + green * 3) + blue * 1) / 41
                df.tfa = df.tfa.round(1)
            case "trea":
                key = (df['Acc'] + df['Pac'] + df['Fin'])
                green = (df['Dri'] + df['Fir'] + df['Pas'] + df['Tec'] + df['Cmp'] + df['Dec'] + df['Fla'] + df['OtB'] +
                         df['Vis'])
                blue = (df['Ant'] + df['Agi'] + df['Bal'])
                df['trea'] = (((key * 5) + green * 3) + blue * 1) / 45
                df.trea = df.trea.round(1)
            case other:
                raise ValueError(f"{pos} : ce poste n'existe pas.")


    df["Wage"] = df["Wage"].apply(lambda x : x.split('€')[0])
    df["Wage"] = df["Wage"].apply(lambda x: int(x.replace('\xa0', '')))

    return df
